class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return int(nums[0] >= target)
        min_len = len(nums)
        acc = 0
        comp = 0
        for i in range(0, len(nums)):
            acc = nums[i]
            if acc >= target:
                return 1
            for j in range(i + 1, len(nums)):
                acc += nums[j]
                if acc >= target and (j - i) < min_len:
                    min_len = (j - i + 1)
                    comp = acc
                    break
                if (j - i) >= min_len:
                    break
                
            
        
        return min_len * int(comp >= target)
        '''
        start = 0
        end = len(nums) - 1
    
        dist = len(nums) - 1
        acc = nums[start] + nums[end]
        while start < end:
    
            # store the distance
            if acc >= target and (end - start) < dist:
                dist = end - start
            # get rid of the smallest element
            if nums[start] < nums[end]:
                acc -= nums[start]
                start += 1
            else: 
                acc -= nums[end]
                end -= 1
        return dist
        '''

                