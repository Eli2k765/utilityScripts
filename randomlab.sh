#!/bin/bash

read -r random_line < <(shuf labs.txt)

echo $random_line && grep -v "$random_line" labs.txt > filename2; mv filename2 labs.txt
