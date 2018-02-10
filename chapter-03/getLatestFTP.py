# encoding: utf-8

import os
import ftplib
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        ftp = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        print('can not connect to %s ' % HOST)
        return
    print('connect to host ', HOST)

    try:
        ftp.login()
    except ftplib.error_perm as e:
        print('can not login')
        ftp.quit()
        return
    print('login as anonymous')

    try:
        ftp.cwd(DIRN)
    except ftplib.error_perm:
        print('can not cd to %s ' % DIRN)
        ftp.quit()
        return
    print('change to %s dir' % DIRN)

    try:
        ftp.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write())
    except ftplib.error_perm:
        print('can not read file %s ' % FILE)
        os.unlink(FILE)
    else:
        print('download %s to CWD' % FILE)
    ftp.quit()


if __name__ == '__main__':
    main()
