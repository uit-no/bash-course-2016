#!/usr/bin/env bash

# this script loops forever and appends a line each 2 seconds to a file
# called output.log
while [ 1 = 1 ]
do
    echo "generating a random integer: $RANDOM" >> output.log
    sleep 2
done

exit 0
