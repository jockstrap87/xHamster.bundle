xHamster.bundle
===============

Video/Adult 18+ Plex-Plugin - Browse, search and watch videos from xHamster.com

==============================================================================================

tested on server:slackware-13.1/unraid-plex 0.9.8.10  clients: roku2, firefox 25.0 plex client 

===========================================================================================


INSTALLATION:
==============================================================================================

from this url:

https://github.com/johnny8ch/xHamster.bundle

look for download zip button and download files as zip.
you will get xHamster.bundle-master.zip

unzip files into:
YourPlexServerBase/Library/Application Support/Plex Media Server/Plug-ins/


unzip -d YourPlexServerBase/Library/Application Support/Plex Media Server/Plug-ins/ 

this will create xHamster.bundle-master directory in above noted directory.
rename xHamster.bundle-master directory to xHamster.bundle

restart your plex server

====================================================================================
Install script for linux:
===================================================================================
#!/bin/sh
if [ -z "${myplexserverbase}" ]
then
echo export myplexserverbase=some_directory_where_plex_is_installed
exit
fi
if [ ! -d "${myplexserverbase}/Library/Application Support/Plex Media Server/Plug-ins/" ]
then
echo yourplexserver base is not a directory
exit
fi
cd "${myplexserverbase}/Library/Application Support/Plex Media Server/Plug-ins/"
wget -O xHamster.bundle-master.zip --no-check-certificate \
https://github.com/johnny8ch/xHamster.bundle/archive/master.zip
unzip  xHamster.bundle-master.zip
if [ -d xHamster.bundle ]
then
mv  xHamster.bundle xHamster.bundle.zz.bak
fi
mv xHamster.bundle-master xHamster.bundle
rm xHamster.bundle-master.zip


================================================================================================

NOTES:
====================================================================================================
ok, so this is attempt to get xHamster running with plex channels

i forked flownex xHamster bundle and uploaded __init__.py to get channel working.

-- also added URL Service for extracting and playing mp4 files

the URL that is served will correspond to mp4 video file with h264/aac encoding.

direct plays on roku - but my linux plex web client wont direct play so it is a bit sketch on that --
but, most sweet on roku !!!

Interface is minimal - but functional

Njoy and dont blame me if you dont backup files and your s*^t breaks ;)


==============================================================================



if anyone from xhamster.com objects to use of this plugin, please advise me of your objection, and i
will remove immediately
