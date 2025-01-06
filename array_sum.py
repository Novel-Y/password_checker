def sum_array(a):
    """A module that returns the sum of an array of numbers

    Args:
        a (int, float): takes an array of integers and float

    Returns: the sum of the input number/s
        
        
    >>> a()
    0
    >>> a(1,2)
    3
    >>> a(1,1.5,2)
    4.5
    """
    if a == None:
       print (0)
        
    else:
        sum_array = sum(a)
        return (sum_array)