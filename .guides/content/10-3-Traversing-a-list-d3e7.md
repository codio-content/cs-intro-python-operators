-----------------

The most common way to traverse the elements of a list is with a <span>for</span> loop. The syntax is the same as for strings:

    for cheese in cheeses:
        print(cheese)

This works well if you only need to read the elements of the list. But if you want to write or update the elements, you need the indices. A common way to do that is to combine the built-in functions <span>`range`</span> and <span>`len`</span>:

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2

This loop traverses the list and updates each element. <span>len</span> returns the number of elements in the list. <span>range</span> returns a list of indices from 0 to $n-1$, where $n$ is the length of the list. Each time through the loop <span>i</span> gets the index of the next element. The assignment statement in the body uses <span>i</span> to read the old value of the element and to assign the new value.

A <span>for</span> loop over an empty list never runs the body:

    for x in []:
        print('This never happens.')

Although a list can contain another list, the nested list still counts as a single element. The length of this list is four:

    ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

