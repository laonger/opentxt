# !/usr/bin/python
# encoding: utf-8

import os, sys, chardet, string
print sys.argv[0]
print sys.argv[1]

encodings={'GB2312': '-2147482062', 'utf-8': '4', 'HZ-GB-2312': '-2147481083    '}

file = open(sys.argv[1],'r')
str = string.join(file.readlines())
str_encoding = chardet.detect(str)['encoding']
print str_encoding
str_encoding=encodings[str_encoding]
print str_encoding
#os.popen('open TextEdit')
os.popen('''/Applications/TextEdit.app/Contents/MacOS/TextEdit -PlainTextEncoding '('''+str_encoding+''')' "'''+sys.argv[1]+'''"''')
