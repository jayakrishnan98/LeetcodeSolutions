class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        first_critical_idx = float('inf')
        previous_critical_idx = float('inf')

        min_distance = float('inf')

        previous = head
        current = head.next
        index = 1

        while current.next is not None:

            a = previous.val
            b = current.val
            c = current.next.val

            if a < b > c or a > b < c:

                if first_critical_idx == float('inf'):
                    first_critical_idx = index
                    previous_critical_idx = index

                else:
                    # Distance from the previous critical point,
                    # NOT from the first critical point
                    min_distance = min(
                        min_distance,
                        index - previous_critical_idx
                    )

                    previous_critical_idx = index

            previous = current
            current = current.next
            index += 1

        # No critical point OR only one critical point
        if (
            first_critical_idx == float('inf')
            or first_critical_idx == previous_critical_idx
        ):
            return [-1, -1]

        return [
            min_distance,
            previous_critical_idx - first_critical_idx
        ]