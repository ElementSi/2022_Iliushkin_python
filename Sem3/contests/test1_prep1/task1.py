nums = [int(n) for n in input().split()]
nums = sorted(nums)
a = int(input())
for i in range(a):
    print(nums[len(nums)-a+i])
