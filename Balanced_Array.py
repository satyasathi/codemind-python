t=int(input())
for i in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    summ=0
    for i in nums:
        summ+=i
    left_sum=0
    for i in range(len(nums)):
        if left_sum==summ-nums[i]-left_sum:
            print("YES")
            break
        else:
            left_sum+=nums[i]
    else:
        print("NO")