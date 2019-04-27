#!/bin/bash

# Disclaimer : requires figlet to be installed

# exit 1 if wrong arguments
# exit 2 if file not found


# constants
EPOCH_DELTA_SEC=10 # in seconds

# globals
BUFFER=`mktemp`
TRAP_CMD='echo "Removing temporary file..."; rm $BUFFER; '

# USAGE
function usage()
{
    echo "usage:    $0"
    echo "          $0 -h|--help"
    echo "          $0 input_file"
    echo "          $0 description location_from location_to"
    echo ""
    echo "    input_file: the input file from which the locations must be read"
    echo "    (default input file is \"input\""
    echo "    description: the message to prompt for the custom ETA"
    echo "    location_from: origin location for the custom ETA"
    echo "    location_to: destination location for the custom ETA"
}

# Checking the arguments
if [[ $# == 0 ]]
then
    INPUT="input"
elif [[ $# == 1 ]]
    if [[ $1 == "-h" or $1 == "--help" ]]
    then
        usage
        exit 0
    else
        INPUT=$1
    fi
elif [[ $# == 3 ]]
    INPUT=`mktmp`
    TRAP_CMD=$TRAP'rm $INPUT;' INT
    echo "$1|$2|$3" > $INPUT
else
    usage
    exit 1
fi

#trap
trap $TRAP_CMD INT

# checking the file
ls $INPUT
if [[ $? != 0 ]]
then
    >&2 echo "Error : File $INPUT does not exist"
    >&2 echo "Type $0 -h for usage"
    exit 2
fi

# main loop
while true
do
    # calculation of waiting time
    CURRENT_EPOCH=`date +%s`
    TARGET_EPOCH=$((CURRENT_EPOCH+EPOCH_DELTA))

    # calling the main script
    python3 eta_tracker.py $INPUT > $BUFFER

    # flush the buffer
    clear
    cat $BUFFER | figlet

    # sleep
    CURRENT_EPOCH=`date +%s`
    if [[ $TARGET_EPOCH -gt $CURRENT_EPOCH ]]
    then
        REMAINING_EPOCH=$((TARGET_EPOCH-CURRENT_EPOCH))
        sleep $REMAINING_EPOCH
    fi
done
