Pytest
======

Pytest allows for easy testing of software, written in Python. In this part, I'll show one small example on how to use pytest.

Installing pytest
-----------------

Installing pytest is as easy as pie. You can do it as follows

.. code-block:: bash

    pip install -U pytest

To test if it was installed:

.. code-block:: bash

    pytest --version

Example
-------

Create a new folder in the src folder, named tests. In this place the file :download:`example <./example_test.py>` as well as an empty file called ``__init__.py``. In the src folder, you also have to include this ``__init__.py`` You can rename the file, however it still has to contain test in the name.

.. code-block:: bash

    pytest

will now run the tests

Exercise
--------

Write a new test for the maximum function in a different file, as well as another test for average in the same file as the example.