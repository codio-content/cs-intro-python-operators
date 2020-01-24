----------
Using your knowledge of for loops, try and recreate the images you see below. Remember, click on the tab that reads **Preview https/...** to see your output. Close the window with the turtle output to stop your program.

<details><summary>*Customize your turtle*</summary><ul><li>`t.color('red')` - Takes a string for the [color](https://www.w3schools.com/colors/colors_names.asp)</li><li>`t.shape('turtle')` - Takes one of the following strings `'turtle'`, `'circle'`, `'square'`, `'arrow'`, `'classic'`, or `'triangle'`.<li>`t.pensize(4)` - Takes a positive number</li><li>`t.speed(1)` - Takes a number in the range 0..10</li></ul></details>

### Challenge 1
![Turtle Challenge 1](.guides/images/turtle-challenge-1.png)
{Try it}(bash .guides/bg.sh python3 code/loops/playground-turtle-2.py)

<details><summary>**Hint**</summary>The trick is to find the pattern and then repeat it four times. The pattern is to go forward and then make a smaller square (with right turns) at the end. The pattern should look something like this: <img src=".guides/images/turtle-graphics-pattern-1.png"/></details>

### Challenge 2
![Turtle Challenge 2](.guides/images/turtle-challenge-2.png)
{Try it}(bash .guides/bg.sh python3 code/loops/playground-turtle-2.py 2)

<details><summary>**Hint**</summary>Since a circle has 360 degrees, you will need a loop that repeats 360 times. Be careful about how far the turtle walks. The circle can get very big, very quickly.</details>

### Challenge 3
![Turtle Challenge 3](.guides/images/turtle-challenge-3.png)
{Try it}(bash .guides/bg.sh python3 code/loops/playground-turtle-2.py 3)

<details><summary>**Hint**</summary>The pattern here is to move forward and make a right turn. The trick is, the amount to move forward needs to get bigger as the loop advances. Think of some operators that you can use to make the loop variable get a little bit bigger each iteration.</details>