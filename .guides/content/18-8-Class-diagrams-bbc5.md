--------------

So far we have seen stack diagrams, which show the state of a program, and object diagrams, which show the attributes of an object and their values. These diagrams represent a snapshot in the execution of a program, so they change as the program runs.

They are also highly detailed; for some purposes, too detailed. A class diagram is a more abstract representation of the structure of a program. Instead of showing individual objects, it shows classes and the relationships between them.

There are several kinds of relationship between classes:

-   Objects in one class might contain references to objects in another class. For example, each Rectangle contains a reference to a Point, and each Deck contains references to many Cards. This kind of relationship is called <span>**HAS-A**</span>, as in, “a Rectangle has a Point.”

-   One class might inherit from another. This relationship is called <span>**IS-A**</span>, as in, “a Hand is a kind of a Deck.”

-   One class might depend on another in the sense that objects in one class take objects in the second class as parameters, or use objects in the second class as part of a computation. This kind of relationship is called a <span>**dependency**</span>.

A <span>**class diagram**</span> is a graphical representation of these relationships. For example, the Figure below shows the relationships between <span>Card</span>, <span>Deck</span> and <span>Hand</span>.

![image](/.guides/img/class1.jpg)



The arrow with a hollow triangle head represents an IS-A relationship; in this case it indicates that Hand inherits from Deck.

The standard arrow head represents a HAS-A relationship; in this case a Deck has references to Card objects.

The star (<span>`*`</span>) near the arrow head is a <span>**multiplicity**</span>; it indicates how many Cards a Deck has. A multiplicity can be a simple number, like <span>52</span>, a range, like <span>5..7</span> or a star, which indicates that a Deck can have any number of Cards.

There are no dependencies in this diagram. They would normally be shown with a dashed arrow. Or if there are a lot of dependencies, they are sometimes omitted.

A more detailed diagram might show that a Deck actually contains a <span>*list*</span> of Cards, but built-in types like list and dict are usually not included in class diagrams.

