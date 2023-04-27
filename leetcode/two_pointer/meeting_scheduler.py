class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        # maintain a two pointer, using slots pointer as the base
        sorted_slots1 = sorted(slots1)
        sorted_slots2 = sorted(slots2)

        p1, p2 = 0, 0
        end1, end2 = len(slots1) - 1, len(slots2) - 1

        while p1 <= end1 and p2 <= end2:

            # checking current two slots has valid meeting interval.
            start_candidate = max(sorted_slots1[p1][0], sorted_slots2[p2][0])
            end_candidate = min(sorted_slots1[p1][1], sorted_slots2[p2][1])
            if end_candidate - start_candidate >= duration:
                return [start_candidate, start_candidate + duration]

            # update the pointer
            # if p1 end is larger 
            if sorted_slots1[p1][1] >= sorted_slots2[p2][1]:
                p2 += 1
            else:
                p1 += 1

        return []

