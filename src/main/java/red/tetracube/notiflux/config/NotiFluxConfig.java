package red.tetracube.notiflux.config;

import io.smallrye.config.ConfigMapping;

@ConfigMapping(prefix = "notiflux")
public interface NotiFluxConfig {
    ModulesConfig modules();
    MqttConfig mqtt();
}
