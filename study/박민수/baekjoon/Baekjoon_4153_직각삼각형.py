while True:
    nums=[int(x) for x in input().split()]
    if sum(nums) == 0:
        break
    nums.sort()
    if nums[0]**2 + nums[1] ** 2 == nums[2]**2:
        print("right")
    else:
        print("wrong")
