package red.tetracube.notiflux.database;

import java.util.UUID;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import red.tetracube.notiflux.enumerations.DeviceType;

@Entity
@Table(name = "devices")
public class DeviceEntity {

    @Id
    public UUID id;

    @Column(name = "internal_name", unique = true, nullable = false)
    public String internalName;

    @Column(name = "slug", unique = true, nullable = false)
    public String slug;

    @Enumerated(EnumType.STRING)
    @Column(name = "device_type", nullable = false)
    public DeviceType deviceType;

}
