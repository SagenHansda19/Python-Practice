if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
"""The any() function in Python is a built-in function that is used 
to check if any element in an iterable (like a list, tuple, or string)
is True. It returns True if at least one element in the iterable is True,
otherwise, it returns False. If the iterable is empty, any() returns False."""