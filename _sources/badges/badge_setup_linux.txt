=====================
Setup Linux
=====================


.. _badge-setup-linux-label:

Your Computer
--------------

.. _badge-setup-linux-what-label:

What is Your Computer?
^^^^^^^^^^^^^^^^^^^^^^^

Your computer is the thing you are reading and typing on :)  You should know
a few things about it before we go much further.

.. _badge-setup-linux-why-label:

Why do I need my Computer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting development work requires at least a passing familiarity with what is
happening inside your machine, what software is installed, and where to look
next for help!

.. _badge-setup-linux-how-label:

Get information about your computer!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Figure out your OS and version
#. sudo privilege is pretty helpful
#. Check to see that you have at least 1 Gb of disk space left.
#. Start up a terminal. You can find the Terminal application at `Applications/Accessories/Terminal`, or it may already be on your menu bar. In your terminal:

   .. code-block:: bash

      $ uname -a 

.. _badge-setup-linux-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^

Know your OS and version number?  Good!


.. _badge-setup-linux-cli-label:

Command Line Interface
-----------------------

.. _badge-setup-linux-cli-what-label:

What is a Command Line Interface (CLI)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A command line interface (CLI) is way of interacting with a computer by typing
commands. DOS is an example of a command line interface. 

.. _badge-setup-linux-cli-why-label:

Why do I need a Command Line Interface (CLI)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many development tools don't have graphic user interfaces--they only have
command line interfaces. 

.. _badge-setup-linux-cli-how-label:

Get a Command Line Interface (CLI)!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Linux comes with a command line interface included!
#. The program used to access the CLI is often called a "terminal".


.. _badge-setup-linux-cli-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^

Start up a terminal. You can find the Terminal application at `Applications/Accessories/Terminal`, or it may already be on your menu bar. In your terminal:

.. code-block:: bash

   $ bash --version


.. _badge-setup-linux-gedit-label:

gedit
------

.. _badge-setup-linux-gedit-what-label:

What is ``gedit``?
^^^^^^^^^^^^^^^^^^^

``gedit`` is a cross-platform, syntax-highlighting text editor.

.. _badge-setup-linux-gedit-why-label:

Why do I need ``gedit``?
^^^^^^^^^^^^^^^^^^^^^^^^^

To write your code in!  Word is a fine program, but it is not a text editor.

.. _badge-setup-linux-gedit-how-label:

Get ``gedit``!
^^^^^^^^^^^^^^^

Gedit is probably installed on your machine already.  

* Ubuntu/Debian:  https://help.ubuntu.com/community/gedit and follow the instructions
* Redhat:  ``yum install gedit``
* Build form source:  http://ftp.gnome.org/pub/GNOME/sources/gedit/2.30/gedit-2.30.2.tar.gz

.. _badge-setup-linux-gedit-verify-label:

.. include:: includes/include_setup_gedit.rst


.. _badge-setup-linux-python-label:

python
--------------------

.. _badge-setup-linux-python-what-label:

What is ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python is a general purpose, dynamically-typed, strongly-typed, interpreted
computer programming language.  

.. _badge-setup-linux-python-why-label:

Why do I need ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well, this is a Python progammming workshop!

.. _badge-setup-linux-python-how-label:

Get ``python``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Linux comes with Python installed!

.. _badge-setup-linux-python-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Start up a terminal. You can find the Terminal application at `Applications/Accessories/Terminal`, or it may already be on your menu bar.
2. Test your Python install at the command prompt. Type ``python`` and hit enter. You should see something like::

    Python 2.5.2 (r252:60911, Jan 24 2010, 17:44:40) 
    [GCC 4.3.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

To exit the Python prompt, type ``exit()``
and press Enter. This will take you back to the Terminal command prompt.

