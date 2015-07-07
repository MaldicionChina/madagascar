sfvelcon = rsf.doc.rsfprog('sfvelcon','user/fomels/Mvelcon.c','''Post-stack velocity continuation by implicit finite differences ''')
sfvelcon.par('vel',rsf.doc.rsfpar('float','0.75','','''final velocity '''))
sfvelcon.par('v0',rsf.doc.rsfpar('float','0.','','''starting velocity '''))
sfvelcon.par('nv',rsf.doc.rsfpar('int','n1','','''number of steps '''))
sfvelcon.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfvelcon.par('add',rsf.doc.rsfpar('bool','n','','''addition flag '''))
sfvelcon.par('inv',rsf.doc.rsfpar('int','0','','''amplitude type '''))
sfvelcon.version('1.7')
sfvelcon.synopsis('''sfvelcon < in.rsf > out.rsf vel=0.75 v0=0. nv=n1 adj=n add=n inv=0''','''''')
rsf.doc.progs['sfvelcon']=sfvelcon

