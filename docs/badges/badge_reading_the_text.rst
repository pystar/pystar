.. badge_reading_the_text:

=========================================
Reading the Text and Secret Handshakes
=========================================

The computer is exact, authors are not.  
Authors are lazy and sloppy, so mistakes slip though.
We hope these common text conventions and text idioms will help you understand
what the authors probably *meant*.

:: 

    # this is a comment, in bash, python, and many other languages.
    # comments can be multiline
    
    /* in some languages, comments look like this */

    # '$' implies a 'unix/terminal/bash' prompt
    $ mycommand  # <- you would type [mycommand] at your prompt.

    # typically, if a line starts with '$ ' (note the space!)
    # you type the rest of the line *as is*.
    # and the output is given without a $.... 
    $ pwd
    /home/pystar/project/here

    # note that the '$ ' is shorthand for *your prompt*,
    # and you don't actually type the '$ ' 


.. code-block:: python

    >>> # remember, '#' is a comment line in python too
    >>> # the 'triple chevron' implies a 'python command line'
    >>> # you might get this line from your prompt by
    >>> # typing ->  $ python
    >>> "a string"
    'a string'
    >>> # don't type the chevrons!  


``keyboard font``
    type the command as written, substituting in for things like ``mydir``
    as appropraite.  

foo, bar, /some/path, some_function, some_var
    standard 'fake' or 'generic' variables, methods, variables

your_function, yourname, mylogin
    `your` and `my` tend to imply *whatever it is you chose*.  

> File > Print Preview
    Typically *single chevron* implies heirarchical nesting.  Most commonly,
    this is used when describing GUI (graphical user interface) commands.

prompt
    Can mean either the python promt, or command line prompt


unix / bash / terminal / shell / command line / CLI
    For the purposes of these tutorials, these all mean 'the command
    line bit where you interact with the system.  Authors tend to be
    sloppy and conflate these.  

home directory
    On UNIX-like systems, where 'your stuff' lives.  Typically written with
    the tilde ``~`` character.  Often, the ``cd`` command will take you to
    your home directory.  

    Ex:  ``~someuser`` might expand to ``/Users/someuser`` (on OSX).   


Learn the Keyboard!
--------------------

:: 

    symbol   name (in programming)
    =======  ==============================
    #        octothorpe, hash, pound
    ()       parens, parentheses
    {}       left and right brace
    []       left and right bracket
    <>       greater than, less than
    ~        tilde
    `        backtick, backquote
    ''       quote
    ""       double quote
    -        dash,hyphen (for programmers)
    /        slash, forward slash
    \        backslash
    !        bang, exclamation point
    |        pipe (vertical bar)
    *        star, asterisk
    =======  ==============================


Common Actions
------------------

navigate (or 'go to')
    #.  in a web context: open a url in your browser, or follow some link
        by clicking.  
        
        ex.:  Navigate to localhost -> (open http://localhost/ )

    #.  at the prompt:  ``cd`` or *change directory* to some path.
        
        ex.:  "Go to your project directory" -> ``$ cd ~yourname/yourproject``

edit
    open the file in your text editor of choice (Gedit, Vim, TextEdit, XCode, etc.)

save
    save the file to the file system.  

commit
    add and commit the files (or equivalent) in your source control system.
    (git, mercurial/hg, svn  and friends)

    ::

        # in git, for example
        git add yourfile
        git commit -m "some message"

explore
    #.  in a web context:  look around at the page, see what links are there.
        Alt., ``view source`` (often by 'right-clicking' on a web page).

    #.  In a CLI context, use commands like ``pwd``, ``ls`` and friends
        to see what files are in a directory, how large they are (using ``ls -l``),
        etc.  When doing so, one should be thinking about why those files 
        are there, what they do, etc.

    #.  In a Python context, use ``dir(mything)``, ``help(mything)``, 
        ``print mything`` and the like to discover its properties and values.  


Check your Understanding
-----------------------------

#.  Which of these are unix commands, and which are Python commands?

    #. ``$ ls``
    #. ``>>> import time``
    #. ``# I don't know what is going on here!``

    ..  container:: answer-hidden
        
        #. unix (bash). 
        #. python.  it imports the ``time`` module.
        #. could be either :).  It's a comment, in any case!  

#.  Explain what this instruction means:

    Go to http://some/url.  Save the source as ``somedir/source.html``.

#.  "Explore your home directory."  What might the author expect you to do?

    ..  container:: answer-hidden

        ::

            $ # on unix
            $ cd ~
            $ ls
            $ ls -alF  # shows *all* files, in *long* format



