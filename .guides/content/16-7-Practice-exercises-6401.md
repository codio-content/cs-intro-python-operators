---------

Code examples from this chapter are available from <http://thinkpython2.com/code/Time1.py>; solutions to the exercises are available from <http://thinkpython2.com/code/Time1_soln.py>.


Write a function called `mul_time` that takes a Time object and a number and returns a new Time object that contains the product of the original Time and the number.

Then use `mul_time` to write a function that takes a Time object that represents the finishing time in a race, and a number that represents the distance, and returns a Time object that represents the average pace (time per mile).

{Try It}(python3 code/Time1.py)

The <span>datetime</span> module provides <span>time</span> objects that are similar to the Time objects in this chapter, but they provide a rich set of methods and operators. Read the documentation at <http://docs.python.org/3/library/datetime.html>.

1.  Use the <span>datetime</span> module to write a program that gets the current date and prints the day of the week.

2.  Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.

3.  For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. Write a program that takes two birthdays and computes their Double Day.

4.  For a little more challenge, write the more general version that computes the day when one person is $n$ times older than the other.

Solution: <http://thinkpython2.com/code/double.py>

{Try It}(python3 code/Time1.py)