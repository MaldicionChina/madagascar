sfdmo = rsf.doc.rsfprog('sfdmo','system/seismic/Mdmo.c','''Kirchhoff DMO with antialiasing by reparameterization. ''')
sfdmo.par('mint',rsf.doc.rsfpar('int','2','','''starting time sample '''))
sfdmo.par('n',rsf.doc.rsfpar('int','32','','''number of offset samples '''))
sfdmo.par('adj',rsf.doc.rsfpar('bool','y','','''adjoint flag '''))
sfdmo.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfdmo.par('type',rsf.doc.rsfpar('int','1','','''type of amplitude (0,1,2,3) '''))
sfdmo.par('h',rsf.doc.rsfpar('float','','',''''''))
sfdmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the third axis is half-offset instead of full offset '''))
sfdmo.par('velhalf',rsf.doc.rsfpar('float','0.75','','''half-velocity '''))
sfdmo.version('1.7')
sfdmo.synopsis('''sfdmo < in.rsf > out.rsf mint=2 n=32 adj=y inv=n type=1 h= half=y velhalf=0.75''','''''')
rsf.doc.progs['sfdmo']=sfdmo

