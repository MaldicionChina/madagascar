sfsglfdcx1 = rsf.doc.rsfprog('sfsglfdcx1','user/fangg/Msglfdcx1.cc','''1D Lowrank FD coefficient of d/dx on staggered grid''')
sfsglfdcx1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfsglfdcx1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfsglfdcx1.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfsglfdcx1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfsglfdcx1.par('size',rsf.doc.rsfpar('','6','','''stencil length'''))
sfsglfdcx1.version('1.7')
sfsglfdcx1.synopsis('''sfsglfdcx1 < velf.rsf > outm.rsf seed=time(NULL eps=1.e-4 npk=20 dt= size=6''','''''')
rsf.doc.progs['sfsglfdcx1']=sfsglfdcx1

