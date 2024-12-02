# NotiFlux

Notiflux is a service that consumes devices telemetries coming from mqtt and send notifications according with your rules.

## Data pipeline

```mermaid
flowchart TD
    dev-pulsar[Device Pulsar] -->|Publishes devices telemetry| mqtt(MQTT Broker)
    notiflux -->|Consumes devices telemetry| mqtt(MQTT Broker)
    notiflux -->|Loads| scripts[Rules scripts]
    scripts[Rules scripts] -->|Checks| E[Devices telemetries]
    scripts[Rules scripts] -->|Return check| notiflux
    notiflux --> alert{Is there some broken rule?}
    alert -->|yes| firebase[Send notification via Firebase]
    alert -->|yes| db[Stores alert in PotgreSQL]
```

## Rule script

This is the minimal example for a rule script

```python
import logging

HANDLED_DEVICE = "UPS"

logger = logging.getLogger("uvicorn")

def evaluate(telemetry: dict):
    logger.info("Running evaluation method for low input voltage")
    return True
```