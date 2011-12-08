.. _dep-django-label:

django
--------------------

.. _dep-django-what-label:

What is ``django``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django is the most-popular web-development framework written in Python.



.. _dep-django-why-label:

Why do I need ``django``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For building our voting application!  


.. _dep-django-how-label:

Get ``django``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We don't want to install django system wide, but rather in our local
virtualenv. We're also going to install ``south``, a Django helper application which will make it easier for us to go back and edit our Django app later.

.. code-block:: bash

    $ pip install django
    $ pip install south

.. _django-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python
    >>> import django
    
To quit the python prompt do::

    exit()

.. _django-app-create-label:

Verify you can create a new Django app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a folder on the desktop called ``django_projects``
Open a new Terminal window and type the following: 

..  code-block:: bash

   mkdir django_projects
   cd django_projects
   django-admin.py startproject myproject

Both commands should provide no output.
Once that's finished, type the following in the Terminal window: 

.. code-block:: bash

    cd myproject
    python manage.py runserver

Output should look like this::

    Validating models...
    0 errors found

    Django version 1.2.5, using settings 'myproject.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


In your browser, go to http://127.0.0.1:8000/ 

In your Terminal window you should see something like:

.. code-block:: bash

    [19/Mar/2011 19:19:26] "GET / HTTP/1.1" 200 2057

Back in the Terminal window where you ran python manage.py runserver, 
type control-c to kill the server. 

Congratulations, you have run your first Django app!
