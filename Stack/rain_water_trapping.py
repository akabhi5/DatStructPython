def get_max_l(arr):
    max_l = [None] * len(arr)
    max_l[0] = arr[0]
    for i in range(1, len(arr)):
        prev_e = max_l[i-1]
        if prev_e > arr[i]:
            max_l[i] = prev_e
        else:
            max_l[i] = arr[i]
    return max_l


def get_max_r(arr):
    max_r = [None] * len(arr)
    max_r[-1] = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        next_e = max_r[i+1]
        if next_e > arr[i]:
            max_r[i] = next_e
        else:
            max_r[i] = arr[i]
    return max_r


def get_max_rain(arr):
    if not arr:
        return 0
        
    mx_l = get_max_l(arr)
    mx_r = get_max_r(arr)
    water = []
    for i in range(len(arr)):
        water.append(min(mx_l[i], mx_r[i]) - arr[i])
    return sum(water)


arr = [3, 0, 0, 2, 0, 4]
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(get_max_rain(arr))
