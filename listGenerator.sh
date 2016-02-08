MAIN_SONGS='../1.tmp'
COVER_SONGS='../2.tmp'
COPY_LIST='../list.tmp'
list=(${MAIN_SONGS} ${COVER_SONGS} ${COPY_LIST})

index=0
while [[ "${list[index]}" != "" ]]; do
	> "${list[index]}"  >/dev/null 2>/dev/null
	index=$(($index+1))
done

git checkout master
cat README.md | egrep "^\* \[" | cut -d "[" -f 2 | cut -d "]" -f 1 > "$MAIN_SONGS"
git checkout covers
cat README.md | egrep "^\* \[" | cut -d "[" -f 2 | cut -d "]" -f 1 > "$COVER_SONGS"

echo "" >> "$MAIN_SONGS"
cat "$MAIN_SONGS" | while read line
do
	cat "$COVER_SONGS" | grep -i "$line" >/dev/null 2>/dev/null
	if [[ "$?" -ne 0 && "$line" != "" ]]; then
		echo "$line" >> "$COPY_LIST"
	fi
done
lines=`cat "$COPY_LIST" | wc -l`

if [[ "$lines" -eq 0 ]]; then
	exit 0
fi

cat "$COPY_LIST" | while read line
do
	echo "$line"
	echo -e "* $line\n  * []()" >> README.md
done