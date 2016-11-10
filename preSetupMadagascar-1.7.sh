#!/bin/bash

#Download Madagascar-1.7
wget http://downloads.sourceforge.net/project/rsf/madagascar/madagascar-1.7/madagascar-1.7.tar.gz -O madagascar_1.7.orig.tar.gz

# untar and extract in madagascar folder
tar -xzf madagascar-1.7.orig.tar.gz -C ./madagascar --strip-components=1
