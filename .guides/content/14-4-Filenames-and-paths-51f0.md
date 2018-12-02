-------------------

Files are organized into <span>**directories**</span> (also called “folders”). Every running program has a “current directory”, which is the default directory for most operations. For example, when you open a file for reading, Python looks for it in the current directory.

The <span>`os`</span> module provides functions for working with files and directories (“os” stands for “operating system”). <span>os.getcwd</span> returns the name of the current directory:

    >>> import os
    >>> cwd = os.getcwd()
    >>> cwd
    '/home/dinsdale'

<span>`cwd`</span> stands for “current working directory”. The result in this example is <span>/home/dinsdale</span>, which is the home directory of a user named <span>dinsdale</span>.

A string like `'/home/dinsdale'` that identifies a file or directory is called a <span>**path**</span>.

A simple filename, like <span>memo.txt</span> is also considered a path, but it is a <span>**relative path**</span> because it relates to the current directory. If the current directory is <span>/home/dinsdale</span>, the filename <span>memo.txt</span> would refer to <span>/home/dinsdale/memo.txt</span>.

A path that begins with <span>/</span> does not depend on the current directory; it is called an <span>**absolute path**</span>. To find the absolute path to a file, you can use <span>os.path.abspath</span>:

    >>> os.path.abspath('memo.txt')
    '/home/dinsdale/memo.txt'

<span>`os.path`</span> provides other functions for working with filenames and paths. For example, <span>os.path.exists</span> checks whether a file or directory exists:

    >>> os.path.exists('memo.txt')
    True

If it exists, <span>os.path.isdir</span> checks whether it’s a directory:

    >>> os.path.isdir('memo.txt')
    False
    >>> os.path.isdir('/home/dinsdale')
    True

Similarly, <span>os.path.isfile</span> checks whether it’s a file.

<span>`os.listdir`</span> returns a list of the files (and other directories) in the given directory:

    >>> os.listdir(cwd)
    ['music', 'photos', 'memo.txt']

To demonstrate these functions, the following example “walks” through a directory, prints the names of all the files, and calls itself recursively on all the directories.

    def walk(dirname):
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)

            if os.path.isfile(path):
                print(path)
            else:
                walk(path)

<span>`os.path.join`</span> takes a directory and a file name and joins them into a complete path.

The <span>os</span> module provides a function called <span>walk</span> that is similar to this one but more versatile. As an exercise, read the documentation and use it to print the names of the files in a given directory and its subdirectories. You can download my solution from <http://thinkpython2.com/code/walk.py>.

