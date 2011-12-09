#!/usr/bin/env python

import os
import os.path as path
import shutil
import urllib2
import sys

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

## note: these functions are all slapdash!

def download(url,fh):
    f = urllib2.urlopen(url)
    fh.write(f.read())
    return True

def makedirs(p):
    if not os.path.exists(p):
        os.makedirs(p)
    return True    

def create_stick(outdir):
    ''' get all downloadable files, organize into folders 

    Note:  could use some love to make this saner/more robust
    '''
    # gedit
    for (proj,os,url) in (
        ('gedit','windows','http://ftp.gnome.org/pub/GNOME/binaries/win32/gedit/2.30/gedit-setup-2.30.1-1.exe'),
        ('gedit','osx','http://ftp.gnome.org/pub/GNOME/binaries/mac/gedit/2.30/gedit-2.30.2.dmg'),
        ('gedit','linux','http://ftp.gnome.org/pub/GNOME/sources/gedit/2.30/gedit-2.30.2.tar.gz'),
        ('git','windows','http://msysgit.googlecode.com/files/Git-1.7.4-preview20110204.exe'),
        ('git','osx','http://git-osx-installer.googlecode.com/files/git-1.7.4.1-i386-leopard.dmg'),
        ('git','linux','http://kernel.org/pub/software/scm/git/git-1.7.4.1.tar.bz2'),
        ('python','windows','http://python.org/ftp/python/2.7.1/python-2.7.1.msi'),
        ):
        logger.info("getting %s %s %s", proj,os,url)
        p = path.join(outdir,os,proj)
        makedirs(p)
        fh = open(path.join(p,path.basename(url)),'w')
        download(url,fh)
        fh.close()
        
helpstring = """give a path to put all of it in """
def help():
    print helpstring

if __name__ == "__main__":
    try:
        outdir = sys.argv[1]
    except IndexError:
        sys.exit(help())
    
    create_stick(outdir)
