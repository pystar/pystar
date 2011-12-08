=====================
Setup Windows
=====================


.. _badge-setup-win-label:

Your Computer
--------------

.. _badge-setup-win-what-label:

What is Your Computer?
^^^^^^^^^^^^^^^^^^^^^^^

Your computer is the thing you are reading and typing on :)  You should know
a few things about it before we go much further.

.. _badge-setup-win-why-label:

Why do I need my Computer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting development work requires at least a passing familiarity with what is
happening inside your machine, what software is installed, and where to look
next for help!

.. _badge-setup-win-how-label:

Get information about your computer!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Figure out your OS and version
#. An Administrator type account is pretty helpful
#. Check to see that you have at least 1 Gb of disk space left.

::
    
    Control Panel > System 


.. image:: /images/windows_sys.jpg

.. _badge-setup-win-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^

Know your OS and version number?  Good!


.. _badge-setup-win-cli-label:

Command Line Interface
-----------------------

.. _badge-setup-win-cli-what-label:

What is a Command Line Interface (CLI)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A command line interface (CLI) is way of interacting with a computer by typing
commands.

.. _badge-setup-win-cli-why-label:

Why do I need a Command Line Interface (CLI)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many development tools don't have graphic user interfaces--they only have
command line interfaces. Windows comes with a command line interface called a command prompt.  Unfortunately, it does not support all of the tools we want to use.

.. _badge-setup-win-cli-how-label:

Get a Command Line Interface (CLI)!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. One of the easiest ways to get all the tools at once is from mysysGit
#. Download and install **msysGit-fullinstall** from http://code.google.com/p/msysgit/downloads/list
#. This will install MSYS/Mingw/GitBash (it has many names!).  

..  note::

    If you are not an administrator on your machine, you might
    have to choose an alternate path for install rather than ``C:\Git``,
    such as ``C:\Documents and Settings\yourname\Git\``.

    You will also want to make the MSYS/MINGW bash window behave in a saner 
    way.  After opening it, 'right-click' on the title bar, and select 
    'properties'.  Under 'Edit Options', enable 'Quick Edit Mode'.


.. _badge-setup-win-cli-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^

In your command window:

.. code-block:: bash

   $ bash --version


.. _badge-setup-win-gedit-label:

gedit
------

.. _badge-setup-win-gedit-what-label:

What is ``gedit``?
^^^^^^^^^^^^^^^^^^^

``gedit`` is a cross-platform, syntax-highlighting text editor.

.. _badge-setup-win-gedit-why-label:

Why do I need ``gedit``?
^^^^^^^^^^^^^^^^^^^^^^^^^

To write your code in!  Word is a fine program, but it is not a text editor.

.. _badge-setup-win-gedit-how-label:

Get ``gedit``!
^^^^^^^^^^^^^^^

* http://ftp.gnome.org/pub/GNOME/binaries/win32/gedit/2.30/gedit-setup-2.30.1-1.exe

.. _badge-setup-win-gedit-verify-label:

.. include:: includes/include_setup_gedit.rst


.. _badge-setup-win-python-label:

python
--------------------

.. _badge-setup-win-python-what-label:

What is ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Python is a general purpose, dynamically-typed, strongly-typed, interpreted
computer programming language.  


.. _badge-setup-win-python-why-label:

Why do I need ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well, this is a Python progammming workshop!

.. _badge-setup-win-python-how-label:

Get ``python``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. code-block:: bash  

    $ echo '#!/bin/sh' > /bin/python
    $ echo 'C:/Python27/python.exe $*' >> /bin/python
    $ echo 'export PATH=$PATH:/c/Python27/Scripts' > ~/.profile
    $ source ~/.profile

From here on, if you are in the msys/mgit/mingw cli, you can type ``python`` 
to get a python prompt, should you need one!

.. _badge-setup-win-python-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After install, show your guide that use can start up ``python``.  You should 
see something like::

    Python 2.7.1 (r271:86832, ...) on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Type ``exit()`` to return to your terminal/shell.  Don't worry if your version
is different than the one shown here.  Any 2.x series python 2.5 or higher
(i.e., 2.5, 2.6, 2.7) should be fine!

