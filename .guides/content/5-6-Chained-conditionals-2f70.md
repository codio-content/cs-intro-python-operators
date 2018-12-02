--------------------

Sometimes there are more than two possibilities and we need more than two branches. One way to express a computation like that is a <span>**chained conditional**</span>:

    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')

<span>elif</span> is an abbreviation of “else if”. Again, exactly one branch will run. There is no limit on the number of <span>elif</span> statements. If there is an <span>else</span> clause, it has to be at the end, but there doesn’t have to be one.

    if choice == 'a':
        draw_a()
    elif choice == 'b':
        draw_b()
    elif choice == 'c':
        draw_c()

Each condition is checked in order. If the first is false, the next is checked, and so on. If one of them is true, the corresponding branch runs and the statement ends. Even if more than one condition is true, only the first true branch runs.

