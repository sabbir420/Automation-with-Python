#!/bin/bash

files="$(grep ' jane ' ../data/list.txt | cut -d ' ' -f 3 | cut -d'/' -f 3)"
for file in $files;do
    if test -e /home/student-02-f1be56ffdcc5/data/$file; then
        echo /home/student-02-f1be56ffdcc5/data/$file >> oldFiles.txt
    fi
done