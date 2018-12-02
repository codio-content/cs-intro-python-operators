-----

Most operating systems provide a command-line interface, also known as a <span>**shell**</span>. Shells usually provide commands to navigate the file system and launch applications. For example, in Unix you can change directories with <span>cd</span>, display the contents of a directory with <span>ls</span>, and launch a web browser by typing (for example) <span>firefox</span>.

Any program that you can launch from the shell can also be launched from Python using a <span>**pipe object**</span>, which represents a running program.

For example, the Unix command <span>`ls -l`</span> normally displays the contents of the current directory in long format. You can launch <span>ls</span> with <span>`os.popen`</span>:

    >>> cmd = 'ls -l'
    >>> fp = os.popen(cmd)

The argument is a string that contains a shell command. The return value is an object that behaves like an open file. You can read the output from the <span>ls</span> process one line at a time with <span>readline</span> or get the whole thing at once with <span>read</span>:

    >>> res = fp.read()

When you are done, you close the pipe like a file:

    >>> stat = fp.close()
    >>> print(stat)
    None

The return value is the final status of the <span>ls</span> process; <span>None</span> means that it ended normally (with no errors).

For example, most Unix systems provide a command called <span>`md5sum`</span> that reads the contents of a file and computes a “checksum”. You can read about MD5 at <http://en.wikipedia.org/wiki/Md5>. This command provides an efficient way to check whether two files have the same contents. The probability that different contents yield the same checksum is very small (that is, unlikely to happen before the universe collapses).

You can use a pipe to run <span>md5sum</span> from Python and get the result:

    >>> filename = 'book.tex'
    >>> cmd = 'md5sum ' + filename
    >>> fp = os.popen(cmd)
    >>> res = fp.read()
    >>> stat = fp.close()
    >>> print(res)
    1e0033f0ed0656636de0d75144ba32e0  book.tex
    >>> print(stat)
    None


Footnote: `popen` is deprecated now, which means we are supposed to stop using it and start using the subprocess module. But for simple cases, I find subprocess more complicated than necessary. So I am going to keep using popen until they take it away.

