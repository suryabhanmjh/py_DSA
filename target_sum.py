nums = [2,3,6,5,8,10,7]
target = 5

data = {}

for i in range(len(nums)):
    ans = target-nums[i]
    if ans in data:
        print(data[ans],i)
    data[nums[i]]=i




# stop_loop = False

# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == target:
#             print(i,j)
#             stop_loop = True
    
#     if stop_loop:
#         break