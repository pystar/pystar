

.. _dep-gedit-label:

gedit
--------------------

.. _dep-gedit-what-label:

What is ``gedit``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``gedit`` is a cross-platform, syntax-highlighting text editor.

.. _dep-gedit-why-label:

Why do I need ``gedit``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To write your code in!  Word is a fine program, but it is not a text editor.

.. _dep-gedit-how-label:

Get ``gedit``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _dep-gedit-windows-how-label:

* Gedit's main site:  http://projects.gnome.org/gedit/ .  Download links are in the upper right corner.
* (alternate) copy the installer from the Group Guide memory stick.

windows
~~~~~~~~~~~~~~~~~~~~~

http://ftp.gnome.org/pub/GNOME/binaries/win32/gedit/2.30/gedit-setup-2.30.1-1.exe


.. _dep-gedit-Mac OSX-how-label:

Mac OSX
~~~~~~~~~~~~~~~~~~~~~

* http://ftp.gnome.org/pub/GNOME/binaries/mac/gedit/2.30/gedit-2.30.2.dmg
* install using the usual OSX 'DMG' style drag and drop installer.
* add the application to your dock if you are so inclined.


.. _dep-gedit-Linux-how-label:

Linux
~~~~~~~~~~~~~~~~~~~~~

Gedit is probably installed on your machine already.  

* ubuntu/debian:  https://help.ubuntu.com/community/gedit and follow the instructions
* redhat:  ``yum install gedit``
* build form source:  http://ftp.gnome.org/pub/GNOME/sources/gedit/2.30/gedit-2.30.2.tar.gz




.. _dep-gedit-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After installing, start ``gedit`` up by clicking on its icon, typing ``gedit`` from your cli or the like.  

Suggested configuration:

In the preferences window

* **view**, turn on: 
    
    * display line numbers
    * display right margin
    * highlight matching bracket
    * highlight current line
    * syntax-highlighting: Highlight Mode -> Scripts -> Python

* **editor**:

    * change tab with to 4
    * check the box to insert spaces instead of tabs

* **font & colors**:

    * choose a good monospace editor font
    * choose a color scheme (Gregg likes Cobalt)

* **plugins**

    * checkupdate
    * code comment
    * drawspaces
    * filebrowser
    * indentlines
    * python console

Once you are satified, restart ``gedit``.  If it looks similar to the screenshot below, you are done!  

.. image:: /images/configured-gedit.png
