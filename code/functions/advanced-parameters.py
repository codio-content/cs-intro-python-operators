def calc_sum(*nums):
    """Calculate the sum of all of the parameters"""
    total = 0
    for num in nums:
        total += num
    print(total)
    
calc_sum()