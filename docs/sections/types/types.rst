Types
=====

Python is a dynamically typed language, this means that it decides the types at run-time. This has the advantage of allowing for quick development, but when the size of your project increases significantly this may actually have the opposite effect.

Type hints
----------

That's why type hints were introduced. Type hints allow you to give types to all function arguments and variables. This way other developers in your team know which type you intended to use. 

MyPy
----

Type hints are useful, however they are not enforced. To actually enforce them, MyPy is used. It can be installed using pip or conda. MyPy gives powerful enforcements of the different types, however as it is a linter, the code will still run if the syntax is correct. 

TODO: work out some examples with MyPy. 