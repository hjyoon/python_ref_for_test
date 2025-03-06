def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float("-inf")
        minRightX = nums1[partitionX] if partitionX != x else float("inf")

        maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float("-inf")
        minRightY = nums2[partitionY] if partitionY != y else float("inf")

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1


nums1 = [1, 3, 8]
nums2 = [7, 9, 10, 11]
ans = findMedianSortedArrays(nums1, nums2)
print(ans)
