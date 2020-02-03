#!/bin/bash

if [ $# -lt 2 ] ; then
  me=`basename "$0"`
  echo "Usage: ./$me input_directory output_directory"
  exit 1
fi

if [ $1 = $2 ] ; then
  echo "Input and output directories are equal!"
  exit 1
fi

# Create output_directory, if it doesn't already exist
mkdir -p $2

# Fix the character encoding of the *.txt files in input_directory
for i in $(ls -d $1/*.txt)
do
  output=$(<<<"$i" sed "s|$1|$2|")
  iconv -f cp1252 -t utf8 $i > $output
  echo $output
done
