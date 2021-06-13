def doubler(num):
    """
    This function returns the argument 'num' multipled by 2

    Example
    -------
    >>> doubler(10)
    30
    """
    return num * 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()