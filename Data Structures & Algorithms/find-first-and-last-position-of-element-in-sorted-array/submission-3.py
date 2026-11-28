class Solution:
    def searchRange(self, a: List[int], k: int) -> List[int]:
        def first():
            low = 0
            high = len(a) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if a[mid] == k:
                    ans = mid
                    high = mid - 1

                elif a[mid] < k:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        def last():
            low = 0
            high = len(a) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if a[mid] == k:
                    ans = mid
                    low = mid + 1

                elif a[mid] < k:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        return [first(), last()]