sflfdc2_7 = rsf.doc.rsfprog('sflfdc2_7','user/songxl/Mlfdc2_7.cc','''2D 10th-order Lowrank FD coefficient''')
sflfdc2_7.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflfdc2_7.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sflfdc2_7.par('npk',rsf.doc.rsfpar('','50','','''maximum rank'''))
sflfdc2_7.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sflfdc2_7.par('size',rsf.doc.rsfpar('','6','','''stencil length'''))
sflfdc2_7.version('1.7')
sflfdc2_7.synopsis('''sflfdc2_7 < velf.rsf > outm.rsf seed=time(NULL eps=1.e-6 npk=50 dt= size=6''','''''')
rsf.doc.progs['sflfdc2_7']=sflfdc2_7

