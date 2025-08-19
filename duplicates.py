# Brute force approach to check for duplicates in a list
# O(n^2) quadratic time complexity

nums = [1, 2, 3, 4, 5]
found_duplicates = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            found_duplicates = True
    if found_duplicates:
        break
        
print(found_duplicates)

# Optimized approach to check for duplicates using a set
# # O(n) linear time complexity faster than the brute force approach O(n^2)

def check_duplicates(arr):
    if (set(arr) != len(arr)):
        return True
    else:
        return False

print(check_duplicates(nums))