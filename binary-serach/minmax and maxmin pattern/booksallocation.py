def bookallocation(nums, k):
    lb = max(nums)
    ub = sum(nums)

    while lb <= ub:
        mid = (lb + ub) // 2
        n = is_true(nums, mid)

        if  n > k :
            lb=mid+1
        else:
            ub=mid-1

    return lb  # ✅ smallest feasible value


def is_true(nums, limit):
    cnt = 1
    total = 0

    for pages in nums:
        if total + pages <= limit:
            total += pages
        else:
            cnt += 1
            total = pages
    return cnt


nums = nums = [12, 34, 67, 90]
m = 2
print(bookallocation(nums, m))  # ✅ Output: 71
