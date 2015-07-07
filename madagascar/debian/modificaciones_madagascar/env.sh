#!/bin/sh

# Path for Madagascar installation directory
export RSFROOT=/usr

# Path for Madagascar source directory
#export RSFSRC=

# Path for Python packages
if [ -n "$PYTHONPATH" ]; then
export PYTHONPATH=$RSFROOT/lib/python2.7/dist-packages:${PYTHONPATH}
else
export PYTHONPATH=$RSFROOT/lib/python2.7/dist-packages
fi

# Path for binary data files part of RSF datasets
export DATAPATH=/var/tmp/

# Path for manual pages
unset MANPATH
export MANPATH=`manpath`:$RSFROOT/share/man

# Path for shared object files
if [ -n "$LD_LIBRARY_PATH" ]; then
export LD_LIBRARY_PATH=$RSFROOT/lib:${LD_LIBRARY_PATH}
else
export LD_LIBRARY_PATH=$RSFROOT/lib
fi

# Path for executables
export PATH=$RSFROOT/bin:$PATH
