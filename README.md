#Empaquetamiento Madagascar por SciDeb

Nos reducirán algunas líneas de código en el proceso de de empaquetamiento
```
$ DEBFULLNAME="nombre completo"
$ DEBEMAIL=correo electronico
$ export DEBFULLNAME DEBEMAIL
```
Para empaquetar el siguiente programa instalar:
```
# apt-get install lintian dh-make devscripts debhelper build-essential scons dh-exec dpatch wget autotools-dev
```
Descargar Madagascar 1.7:
```
chmod +x preSetupMadagascar-1.7.sh  

./preSetupMadagascar-1.7.sh
```

Desde la carpeta seismic-unix/seismic-unix/ ejecutar el siguiente comando:
```
$ debuild -r'fakeroot' -i -us -uc -B
```
