from lib import utils
################################################################################
utils.output("""
First things first: The 'Hello, world!' program. It's the traditional first
program to write, and far be it from me to break tradition. Since Python is an
interpreted language, we can take care of this right here.

In the debugger, type the following code and press Enter:
\033[92;40m
print('Hello, world!')
\033[0;97m

(Remember to use the 'continue' or 'c' command to return)
""", set_trace=True, clear=True, title=" Hello, world! ")

################################################################################
## 
## print('Hello, world!')
##
################################################################################
utils.output("""
The 'print' statement accepts a string as a parameter. A string is a series of
characters and is enclosed by quotes. There are two types of quotes in Python:

\033[34m
    - single quote (') \033[97m - Signifies a literal value.
\033[34m
    - double quote (") \033[97m - Takes expansion into account

   (Note: We're talking apostrophes and quotation marks here, not two 
          apostrophes!)

The difference between single and double quotes is most important when using
escape characters. An escape character (typically '\'), is used to tell the
interpreter that the character should be interpreted as part of the string, and
not on its own. Consider the following:
\033[34m
    'I\'m a string with single quotes. My apostrophe needs escaped!'
    "With \"double quotes\", it's exactly the opposite."
\033[97m

You can also use triple quotes (which go against what I've said above). 
Triple quotes are three of the same quote style together:

'''This is a triple-quoted string. You can write pretty much anything inside
of here'''

(If you inspect the source code, you'll see that these blocks of text are all
written inside triple-double quotes)

Try printing different strings to the screen with the 'print' function.
\033[32;40m
print("It's pretty much the same as the \"Hello, world\" program above")
print('I\'m escaped')
\033[97m

When you're done, press 'c' to return.
""", clear=True, set_trace=True, title=" Hello again! ")

################################################################################
## More strings and printing
################################################################################
## Init these here so they're at least defined.
name = None
age = None
favorite_color = None

utils.output("""
Variables are named containers for data. They can contain letters, numbers or
the underscore character, but must start with a letter or underscore. Values 
are assigned to variables with the = sign.

\033[32;40m
name = 'Curtis'
print("Hello, " + name)
\033[97m

The + sign concatenates (joins) strings, but adds numeric values. When 
concatenating strings, pay attention to the spaces:

\033[32;40m
name = 'John' + 'Doe'
name = 'John ' + "Doe"
\033[97m

Remember, variables:
\033[93m
 * Can contain numbers, letters or the underscore character
 * Must start with a letter or an underscore
 * Must not be a reserved word/keyword (if, else, import, print, etc)

Set the following variables. Remember to press 'n' first to return to the right
scope.

\033[32;40m
name
age
favorite_color
\033[97m
""", set_trace=True, clear=True, title=" Variables ")
################################################################################
## Set variable names here:
##    name
##    age
##    favorite_color
################################################################################

utils.output("Set your variables now, then press 'c' when you're done")
## Cast these to strings to prevent errors below.
name = str(name)
age = str(age)
favorite_color = str(favorite_color)

utils.output("""
Hello, %s. It looks like you're %s years old and your favorite color is %s.

Now that you've got the hang of it, it's time to revisit the debugger. As you
already know, you can use python's \033[32;40mprint\033[00;97;01m function to
print the value of a variable.

The debugger has a shortcut 'p' that will print the value of a symbol. If you
print an object that's not a string, integer, etc, you'll sometimes see it
represented like this:

\033[32;40mp os\033[0m
<module 'os' from '/usr/lib/python/os.pyc'>\033[01;97m

\033[32;40m
fh = open('myfile.txt', 'w')
p fh
\033[0m
<open file 'myfile.txt', mode 'w' at 0x7f6647be2600>\033[01;97m

This indicates an object that can't be printed nicely in a human-readable 
format, so it tries to give you enough information to determine what it is that
is stored in the variable. This comes from the object's __str__ or __repr__
functions, which will be discussed later.
""" % (name, age, favorite_color), 
       set_trace=True, clear=True, title=" Variables ")
################################################################################
