-----------------

In general, you can’t perform mathematical operations on strings, even if the strings look like numbers, so the following are illegal:

    '2'-'1'    'eggs'/'easy'    'third'*'a charm'

But there are two exceptions, <span>+</span> and <span>*</span>.

The <span>+</span> operator performs <span>**string concatenation**</span>, which means it joins the strings by linking them end-to-end. For example:

    >>> first = 'throat'
    >>> second = 'warbler'
    >>> first + second
    throatwarbler

The <span>*</span> operator also works on strings; it performs repetition. For example, `'Spam'*3` is `'SpamSpamSpam'`. If one of the values is a string, the other has to be an integer.

This use of <span>+</span> and <span>*</span> makes sense by analogy with addition and multiplication. Just as <span>4\*3</span> is equivalent to <span>4+4+4</span>, we expect `'Spam'*3` to be the same as `'Spam'+'Spam'+'Spam'`, and it is. On the other hand, there is a significant way in which string concatenation and repetition are different from integer addition and multiplication. Can you think of a property that addition has that string concatenation does not?

