def two_sum(nums, target):
     for i in range(len(nums)):
         for j in range(i + 1, len(nums)):
             if nums[i] + nums[j] == target:
                 return [i, j]
     else:
         return []

print(two_sum([1, 2, 3, 4, 5], 7))

from collections import Counter
s = "leetcode"
counts = Counter(s)   # internally uses a HashMap
for i, ch in enumerate(s):
    if counts[ch] == 1:
        print(i)  # index of first unique char
        break
