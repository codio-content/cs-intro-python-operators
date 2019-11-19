## Tutorial Lab 1: Using the for loop
Use the text editor open in the left pane, and enter the following code:

```python
for x in range(0, 10):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

[Code Visualizer](open_tutor code/loops/lab-1.py)
{Try it}(python3 code/loops/lab-1.py)

1) The for loop runs through all the values from 0 to 10, specified in the range command.
2) Then a comparison is made using an if statement.
3) If `x` modulo 2 results in 0, then print `Even`.
4) If `x` modulo 2 is any other number that is not 0, then print `Odd`.

{Check It!|assessment}(parsons-puzzle-3300199222)
