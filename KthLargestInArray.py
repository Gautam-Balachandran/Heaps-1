# Time Complexity : O(nlog(k))
# Space Complexity : O(k)

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        if not nums:
            return -1
        
        # Use a min-heap to keep track of the k largest elements
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the k-th largest element
        return min_heap[0]


# Examples

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4
print(sol.findKthLargest([1], 1))  # Output: 1