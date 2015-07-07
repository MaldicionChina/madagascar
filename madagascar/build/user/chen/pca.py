sfpca = rsf.doc.rsfprog('sfpca','user/chen/Mpca.c','''KL transform. ''')
sfpca.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfpca.par('nc',rsf.doc.rsfpar('int','n1','','''number of components [ 0 < nc < n1 ] '''))
sfpca.par('eta',rsf.doc.rsfpar('float','0.9','','''energy ratio for signal subspace [ 0 eta < 1 ]'''))
sfpca.version('1.7')
sfpca.synopsis('''sfpca < in.rsf > out.rsf verb=y nc=n1 eta=0.9''','''''')
rsf.doc.progs['sfpca']=sfpca

