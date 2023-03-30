print(__name__)
print(__annotations__)
print(__builtins__)
print(__doc__)
print(__loader__)
print(__package__)
print(__spec__)

""" 
_foo: Only a convention. A way for the programmer to indicate that the variable is private (whatever that means in Python).

__foo: This has real meaning. The interpreter replaces this name with _classname__foo as a way to ensure that the name will not overlap with a similar name in another class.

__foo__: Only a convention. A way for the Python system to use names that won't conflict with user names.
"""