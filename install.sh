#!/bin/sh

curl https://pypi.python.org/packages/ca/f4/91a056f11751701c24f86c692d92fee290b0ba3f99f657cdeb85ad3da402/feedparser-5.2.1.tar.gz#md5=d552f7a2a55e8e33b2a3fe1082505b42 --output feedparser.tar.gz
tar -xf feedparser.tar.gz
cd feedparser-5.2.1/
python setup.py install
cd ..
rm feedparser.tar.gz
rm -rf feedparser-5.2.1/
