sfsglfdc1 = rsf.doc.rsfprog('sfsglfdc1','user/fangg/Msglfdc1.cc','''1D Lowrank FD coefficient of d/dx on staggered grid (optimized)''')
sfsglfdc1.par('sx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdc1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfsglfdc1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfsglfdc1.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfsglfdc1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfsglfdc1.par('wavnumcut',rsf.doc.rsfpar('','1.0','','''wavenumber cut percentile'''))
sfsglfdc1.par('size',rsf.doc.rsfpar('','6','','''stencil length'''))
sfsglfdc1.version('1.7')
sfsglfdc1.synopsis('''sfsglfdc1 < velf.rsf > outm.rsf sx=fsx.rsf seed=time(NULL eps=1.e-4 npk=20 dt= wavnumcut=1.0 size=6''','''''')
rsf.doc.progs['sfsglfdc1']=sfsglfdc1

