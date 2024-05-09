#! usr/bin/bash
if [ ! -d $3 ]; then
    echo "$0: Error opening dir: $3"
else
    FIND_CMD="find $3 -type f"
    $FIND_CMD -size +$1c -size -$2c -printf "%h, %f, %s\n" > file.txt
cat file.txt
fi
exit 0
