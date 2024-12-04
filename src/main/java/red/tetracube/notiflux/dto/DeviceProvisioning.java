package red.tetracube.notiflux.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

import io.smallrye.common.constraint.NotNull;
import jakarta.validation.constraints.NotEmpty;
import red.tetracube.notiflux.enumerations.DeviceType;

import java.util.UUID;

public record DeviceProvisioning(
        @NotNull @JsonProperty UUID deviceId,
        @NotNull @JsonProperty DeviceType deviceType,
        @NotNull @NotEmpty @JsonProperty String internalName,
        @NotNull @NotEmpty @JsonProperty String slug
) {
}
