## Tutorial Lab 3: Order of Operations

Python uses PEMDAS when determining the order of operations.

![PEMDAS](.guides/images/pemdas.png)

<details><summary><b>Modulo and PEMDAS</b></summary>Since modulo is based on division, modulo operations happen at the time of multiplication and division, going from left to right.</details>

Use the text editor open in the left pane, and enter the following code:

```python
print(5 * 8 // 3 + (18 - 8) ** 2 - 25)
```

{Try it}(python3 code/operators/lab-order-of-operations.py)

Unfortunately, the [code visualizer](open_tutor code/operators/lab-order-of-operations.py) is not very helpful. It executes an entire line of code, so you will not see the order of operations. Below are the steps that Python takes when evaluating the code above.
1) `5 * 8 // 3 + (18 - 8) ** 2 - 25`
2) `5 * 8 // 3 + 10 ** 2 - 25`
3) `5 * 8 // 3 + 100 - 25`
4) `40 // 3 + 100 - 25`
5) `13 + 100 - 25`
6) `113 - 25`
7) `88`

{Check It!|assessment}(fill-in-the-blanks-1619853519)
