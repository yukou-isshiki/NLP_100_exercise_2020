#!/usr/bin/env bash
diff <(cut -f 1 ../popular-names.txt) ../col1.txt
diff <(cut -f 2 ../popular-names.txt) ../col2.txt