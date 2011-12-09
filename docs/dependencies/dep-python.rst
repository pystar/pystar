

.. _dep-python-label:

python
--------------------

.. _dep-python-what-label:

What is ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Python is a general purpose, dynamically-typed, strongly-typed, interpreted
computer programming language.  


.. _dep-python-why-label:

Why do I need ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well, this is a Python progammming workshop!

.. _dep-python-how-label:

Get ``python``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. _dep-python-windows-how-label:

windows
~~~~~~~~~~~~~~~~~~~~~


1. Go to http://python.org/download/ and download the latest version of Python 2.7 (2.7.1 at the time of writing). Unless you know otherwise, get the "Windows Installer" version, and not the "Windows X86-64 Installer" version.

2. Start up a command prompt by clicking on the Start menu, clicking the ``Run...`` option, typing ``cmd``, and hitting enter. If you are using Windows Vista, you should click on the Start menu, type ``cmd`` into the Search field directly above the Start menu button, and click on ``cmd`` in the search results above the Search field.

Test your Python install by typing ``\Python27\python.exe``
and hitting enter. You should see something like::

    Python 2.7.1 (r271:86832, ...) on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

To exit the Python prompt, type ``exit()`` and press Enter. This will take you back to the Windows command prompt.

We also would like to make sure our python is available from the msys/mgit/mingw cli.  
After starting up msys/mgit:

::  

    $ echo '#!/bin/sh' > /bin/python
    $ echo 'C:/Python27/python.exe $*' >> /bin/python
    $ echo 'export PATH=$PATH:/c/Python27/Scripts' > ~/.profile
    $ source ~/.profile

From here on, if you are in the msys/mgit/mingw cli, you can type ``python`` 
to get a python prompt, should you need one!



.. _dep-python-Mac OSX-how-label:

Mac OSX
~~~~~~~~~~~~~~~~~~~~~

OS X ships with Python installed, so the goal of this page is to make sure you can start a Terminal and run Python from the command line.

1. Start up a Terminal. You can find the Terminal application through Spotlight, or navigate to Applications/Utilities/Terminal
2. Test your Python install at the command prompt. Type python and hit enter. You should see something like::

    Python 2.6.1 (r261:67515, Feb 11 2010, 00:51:29) 
    [GCC 4.2.1 (Apple Inc. build 5646)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>



.. _dep-python-Linux-how-label:

Linux
~~~~~~~~~~~~~~~~~~~~~

Linux ships with Python installed, so the goal of this page is to make sure you can start a terminal and run Python from the command line.

1. Start up a terminal. You can find the Terminal application at `Applications/Accessories/Terminal`, or it may already be on your menu bar.
2. Test your Python install at the command prompt. Type ``python`` and hit enter. You should see something like::

    Python 2.5.2 (r252:60911, Jan 24 2010, 17:44:40) 
    [GCC 4.3.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

To exit the Python prompt, type ``exit()``
and press Enter. This will take you back to the Terminal command prompt.




.. _dep-python-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After install, show your guide that use can start up ``python``.  You should 
see something like::

    Python 2.6.1 (r261:67515, Feb 11 2010, 00:51:29) 
    [GCC 4.2.1 (Apple Inc. build 5646)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Type ``exit()`` to return to your terminal/shell.  Don't worry if your version
is different than the one shown here.  Any 2.x series python 2.5 or higher
(i.e., 2.5, 2.6, 2.7) should be fine!




