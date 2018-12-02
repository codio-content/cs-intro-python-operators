If the interpreter says there is an error and you don’t see it, that might be because you and the interpreter are not looking at the same code. Check your programming environment to make sure that the program you are editing is the one Python is trying to run.

If you are not sure, try putting an obvious and deliberate syntax error at the beginning of the program. Now run it again. If the interpreter doesn’t find the new error, you are not
running the new code.

There are a few likely culprits:
- You edited the file and forgot to save the changes before running it again. Some programming environments do this for you, but some don’t.
- You changed the name of the file, but you are still running the old name.
- Something in your development environment is configured incorrectly.
- If you are writing a module and using import, make sure you don’t give your module the same name as one of the standard Python modules.
- If you are using import to read a module, remember that you have to restart the interpreter or use reload to read a modified file. If you import the module again, it doesn’t do anything.

If you get stuck and you can’t figure out what is going on, one approach is to start again with a new program like “Hello, World!”, and make sure you can get a known program to run. Then gradually add the pieces of the original program to the new one.