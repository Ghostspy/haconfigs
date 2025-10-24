from __future__ import annotations

from datetime import datetime, timedelta

from ..common.consts import (
    DEVICE_DATA_DOMAIN,
    DEVICE_DATA_IP,
    DEVICE_DATA_MAC,
    DEVICE_DATA_NAME,
    DEVICE_DATA_RECEIVED,
    DEVICE_DATA_SENT,
    DHCP_SERVER_LEASED,
    TRAFFIC_DATA_DIRECTION_RECEIVED,
    TRAFFIC_DATA_DIRECTION_SENT,
)
from .edge_os_traffic_data import EdgeOSTrafficData


class EdgeOSDeviceData:
    hostname: str
    ip: str
    mac: str
    domain: str | None
    is_leased: bool
    traffic: EdgeOSTrafficData

    def __init__(
        self, hostname: str, ip: str, mac: str, domain: str | None, is_leased: bool
    ):
        self.hostname = hostname
        self.ip = ip
        self.mac = mac
        self.domain = domain
        self.received = EdgeOSTrafficData(TRAFFIC_DATA_DIRECTION_RECEIVED)
        self.sent = EdgeOSTrafficData(TRAFFIC_DATA_DIRECTION_SENT)
        self.is_leased = is_leased

    @property
    def unique_id(self) -> str:
        return self.mac

    @property
    def last_activity(self) -> int:
        received_activity = int(self.received.last_activity)
        sent_activity = int(self.sent.last_activity)

        last_activity = (
            received_activity if received_activity > sent_activity else sent_activity
        )

        return last_activity

    @property
    def last_activity_in_seconds(self) -> int:
        now = datetime.now().timestamp()

        diff = int(now) - int(self.last_activity)
        last_activity_in_seconds = int(timedelta(seconds=diff).total_seconds())

        return last_activity_in_seconds

    def to_dict(self):
        obj = {
            DEVICE_DATA_NAME: self.hostname,
            DEVICE_DATA_IP: self.ip,
            DEVICE_DATA_MAC: self.mac,
            DEVICE_DATA_DOMAIN: self.domain,
            DEVICE_DATA_RECEIVED: self.received.to_dict(),
            DEVICE_DATA_SENT: self.sent.to_dict(),
            DHCP_SERVER_LEASED: self.is_leased,
        }

        return obj

    def get_attributes(self):
        device_attributes = self.to_dict()

        attributes = {
            attribute: device_attributes[attribute]
            for attribute in device_attributes
            if attribute not in [DEVICE_DATA_RECEIVED, DEVICE_DATA_SENT]
        }

        return attributes

    def __repr__(self):
        to_string = f"{self.to_dict()}"

        return to_string
