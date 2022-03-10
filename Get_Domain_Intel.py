#!/usr/bin/env python
#coding=utf-8

import wget

#Set Sources of Threat Intelligence
TI_URLs = ['']

#Download from URLs
for i in TI_URLs:
    wget.download(i, out = '/etc/ti/domains/')