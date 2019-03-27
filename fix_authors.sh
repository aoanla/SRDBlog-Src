#!/bin/bash


for l in `cat srd-all.authors`;
do
	METAFILE=posts/${l%%|*}.meta
	AUTHOR=${l##*|}
	echo METAFILE is $METAFILE
	echo AUTHOR is $AUTHOR
	sed "s/^$/.. author: $AUTHOR/" $METAFILE > file.tmp
	echo >> file.tmp
	mv file.tmp $METAFILE
done	
