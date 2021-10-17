#!/usr/bin/env python3


class Robot():
    def __init__(self, name, mqtt_client):
        self.name = name
        self.mqtt_client = mqtt_client

    def loop(self):
        pass
