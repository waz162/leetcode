class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_map ={}
        index = 0

        for i in range(len(nums)):
            if nums[i] not in my_map:
                my_map[nums[i]] = 1
                nums[index] = nums[i]
                index += 1
            elif my_map[nums[i]] == 1:
                my_map[nums[i]] += 1
                nums[index] = nums[i]
                index += 1
            else:
                continue

        return index