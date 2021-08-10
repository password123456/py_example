#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import re
from datetime import datetime, timedelta


def main():
    INPUT_LOG = 'access.log'

    lineformat = re.compile(
        r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""",
        re.IGNORECASE)

    try:
        if os.path.exists(INPUT_LOG):
            f = open(INPUT_LOG, 'r')
            n = 0
            for n,line in enumerate(f.read().split('\n')):
                data = re.search(lineformat, line)
                #print(data)
                if data:
                    n = n + 1
                    datadict = data.groupdict()
                    ip = datadict["ipaddress"]
                    datetimestring = datadict["dateandtime"]

                    t = datetime.strptime(datetimestring, '%d/%b/%Y:%H:%M:%S %z')
                    t = t.strftime('%Y-%m-%d %H:%M:%S')
                    print(t)
                    url = datadict["url"]
                    bytessent = datadict["bytessent"]
                    referrer = datadict["refferer"]
                    useragent = datadict["useragent"]
                    status = datadict["statuscode"]
                    method = data.group(6)

                    '''
                    print('ip: %s\ntime: %s' % (ip, datetimestring))
                    print('time: %s' % datetimestring)
                    print('url: %s' % url)
                    print('bytessent: %s' % bytessent)
                    print('referrer: %s' % referrer)
                    print('useragent: %s' % useragent)
                    print('status: %s' % status)
                    print('method: %s' % method)
                    '''

            f.close()
            print('Total Log: %d' % n )
        else:
            print('%s not found\n' % INPUT_LOG)
    except Exception as e:
        print(e)
        sys.exit(1)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)