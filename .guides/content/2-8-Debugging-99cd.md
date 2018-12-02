---------

Three kinds of errors can occur in a program: syntax errors, runtime errors, and semantic errors. It is useful to distinguish between them in order to track them down more quickly.

Syntax error:
:   “Syntax” refers to the structure of a program and the rules about that structure. For example, parentheses have to come in matching pairs, so <span>(1 + 2)</span> is legal, but <span>8)</span> is a <span>**syntax error**</span>.

    If there is a syntax error anywhere in your program, Python displays an error message and quits, and you will not be able to run the program. During the first few weeks of your programming career, you might spend a lot of time tracking down syntax errors. As you gain experience, you will make fewer errors and find them faster.

Runtime error:
:   The second type of error is a runtime error, so called because the error does not appear until after the program has started running. These errors are also called <span>**exceptions**</span> because they usually indicate that something exceptional (and bad) has happened.

    Runtime errors are rare in the simple programs you will see in the first few chapters, so it might be a while before you encounter one.

Semantic error:
:   The third type of error is “semantic”, which means related to meaning. If there is a semantic error in your program, it will run without generating error messages, but it will not do the right thing. It will do something else. Specifically, it will do what you told it to do.

    Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.

