# optimized solution O(n)

def find_pair(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target - nums[i]], i]
        hash_map[nums[i]] = i
    return None

nums = [8, 7, 2, 5, 3, 1]
target = 12

print(find_pair(nums, target))