.. _webapp_answers:

Answers for Webapp Questions
--------------------------------------

..  danger::

    Looking at these answers **too soon** can cause 
    indigestion, headaches, hair loss, mass panic
    and other side-effects.  Be cautious!  Think 
    through the question **first**!  

    Remember

    - you can do this!
    - effort matters!




.. _webapp_answers_8103:

How do I start a server on port 8103 and navigate to it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  ``http://127.0.0.1:8000/``
#.  Navigate to http://127.0.0.1:8103/



.. _webapp_answers_verify_shutdown:

How do I verify the server is shut down?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

go to http://127.0.0.1:8000/ and see if you get a 404, or 500!


.. _webapp_answers_single_quote:

How do I put single quote in the SECRET_KEY?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recall (or know!) that python can single-quote, double quote, or triple quote strings::

    SECRET_KEY="that's my string"

or::

    SECRET_KEY='''that's my string'''


.. _webapp_answers_database_db_exists:

Does ``database.db`` exist?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It shouldn't!  Use ``ls`` to find out!


.. _webapp_answers_django_standard_apps:

Why are the standard apps standard?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* They are useful for most web projects.
* They are tedious to write, or hard to code correctly or both.


By default, ``INSTALLED_APPS`` contains the following apps, all of which come with Django:

* django.contrib.auth -- An authentication system.
* django.contrib.contenttypes -- A framework for content types.
* django.contrib.sessions -- A session framework.
* django.contrib.sites -- A framework for managing multiple sites with one Django installation.
* django.contrib.messages -- A messaging framework.

These applications are included by default as a convenience.  


.. _webapp_answers_django_magical:

Does this all seem magical?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, this is all somewhat magical.  Eventually, that should start to worry
you, but for now, accept that it mostly works, most of the time. 





.. _webapp_answers_dev_server_still_works:

Why does the dev server still work when settings.py has been deleted?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because ``settings.pyc`` still exists, and that's what the machine is actually looking at when you run the code that runs the dev server. That's why the dev server does not work when you also delete ``settings.pyc``. Now the computer has no idea what you're talking about, since the original code and the compiled byte code are both gone.



.. _webapp_answers_database_db_exists_after_sync:

Does ``database.db`` exist *now*?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Now** it should!  That is one of the magical bits of ``dbsync``.  

Use ``ls`` to verify it!



.. _webapp_answers_know_what_saved:

How do I know if my work is saved in git?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ git status
    # nothing should be in 'untracked' that suprises you.
    # if there are 'modified files', then let's see what is different
    $ git diff
    # shows the diffs between what is on disk and what git knows about
    # If there *are* diffs: 
    #    git add  # the files,
    #    git commit -m "some message"  
 


.. _webapp_answers_sqlite_one_writer_implications:

What are the implications of Sqlite only handling one writer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* performance is blocked by how fast that one writer can write
* multiple processes can clobber each others' data.


.. _webapp_answers_git_magical:

Is Git magical?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django is magical.  ``git`` is *creepy*.  




.. _webapp_answers_why_testing_matters:

Why does testing matter?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Among other reasons:

* ensure that the features actually work as expected.
* help make it clear what "as expected" actually means.
* stop code changes from breaking things that used to work.
* keep code split into reasonable, understandable chunks
  ("if I can't figure out how to test it, it's probably doing to much!").



.. _webapp_answers_why_not_save_database_db:

Why don't we commit ``database.db``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Becuase ``database.db`` is just a 'test database' and doesn't have anything
"real" in it, we don't care about it.  Generally files that are 'built', like
``.pyc`` files, the build html files of this book, and the like aren't put
under version control.  


.. _webapp_answers_is_polls_importable:

Is polls importable?
^^^^^^^^^^^^^^^^^^^^^^^^^^

We don't know. Is it?  It *should* be.

::

    $ cd myproject
    $ python
    >>> import polls

If you got an ``ImportError``, it's just as it sounds!  Check ``sys.path``, file
permissions, and the like.



.. _webapp_answers_pyc_files:

