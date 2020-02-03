#!/bin/bash

if [ $# -lt 1 ] ; then
  me=`basename "$0"`
  echo "Usage: ./$me input01.pbf input02.pbf input03.pbf ..."
  exit 1
fi

count=0

for i in "$@"
do
  numfeatures=$(~/modules/vt2geojson/vt2geojson "$i" | grep geometry | wc -l)
  count=$((count+numfeatures))
  echo "$i: $numfeatures / $count"
done
