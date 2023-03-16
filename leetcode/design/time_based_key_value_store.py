'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

'''
from collections import defaultdict, OrderedDict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # key -> timestamp_bucket_id -> timestamp -> value
        self.store = defaultdict(OrderedDict)
        self.bucket_size = 250

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamp_bucket_id = timestamp // self.bucket_size
        if timestamp_bucket_id not in self.store[key]:
            self.store[key][timestamp_bucket_id] = OrderedDict()

        self.store[key][timestamp_bucket_id][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        timestamp_bucket_id = timestamp // self.bucket_size
        # indicating timestamp is out of bound, return the current max timestamp bucket id
        if timestamp_bucket_id not in self.store[key] and self.store[key]:
            timestamp_bucket_id = list(self.store[key].keys())[-1]

        timestamp_value_map = self.store[key][timestamp_bucket_id]
        timestamps = list(timestamp_value_map.keys())
        index = bisect_right(timestamps, timestamp)
        if index > 0:
            target_timestamp = timestamps[index - 1]
            return timestamp_value_map[target_timestamp]
        else:
            return ""