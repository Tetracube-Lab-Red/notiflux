package red.tetracube.notiflux.services;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.transaction.Transactional;
import red.tetracube.notiflux.database.DeviceEntity;
import red.tetracube.notiflux.dto.DeviceProvisioningRequest;

@ApplicationScoped
public class DevicesServices {

    @Transactional
    public void deviceProvisioning(DeviceProvisioningRequest request) {
        var device = new DeviceEntity();
        device.deviceType = request.deviceType();
        device.id = request.deviceId();
        device.internalName = request.internalName();
        device.slug = request.slug();
        device.persist();
    }

}