What are these ``.pyc`` files anyway?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From `PEP 3147 <http://www.python.org/dev/peps/pep-3147/#background>`_:

    CPython (the 'standard' variety of Python) compiles its source code into "byte code", and for performance reasons, it caches this byte code on the file system whenever the source file has changes. This makes loading of Python modules much faster because the compilation phase can be bypassed. When your source file is ``foo.py``, CPython caches the byte code in a ``foo.pyc`` file right next to the source.

When you import or otherwise run a piece of Python code, it will create a .pyc file of the compiled byte code automatically when it can. 




.. _webapp_answers_django_project_testing_results:

What is the result of the standard ``test``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some that we got when we ran things:

.. include::  test_log_default.txt

Note the missing templates, which make some sense.  We think the 
``ERROR: test_password_change_fails_with_invalid_old_password`` has to do 
with sqlite, but who knows?  We probably *should know*.  


.. _webapp_answers_why_only_restore_py_not_pyc:


Why do I only need to restore settings.py and not settings.pyc?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well first off, remember how we set up git to exclude ``.pyc`` files from the repo? So ``settings.pyc`` was never put into the repo and therefore cannot be recovered from it. Not to worry though. When you restore ``settings.py`` and restart the dev server, ``settings.pyc`` is built automatically. Nifty!


.. _webapp_answers_the_right_framework:

Which framework is right?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Which one do **you** think is right?  Why is that, again?

You are completely correct -- gold star!



.. _webapp_answers_polls_vs_admin:

Why not admin for **everything**?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Why not, indeed!?

The ``django.admin`` app is one django's killer apps!  It's 
easy to use, powerful, decently extensible.  Many sites are
just  ``admin`` sites, dressed in nicer clothes, and given 
nicer ``URLConf``'s.

There are some concerns though:

* users and permissions
  (ensuring the right people can edit the right things)
* the admin site relies heavily on ``django.models`` to work right.
  If your needs aren't met by them, admin doesn't work.




.. _webapp_answers_no_like_django:

Why don't people like Django?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* It's too magical.  Too many mysterious files
* ``django.models`` is limited.  Not everything is expressable as a 1:1 
  mapping with a db table.  What if I want to store in other types of 
  data stores?  
* (insert more reasons here!)



.. _webapp_answers_added_polls:

With polls added to the app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        # Uncomment the next line to enable the admin:
        # 'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
         'polls',
     )

.. _webapp_answers_root_urlconf:

What is the ``ROOT_URLCONF``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Look in ``settings.py``::

    ROOT_URLCONF = 'myproject.urls'

This setting is  *for a python module*.  In those, ``.`` implies a directory structure,
so Django will look at ``myproject/urls.py``.  :ref:`Magical? <webapp_answers_django_magical>`


.. _webapp_answers_missing_choice:

What writes the error message when a choice is missing?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Look in ``views.py``:

.. code-block:: python


    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))



.. _webapp_answers_urlconf_polls_vote:

What is triggered by  http://127.0.0.1:8000/polls/23/results/ ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Given::

    urlpatterns = patterns('',
     (r'^polls/$', 'polls.views.index'),
     (r'^polls/(\d+)/$', 'polls.views.detail'),
     (r'^polls/(\d+)/results/$', 'polls.views.results'),
     (r'^polls/(\d+)/vote/$', 'polls.views.vote'),
    )

We ignore the http://127.0.0.1:8000/ bit.

The rest `polls/23/results/`  fails to match first two, but does match
``r'^polls/(\d+)/results/$'``, which **captures** the 23.  

Thus ``polls.views.results`` is called with the argument ``23``.  


.. _webapp_answers_request_post_values_strings:

Why are ``request.POST`` values always strings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Think about the interaction process with websites.  You enter text,
  and it goes off for processing.  
* Strings are the universal currency of computing!  
* Even when something looks like an int, it is better not to guess (e.g. ZIP codes).
* `Explicit is better than Implicit` is part of the `Zen of Python <http://www.python.org/dev/peps/pep-20/>`_ .  SNARK:  :ref:`Django isn't always very explicit <webapp_answers_django_magical>`.



