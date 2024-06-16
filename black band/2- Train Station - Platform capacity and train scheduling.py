from typing import List, Tuple, Dict
from collections import defaultdict


# Define data structures
class Train:
    def __init__(self, id, arrival_time, departure_time, length, passenger_capacity):
        self.id = id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.length = length
        self.passenger_capacity = passenger_capacity


class Platform:
    def __init__(self, id, length, capacity):
        self.id = id
        self.length = length
        self.capacity = capacity
        self.schedule = []


# Function to check if a train can be assigned to a platform
def can_assign(train: Train, platform: Platform):

    if train.length > platform.length:
        return False

    if len(platform.schedule) >= platform.capacity:
        return False

    for scheduled_train in platform.schedule:
        if not (
                train.departure_time <= scheduled_train.arrival_time or train.arrival_time >= scheduled_train.departure_time):
            return False
    return True


# Function to assign trains to platforms
def assign_trains_to_platforms(trains: List[Train], platforms: List[Platform], connections: List[Tuple[int, int]]):
    trains.sort(key=lambda t: t.arrival_time)  # Sort trains by arrival time
    platform_dict = {platform.id: platform for platform in platforms}

    # Adjacency list for connections
    connection_map = defaultdict(list)
    for train1, train2 in connections:
        connection_map[train1].append(train2)
        connection_map[train2].append(train1)

    # Assignment of trains to platforms
    assignment = {}

    for train in trains:
        assigned = False
        for platform in platforms:
            if can_assign(train, platform):
                platform.schedule.append(train)
                assignment[train.id] = platform.id
                assigned = True
                break
        if not assigned:
            print(f"Unable to assign train {train.id}")
            return None

    # Ensure connections are respected
    for train1, train2 in connections:
        if train1 in assignment and train2 in assignment:
            if assignment[train1] != assignment[train2]:
                print(f"Connection constraint violated between train {train1} and train {train2}")
                return None

    return assignment



trains = [
    Train(1, 8, 10, 5, 200),
    Train(2, 9, 12, 4, 150),
    Train(3, 11, 13, 3, 100)
]

platforms = [
    Platform(1, 6, 2),
    Platform(2, 5, 2)
]

connections = [
    (1, 2),
    (2, 3)
]

assignment = assign_trains_to_platforms(trains, platforms, connections)

if assignment:
    print("Train assignments:")
    for train_id, platform_id in assignment.items():
        print(f"Train {train_id} -> Platform {platform_id}")
else:
    print("No valid assignment found")
