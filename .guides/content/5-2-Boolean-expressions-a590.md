-------------------

A <span>**boolean expression**</span> is an expression that is either true or false. The following examples use the operator <span>==</span>, which compares two operands and produces <span>True</span> if they are equal and <span>False</span> otherwise:

    >>> 5 == 5
    True
    >>> 5 == 6
    False

<span>True</span> and <span>False</span> are special values that belong to the type <span>bool</span>; they are not strings:

    >>> type(True)
    <class 'bool'>
    >>> type(False)
    <class 'bool'>

The <span>==</span> operator is one of the <span>**relational operators**</span>; the others are:

          x != y               # x is not equal to y
          x > y                # x is greater than y
          x < y                # x is less than y
          x >= y               # x is greater than or equal to y
          x <= y               # x is less than or equal to y

Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (<span>=</span>) instead of a double equal sign (<span> == </span>). Remember that <span>=</span> is an assignment operator and <span>==</span> is a relational operator. There is no such thing as <span> =\< </span> or <span>=\></span>.

