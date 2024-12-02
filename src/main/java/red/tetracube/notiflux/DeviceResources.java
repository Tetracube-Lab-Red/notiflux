package red.tetracube.notiflux;

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
import red.tetracube.notiflux.dto.DeviceProvisioningRequest;

@RequestScoped
@Authenticated
@Path("/devices")
public class DeviceResources {

    @RunOnVirtualThread
    @POST
    @Path("/")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public void deviceCreate(@RequestBody @Valid DeviceProvisioningRequest request) {
       
    }

}
