#!/usr/bin/env python
#coding=utf-8

import hashlib
import wget
import TI_Sources
import re
import requests

#Download from URLs
for i in TI_Sources.TI_Domain:
    wget.download(i, out = '/etc/ti/domain/')
for i in TI_Sources.TI_IP:
    wget.download(i, out = '/etc/ti/ip/')
r = requests.get('')
lst = r.content
test = re.findall(r'<a[^>]* href="([^"]*)"', lst)
for i in test:
    if re.search(r'csv$', i) != None:
        print(i)

new_file = 'new_file'
old_file = 'old_file'


def filechk(new_file, old_file):

    #open new file & old file
    new_file_0 = open(new_file, 'r', encoding='utf-8').read()
    old_file_0 = open(old_file, 'r', encoding='utf-8').read()

    #generate hashes for new & old files
    new_hash = hashlib.md5(new_file_0.encode()).hexdigest()
    old_hash = hashlib.md5(old_file_0.encode()).hexdigest()

    if new_hash == old_hash:
        return True
    else:
        return False