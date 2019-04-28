function usage
{
	echo "usage:    $0                 to install and erase all previous files"
	echo "          $0 clean           to clean before installation"
}


TARFILE=ETATracker.tar.gz
INPUTFILE=input
THIS=`echo $0 | xargs basename`

if [[ $# == 1 ]]
then
	if [[ $1 == "clean" ]]
	then
		echo ">>> Cleanin in progress..."
		for FILE in `ls -A | grep -v $THIS | grep -v $TARFILE | grep -v $INPUTFILE`
		do
			rm -rf $FILE
		done
		echo ">>> Done."
		shift
	else
		usage
		exit 0
	fi
fi

if [[ $# != 0 ]]
then
	usage
	exit 0
fi

echo ">>> Installation in progres..."
tar xzvf $TARFILE
echo ">>> Done."


echo ">>> Conversion of DOS files..."
dos2unix *
echo ">>> Done."
