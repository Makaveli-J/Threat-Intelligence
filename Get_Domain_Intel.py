#!/usr/bin/env python
#coding=utf-8

import hashlib
import wget

#Set Sources of Threat Intelligence
TI_URLs = ['']

#Download from URLs
for i in TI_URLs:
    wget.download(i, out = '/etc/ti/domains/')

new_file = 'newfile'
old_file = 'old_file'

#Check if file content updated
new_hash = hashlib.md5(new_file.encode()).hexdigest()
old_hash = hashlib.md5(old_file.encode()).hexdigest()