#!/usr/bin/env python
#coding=utf-8

import hashlib
import wget
import TI_Sources

#Download from URLs
for i in TI_Sources.TI_Domain:
    wget.download(i, out = '/etc/ti/domain/')
for i in TI_Sources.TI_IP:
    wget.download(i, out = '/etc/ti/ip/')

new_file = 'new_file'
old_file = 'old_file'

#Check if file content updated
new_hash = hashlib.md5(new_file.encode()).hexdigest()
old_hash = hashlib.md5(old_file.encode()).hexdigest()
def filechk(new_file, old_file):
