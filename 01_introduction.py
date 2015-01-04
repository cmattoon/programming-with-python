from lib import utils
utils.clearscreen()
################################################################################
utils.output("""
This is an interactive python tutorial that runs inside the Python interpreter
and uses the Python debugger (pdb) to let you peek at the internals as you go
along.

This started off as an 'Introduction to Programming' tutorial, so if you're 
already familiar with "programming 101" stuff (variables, types, interpreters
vs compilers, etc), feel free to skip ahead.

Throughout this tutorial, you'll see two main kinds of breaks: either you'll
be asked to press ENTER, or you'll be dropped into the debugger.

When you see this prompt, press ENTER to continue to the next step.
""", set_enter=True, title=" Introduction (1/3) ")
################################################################################
utils.output("""
When you enter the debugger, you'll see a message like the following:
\033[0m
--Return--
> /path/to/this/tutorial/lib/utils.py(92)output()->None
-> pdb.set_trace()
(Pdb) 
\033[97;01m
This tells you the current file (lib/utils.py) and line number (92). It also
tells you that the function 'output()' is returning the value 'None'. The 
current command should almost always be 'pdb.set_trace()', which tells the
debugger to stop here.

Once you're in the debugger, you can view information about objects, change the
value of variables and even execute regular Python statements. The debugger has
access to everything the Python interpreter does, so it's a pretty good learning
environment despite the extra steps involved.

Although the debugger has several commands, you'll only need a couple of them
to navigate this tutorial. More debugger commands will be shown as they are
needed.
\033[94m
    cont (c) - Continue execution until the next breakpoint

    next (n) - Continue execution until the next instruction.

    list (l) - Lists the source code. By default, shows 11 lines surrounding 
                 the current line number.
\033[97m

You can access the help menu for the debugger by typing 'help' at the (Pdb) 
prompt. To return to the tutorial from the debugger, use the 'c' or 'cont'
command.

Now you're in the debugger. Type 'help' and see what other commands are 
available to use. When you're done viewing the help menu, press 'c' to 
continue.

""", clear=True, set_trace=True, title=" Introduction (2/3) ")

################################################################################
##
## Pdb help menu
##
################################################################################

utils.output("""
Back to the tutorial!

This is the end of the introduction. You should be able to navigate around now
(unfortunately, there's no feature to skip or go back yet!).


""", clear=True, title=" Introduction (3/3) ", set_enter=True)

