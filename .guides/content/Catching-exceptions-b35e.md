-------------------

A lot of things can go wrong when you try to read and write files. If you try to open a file that doesn’t exist, you get an <span>IOError</span>:

    >>> fin = open('bad_file')
    IOError: [Errno 2] No such file or directory: 'bad_file'

If you don’t have permission to access a file:

    >>> fout = open('/etc/passwd', 'w')
    PermissionError: [Errno 13] Permission denied: '/etc/passwd'

And if you try to open a directory for reading, you get

    >>> fin = open('/home')
    IsADirectoryError: [Errno 21] Is a directory: '/home'

To avoid these errors, you could use functions like <span>os.path.exists</span> and <span>os.path.isfile</span>, but it would take a lot of time and code to check all the possibilities (if “<span>Errno 21</span>” is any indication, there are at least 21 things that can go wrong).

It is better to go ahead and try—and deal with problems if they happen—which is exactly what the <span>try</span> statement does. The syntax is similar to an <span>if...else</span> statement:

    try:    
        fin = open('bad_file')
    except:
        print('Something went wrong.')

Python starts by executing the <span>try</span> clause. If all goes well, it skips the <span>except</span> clause and proceeds. If an exception occurs, it jumps out of the <span>try</span> clause and runs the <span>except</span> clause.

Handling an exception with a <span>try</span> statement is called <span>**catching**</span> an exception. In this example, the <span>except</span> clause prints an error message that is not very helpful. In general, catching an exception gives you a chance to fix the problem, or try again, or at least end the program gracefully.

