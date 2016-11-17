A small intro to the small, tiny first steps:

We are going to spend 10 minutes getting friendly with command line.

First step is to try the infamous "hello world"-party trick:

Type: (be ware of geeky linux humor inherited from the geeky communities in the 70-ties 
(unix world from before PC). (FO anecdote)

$ echo “hello world”

We will look into how to get info on command line systems:

We have manuals like everywhere else. And linux have even rather logical names for 
things if you are rather established in plain english and as mentioned above,  geeky humour.

Lets have a look at manuals and info in various forms:

* man pages

$ man cp
$ cp --help

And for contrast:

$ man apropos
$ apropos --help

So what is difference between apropos and whatis?

$ whatis cp

and then

$ apropos cp


Read more about both using man:
$ man whatis
$ man apropos

(Often examples in man pages). 

$ man whatis
$ whatis --help

Then, a little about history and how to find old commands:

$ history

The commands you type in the command line terminal window is stored
for resuse. The way of refinding some of the things you have typed, 
is by using the history functionality.

The file containing the (on Stallo) last 1000 commands is called .bash_history.
I will comment on the name for the next session.

First:

$ history

Then:

Type arrow up
Repeat the last instruction 5 more times.
What do you see?

Another clever feature:

$ ctrl-r man ...

That was the small first steps in command line and bash. Now we move over to...

