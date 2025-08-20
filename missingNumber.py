nums = [2, 1, 0, 5, 3]

# O(n log n) because i sorted this list first. if that's the case it will be O(n) linear time
def missingNumber(nums):
    n = len(nums)
    nums.sort()
    if 0 not in nums:
        return "missing number is 0"

    for i in range(n - 1):
        if nums[i + 1] - nums[i] != 1:
            return f"missing number is {nums[i] + 1}"

print(missingNumber(nums))

# O(n) math trick

def missingNumber(nums):
    n = len(nums)
    expected_sum  = n * (n + 1) // 2
    actual_sum = sum(nums)
    missingNumber = expected_sum - actual_sum
    return f"missing number was {missingNumber}"

print(missingNumber(nums))