class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        # Pointer for the last element in nums2
        p2 = n - 1
        # Pointer for the very last position in nums1 (where the largest element goes)
        p_write = m + n - 1

        # Merge in reverse order
        while p2 >= 0:
            # If nums1 still has elements and its element is larger than nums2's element
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_write] = nums1[p1]
                p1 -= 1
            else:
                # If nums2's element is larger, or nums1 is exhausted
                nums1[p_write] = nums2[p2]
                p2 -= 1
            
            # Move the write pointer backward
            p_write -= 1
        