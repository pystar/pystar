

.. _dep-pip-label:

pip
--------------------

.. _dep-pip-what-label:

What is ``pip``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip`` is a utility for install and uninstalling Python packages. 
Packages are bundles of code that give additional functionality to an
existing Python installation.

.. _dep-pip-why-label:

Why do I need ``pip``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install and manage packages in a consistent way in Python.

.. _dep-pip-how-label:

Get ``pip``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, install ``ez_setup`` to get ``easy_install`` (the *old* python
package managers).

#. Open a terminal and run these commands: ::

        $ curl http://peak.telecommunity.com/dist/ez_setup.py | python
        $ easy_install pip
        
.. _pip-verify-label:


Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run ``pip`` .   You should see something like::

    $ pip
    Usage: pip COMMAND [OPTIONS]

    pip: error: You must give a command (use "pip help" to see a list of commands)
