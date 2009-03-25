# !/usr/bin/env python
# encoding: utf-8

import sys, string

file = open(sys.argv[1],'r')
str = file.readlines()
str.sort()
str=string.join(str)
print str
