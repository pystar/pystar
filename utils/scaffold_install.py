from jinja2 import Template

t = Template(('''

.. _dep-{{dep}}-label:

{{dep}}
--------------------

.. _dep-{{dep}}-what-label:

What is ``{{dep}}``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


{{dep}} is

.. _dep-{{dep}}-why-label:

Why do I need ``{{dep}}``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To...

.. _dep-{{dep}}-how-label:

Get ``{{dep}}``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{% for os in oses %}
.. _dep-{{dep}}-{{os}}-how-label:

{{os}}
~~~~~~~~~~~~~~~~~~~~~

On {{os}} go to http://example.com/ and get it!

{% endfor %}


[some links, install instructions]

.. _{{dep}}-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After it installs, run ``some command``

'''
))



def main():
    oses = ('windows','Mac OSX', 'Linux')
    deps = ('gedit git python pip virtualenv django'.split())
    for dep in deps:
        of = file("dep-%s.rst" % dep,'w')
        of.write(t.render(**dict(dep=dep,oses=oses)))
            
    
main()
