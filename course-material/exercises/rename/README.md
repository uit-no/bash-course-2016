In this exercise we start with a tree of files
with the structure data/year/month/day which contains
temperatures measured hourly in Tromso for few selected days:
```
`-- data
    |-- 2013
    |   |-- nov
    |   |   |-- 01
    |   |   |-- 02
    |   |   |-- 03
    |   |   `-- 04
    |   `-- oct
    |       |-- 28
    |       |-- 29
    |       |-- 30
    |       `-- 31
    |-- 2014
    |   |-- nov
    |   |   |-- 01
    |   |   |-- 02
    |   |   |-- 03
    |   |   `-- 04
   etc.
```

The goal of this exercise is to move and rename these files to the following
structure:
```
data/2013-nov-01.temperature
data/2013-nov-02.temperature
data/2013-nov-03.temperature
data/2013-nov-04.temperature
data/2013-oct-28.temperature
etc.
```

However, we do not want to do this manually but we want to script it. Your task
is to find a good solution to this problem. Ideally it should be general and
should work also for other months and years and in principle scale to thousands
of files.
