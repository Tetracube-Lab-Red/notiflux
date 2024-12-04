package red.tetracube.notiflux.broker;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.hivemq.client.mqtt.MqttClient;
import com.hivemq.client.mqtt.datatypes.MqttQos;
import com.hivemq.client.mqtt.mqtt5.Mqtt5AsyncClient;
import com.hivemq.client.mqtt.mqtt5.message.connect.connack.Mqtt5ConnAckReasonCode;
import com.hivemq.client.mqtt.mqtt5.message.subscribe.suback.Mqtt5SubAck;
import io.quarkus.runtime.StartupEvent;
import io.smallrye.mutiny.Uni;
import io.vertx.mutiny.core.eventbus.EventBus;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.enterprise.event.Observes;
import jakarta.inject.Inject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import red.tetracube.notiflux.config.NotiFluxConfig;
import red.tetracube.notiflux.enumerations.DeviceType;

import java.util.AbstractMap;
import java.util.Map;
import java.util.UUID;

@ApplicationScoped
public class BrokerClient {

    @Inject
    ObjectMapper objectMapper;

    @Inject
    EventBus eventBus;

    private final Mqtt5AsyncClient client;

    private final static Logger LOGGER = LoggerFactory.getLogger(BrokerClient.class);

    public BrokerClient(NotiFluxConfig notiFluxConfig) {
        client = MqttClient.builder()
                .identifier(notiFluxConfig.mqtt().clientName() + "-" + UUID.randomUUID())
                .automaticReconnectWithDefaultConfig()
                .automaticReconnect()
                .applyAutomaticReconnect()
                .serverHost(notiFluxConfig.mqtt().address())
                .useMqttVersion5()
                .build()
                .toAsync();
    }

    void startup(@Observes StartupEvent event) {
        Uni.createFrom()
                .completionStage(
                        client.connect()
                )
                .call(mqtt5ConnAck -> {
                    if (mqtt5ConnAck.getReasonCode() == Mqtt5ConnAckReasonCode.SUCCESS) {
                        return listenDevicesEvents();
                    }
                    return Uni.createFrom().voidItem();
                })
                .subscribe()
                .with(connectAck -> {
                    LOGGER.info("MQTT connection result code {}", connectAck.getReasonCode());
                });
    }

    /*public Multi<DeviceTelemetryData> getDeviceTelemetryIdStream() {
        return deviceTelemetryIdStream
                .invoke(telemetryEntry -> LOGGER.info("Arrived from device device {}", telemetryEntry.getValue()))
                .<Optional<DeviceTelemetryData>>map(telemetryEntry -> {
                    try {
                        return Optional.ofNullable(
                                telemetryServices.getLatestDeviceTelemetry(telemetryEntry.getKey(), telemetryEntry.getValue())
                        );
                    } catch (Exception e) {
                        LOGGER.error("Cannot retrieve telemetry due error: ", e);
                        return Optional.empty();
                    }
                })
                .filter(optionalTelemetry -> {
                    if (optionalTelemetry.isEmpty()) {
                        LOGGER.warn("Incoming device telemetry is null");
                    }
                    return optionalTelemetry.isPresent();
                })
                .map(Optional::get);
    }*/

    private Uni<Mqtt5SubAck> listenDevicesEvents() {
        var telemetrySubscription = client.subscribeWith()
                .topicFilter("devices/telemetry/#")
                .qos(MqttQos.AT_LEAST_ONCE)
                .callback(mqtt5Publish -> {
                    try {
                        var topicLevels = mqtt5Publish.getTopic().getLevels();
                        var deviceType = DeviceType.valueOf(topicLevels.getLast());
                        var deviceInternalName = new String(mqtt5Publish.getPayloadAsBytes());
                        eventBus.publish(
                                "device-telemetry",
                                new AbstractMap.SimpleEntry<>(
                                        deviceType,
                                        deviceInternalName
                                )
                        );
                    } catch (Exception e) {
                        LOGGER.error("Invalid telemetry entry due error:", e);
                    }
                })
                .send();
        return Uni.createFrom().completionStage(telemetrySubscription)
                .invoke(mqtt5SubAck -> {
                    LOGGER.info("Telemetry subscription completed with status {}", mqtt5SubAck.getReasonCodes());
                });
    }
/*
    private void publishMessage(String topic, Object message) throws JsonProcessingException {
        var serializedMessage = objectMapper.writeValueAsBytes(message);
        var publishPublisher = this.client
                .publishWith()
                .topic(topic)
                .qos(MqttQos.EXACTLY_ONCE)
                .payload(serializedMessage)
                .send();
        Uni.createFrom().completionStage(publishPublisher)
                .subscribe()
                .with(publishResult -> {
                    if (publishResult.getError().isPresent()) {
                        LOGGER.error("Publish finished with error {}", publishResult.getError());
                        return;
                    }
                    LOGGER.info("Publish completes successfully");
                });
    }*/

}
