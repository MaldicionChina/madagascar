sfaastack = rsf.doc.rsfprog('sfaastack','system/seismic/Maastack.c','''Stack with antialiasing ''')
sfaastack.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfaastack.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag '''))
sfaastack.par('n2',rsf.doc.rsfpar('int','15','',''''''))
sfaastack.par('n2',rsf.doc.rsfpar('int','1','',''''''))
sfaastack.par('vel',rsf.doc.rsfpar('float','1.5','','''velocity '''))
sfaastack.par('antialias',rsf.doc.rsfpar('float','1.','','''antialiasing '''))
sfaastack.par('box',rsf.doc.rsfpar('bool','n','','''box antialiasing '''))
sfaastack.version('1.7')
sfaastack.synopsis('''sfaastack < inp.rsf > out.rsf adj=n inv=n n2=15 n2=1 vel=1.5 antialias=1. box=n''','''''')
rsf.doc.progs['sfaastack']=sfaastack

