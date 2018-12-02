-----------------

The syntax for accessing the elements of a list is the same as for accessing the characters of a string—the bracket operator. The expression inside the brackets specifies the index. Remember that the indices start at 0:

    >>> cheeses[0]
    'Cheddar'

Unlike strings, lists are mutable. When the bracket operator appears on the left side of an assignment, it identifies the element of the list that will be assigned.

    >>> numbers = [42, 123]
    >>> numbers[1] = 5
    >>> numbers
    [42, 5]

The one-eth element of <span>numbers</span>, which used to be 123, is now 5.

The figure below shows the state diagram for <span>cheeses</span>, <span>numbers</span> and <span>empty</span>:

![image](/.guides/img/liststate.jpg)



Lists are represented by boxes with the word “list” outside and the elements of the list inside. <span>cheeses</span> refers to a list with three elements indexed 0, 1 and 2. <span>numbers</span> contains two elements; the diagram shows that the value of the second element has been reassigned from 123 to 5. <span>`empty`</span> refers to a list with no elements.

List indices work the same way as string indices:

-   Any integer expression can be used as an index.

-   If you try to read or write an element that does not exist, you get an <span>IndexError</span>.

-   If an index has a negative value, it counts backward from the end of the list.

The <span>`in`</span> operator also works on lists.

    >>> cheeses = ['Cheddar', 'Edam', 'Gouda']
    >>> 'Edam' in cheeses
    True
    >>> 'Brie' in cheeses
    False

