sflffdan = rsf.doc.rsfprog('sflffdan','user/songxl/Mlffdan.cc','''2D high-order TTI Lowrank FFD coefficient''')
sflffdan.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflffdan.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sflffdan.par('npk',rsf.doc.rsfpar('','50','','''maximum rank'''))
sflffdan.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sflffdan.par('pr',rsf.doc.rsfpar('','0.25','','''time step'''))
sflffdan.par('size',rsf.doc.rsfpar('','9','','''stencil length'''))
sflffdan.par('de',rsf.doc.rsfpar('','1','','''stencil length'''))
sflffdan.version('1.7')
sflffdan.synopsis('''sflffdan < velz.rsf > outm.rsf seed=time(NULL eps=1.e-6 npk=50 dt= pr=0.25 size=9 de=1''','''''')
rsf.doc.progs['sflffdan']=sflffdan

