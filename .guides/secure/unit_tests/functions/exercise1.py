def avg(n1, n2):
  try:
    return(n1 + n2) / 2
  except TypeError:
    return("Please use two numbers as parameters")