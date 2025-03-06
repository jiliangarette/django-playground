# `two sum` problem 

# ```
# nums = [2, 7, 11, 15]
# target = 9
# ```

# should return something like `nums[0]` and `nums[1]`
# and the answer return should `[0,1]` indexes?

# brute force method

# loop the array
# do a 2x2 matrix 
# check if the outerloop and innerloop equals to the target
# if correct, it should return a new array of the index
# if not, it should return that there is no 2 value thats equal to the target


def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if (nums[i] + nums[j] == target):
                return [i,j]
    return f'no two numbers are equal to {target}'


nums = [2, 9, 9, 1]
target = 9
print(twoSum(nums, target))