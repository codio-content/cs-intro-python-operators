def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each element"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))
        
parameter_types(range(10), "", parameter_types, 45)