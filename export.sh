TMPFILE=`mktemp`.tar.gz
tar czvf $TMPFILE `cat export_list.txt`
echo Need password to connect to target:
scp $TMPFILE vultrao@ritchie:/srv/services/ETATracker/ETATracker.tar.gz
rm $TMPFILE
