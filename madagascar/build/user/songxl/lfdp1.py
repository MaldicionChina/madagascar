sflfdp1 = rsf.doc.rsfprog('sflfdp1','user/songxl/Mlfdp1.cc','''1D 10th-order Lowrank FD coefficient''')
sflfdp1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflfdp1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sflfdp1.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sflfdp1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sflfdp1.par('size',rsf.doc.rsfpar('','6','','''stencil length'''))
sflfdp1.version('1.7')
sflfdp1.synopsis('''sflfdp1 < velf.rsf > outm.rsf seed=time(NULL eps=1.e-4 npk=20 dt= size=6''','''''')
rsf.doc.progs['sflfdp1']=sflfdp1

