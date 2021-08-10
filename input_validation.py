#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def main():
    print('--- parameter filetering example ---')
    p = "'<script>alert(1)</script>"
    print('[+] input: %s' % p )

    p = p.lower()
    p = p.replace('<','&lt;')
    p = p.replace('>', '&gt;')
    p = p.replace('&', '&amp;')
    p = p.replace('"', '&quot;')
    p = p.replace("'", '&#x27;')
    p = p.replace('/', '&#x2F;')
    p = p.replace('script', 'x-script;')

    print('[-] output: %s\n' % p )


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)


