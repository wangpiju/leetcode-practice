# two sum in python
def two_sum(nums, target):
    """
    Find two numbers in nums that add up to target.

    :param nums: List of integers
    :param target: Integer target sum
    :return: Tuple of indices of the two numbers that add up to target
    """
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], index)
        num_to_index[num] = index
    
    return None
# --- Simple tests below ---
def run_tests():
    # Basic case
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    # Duplicate values
    assert two_sum([3, 3], 6) == (0, 1)

    # Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)

    # Empty and single-element cases (no solution)
    assert two_sum([], 5) is None
    assert two_sum([3], 3) is None

    # No solution
    assert two_sum([1, 2, 3], 7) is None

if __name__ == "__main__":
    run_tests()
    print("All tests passed.")