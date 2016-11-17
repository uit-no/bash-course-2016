# Data Mining

## Finding files

### `find`

Most common use case: finding big or old files

Basic syntax:

```
find /path/to/dir -name "filename"
```

find files older than 7 days

```
find /path/to/dir -mtime +7
```

find files larger than 50k (and use `du` to print the actual size )

```
find /path/to/dir -type f -size +50k -exec du -sh {} \;
```

Sometimes it's easier to use `du` on its own.


### `which`

Find path to executable you know the name of.

### `locate`

- Quicker than `find` but not as flexible.
- Based on database.
- Not so useful on stallo.

## Finding strings in files

### grep

Basic syntax:

```
grep string file
```

case sensitive matching by default

```
grep the gettysburg.txt
grep The gettysburg.txt
```

Use `-i` for case insensitive matching

```
grep -i the gettysburg.txt
```

only print matching part `-o`

```
grep -o The gettysburg.txt
```

Beware of special character. Does not work as expected:

```
grep "--" gettysburg.txt
```

Need to escape special characters

```
grep "\-\-" gettysburg.txt
```

Need to quote spaces

```
grep " the " gettysburg.txt
```

Counting matches `-c`

```
grep -c "\-\-" gettysburg.txt
grep -c the gettysburg.txt
grep -c The gettysburg.txt
grep -c -i The gettysburg.txt
```

Invert match `-v`

```
grep -v The gettysburg.txt
```

If you know regular expressions `egrep` is more powerful

```
egrep -o "(and|The)" gettysburg.txt
```

## Replacing strings in files

## sed

Using `sed` replacing words (but can do much more)

```
sed s/we/I/ gettysburg.txt
sed s/we/I/ gettysburg.txt |grep we
```

use `g` to replace all occurences on a line

```
sed s/we/I/g gettysburg.txt |grep we
sed s/we/I/g gettysburg.txt
```

you need to escape special characters

```
sed s/\\./\!/ gettysburg.txt
```

## translate characters

#### `tr`


lower case

```
tr A-Z a-z
```

special notation for some set of characters

```
tr [:upper:] [:lower:]
```

pretty printing `PATH` on separate lines

```
printenv PATH | tr ":" "\n"
```

some useful flags
 - `-d` deletes
 - `-c` matches complement
 - `-s` squeeze repeated characters

## Sorting lines of text

### `sort`

If you are sorting numbers be ware that the default is alphabetic ordering

```
sort numbers.csv
```

Use `-n` for numeric sort

```
sort -n numbers.csv
```

## Removing duplicate lines

### `uniq`

Often useful after using commands like `grep` or `sort`.

## Extract a column

### `cut`

Extract third column from a csv file

```
cut -d"," -f 3 numbers.csv
```

here `-d` specifies the delimiter and `-f` the column (field).


```
cut -d"," -f 3 numbers.csv |sort
cut -d"," -f 3 numbers.csv |sort -n
```

### `awk`

Often easier to use `awk` (can do much more, it's a complete programming language)

Print all columns.

```
awk '{print $0}' file
```

Print the 3rd column.

```
awk '{print $3}' file
```

Print the 1st and the 3rd columns.

```
awk '{print $1 $3}' file
```

In `awk` the delimiter is specified with the `-F` flag and called a field separator.

## Combining commands using pipes

### `|`

- Many bash commands reads text as input and write text as output.
- This makes it easy to chain commands together in pipelines.
- The output from one command is directly "piped" into the next.

Instead of

```
command1 > result1.tmp
command2 < result1.tmp > result2.tmp
command3 < result2.tmp > result.out
```

you can do

```
command1 | command2 | command3 > result.out
```
