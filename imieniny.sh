#!/bin/sh
# $Id$

DATADIR=/usr/share/imieniny
LANGNAME=

print_nameday() {
     mfile=$DATADIR/$LANG/`date +'%m'`.txt
     if [ -f $mfile ]; then 
	awk -v dzien=`date +'%-d'` '{if(NR==dzien){print}}' $mfile | iconv -f utf-8
     else 
	return 1
     fi	
}

if [ -n "$LC_ALL" ]; then
    LANGNAME="$LC_ALL"
elif [ -n "$LC_MESSAGES" ]; then
    LANGNAME="$LC_MESSAGES"
elif [ -n "${LANG}" ]; then
    LANGNAME="$LANG"
else 
    LANGNAME="C"
fi

if [ ! -d $DATADIR/$LANGNAME ]; then
    echo "Unsupported locale configuration." >&2
    exit 1
fi

case "$LANGNAME" in
    pl_PL*|pl)
	 echo -n "`date +%x`, imieniny "  
	 print_nameday
	 exit $?
	 ;;
    *)
	echo "Error: $LANG directory exists, but is not supported." >&2
	exit 1
	;;
esac

# Shouldn't reach that point:
exit 1
