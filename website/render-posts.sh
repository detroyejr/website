#!/bin/bash

for f in posts/*; do
    n=$(echo $f | sed 's/.md/.html/g')
    pandoc --highlight-style monochrome -f markdown -t html $f -o app/$n
done
