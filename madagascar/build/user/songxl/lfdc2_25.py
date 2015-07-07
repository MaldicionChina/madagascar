sflfdc2_25 = rsf.doc.rsfprog('sflfdc2_25','user/songxl/Mlfdc2_25.cc','''2D 10th-order Lowrank FD coefficient''')
sflfdc2_25.par('s1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflfdc2_25.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflfdc2_25.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sflfdc2_25.par('npk',rsf.doc.rsfpar('','50','','''maximum rank'''))
sflfdc2_25.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sflfdc2_25.par('size',rsf.doc.rsfpar('','9','','''stencil length'''))
sflfdc2_25.version('1.7')
sflfdc2_25.synopsis('''sflfdc2_25 < velf.rsf > outm.rsf s1=s1f.rsf seed=time(NULL eps=1.e-6 npk=50 dt= size=9''','''''')
rsf.doc.progs['sflfdc2_25']=sflfdc2_25

