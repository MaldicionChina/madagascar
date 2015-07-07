sflfdc1 = rsf.doc.rsfprog('sflfdc1','user/songxl/Mlfdc1.cc','''1D 10th-order Lowrank FD coefficient''')
sflfdc1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflfdc1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sflfdc1.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sflfdc1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sflfdc1.version('1.7')
sflfdc1.synopsis('''sflfdc1 < velf.rsf > outm.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sflfdc1']=sflfdc1

