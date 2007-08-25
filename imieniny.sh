#!/bin/sh
# $Id$

DATADIR=/usr/share/imieniny
LANGNAME=

print_nameday() {
     mfile=$DATADIR/$LANG/`date +'%m'`.txt
     if [ -f $mfile ]; then 
	awk -v dzien=`date +'%-d'` '{if(NR==dzien){print}}' $mfile
     else 
	return 1
     fi	
}

if [ -n "$LC_ALL" ]; then
    LANGNAME="$LC_ALL"
elif [ -n "${LC_TIME}" ]; then
    LANGNAME="$LC_TIME"
elif [ -n "${LANG}" ]; then
    LANGNAME="$LANG"
else 
    LANGNAME="C"
fi

if [ ! -d $DATADIR/$LANGNAME ]; then
    exit 1
fi

case "$LANGNAME" in
    pl_PL*|pl)
	 echo -n "`date +%Y.%m.%d`, imieniny "  
	 print_nameday
	 exit $?
	 ;;
    *)
	echo "Error: $LANG directory exists, but is not supported."
	exit 1
	;;
esac

# Shouldn't reach that point:
exit 1
