[clever name here]
==================
**status**: development

This is an interactive tutorial for Python that uses `pdb` as the environment.
This allows the user to start writing code as soon as possible and introduces
the newcomer to debugging early on. It also provides a convenient way to
demonstrate low-level details and other subtleties interactively.

Initially, breakpoints are used to control program flow for the tutorial itself. 
I'm attempting to keep the lessons clean (move extra code to the `lib/` folder)
and set up code *before* calling `pdb.set_trace()`.

This is an attempt at an "intro to programming" tutorial in addition to just
the Python language.

Getting Started
============
You'll need to install Python and make sure `pdb` is available, too. You should 
be able to run everything from the root directory by calling

`python <lesson_filename>`

Lessons
-------

 * **01** - Introduction, usage instructions
 * **02** - Python
 * **03** - Types and Variables
