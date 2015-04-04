pho - PytHon utility for Organizing tasks
=========================================

Or just "Phở", `a Vietnamese soup - the most delicious food in the world
<http://en.wikipedia.org/wiki/Pho>`_.

.. image:: https://raw.github.com/hvnsweeting/pho/master/misc/pho.jpeg


``pho`` helps creating a shell script associates to a task.

It provides an easily way to run/edit that script to automate the repeat jobs,
or adding comment to that script as work dairy.

Installation
------------

By using pip::

    pip install mpho # the name ``pho`` is taken already, sad :(

Example
-------

User works on task ``t1235``, he creates a task (script)::

  pho create t1235

When doing task ``t1235``, user needs to run a command repeatedly, he can
edit the script by::

  pho edit t1235 # open shell script in editor set in $EDITOR

To run that script, just use::

  pho run t1235

To mark a task as done::

  pho done t1235

Or return it to undone::

  pho undone t1235

To list all tasks::

  pho list
  pho list --all # to list also done tasks

Showing specific script of task::

  pho show t1235

Appending a comment to script file::

  pho comment t1235 'http://a_link_that_help'

Deleting a task (you should not do this, but you can)::

  pho delete t1235

Authors
-------

Viet Hung Nguyen <hvn@familug.org>
