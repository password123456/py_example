#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os


def main():
    print(os.getcwd())
    upload_filename = '../../333.jsp'
    upload_filename = './././../../../333.jpg'
    upload_filename = '333.jsp'

    try:
        if not upload_filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print('[-] intput: %s' % upload_filename)
            print('[-] error: upload file extention is not image files')
            sys.exit(1)

        if './' in upload_filename.lower() or '../' in upload_filename.lower():
            print('[+] input: %s' % upload_filename)

            upload_filename = upload_filename.rsplit('.', 1)
            u_filename = upload_filename[0]
            u_filext = upload_filename[1]
            print('%s %s' % (u_filename, u_filext))

            u_filename = u_filename.replace('.', '')
            u_filename = u_filename.replace('/', '')
            print('[-] convert: %s.%s' % (u_filename, u_filext))

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