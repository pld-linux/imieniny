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


if [ ${LANG}x != x ]; then
    LANGNAME=$LANG
else 
    LANGNAME="C"
fi

if [ ! -d $DATADIR/$LANGNAME ]; then
    exit 1
fi

case "$LANGNAME" in
    pl_PL|pl)
	 echo -n "`date +%Y.%m.%d`, imieniny "  
	 print_nameday
	 exit $?
    ;;
    esac
fi
exit 1
