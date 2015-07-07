sfveltran = rsf.doc.rsfprog('sfveltran','system/seismic/Mveltran.c','''Hyperbolic Radon transform ''')
sfveltran.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfveltran.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing '''))
sfveltran.par('s02',rsf.doc.rsfpar('float','0.','','''reference slowness squared (for antialiasing) '''))
sfveltran.par('pull',rsf.doc.rsfpar('bool','y','','''pull or push operator '''))
sfveltran.version('1.7')
sfveltran.synopsis('''sfveltran < in.rsf > out.rsf adj=n anti=1. s02=0. pull=y''','''''')
rsf.doc.progs['sfveltran']=sfveltran

