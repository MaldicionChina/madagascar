sflfdanc2_25 = rsf.doc.rsfprog('sflfdanc2_25','user/songxl/Mlfdanc2_25.cc','''2D high-order TTI Lowrank FD coefficient''')
sflfdanc2_25.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflfdanc2_25.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sflfdanc2_25.par('npk',rsf.doc.rsfpar('','50','','''maximum rank'''))
sflfdanc2_25.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sflfdanc2_25.par('size',rsf.doc.rsfpar('','17','','''stencil length'''))
sflfdanc2_25.par('de',rsf.doc.rsfpar('','1','','''stencil length'''))
sflfdanc2_25.version('1.7')
sflfdanc2_25.synopsis('''sflfdanc2_25 < velz.rsf > outm.rsf seed=time(NULL eps=1.e-6 npk=50 dt= size=17 de=1''','''''')
rsf.doc.progs['sflfdanc2_25']=sflfdanc2_25

