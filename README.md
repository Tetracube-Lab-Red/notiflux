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