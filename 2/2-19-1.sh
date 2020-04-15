#!/usr/bin/env bash

diff <(python3 2-19-1.py) <(cat ../popular-names.txt | cut -f 1 | sort | uniq -c | sort -r)

