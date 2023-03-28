import random


class RandomizedSet:

    def __init__(self):
        self.value_position_map = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.value_position_map:
            return False

        self.nums.append(val)
        self.value_position_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_position_map:
            return False

        last_value = self.nums[-1]
        self.nums[self.value_position_map[val]] = last_value
        self.nums.pop()
        self.value_position_map[last_value] = self.value_position_map[val]
        self.value_position_map.pop(val)
        return True

    def getRandom(self) -> int:
        # print(self.nums)
        rand_idx = random.randint(0, len(self.nums) - 1)
        return self.nums[rand_idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()