sfTestfd2d = rsf.doc.rsfprog('sfTestfd2d','user/pyang/MTestfd2d.c','''A demo of 2D FD test''')
sfTestfd2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfTestfd2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestfd2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestfd2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestfd2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestfd2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestfd2d.version('1.7')
sfTestfd2d.synopsis('''sfTestfd2d < Fv.rsf > Fw.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1''','''  Sponage absorbing boundary condition
''')
rsf.doc.progs['sfTestfd2d']=sfTestfd2d

