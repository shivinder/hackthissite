#!/usr/bin/env python3

with open('PNG.png','rb') as picture_binary:
    for line in picture_binary:
        print(line)