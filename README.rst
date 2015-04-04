pho - PytHon utility for Organizing tasks
=========================================

Or just "Phở", `a Vietnamese soup - the most delicious food in the world
<http://en.wikipedia.org/wiki/Pho>`_.

.. image:: https://raw.github.com/hvnsweeting/pho/master/misc/pho.jpeg

``pho`` helps creating a shell script associates to a task, run it easily as
a helper. It helps keeping a log/tool that helps user later when there is
a need to look back the task.

Installation
------------

By using pip::

    pip install mpho # the name ``pho`` is taken already, sad :(

Example
-------

User works on task ``t1235``, he creates a task::

  pho create t1235 #  this will create a shell script

When doing task ``t1235``, user needs to run a command repeatedly, he can
edit the script by::

  pho edit t1235 # open shell script in editor set in $EDITOR

To run that script, just use::

  pho run t1235

To mark a task as done::

  pho done t1235

Or return it to undone::

  pho undone t1235

List all task::

  pho list
  pho list --all # to list also done tasks

Author
------

Viet Hung Nguyen <hvn@familug.org>
