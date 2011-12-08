Command Line Navigation
================================

This badge is to learn how to navigate using the command line (CLI).

    .. note:

        The command line is case sensitive. 

Commands
--------

Commands used when navigating in the CLI:

* cd
* ls
* mkdir
* pwd

Concepts
---------

Navigation requires an understanding of the above commands and of file system paths, both relative and absolute.

Absolute power corrupts absolutely
....................................

Absolute paths are the full name to a file or directory starting from root.

If I want to navigate to a folder in my Documents folder (on a Mac), the absolute path would look something like::

    $ cd /Users/Amanda/Documents/Thesis/

It's all relative
..................

Relative paths are partial path names relative to where you are in the directory structure.

If I am in ``/Users/Amanda``, then the way to get to my Thesis folder using the relative path would look something like::

    $ cd Documents/Thesis

If I am in my Thesis folder and I want to move to a different folder within my Documents directory, I would do something like::

    $ cd ../IF

The double dot notation is shorthand for "go up a directory," which is this case is Documents. From there, I can then go down into my IF directory (and play some text adventure games).

Here is a more complicated example: from my IF directory, I could get to a folder of pictures in my Pictures directory (absolute path: /Users/Amanda/Pictures/atlanta) by typing::

    $ cd ../../Pictures/atlanta/

The first ``..`` takes me up to Documents, the second ``..`` takes me up to my user directory (Amanda) and from there I can go down into Pictures and then into atlanta.

Do
--

Open a command line window. Explore your file system in the CLI using the following commands and using absolute and relative path names:

* ls
* pwd
* cd

``ls`` means "list" and it will show you the list of files in the directory you are in. Try using some optional arguments such as ``-a``, ``-p``, or ``-l``. What do they show you that just running ``ls`` without arguments doesn't?

``pwd`` means "print working directory," which is fairly self explainitory. Try typing it in different directories. What does it return?

``cd`` means "change directory," which is also fairly self explainitory. Try typing in ``cd`` by itself. Where does it bring you? Try navigating to a directory within your files system and list the files in that directory. Use absolute and relative paths to visit several different directories on your file system.

Done
----

Here's an example of what your CLI screen might look like after completing the above work:

.. code-block:: bash

    amanda-nyrens-macbook-pro:~ Amanda$ pwd
    /Users/Amanda
    amanda-nyrens-macbook-pro:~ Amanda$ ls
    Calibre Library	Documents	Icon?		Movies		Pictures	Sites		VirtualBox VMs
    Desktop		Downloads	Library		Music		Public		Speelies	mydir
    amanda-nyrens-macbook-pro:~ Amanda$ cd Desktop/
    amanda-nyrens-macbook-pro:Desktop Amanda$ ls
    command.txt	git-amanda	pystar		python
    amanda-nyrens-macbook-pro:Desktop Amanda$ ls -l
    total 424
    -rw-rw-rw-   1 Amanda  staff  213063 Jul 27  1999 command.txt
    drwxr-xr-x   6 Amanda  staff     204 Mar 22 16:18 git-amanda
    drwxr-xr-x   7 Amanda  staff     238 Apr  9 09:31 pystar
    drwxr-xr-x  33 Amanda  staff    1122 Apr  9 09:23 python
    amanda-nyrens-macbook-pro:Desktop Amanda$ cd git-amanda/pystar_amanda/
    amanda-nyrens-macbook-pro:pystar_amanda Amanda$ ls -a
    .		..		.DS_Store	.git		README.rst	docs		utils		web
    amanda-nyrens-macbook-pro:pystar_amanda Amanda$ pwd
    /Users/Amanda/Desktop/git-amanda/pystar_amanda
    amanda-nyrens-macbook-pro:pystar_amanda Amanda$ cd ../../../Documents/Thesis/
    amanda-nyrens-macbook-pro:Thesis Amanda$ ls -lrt
    total 86920
    -rwxrwxrwx@  1 Amanda  staff     24576 Oct  4  2005 thesis proposal.doc
    -rw-r--r--@  1 Amanda  staff  12562780 Feb 15  2006 ES2e-CH18.pdf
    -rw-rw----   1 Amanda  staff      4197 Mar  8  2006 thesis references-Converted.txt
    -rw-r--r--@  1 Amanda  staff   3475730 Mar  9  2006 chester_2003.pdf
    -rw-r--r--@  1 Amanda  staff    908091 Mar  9  2006 evaluating sand and clay models.pdf
    -rw-r--r--@  1 Amanda  staff     34304 Mar 19  2006 thesis budget.xls
    -rw-r--r--@  1 Amanda  staff         0 Mar 24  2006 Icon?
    -rw-r--r--@  1 Amanda  staff     37376 Mar 29  2006 Manuscript preparation WORD.doc
    -rw-r--r--@  1 Amanda  staff     31744 Mar 29  2006 Remaining Important Dates for Departmental Honors Students 2005-06.doc
    -rw-r--r--@  1 Amanda  staff   3064448 Apr  9  2006 storti salvini mcclay.pdf
    -rwxrwxrwx@  1 Amanda  staff     39424 Apr 13  2006 thrust analysis.xls
    -rw-r--r--@  1 Amanda  staff   9557504 Apr 30  2006 Thesis.doc
    drwxr-xr-x  38 Amanda  staff      1292 Apr 30  2006 Images
    -rw-r--r--@  1 Amanda  staff  14669824 May  7  2006 thesis.ppt
    amanda-nyrens-macbook-pro:Thesis Amanda$ pwd
    /Users/Amanda/Documents/Thesis
    amanda-nyrens-macbook-pro:Thesis Amanda$ 






