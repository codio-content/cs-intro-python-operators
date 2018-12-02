###
If a program stops and seems to be doing nothing, it is “hanging”. Often that means that it is caught in an infinite loop or infinite recursion.

-   If there is a particular loop that you suspect is the problem, add a <span>print</span> statement immediately before the loop that says “entering the loop” and another immediately after that says “exiting the loop”.

    Run the program. If you get the first message and not the second, you’ve got an infinite loop. Go to the “Infinite Loop” section below.

-   Most of the time, an infinite recursion will cause the program to run for a while and then produce a “RuntimeError: Maximum recursion depth exceeded” error. If that happens, go to the “Infinite Recursion” section below.

    If you are not getting this error but you suspect there is a problem with a recursive method or function, you can still use the techniques in the “Infinite Recursion” section.

-   If neither of those steps works, start testing other loops and other recursive functions and methods.

-   If that doesn’t work, then it is possible that you don’t understand the flow of execution in your program. Go to the “Flow of Execution” section below.

