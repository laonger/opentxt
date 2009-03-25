# !/usr/bin/evn python
# encoding: utf-8

import os, sys, chardet, string, glob
print sys.argv[0]

#encodings={'GB2312': '-2147482062', 'utf-8': '4', 'HZ-GB-2312': '-2147481083'}
files=glob.glob('*.txt')
for f in files:
	str=''
	str_encoding=''
	file = open(f,'r')
	str = string.join(file.readlines())
	file.close()
	str_encoding = chardet.detect(str)['encoding']
	if str_encoding == None:
		print f+': '+'NONE'
	else:
		#print 'f:'+f
		#print 'str_encoding:'+str_encoding
		print f+': '+str_encoding
