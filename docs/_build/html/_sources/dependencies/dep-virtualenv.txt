

.. _dep-virtualenv-label:

virtualenv
--------------------

.. _dep-virtualenv-what-label:

What is ``virtualenv``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``virtualenv`` is a tool that creates "new" Python installations that are 
copies of your installed Python.  These "virtual environments" are clean and 
consistent.  

.. _dep-virtualenv-why-label:

Why do I need ``virtualenv``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To keep work areas clean and consistent, and minimize assumptions about
what tools are installed where.  This makes it easier to have repeatable,
consistent builds.


.. _dep-virtualenv-how-label:

Get ``virtualenv``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:: 
    
    $ pip install virtualenv

.. _dep-virtualenv-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # assume you have created a directory D and moved to it!
    $ virtualenv --no-site-packages testenv
    $ . testenv/bin/activate  # windows -> . testenv\Scripts\activate.bat
    # your prompt should change to say (testenv)
    $ deactivate
    # remove the testenv directory
    rm -rf testenv


* http://pypi.python.org/pypi/virtualenv


