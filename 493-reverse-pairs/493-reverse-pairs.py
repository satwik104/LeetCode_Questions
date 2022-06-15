class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def mergesort(l, r):
            if l>=r: return 0
            
            mid = (l+r)//2
            count = mergesort(l,mid) + mergesort(mid+1,r)
            j = mid + 1
            
            for i in range(l, mid+1):
                while j<=r and nums[i] > 2 * nums[j]:
                    j+=1
                count += j - mid - 1
            
            nums[l:r+1] = sorted(nums[l:r+1])
            return count
        
        return mergesort(0, len(nums)-1)