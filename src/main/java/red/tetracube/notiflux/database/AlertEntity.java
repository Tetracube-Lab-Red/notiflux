package red.tetracube.notiflux.database;

import java.time.Instant;
import java.util.UUID;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "alerts")
public class AlertEntity {
    
    @Id
    public UUID id;

    @ManyToOne(fetch = FetchType.LAZY, targetEntity = DeviceEntity.class)
    @JoinColumn(name = "device_id", nullable = false)
    public DeviceEntity device;

    @ManyToOne(fetch = FetchType.EAGER, targetEntity = RuleEntity.class)
    @JoinColumn(name = "rule_id", nullable = false)
    public RuleEntity rule;

    @Column(name = "open_event_id", nullable = false)
    public UUID openEventId;

    @Column(name = "open_event_ts", nullable = false)
    public Instant openEventTS;

    @Column(name = "close_event_id", nullable = true)
    public UUID closeEventId;

    @Column(name = "close_event_ts", nullable = true)
    public Instant closeEventTS;

}