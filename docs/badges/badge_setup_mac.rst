=====================
Setup Mac 
=====================


.. _badge-setup-mac-label:

Your Computer
--------------

.. _badge-setup-mac-what-label:

What is Your Computer?
^^^^^^^^^^^^^^^^^^^^^^^

Your computer is the thing you are reading and typing on :)  You should know
a few things about it before we go much further.

.. _badge-setup-mac-why-label:

Why do I need my Computer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting development work requires at least a passing familiarity with what is
happening inside your machine, what software is installed, and where to look
next for help!

.. _badge-setup-mac-how-label:

Get information about your computer!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Figure out your OS and version
#. An Admin type account is pretty helpful ("Allow user to administer this
   computer")
#. Check to see that you have at least 1 Gb of disk space left.

::
    
    Apple menu (upper left) > About This Mac

.. image:: /images/about_mac.png


.. _badge-setup-mac-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^

Know your OS and version number?  Good!


.. _badge-setup-mac-cli-label:

Command Line Interface
-----------------------

.. _badge-setup-mac-cli-what-label:

What is a Command Line Interface (CLI)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A command line interface (CLI) is way of interacting with a computer by typing
commands. 

.. _badge-setup-mac-cli-why-label:

Why do I need a Command Line Interface (CLI)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many development tools don't have graphic user interfaces--they only have
command line interfaces. 

.. _badge-setup-mac-cli-how-label:

Get a Command Line Interface (CLI)!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Macs come with a command line interface included!

.. _badge-setup-mac-cli-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^

1. Start up a Terminal. You can find the Terminal application through Spotlight, or navigate to `Applications/Utilities/Terminal`. In your terminal, type:

   .. code-block:: bash

      bash --version
  
  Output should look similar to:

   .. code-block:: bash

      $ bash --version
      GNU bash, version 3.2.48(1)-release (x86_64-apple-darwin10.0)
      Copyright (C) 2007 Free Software Foundation, Inc.


.. _badge-setup-mac-terminal-label:

Terminal
--------

While ``Terminal`` is a full-featured utility, its default configuration is a bit poor for programming usage.  Let's configure ``Terminal`` to be a bit more friendly.

1. In your Terminal, copy and paste this command into your terminal and then hit enter.  All this yarnbarf is to enable a colored terminal prompt.
  .. code-block:: bash

    echo "export PS1='\[\e[0;33m\]\u\[\e[0;37m\]\[\e[0;36m\](\W)\[\e[0;0m\]\$ '" >> .bash_profile
2. Click ``Terminal`` in the upper-left hand corner, and go to Preferences.
3. Click on the Settings Section (right of Startup and left of Window Groups)
  a. Highlight the Pro choice in the list on the left, and then click the Default button underneath
4. Click the Window tab (left of Text and right of Shell)
  a. Click the black block left of "Color" and drag the Opacity slider to the right (100%)
  b. Set the number of Rows to 40, under the Window Size section.  Feel free to adjust taller or shorter to taste.
5. Close your Preferences window and terminal, and then go to Shell > New Window

Done properly, your new terminal should look like this:

.. image:: /images/configured-terminal.app.png


.. _badge-setup-mac-gedit-label:

gedit
------

.. _badge-setup-mac-gedit-what-label:

What is ``gedit``?
^^^^^^^^^^^^^^^^^^^

``gedit`` is a cross-platform, syntax-highlighting text editor.

.. _badge-setup-mac-gedit-why-label:

Why do I need ``gedit``?
^^^^^^^^^^^^^^^^^^^^^^^^^

To write your code in!  Word is a fine program, but it is not a text editor.

.. _badge-setup-mac-gedit-how-label:

Get ``gedit``!
^^^^^^^^^^^^^^^

* http://ftp.gnome.org/pub/GNOME/binaries/mac/gedit/2.30/gedit-2.30.2.dmg
* Install using the usual OSX 'DMG' style drag and drop installer.
* Add the application to your dock if you are so inclined.

.. _badge-setup-mac-gedit-verify-label:

.. include:: includes/include_setup_gedit.rst


.. _badge-setup-mac-python-label:

python
--------------------

.. _badge-setup-mac-python-what-label:

What is ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Python is a general purpose, dynamically-typed, strongly-typed, interpreted
computer programming language.  


.. _badge-setup-mac-python-why-label:

Why do I need ``python``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well, this is a Python programming workshop!

.. _badge-setup-mac-python-how-label:

Get ``python``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OS X comes with Python installed!

.. _badge-setup-mac-python-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Start up a Terminal. You can find the Terminal application through Spotlight, or navigate to `/Applications/Utilities/Terminal`
2. Test your Python install at the command prompt. Type python and hit enter. You should see something like::

    Python 2.6.1 (r261:67515, Feb 11 2010, 00:51:29) 
    [GCC 4.2.1 (Apple Inc. build 5646)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Type ``exit()`` to return to your terminal/shell.  Don't worry if your version
is different than the one shown here.  Any 2.x series python 2.5 or higher
(i.e., 2.5, 2.6, 2.7) should be fine!

