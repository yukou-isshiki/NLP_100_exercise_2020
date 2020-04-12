#!/usr/bin/env bash

line_amount=3

diff <(python3 2-15-1.py $line_amount) <(tail -n $line_amount ../popular-names.txt)