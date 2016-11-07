In this exercise we simulate a typical situation where you want to run a
possibly large series of calculations but the calculations can fail and we do
not want to inspect each of them manually.

Try executing the `script.sh` a couple of times. Mostly it will report that it
worked but sometimes it will report failure. Try it.

There are two more scripts: `postprocess.sh` and `cleanup.sh` - try both.  They
don't do anything really except echoing some text but we can imagine that they
do some post-processing or cleanup work.

Our goal is to run the `postprocess.sh` script if `script.sh` finishes without
failure. If `script.sh` fails, we wish to run the `cleanup.sh` script instead.

Your goal is to write a script called `repeat.sh` which will execute
`script.sh` 20 times (or 2000 times) and automatically decide whether to launch
the `postprocess.sh` or `cleanup.sh` script based on the outcome of
`script.sh`. Hints are on the bottom of this page.

The output of the `repeat.sh` script should look similar to this one (the
individual outcomes will be different in each run):
```
starting calculations

running calculation 1
oh no! calculation failed!
running the cleanup script ...

running calculation 2
yay! calculation worked!
running the post-processing script ...

running calculation 3
yay! calculation worked!
running the post-processing script ...

running calculation 4
oh no! calculation failed!
running the cleanup script ...

running calculation 5
yay! calculation worked!
running the post-processing script ...

etc.
```

Hints:

- Use exit codes in `script.sh` to report success or failure to the `repeat.sh` script. Chain scripts with `&&` and `||`.
- Use `seq` to generate the loop variable.
