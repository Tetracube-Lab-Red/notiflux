package red.tetracube.notiflux;

import jakarta.inject.Inject;
import org.eclipse.microprofile.openapi.annotations.parameters.RequestBody;

import io.quarkus.security.Authenticated;
import io.smallrye.common.annotation.RunOnVirtualThread;
import jakarta.enterprise.context.RequestScoped;
import jakarta.validation.Valid;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import red.tetracube.notiflux.dto.DeviceProvisioning;
import red.tetracube.notiflux.services.DevicesServices;

@RequestScoped
@Authenticated
@Path("/devices")
public class DeviceResources {

    @Inject
    DevicesServices devicesServices;

    @RunOnVirtualThread
    @POST
    @Path("/")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public DeviceProvisioning deviceCreate(@RequestBody @Valid DeviceProvisioning request) {
        return devicesServices.deviceProvisioning(request);
    }

}
