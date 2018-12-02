----------

To explain how hashtables work and why their performance is so good, I start with a simple implementation of a map and gradually improve it until it’s a hashtable.

I use Python to demonstrate these implementations, but in real life you wouldn’t write code like this in Python; you would just use a dictionary! So for the rest of this chapter, you have to imagine that dictionaries don’t exist and you want to implement a data structure that maps from keys to values. The operations you have to implement are:

<span>add(k, v)</span>:
:   Add a new item that maps from key <span>k</span> to value <span>v</span>. With a Python dictionary, <span>d</span>, this operation is written <span>d[k] = v</span>.

<span>get(k)</span>:
:   Look up and return the value that corresponds to key <span>k</span>. With a Python dictionary, <span>d</span>, this operation is written <span>d[k]</span> or <span>d.get(k)</span>.

For now, I assume that each key only appears once. The simplest implementation of this interface uses a list of tuples, where each tuple is a key-value pair.

    class LinearMap:

        def __init__(self):
            self.items = []

        def add(self, k, v):
            self.items.append((k, v))

        def get(self, k):
            for key, val in self.items:
                if key == k:
                    return val
            raise KeyError

<span>add</span> appends a key-value tuple to the list of items, which takes constant time.

<span>get</span> uses a <span>for</span> loop to search the list: if it finds the target key it returns the corresponding value; otherwise it raises a <span>KeyError</span>. So <span>get</span> is linear.

An alternative is to keep the list sorted by key. Then <span>get</span> could use a bisection search, which is $O(\log n)$. But inserting a new item in the middle of a list is linear, so this might not be the best option. There are other data structures that can implement <span>add</span> and <span>get</span> in log time, but that’s still not as good as constant time, so let’s move on.

One way to improve <span>LinearMap</span> is to break the list of key-value pairs into smaller lists. Here’s an implementation called <span>BetterMap</span>, which is a list of 100 LinearMaps. As we’ll see in a second, the order of growth for <span>get</span> is still linear, but <span>BetterMap</span> is a step on the path toward hashtables:

    class BetterMap:

        def __init__(self, n=100):
            self.maps = []
            for i in range(n):
                self.maps.append(LinearMap())

        def find_map(self, k):
            index = hash(k) % len(self.maps)
            return self.maps[index]

        def add(self, k, v):
            m = self.find_map(k)
            m.add(k, v)

        def get(self, k):
            m = self.find_map(k)
            return m.get(k)

`__init__` makes a list of <span>n</span> <span>LinearMap</span>s.

`find_map` is used by <span>add</span> and <span>get</span> to figure out which map to put the new item in, or which map to search.

`find_map` uses the built-in function <span>hash</span>, which takes almost any Python object and returns an integer. A limitation of this implementation is that it only works with hashable keys. Mutable types like lists and dictionaries are unhashable.

Hashable objects that are considered equivalent return the same hash value, but the converse is not necessarily true: two objects with different values can return the same hash value.

`find_map` uses the modulus operator to wrap the hash values into the range from 0 to <span>len(self.maps)</span>, so the result is a legal index into the list. Of course, this means that many different hash values will wrap onto the same index. But if the hash function spreads things out pretty evenly (which is what hash functions are designed to do), then we expect $n/100$ items per LinearMap.

Since the run time of <span>LinearMap.get</span> is proportional to the number of items, we expect BetterMap to be about 100 times faster than LinearMap. The order of growth is still linear, but the leading coefficient is smaller. That’s nice, but still not as good as a hashtable.

Here (finally) is the crucial idea that makes hashtables fast: if you can keep the maximum length of the LinearMaps bounded, <span>LinearMap.get</span> is constant time. All you have to do is keep track of the number of items and when the number of items per LinearMap exceeds a threshold, resize the hashtable by adding more LinearMaps.

Here is an implementation of a hashtable:

    class HashMap:

        def __init__(self):
            self.maps = BetterMap(2)
            self.num = 0

        def get(self, k):
            return self.maps.get(k)

        def add(self, k, v):
            if self.num == len(self.maps.maps):
                self.resize()

            self.maps.add(k, v)
            self.num += 1

        def resize(self):
            new_maps = BetterMap(self.num * 2)

            for m in self.maps.maps:
                for k, v in m.items:
                    new_maps.add(k, v)

            self.maps = new_maps

Each <span>HashMap</span> contains a <span>BetterMap</span>; `__init__` starts with just 2 LinearMaps and initializes <span>num</span>, which keeps track of the number of items.

<span>get</span> just dispatches to <span>BetterMap</span>. The real work happens in <span>add</span>, which checks the number of items and the size of the <span>BetterMap</span>: if they are equal, the average number of items per LinearMap is 1, so it calls <span>resize</span>.

<span>resize</span> make a new <span>BetterMap</span>, twice as big as the previous one, and then “rehashes” the items from the old map to the new.

Rehashing is necessary because changing the number of LinearMaps changes the denominator of the modulus operator in `find_map`. That means that some objects that used to hash into the same LinearMap will get split up (which is what we wanted, right?).

Rehashing is linear, so <span>resize</span> is linear, which might seem bad, since I promised that <span>add</span> would be constant time. But remember that we don’t have to resize every time, so <span>add</span> is usually constant time and only occasionally linear. The total amount of work to run <span>add</span> $n$ times is proportional to $n$, so the average time of each <span>add</span> is constant time!

To see how this works, think about starting with an empty HashTable and adding a sequence of items. We start with 2 LinearMaps, so the first 2 adds are fast (no resizing required). Let’s say that they take one unit of work each. The next add requires a resize, so we have to rehash the first two items (let’s call that 2 more units of work) and then add the third item (one more unit). Adding the next item costs 1 unit, so the total so far is 6 units of work for 4 items.

The next <span>add</span> costs 5 units, but the next three are only one unit each, so the total is 14 units for the first 8 adds.

The next <span>add</span> costs 9 units, but then we can add 7 more before the next resize, so the total is 30 units for the first 16 adds.

After 32 adds, the total cost is 62 units, and I hope you are starting to see a pattern. After $n$ adds, where $n$ is a power of two, the total cost is $2n-2$ units, so the average work per add is a little less than 2 units. When $n$ is a power of two, that’s the best case; for other values of $n$ the average work is a little higher, but that’s not important. The important thing is that it is $O(1)$.

The Figure below shows how this works graphically. Each block represents a unit of work. The columns show the total work for each add in order from left to right: the first two <span>adds</span> cost 1 units, the third costs 3 units, etc.

![image](/.guides/img/towers.jpg)

The extra work of rehashing appears as a sequence of increasingly tall towers with increasing space between them. Now if you knock over the towers, spreading the cost of resizing over all adds, you can see graphically that the total cost after $n$ adds is $2n - 2$.

An important feature of this algorithm is that when we resize the HashTable it grows geometrically; that is, we multiply the size by a constant. If you increase the size arithmetically—adding a fixed number each time—the average time per <span>add</span> is linear.

You can download my implementation of HashMap from <http://thinkpython2.com/code/Map.py>, but remember that there is no reason to use it; if you want a map, just use a Python dictionary.

