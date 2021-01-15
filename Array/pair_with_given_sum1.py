# bruteforce solution O(n^2)

def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

nums = [8, 7, 2, 5, 3, 1]
target = 12

print(find_pair(nums, target))