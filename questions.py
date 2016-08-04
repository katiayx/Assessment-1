def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    numbers.sort() #tried sorted(numbers), but doctest did not pass. 
    #but numbers.sort()returns nothing, while sorted(numbers) actually returns a 
    #sorted list. Why?
    if numbers == []:
        return None
    else:
        return numbers[-1]


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    for i in range(len(words)): #by finding the length of the word
    #and then indexing it using range, 
        print word[i]#individual word can be printed. But I'm not sure
        #how to concanate the words together using index.

