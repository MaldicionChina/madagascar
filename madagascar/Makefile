SCONS = RSFROOT=/mnt/Archivos/Universidad_de_Antioquia/Proyectos/C3_LINUX/debian_packaging/paquetes/En_Proceso/madagascar/Paquete/madagascar-1.7/debian/madagascar/usr PYTHONPATH=/mnt/Archivos/Universidad_de_Antioquia/Proyectos/C3_LINUX/debian_packaging/paquetes/En_Proceso/madagascar/Paquete/madagascar-1.7/debian/madagascar/usr/lib/python2.7/dist-packages /usr/bin/scons

all:
	$(SCONS)

install:
	$(SCONS) install

clean:
	$(SCONS) -c
	rm .sconsign*

distclean:
	$(SCONS) -c install
	rm -r .sconsign* build

