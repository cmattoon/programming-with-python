"""
This module contains some utility functions for the tutorial. It's here to keep
the tutorial file clean.

It's imported into the main script with the statement
    from lib import utils

Each of the functions is then accessed via:

utils.output("Something")
utils.clearscreen()
...
"""
import os
import sys
import pdb
TERM_WIDTH = 80

def clearscreen():
    """This function clears the screen. It's really just a friendly wrapper
    for 'os.system("clear")' or 'os.system("cls")'
    """
    try:
        os.system('clear') # Linux & OS/X
    except:
        os.system('cls') # Windows

def output(*args, **kwargs):
    ### Add feature to limit output to TERM_WIDTH
    """This function is responsible for displaying output and handling pauses
    in the tutorial.

    Args:
       - text (string) The string to print to the screen

    Kwargs: (keyword arguments - all are optional. Default values shown in
        parentheses after type.)

       - clear (bool, False) If True, calls 'clear()' before displaying text
       - set_enter (bool, False) If True, requires user to press ENTER
       - set_trace (bool, False) If True, passes control to pdb
       - title (string, None) If not None, prints a section header
    """
    ## The difference between *args and **kwargs:
    ##     Args:
    ##         myfunction('arg1', 'arg2', 100)
    ##
    ##     Kwargs:
    ##         myfunction(arg1='arg1', arg2='arg2', arg3=100)
    ##
    ## Access args as a tuple:
    ##     text = args[0]
    ##
    ## Access kwargs like so:
    ##     kwargs.get(kwarg_name, default_value)
    try:
        text = args[0]
    except IndexError:
        ## This will be thrown if no title is passed
        raise ValueError("Text must not be empty")

    clear = kwargs.get('clear', False)
    enter = kwargs.get('set_enter', False)
    trace = kwargs.get('set_trace', False)
    title = kwargs.get('title', None)
    outfd = kwargs.get('outfd', sys.stdout)

    if clear:
        clearscreen()

    ## Make the text style bold white
    outfd.write("\033[97;01m")

    ## Print the title if it exists
    if title is not None:
        title = "\033[32;40m%s\033[97;49m" % str(title).center(TERM_WIDTH - 4, '-')
        outfd.write(title)

    ## Print 'text'
    outfd.write(text)
    
    if enter:
        ## Pause for user input...
        sys.stdout.write(" --= Press ENTER to continue =-- ")
        raw_input()

    ## Return the text style to normal
    outfd.write("\033[0m")

    ## Finally, set the trace if indicated.
    if trace:
        pdb.set_trace() ### PRESS 'n' TO ENTER DEBUGGER OR 'c' TO RETURN ###
        

