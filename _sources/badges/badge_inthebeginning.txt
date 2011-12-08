.. badge_inthebeginning:

In the Beginning was the Command Line
===========================================

History matters.  At first glance, many of the commands and idioms of 
programming seem deliberately obscure.  But they are the culmination of 
an evolutionary process, with twists and turns and dead-ends.  Knowing 
some history, and in particular the history of the Unix operating system,
sheds light on what is otherwise occult.

*In the Beginning Was the Command Line* is a book by Neal Stephenson. 
Unlike many of his other works, it is short and available for (legal) free download on the internet. 

#. For the entire plain text version you can go to his site: http://www.cryptonomicon.com/beginning.html
#. Read the section entitled "THE HOLE HAWG OF OPERATING SYSTEMS." here: http://steve-parker.org/articles/others/stephenson/holehawg.shtml


.. note:: 

    this badge is a bit incomplete, and you will benefit from having a 
    guide around to help you through it)


Now that you have read the section, let's honor our shared history by using Unix 
commands to do the same work for us.

:: 

    curl -s 'http://www.cryptonomicon.com/command.zip' | gunzip | grep -i -A22 'pipe' | less
    # type 'q' to quit from 'less' when you are done.
Let's break this down.

#.  The ``|`` takes the text **output** from one command and **pipes** it into 
    the **input** of the next command.
#.  research curl:  ``man curl``.  What does curl do?  What about the
    ``-s`` option?

    ..  container:: answer-hidden
        
        Curl is a command line client for hitting urls.  We can use it
        to download the web page.  ``-s`` makes it run 'silently'.

#.  ``gunzip``?  What is does gunzip do?

    ..  container:: answer-hidden
        
        it unzips the file :)  Nothing magical there!  

#.  What file is ``gunzip`` operating on?

    ..  container:: answer-hidden
        
        None, really.  Or rather it's operating on a special file called
        ``stdin``, which is here attached to the ``stdout`` out of the curl
        command, via the **pipe**.  

#.  ``grep -i -A22 'pipe'`` .  ``grep`` is the *general regular expression
    parser*, that is used to find lines in a file matching an expression.
    Here, we have thrown on some special switches:

    * ``-i`` for *case insensitive*
    * ``-A22`` for 'show me the 22 lines *after* my match.  Since each
      line in the original is a paragraph, this has the effect of getting us
      the whole section.
    * ``'pipe'`` is what to search on in the incoming stream.  

#.  ``less`` is a **pager**, which is a program that takes a stream of text,
    and turns it in 'screen-size' 'pages' for easier viewing.


Exercises:

#.  Look at all the lines including the word *pride* in *Pride and Prejudice*
    (downloadable at http://www.gutenberg.org/files/1342/1342-h/1342-h.htm)

    ..  container:: answer-hidden

        ::

            curl 'http://www.gutenberg.org/files/1342/1342-h/1342-h.htm' | grep -i 'pride' | less

#.  Count those lines using the ``wc`` command.

    ..  container:: answer-hidden

        ::

            curl 'http://www.gutenberg.org/files/1342/1342-h/1342-h.htm' | grep -i 'pride' | wc




