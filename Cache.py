

import collections

CACHE_SIZE = 16

class Cache:
    def __init__(self):
        self.cache = collections.deque(maxlen=CACHE_SIZE)
        self.flush_cache()

    def flush_cache(self):
        for i in range(CACHE_SIZE):
            self.cache.append((0, 0))  # Initial adress is (0,0)

    def search_cache(self, address):
        for i in range(CACHE_SIZE):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None

    def write_cache(self, address, value):
        self.cache.append((address, value))

    def __str__(self):
        cache_str = "Cache Contents:\n"
        for slot_number, (address, value) in enumerate(self.cache):
            cache_str += f"Slot {slot_number + 1}: Address={address}, Value={value}\n"
        return cache_str

# Method added to print out contents of Cache
    def print_cache(self):
        print("Cache Contents:")
        for i, (address, value) in enumerate(self.cache):
            print(f"Slot {i + 1}: Address={address}, Value={value}")
        print("\n")


