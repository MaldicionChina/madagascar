sfTestfd3d = rsf.doc.rsfprog('sfTestfd3d','user/pyang/MTestfd3d.c','''3D acoustic time-domain FD modeling''')
sfTestfd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestfd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestfd3d.par('frsf',rsf.doc.rsfpar('bool','n','','''free surface or not '''))
sfTestfd3d.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfTestfd3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfTestfd3d.par('ns',rsf.doc.rsfpar('int','1','',''''''))
sfTestfd3d.par('nb',rsf.doc.rsfpar('int','30','',''''''))
sfTestfd3d.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfTestfd3d.par('fm',rsf.doc.rsfpar('float','20','',''''''))
sfTestfd3d.version('1.7')
sfTestfd3d.synopsis('''sfTestfd3d < Fv.rsf > Fw.rsf verb=n verb=n frsf=n nt= kt= ns=1 nb=30 dt= fm=20''','''4th order in space, 2nd order in time, sponge absorbing boundary condition.
''')
rsf.doc.progs['sfTestfd3d']=sfTestfd3d

