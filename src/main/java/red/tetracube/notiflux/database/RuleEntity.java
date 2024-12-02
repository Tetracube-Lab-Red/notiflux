package red.tetracube.notiflux.database;

import java.util.UUID;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import red.tetracube.notiflux.enumerations.DeviceType;

@Entity
@Table(name = "rules")
public class RuleEntity {

    @Id
    public UUID id;

    @Column(name = "rule_expression", nullable = false)
    public String ruleExpression;

    @Column(name = "device_type", nullable = false)
    public DeviceType deviceType;

    @Column(name = "alert_name", nullable = false)
    public String alertName;

    @Column(name = "alert_target_field", nullable = false)
    public String alertTargetField;
    
}
