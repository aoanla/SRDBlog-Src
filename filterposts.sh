#!/bin/bash

#find a list of all of the posts which exist

#find ./posts/ -name "*.md"

for item in $(find ./posts/ -name "*.md")
do
	sed 's/scottishrollerderby.wordpress.com/scottishrollerderbyblog.com/g; sIhttp://%EF%BF%BCIIg; s/scottishrollerderby.files.wordpress.com/scottishrollerderbyblog.com/g' $item > ${item}.new
	sed 'sI/scottishrollerderbyblogI/www.scottishrollerderbyblogIg;' ${item}.new > ${item}
	#rm $item
	#mv ${item}.new $item
done

#metas to process
#find ./posts/ -name "*.meta"

for item in $(find ./posts/ -name "*.meta")
do
	python filterpost-meta.py $item
	rm $item
	mv ${item}.new $item
done
