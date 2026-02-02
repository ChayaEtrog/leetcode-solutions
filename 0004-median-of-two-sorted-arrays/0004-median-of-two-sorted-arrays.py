class Solution(object):
    def kth(self,A, B, k):
        i = j = 0
        while True:
            if i == len(A):
                return B[j + k - 1]

            if j == len(B):
                return A[i + k -1]

            if k == 1:
                return min(A[i], B[j])


            half = k//2
            new_i = min(i + half, len(A)) - 1
            new_j = min(j + half, len(B)) - 1

            if A[new_i] <= B[new_j]:
                k -= (new_i - i + 1)
                i = new_i + 1
            else:
                k -= (new_j - j + 1)
                j = new_j + 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.kth(nums1, nums2, total // 2 + 1)
        
        else:
            left = self.kth(nums1, nums2, total // 2)
            right = self.kth(nums1, nums2, total // 2 + 1)
            return float(left + right) / 2


        