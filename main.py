#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time
import signal

from Robot import Robot


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        client.disconnect()
        exit(1)


signal.signal(signal.SIGINT, handler)


if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("192.168.178.44", 1883, 60)
    client.loop_start()
    test_robo = Robot("robo1", client)
    while True:
        Robot.loop()
        time.sleep(1)
