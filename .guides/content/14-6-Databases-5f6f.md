---------

A <span>**database**</span> is a file that is organized for storing data. Many databases are organized like a dictionary in the sense that they map from keys to values. The biggest difference between a database and a dictionary is that the database is on disk (or other permanent storage), so it persists after the program ends.

The module <span>dbm</span> provides an interface for creating and updating database files. As an example, I’ll create a database that contains captions for image files.

Opening a database is similar to opening other files:

    >>> import dbm
    >>> db = dbm.open('captions', 'c')

The mode `'c'` means that the database should be created if it doesn’t already exist. The result is a database object that can be used (for most operations) like a dictionary.

When you create a new item, <span>dbm</span> updates the database file.

    >>> db['cleese.png'] = 'Photo of John Cleese.'

When you access one of the items, <span>dbm</span> reads the file:

    >>> db['cleese.png']
    b'Photo of John Cleese.'

The result is a <span>**bytes object**</span>, which is why it begins with <span>b</span>. A bytes object is similar to a string in many ways. When you get farther into Python, the difference becomes important, but for now we can ignore it.

If you make another assignment to an existing key, <span>dbm</span> replaces the old value:

    >>> db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
    >>> db['cleese.png']
    b'Photo of John Cleese doing a silly walk.'

Some dictionary methods, like <span>keys</span> and <span>items</span>, don’t work with database objects. But iteration with a <span>for</span> loop works:

    for key in db:
        print(key, db[key])

As with other files, you should close the database when you are done:

    >>> db.close()

