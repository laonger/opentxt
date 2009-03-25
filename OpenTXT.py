# !/usr/bin/python
# encoding: utf-8

import os, sys, chardet, string
#print sys.argv[0]
#print sys.argv[1]

encodings={'GB2312':'-2147482062', 'utf-8':'4', 'HZ-GB-2312':'-2147481083',\
		'ISO-8859-2':'-1677721344', 'UTF-32BE':'-1946156800', 'EUC-TW':'-2147481295',\
		'Big5':'-2147483646', 'IBM855':'-2147480575', 'ascii':'1', 'UTF-16BE':'10',\
		'NONE':'-1744830208'}

file = open(sys.argv[1],'r')
str = string.join(file.readlines())
file.close()
str_encoding = chardet.detect(str)['encoding']
if str_encoding == None:
	str_encoding = 'None'
else:
	print str_encoding
	str_encoding=encodings[str_encoding]
	print str_encoding
	#os.popen('open TextEdit')
	os.popen('''/Applications/TextEdit.app/Contents/MacOS/TextEdit -PlainTextEncoding '('''+str_encoding+''')' "'''+sys.argv[1]+'''"''')
