class Solution:
    def maximumSwap(self, num: int) -> int:
        x = 0
        nums = [(x) for x in str(num)]
        first = nums
        # print(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                # print(nums)
                if int(''.join(map(str, nums))) > x:
                    x = int(''.join(map(str, nums)))
                nums = first.copy()
        return (x)
