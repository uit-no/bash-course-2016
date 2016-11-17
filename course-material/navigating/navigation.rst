navigation, or more precisely, how to navigate in the file tree structure 
of your computer.


We need a couple of tools for making this work in a proper way.

First we need to see files in a given folder, and navigate in between folders.

(How familiar are you with cd = change directory?)

cd / cd ../ cd - / cd ~

Please do as follows:
$ pwd
$ cd 
$ pwd
$ cd ~
$ pwd 
 - do you see any difference?

cd (what we got from the first `pwd`)
Then 
$ cd ..
$ pwd
$ cd -
$ pwd # see the pattern?

# Cool thing if we have time: `cd !$`

then we would like to find out what is in the folder
where we just landed: Command is called list - short ls

$ ls # if you would like to know more: man ls

Now we copy one of the files:

$ cp navigation.rst navigation_mycopy.txt
$ ls

Then we try to make a hidden file:

$ cp navigation.rst .navigate.txt
$ ls # we do not see it, hidden.

Then we try long listing:

$ ls -l # Still not see it?

Ok, try to list all files:

$ ls -a

This can also be combined, and you can also sort on time of modification:

$ ls -t

or

$ ls -tr

You can also see the filestructure in a tree-type structure using tree.

$ tree # for more info; type man tree or tree --help.

We need another directory: Command is make directory; mkdir for short

$ mkdir copyandrename
$ cd !$ # aka cd copyandrename

then move the two copies you made here:

# Typically I allways check if there are something present with ls

$ mv ../.navigate.txt . # Means move from one step out
$ mv ../navigation_mycopy.txt .

mv is also used when renaming files:

$ mv navigation_mycopy.txt navigation_yourcopy.tst

A small chat about deleting:

$ cp navigation_yourcopy.tst navigation_mycopy.txt
$ rm navigation_yourcopy.tst # command is called remove.

There is a profound difference between rm and rmdir:

$ cd ..
$ cp -R copyandrename copyanddelete # recursive copying of folder with content
$ rmdir copyanddelete

What message do I get?

Then

$ cp -R	copyandrename copyanddelete2
$ cd copyanddelete
$ rm *
$ ls -a
$ cd ..
$ rmdir copyanddelete

Did it work this time? Also try:

$ ls copyanddelete2
$ rm -fR copyanddelete2 

What message did I get now?

$ ls -a


Small exercises: Find the files and folders that contains the material for Stallo introduction and Firststeps.

Now we need to investigate file permissions!