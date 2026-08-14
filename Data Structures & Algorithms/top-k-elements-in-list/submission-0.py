class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums: # Iterating through list nums; Key is equal to num
            count[num] = count.get(num, 0) + 1 # Check if dict contains key. If not, add to dict count
            
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return []

# [1, 1, 1, 2, 2, 3]
# {1: 3, 2: 2, 3: 1}

# [0, 1, 2, 3] k = 2
# [2, 3]