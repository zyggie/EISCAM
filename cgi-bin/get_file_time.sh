#!/bin/bash
# Gets the ctime of a file by stripping the stuff you don't want from the output of "stat"
# Credit to SO for the tip to use "cut" http://stackoverflow.com/questions/3033100/extracting-character-range-form-longline-with-sed-or-awk-or-grep
# Takes one argument, tested on jpg files created by raspistill. Use it some other way at your peril.
stat $1 |grep 'Change:' |cut -d ' ' -f 3

