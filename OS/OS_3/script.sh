#!/bin/bash

urlPattern="^http(s)?:\/\/(\S)+\.((jpg)|(webp)|(gif)|(png)|(svg)|(jpeg))$"

output="./xphoto"

if [[ $1 =~ $urlPattern ]]; then
	wget -q $1 -P $output
else
	echo "There's the exception"
fi


