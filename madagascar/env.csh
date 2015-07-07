#!/bin/csh

# Path for Madagascar installation directory
setenv RSFROOT /mnt/Archivos/Universidad_de_Antioquia/Proyectos/C3_LINUX/debian_packaging/paquetes/En_Proceso/madagascar/Paquete/madagascar-1.7/debian/madagascar/usr

# Path for Madagascar source directory
setenv RSFSRC /mnt/Archivos/Universidad_de_Antioquia/Proyectos/C3_LINUX/debian_packaging/paquetes/En_Proceso/madagascar/Paquete/madagascar-1.7

# Path for Python packages
if ($?PYTHONPATH) then
setenv PYTHONPATH $RSFROOT/lib/python2.7/dist-packages:${PYTHONPATH}
else
setenv PYTHONPATH $RSFROOT/lib/python2.7/dist-packages
endif

# Path for binary data files part of RSF datasets
setenv DATAPATH /var/tmp/

# Path for manual pages
setenv MANPATH `manpath`:$RSFROOT/share/man

# Path for shared object files
if ($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH $RSFROOT/lib:${LD_LIBRARY_PATH}
else
setenv LD_LIBRARY_PATH $RSFROOT/lib
endif

# Path for executables
set path = ($RSFROOT/bin $path)
