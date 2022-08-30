Types
=====

Python is a dynamically typed language, this means that it decides the types at run-time. This has the advantage of allowing for quick development, but when the size of your project increases significantly this may actually have the opposite effect.

Type hints
----------

That's why type hints were introduced. Type hints allow you to give types to all function arguments and variables. This way other developers in your team know which type you intended to use. 

MyPy
----

Type hints are useful, however they are not enforced. To actually enforce them, MyPy is used. It can be installed using pip or conda. MyPy gives powerful enforcements of the different types, however as it is a linter, the code will still run if the syntax is correct. 

Examples
--------

To show you the power of types and mypy, we'll create a small application that allows for a user to input names and score and then calculates the average and the person with the highest score.
To speed up the process, some things are already provided:

    * :download:`Average function <./average.py>`,
    * :download:`Maximum function <./maximunm.py>`,
    * :download:`Report function <./report.py>`,
    * :download:`Start of the main function <./main.py>`,

Download each of the files and put them in the src folder. Complete the imports and call the functions. You may need to change the types of some of the functions if necessary.
To use mypy, press ctr+shift+p and search for linter, select mypy and install if necessary. Alternatively, you can use the command mypy. 
