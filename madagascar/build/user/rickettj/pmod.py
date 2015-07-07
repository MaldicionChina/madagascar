sfpmod = rsf.doc.rsfprog('sfpmod','user/rickettj/Mpmod.c','''Random plane wave modeling. ''')
sfpmod.par('np',rsf.doc.rsfpar('int','1','',''''''))
sfpmod.par('gauss',rsf.doc.rsfpar('int','0','',''''''))
sfpmod.par('type',rsf.doc.rsfpar('int','1','','''1 single plane layer
       2 two plane layers
       3 point diffractor '''))
sfpmod.par('ampmax',rsf.doc.rsfpar('float','1.','',''''''))
sfpmod.par('rc1',rsf.doc.rsfpar('float','0.2','',''''''))
sfpmod.par('rc2',rsf.doc.rsfpar('float','0.2','',''''''))
sfpmod.par('h1',rsf.doc.rsfpar('float','200.','',''''''))
sfpmod.par('h2',rsf.doc.rsfpar('float','150.','',''''''))
sfpmod.par('v1',rsf.doc.rsfpar('float','2000.','',''''''))
sfpmod.par('v2',rsf.doc.rsfpar('float','3000.','',''''''))
sfpmod.par('pmax',rsf.doc.rsfpar('float','0.000332','',''''''))
sfpmod.par('phi',rsf.doc.rsfpar('float','0.1','',''''''))
sfpmod.par('xloc',rsf.doc.rsfpar('float','200.','',''''''))
sfpmod.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfpmod.version('1.7')
sfpmod.synopsis('''sfpmod < inp.rsf > out.rsf np=1 gauss=0 type=1 ampmax=1. rc1=0.2 rc2=0.2 h1=200. h2=150. v1=2000. v2=3000. pmax=0.000332 phi=0.1 xloc=200. seed=time(NULL)''','''''')
rsf.doc.progs['sfpmod']=sfpmod

