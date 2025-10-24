from copy import copy
from dataclasses import dataclass

from custom_components.edgeos.common.consts import ENTITY_VALIDATIONS, UNIT_MAPPING
from custom_components.edgeos.common.enums import (
    DeviceTypes,
    EntityKeys,
    EntityValidation,
    UnitOfEdgeOS,
)
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.number import NumberEntityDescription
from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.components.switch import SwitchEntityDescription
from homeassistant.const import PERCENTAGE, EntityCategory, Platform, UnitOfTime
from homeassistant.helpers.entity import EntityDescription


@dataclass(frozen=True, kw_only=True)
class IntegrationEntityDescription(EntityDescription):
    platform: Platform | None = None
    device_type: DeviceTypes | None = None
    entity_validation: EntityValidation | None = None


@dataclass(frozen=True, kw_only=True)
class IntegrationBinarySensorEntityDescription(
    BinarySensorEntityDescription, IntegrationEntityDescription
):
    platform: Platform | None = Platform.BINARY_SENSOR
    on_value: str | bool | None = None
    attributes: list[str] | None = None


@dataclass(frozen=True, kw_only=True)
class IntegrationSensorEntityDescription(
    SensorEntityDescription, IntegrationEntityDescription
):
    platform: Platform | None = Platform.SENSOR


@dataclass(frozen=True, kw_only=True)
class IntegrationSelectEntityDescription(
    SelectEntityDescription, IntegrationEntityDescription
):
    platform: Platform | None = Platform.SELECT


@dataclass(frozen=True, kw_only=True)
class IntegrationSwitchEntityDescription(
    SwitchEntityDescription, IntegrationEntityDescription
):
    platform: Platform | None = Platform.SWITCH
    on_value: str | bool | None = None
    action_name: str | None = None


@dataclass(frozen=True, kw_only=True)
class IntegrationDeviceTrackerEntityDescription(IntegrationEntityDescription):
    platform: Platform | None = Platform.DEVICE_TRACKER


@dataclass(frozen=True, kw_only=True)
class IntegrationNumberEntityDescription(
    NumberEntityDescription, IntegrationEntityDescription
):
    platform: Platform | None = Platform.NUMBER


