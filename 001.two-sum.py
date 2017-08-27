# coding=utf-8
# coding=utf-8


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    inverse_dict = dict(zip(nums, range(len(nums))))  # 构建字典，数字为键，index为值，便于后面查找
    for index, number in enumerate(nums):
        difference = target - number
        if difference in nums:
            if inverse_dict[difference] != index:
                return [index, inverse_dict[difference]]  # 题目明确指出必只有一个解，故不考虑特殊情况了
