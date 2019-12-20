def odds_or_evens(my_bool, nums):
    return_list = []
    for num in nums:
      if my_bool:
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(nums)
                
    return return_list