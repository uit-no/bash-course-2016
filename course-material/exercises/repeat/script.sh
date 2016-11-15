#!/usr/bin/env bash

# generates pseudorandom integer in the range 0 to 32767
random_integer=$RANDOM

# if the integer is >= 22000, we let the calculation fail
if [ "$random_integer" -ge "22000" ]
then
    echo "oh no! calculation failed!"
else
    echo "yay! calculation worked!"
fi

exit 0
