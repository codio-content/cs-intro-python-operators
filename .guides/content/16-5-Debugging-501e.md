---------

A Time object is well-formed if the values of <span>minute</span> and <span>second</span> are between 0 and 60 (including 0 but not 60) and if <span>hour</span> is positive. <span>hour</span> and <span>minute</span> should be integral values, but we might allow <span>second</span> to have a fraction part.

Requirements like these are called <span>**invariants**</span> because they should always be true. To put it a different way, if they are not true, something has gone wrong.

Writing code to check invariants can help detect errors and find their causes. For example, you might have a function like `valid_time` that takes a Time object and returns <span>False</span> if it violates an invariant:

    def valid_time(time):
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

At the beginning of each function you could check the arguments to make sure they are valid:

    def add_time(t1, t2):
        if not valid_time(t1) or not valid_time(t2):
            raise ValueError('invalid Time object in add_time')
        seconds = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

Or you could use an <span>**assert statement**</span>, which checks a given invariant and raises an exception if it fails:

    def add_time(t1, t2):
        assert valid_time(t1) and valid_time(t2)
        seconds = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

<span>`assert`</span> statements are useful because they distinguish code that deals with normal conditions from code that checks for errors.

