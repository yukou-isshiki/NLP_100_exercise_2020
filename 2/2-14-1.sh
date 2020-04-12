#!/usr/bin/env bash

line_amount=4

diff <(python3 2-14-1.py $line_amount) <(head -n $line_amount ../popular-names.txt)