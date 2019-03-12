#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fileinput
#import re


# Create a new .md-file for each line in the input-file

if __name__ == '__main__':
    for line in fileinput.input():
        name = line.strip()
        url = name.replace(" ","")
        url = url.replace("ä", "ae")
        url = url.replace("ö", "oe")
        url = url.replace("ü", "ue")
        url = url.replace("ß", "ss")
        url = url.replace(",", "&")
        url = url.replace("/", "-")
        f = open("%s.md" % url, "w+")
        f.write("---\nlayout: institution\ntitle: " + name + "\nmyvariable: "  + "\n---\n")
