class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}  # key -> (value, freq)
        self.freq_map = {}  # freq -> {keys in this freq}
        self.min_freq = 0  # track the minimum frequency for quick eviction

    def _update_freq(self, key):
        value, freq = self.data[key]
        self.data[key] = (value, freq + 1)

        # Remove key from current freq set
        self.freq_map[freq].remove(key)
        if not self.freq_map[freq]:  
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add key to new freq set
        if freq + 1 not in self.freq_map:
            self.freq_map[freq + 1] = set()
        self.freq_map[freq + 1].add(key)

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self._update_freq(key)
        return self.data[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.data:
            self.data[key] = (value, self.data[key][1])
            self._update_freq(key)
