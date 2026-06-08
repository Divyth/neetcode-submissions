class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count [n] += 1

            if len(count) <= 2:
                continue
            new_count = defaultdict(int) #new_count holds only the elements that still have votes (count > 1), with each count reduced by 1

            for n, c in count.items():
                if c > 1:
                    new_count[n] = c -1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res