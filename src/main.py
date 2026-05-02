import threading
import time
import numpy as np
import matplotlib.pyplot as plt

class StationEventCenter:
    def __init__(self):
        self._subscribers = []
        self._lock = threading.Lock()

    def subscribe(self, observer):
        with self._lock:
            self._subscribers.append(observer)

    def notify(self, event_type, data):
        with self._lock:
            for subscriber in self._subscribers:
                subscriber.update(event_type, data)


class AnnouncementSystem:
    def update(self, event_type, data):
        if event_type == "TRAIN_DELAY":
            print(f"📢 PA SYSTEM: Attention! Train {data['id']} is delayed by {data['minutes']} mins.")
        elif event_type == "EMERGENCY":
            print(f"🚨 PA SYSTEM: EMERGENCY! Please follow evacuation procedures.")

class SecurityOffice:
    def update(self, event_type, data):
        if event_type == "EMERGENCY":
            print(f"👮 SECURITY: Dispatching officers to {data['location']} immediately!")



