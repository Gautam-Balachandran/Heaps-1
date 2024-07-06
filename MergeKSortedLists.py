# Time Complexity : O(nlogk)
# Space Complexity : O(k)

from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        # This ensures the PriorityQueue can compare ListNode objects based on their values
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        pq = PriorityQueue()
        dummy = ListNode(-1)
        cur = dummy
        
        # Add the first node of each list to the priority queue
        for l in lists:
            if l:
                pq.put((l.val, l))
        
        while not pq.empty():
            val, min_node = pq.get()
            cur.next = min_node
            cur = cur.next
            if min_node.next:
                pq.put((min_node.next.val, min_node.next))
        
        return dummy.next

# Examples
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Helper function to create a linked list from a list
def create_list(arr):
    dummy = ListNode()
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

# Example 1
list1 = create_list([1, 4, 5])
list2 = create_list([1, 3, 4])
list3 = create_list([2, 6])
lists = [list1, list2, list3]

sol = Solution()
merged_head = sol.mergeKLists(lists)
print_list(merged_head) # Output : 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

# Example 2
list1 = create_list([1, 3, 8])
list2 = create_list([2, 4, 6])
list3 = create_list([0, 9, 10])
lists = [list1, list2, list3]

sol = Solution()
merged_head = sol.mergeKLists(lists)
print_list(merged_head) # Output : 0 -> 1 -> 2 -> 3 -> 4 -> 6 -> 8 -> 9 -> 10 -> None

# Example 3
list1 = create_list([5, 7, 8])
list2 = create_list([3, 6, 9])
list3 = create_list([1, 2, 4])
list4 = create_list([0, 11, 13])
lists = [list1, list2, list3, list4]

sol = Solution()
merged_head = sol.mergeKLists(lists)
print_list(merged_head) # Output : 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 11 -> 13 -> None