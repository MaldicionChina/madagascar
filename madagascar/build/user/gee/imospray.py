sfimospray = rsf.doc.rsfprog('sfimospray','user/gee/Mimospray.c','''Inversion of constant-velocity nearest-neighbor inverse NMO. ''')
sfimospray.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfimospray.par('n2',rsf.doc.rsfpar('int','20','','''number of offsets (if inv=n) '''))
sfimospray.par('d2',rsf.doc.rsfpar('float','200.','','''offset sampling (if inv=n) '''))
sfimospray.par('o2',rsf.doc.rsfpar('float','0.','','''offset origin (if inv=n) '''))
sfimospray.par('v',rsf.doc.rsfpar('float','1000.','','''velocity '''))
sfimospray.version('1.7')
sfimospray.synopsis('''sfimospray < in.rsf > out.rsf adj=n n2=20 d2=200. o2=0. v=1000.''','''''')
rsf.doc.progs['sfimospray']=sfimospray

