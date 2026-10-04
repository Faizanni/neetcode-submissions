class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set()
        for n in nums:
            if n in uniq:
                return True
            uniq.add(n)
        return False