ENTITY_DESCRIPTIONS: list[IntegrationEntityDescription] = [
    IntegrationSensorEntityDescription(
        key=EntityKeys.CPU_USAGE,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:chip",
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.RAM_USAGE,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:memory",
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationBinarySensorEntityDescription(
        key=EntityKeys.FIRMWARE,
        device_class=BinarySensorDeviceClass.UPDATE,
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.LAST_RESTART,
        device_class=SensorDeviceClass.TIMESTAMP,
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.UNKNOWN_DEVICES,
        native_unit_of_measurement=UnitOfEdgeOS.DEVICES,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:help-network-outline",
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationSwitchEntityDescription(
        key=EntityKeys.LOG_INCOMING_MESSAGES,
        entity_category=EntityCategory.CONFIG,
        icon="mdi:math-log",
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationNumberEntityDescription(
        key=EntityKeys.CONSIDER_AWAY_INTERVAL,
        native_max_value=600,
        native_min_value=0,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        entity_category=EntityCategory.CONFIG,
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationNumberEntityDescription(
        key=EntityKeys.UPDATE_ENTITIES_INTERVAL,
        native_max_value=600,
        native_min_value=0,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        entity_category=EntityCategory.CONFIG,
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationNumberEntityDescription(
        key=EntityKeys.UPDATE_API_INTERVAL,
        native_max_value=600,
        native_min_value=0,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        entity_category=EntityCategory.CONFIG,
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationSelectEntityDescription(
        key=EntityKeys.UNIT,
        options=list(UNIT_MAPPING.keys()),
        entity_category=EntityCategory.CONFIG,
        device_type=DeviceTypes.SYSTEM,
    ),
    IntegrationBinarySensorEntityDescription(
        key=EntityKeys.INTERFACE_CONNECTED,
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        device_type=DeviceTypes.INTERFACE,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_RECEIVED_DROPPED,
        native_unit_of_measurement=UnitOfEdgeOS.DROPPED,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:package-variant-minus",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_SENT_DROPPED,
        native_unit_of_measurement=UnitOfEdgeOS.DROPPED,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:package-variant-minus",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_RECEIVED_ERRORS,
        native_unit_of_measurement=UnitOfEdgeOS.ERRORS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:timeline-alert",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_SENT_ERRORS,
        native_unit_of_measurement=UnitOfEdgeOS.ERRORS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:timeline-alert",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_RECEIVED_PACKETS,
        native_unit_of_measurement=UnitOfEdgeOS.PACKETS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:package-up",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_SENT_PACKETS,
        native_unit_of_measurement=UnitOfEdgeOS.PACKETS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:package-up",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_RECEIVED_RATE,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:download-network-outline",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_SENT_RATE,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:upload-network-outline",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_RECEIVED_TRAFFIC,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        icon="mdi:download-network-outline",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.INTERFACE_SENT_TRAFFIC,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        icon="mdi:upload-network-outline",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSwitchEntityDescription(
        key=EntityKeys.INTERFACE_MONITORED,
        entity_category=EntityCategory.CONFIG,
        icon="mdi:monitor-eye",
        device_type=DeviceTypes.INTERFACE,
    ),
    IntegrationBinarySensorEntityDescription(
        key=EntityKeys.INTERFACE_STATUS,
        icon="mdi:monitor-eye",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.NON_ADMIN_ONLY,
    ),
    IntegrationSwitchEntityDescription(
        key=EntityKeys.INTERFACE_STATUS,
        icon="mdi:ethernet",
        device_type=DeviceTypes.INTERFACE,
        entity_validation=EntityValidation.ADMIN_ONLY,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.DEVICE_RECEIVED_RATE,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:download-network-outline",
        device_type=DeviceTypes.DEVICE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.DEVICE_SENT_RATE,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:upload-network-outline",
        device_type=DeviceTypes.DEVICE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.DEVICE_RECEIVED_TRAFFIC,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        icon="mdi:download-network-outline",
        device_type=DeviceTypes.DEVICE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSensorEntityDescription(
        key=EntityKeys.DEVICE_SENT_TRAFFIC,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        icon="mdi:upload-network-outline",
        device_type=DeviceTypes.DEVICE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationDeviceTrackerEntityDescription(
        key=EntityKeys.DEVICE_TRACKER,
        device_type=DeviceTypes.DEVICE,
        entity_validation=EntityValidation.MONITORED,
    ),
    IntegrationSwitchEntityDescription(
        key=EntityKeys.DEVICE_MONITORED,
        entity_category=EntityCategory.CONFIG,
        icon="mdi:monitor-eye",
        device_type=DeviceTypes.DEVICE,
    ),
]


def get_entity_descriptions(
    platform: Platform,
    device_type: DeviceTypes,
    is_monitored: bool | None,
    is_admin: bool | None,
) -> list[IntegrationEntityDescription]:
    entity_descriptions = copy(ENTITY_DESCRIPTIONS)

    result = [
        entity_description
        for entity_description in entity_descriptions
        if entity_description.platform == platform
        and entity_description.device_type == device_type
        and is_valid_entity(entity_description, is_monitored, is_admin)
    ]

    return result


def is_valid_entity(
    entity_description: IntegrationEntityDescription,
    is_monitored: bool | None,
    is_admin: bool | None,
):
    is_valid = entity_description.entity_validation is None

    if entity_description.entity_validation is not None:
        validation = ENTITY_VALIDATIONS[entity_description.entity_validation]
        is_valid = validation(is_monitored, is_admin)

    return is_valid


def get_platforms() -> list[str]:
    platforms = {
        entity_description.platform: None for entity_description in ENTITY_DESCRIPTIONS
    }
    result = list(platforms.keys())

    return result


PLATFORMS = get_platforms()
