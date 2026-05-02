import threading
import random
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


class Train(threading.Thread):
    def __init__(self, train_id, event_center, station):
        super().__init__()
        self.train_id = train_id
        self.event_center = event_center
        self.station = station
        self.capacity = 50
        self.current_passengers = []
        self.is_delayed = False

    def run(self):
        while True:
            travel_time = random.randint(3, 7)
            if self.is_delayed:
                travel_time += 10
            time.sleep(travel_time)

            print(f"🚆 Train {self.train_id} requesting platform at {self.station.name}...")

            with self.station.platform_lock:
                self.event_center.notify("TRAIN_ARRIVAL", {"id": self.train_id, "station": self.station.name})

                # 3. Simulate Boarding time
                print(f"✅ Train {self.train_id} is boarding at {self.station.name}.")
                time.sleep(3)  # Time for Passenger threads to interact[cite: 10]

                self.event_center.notify("TRAIN_DEPARTURE", {"id": self.train_id})

            # 4. Small chance of a new disruption after departing
            if random.random() < 0.1:  # 10% chance
                self.trigger_random_delay()

    def trigger_random_delay(self):
        self.is_delayed = True
        # Madrid Line 10 Scenario: Unexpected system failure[cite: 2]
        self.event_center.notify("TRAIN_DELAY", {"id": self.train_id, "minutes": 15})
        time.sleep(5)  # Simulation time for the 'fix'
        self.is_delayed = False



