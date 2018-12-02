------------------

Sometimes you don’t know it’s time to end a loop until you get half way through the body. In that case you can use the <span>break</span> statement to jump out of the loop.

For example, suppose you want to take input from the user until they type <span>done</span>. You could write:

    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)

    print('Done!')

The loop condition is <span>True</span>, which is always true, so the loop runs until it hits the break statement.

Each time through, it prompts the user with an angle bracket. If the user types <span>done</span>, the <span>break</span> statement exits the loop. Otherwise the program echoes whatever the user types and goes back to the top of the loop. Here’s a sample run:

    > not done
    not done
    > done
    Done!

This way of writing <span>while</span> loops is common because you can check the condition anywhere in the loop (not just at the top) and you can express the stop condition affirmatively (“stop when this happens”) rather than negatively (“keep going until that happens”).

