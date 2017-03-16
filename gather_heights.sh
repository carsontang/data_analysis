#! /bin/bash
for x in {a..z}
do
				curl http://www.basketball-reference.com/players/${x}/ \
				| awk '/<tbody>/,/<\/tbody>/' | perl -p -e 's/<tr  class="">/<tr>/g' \
				| tail -n +2 | sed '$d' | sed 's/<tr>//g' | tr -s '\n' \
				| sed -E -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' -e 's/<\/td>//g' -e 's/<td.*" >//g' -e 's/<td.*csk="[0-9.]*">//g' \
				| sed -E 's/^$/NONE/g' | sed -E -e 's/<a href=.*>(.*)<\/a>/\1/g' | tail -n +2 \
				| sed 's/<\/tr>//g' | gawk 'BEGIN { RS="\n\n"; FS="\n"; } {print $5}' | gawk -F- '{print $1 + $2/12}' >> heights.txt
done
