#!/bin/env python3
#
# Script gets a list of possible css properties from mozilla and creates a flow type definition.
#

import re
import sys
import requests
from bs4 import BeautifulSoup

sl = re.compile('-')

def conv(w):
    global sl
    m = sl.search(w)
    while m:
        w = list(w)
        w[m.start()+1] = w[m.start()+1].upper()
        w[m.start()] = ''
        w = ''.join(w)
        m = sl.search(w)
    return w

def main():
    if len(sys.argv) != 2:
        print('Usage: {0} output_filename'.format(sys.argv[0]))
        return
    file_name = sys.argv[1]
    excluded_chars = re.compile('[^\w ^-]')
    exlude = re.compile(r'\bvh\b|\bvw\b|\bvmax\b|\bvmin\b|\bpx\b|\bmm\b|\bq\b|\bcm\b|\bin\b|\bpt\b|\bpc\b|\bmozmn\b|\bem\b|\bex\b|\bch\b|\brem\b|\belementname\b|\bA B\b|\bdeg\b|\bgrad\b|\brad\b|\bturn\b|\bhz\b|\bkhz\b|\bs\b|\bms\b|\bunset\b|\bdpi\b|\bdpcm\b|\bdppx\b')
    r = requests.get('https://developer.mozilla.org/en-US/docs/Web/CSS/Reference')
    s = BeautifulSoup(r.text, 'lxml')
    all_css = [a.text for a in s.find_all('code')]
    css_props = [conv(t) for t in all_css if not excluded_chars.search(t)]
    with open(file_name, 'w') as f:
        f.write('declare type InlineStyle = {\n')
        for p in css_props[1:]:
            if not exlude.search(p):
                f.write('  {0}?: string,\n'.format(p))
        f.write('};\n')
    return

if __name__ == '__main__':
    main()
