----------

## Division

Division in Python is done with the `/` operator

```python
a = 25
b = 5
print(a / b)
```

{try it}(python3 code/operators/playground-division.py 1)

|||challenge
## What happens if you:
* Change `b` to `0`?
* Change `b` to `True`?
* Change `b` to `0.5`?
* Change the code to
```python
a = 25
b = 5
a /= b
print(a)
```

|||

{try it}(python3 code/operators/playground-division.py 2)

<details><summary><b>Reminder</b></summary><ul><li><code>/=</code> works similar to <code>+=</code> and <code>-=</code></li><li><code>True</code> has the value of 1</li><li><code>False</code> has the value of 0</li></ul></details>

## Floor Division

Normal division in Python always returns a float. If you want an integer, use floor division (`//`). Floor division does not round up, nor round down. It removes the decimal value from the answer.

![Floor Division](.guides/images/floor-division.png)

```python
a = 5
b = 2
print(a // b)
```

{try it}(python3 code/operators/playground-division.py 3)

{Check It!|assessment}(multiple-choice-2775133348)
