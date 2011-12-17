.. _badge_python_data_types:

===========================
Tour The Python Data Types!
===========================

Try these in your own Python interactive shell:

.. code-block:: bash

    $ python

Numbers
-------

Addition

.. code-block:: bash

    >>> 2 + 2
    4

Subtraction

.. code-block:: bash

    >>> 0 - 2
    -2

Multiplication

.. code-block:: bash

    >>> 2 * 3
    6

Division

.. code-block:: bash

    >>> 4 / 2
    2
    >>> 1 / 2
    0

Integer divison produces an integer. You need a number that knows
about the decimal point to get a decimal out of division:

.. code-block:: bash

    >>> 1.0 / 2
    0.5
    >>> float(1) / 2
    0.5

Remainder (Modulo)

.. code-block:: bash

    >>> 4 % 2
    0
    >>> 4 % 3
    1

Types

.. code-block:: bash

    >>> type(1)
    <type 'int'>
    >>> type(1.0)
    <type 'float'>

Strings
-------

.. code-block:: bash

    >>> "Hello"
    'Hello'

Printing strings

.. code-block:: bash

    >>> print "Hello"
    Hello

String concatenation

.. code-block:: bash

    >>> print "Hello" + "World"
    HelloWorld

    >>> print "Hello", "World"
    Hello World

Printing different data types together

.. code-block:: bash

    >>> print "Hello", "World", 1
    Hello World 1

String formatting

.. code-block:: bash

    >>> print "Hello %d" % (1,)
    Hello 1
    >>> print "Hello %s" % ("World",)
    Hello World

    >>> type("Hello")
    <type 'str'>

Lists
-----

List initialization

.. code-block:: bash

    >>> my_list = list()
    >>> my_list 
    []
    >>> your_list = []
    >>> your_list
    []
    >>> her_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    >>> her_list
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

Access and adding elements to a list

.. code-block:: bash

    >>> len(my_list)
    0
    >>> my_list[0]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    >>> my_list.append("Alice")
    >>> my_list
    ['Alice']
    >>> len(my_list)
    1
    >>> my_list[0]
    'Alice'
    >>> my_list.insert(0, "Amy")
    >>> my_list
    ['Amy', 'Alice']

Changing elements in a list

.. code-block:: bash

    >>> your_list.append("apples")
    >>> your_list[0]
    'apples'
    >>> your_list[0] = "bananas"
    >>> your_list
    ['bananas']

Slicing lists

.. code-block:: bash

    >>> her_list
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> her_list[0]
    'a'
    >>> her_list[0:3]
    ['a', 'b', 'c']
    >>> her_list[:3]
    ['a', 'b', 'c']
    >>> her_list[-1]
    'h'
    >>> her_list[5:]
    ['f', 'g', 'h']
    >>> her_list[:]
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

Sharing versus copying:
Sharing

.. code-block:: bash

    >>> my_list
    ['Alice']
    >>> your_list = my_list
    >>> your_list
    ['Alice']
    >>> my_list[0] = "Bob"
    >>> my_list
    ['Bob']
    >>> your_list
    ['Bob']

Copying

.. code-block:: bash

    >>> my_list
    ['Alice']
    >>> your_list = my_list[:]
    >>> my_list[0] = "Bob"
    >>> my_list
    ['Bob']
    >>> your_list
    ['Alice']

Strings can be manipulated like lists

.. code-block:: bash

    >>> my_string = "Hello World"
    >>> my_string[0]
    'H'
    >>> my_string[:5]
    'Hello'
    >>> my_string[6:]
    'World'
    >>> my_string[6:] = "Jessica"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    >>> my_string = my_string[:6] + "Jessica"
    >>> my_string
    'Hello Jessica'

    >>> type(my_string)
    <type 'str'>

Dictionaries
------------

Dictionary initialization

.. code-block:: bash

    >>> my_dict = dict()
    >>> your_dict = {}
    >>> her_dict = {"Alice" : "chocolate", "Bob" : "strawberry", "Cara" : "mint chip"}
    >>> her_dict
    {'Bob': 'strawberry', 'Cara': 'mint chip', 'Alice': 'chocolate'}

Adding elements

.. code-block:: bash

    >>> her_dict["Dora"] = "vanilla"
    >>> her_dict
    {'Bob': 'strawberry', 'Cara': 'mint chip', 'Dora': 'vanilla', 'Alice': 'chocolate'}

Accessing elements

.. code-block:: bash

    >>> her_dict["Alice"] 
    'chocolate'
    >>> her_dict.get("Alice")
    'chocolate'

    >>> her_dict["Eve"]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'Eve'
    >>> "Eve" in her_dict
    False
    >>> "Alice" in her_dict
    True
    >>> her_dict.get("Eve")
    >>> her_dict.get("Alice")
    'chocolate'

Changing elements

.. code-block:: bash

    >>> her_dict["Alice"] = "coconut"
    >>> her_dict
    {'Bob': 'strawberry', 'Cara': 'mint chip', 'Dora': 'vanilla', 'Alice': 'coconut'}

    >>> type(my_dict)
    <type 'dict'>
    
    >>> her_dict.get("Alice")
    'coconut'

Tuples
------

Initialization

.. code-block:: bash

    >>> tuple()
    ()
    >>> ("apple", "oranges", "bananas")
    ('apple', 'oranges', 'bananas')
    >>> my_tuple = ("apple", "oranges", "bananas")

Accessing elements of a tuple: just like lists

.. code-block:: bash

    >>> my_tuple = ("apple", "oranges", "bananas")
    >>> my_tuple[0]
    'apple'
    >>> len(my_tuple)
    3
    >>> my_tuple[-1]
    'bananas'
    >>> my_tuple[:2]
    ('apple', 'oranges')

Adding or changing elements of a tuple: can't do it! Not a mutable data type.

.. code-block:: bash

    >>> my_tuple[:2]
    ('apple', 'oranges')
    >>> my_tuple[0] = "figs"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

    >>> type(my_tuple)
    <type 'tuple'>
