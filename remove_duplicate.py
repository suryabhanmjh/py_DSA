# remove duplicate
def remove_duplicates(nums):
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    return nums
li = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates(li)) 
    