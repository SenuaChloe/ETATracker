#!/bin/bash

# Script to export to distant server
# By default, exports to $TARGET

source ./configure.sh

if [[ $# -gt 1 ]]
then
    echo "usage:    $0 target"
    echo "    target: where to export all that"
    exit 1
elif [[ $# == 1 ]]
then
    TARGET=$1
fi

TMPFILE=`mktemp`.tar.gz
tar czvf $TMPFILE `cat export_list.txt`
echo Need password to connect to target:
scp $TMPFILE $TARGET
rm $TMPFILE
