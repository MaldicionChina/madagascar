sflosignoi = rsf.doc.rsfprog('sflosignoi','user/gee/Mlosignoi.c','''Local signal and noise separation (N-dimensional).''')
sflosignoi.par('sfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflosignoi.par('nfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflosignoi.par('eps',rsf.doc.rsfpar('float','','','''regularization parameter '''))
sflosignoi.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sflosignoi.par('slag',rsf.doc.rsfpar('string ',desc=''''''))
sflosignoi.par('nlag',rsf.doc.rsfpar('string ',desc=''''''))
sflosignoi.version('1.7 Mlosignoi.c 7591 2011-08-15 17:11:55Z sfomel')
sflosignoi.synopsis('''sflosignoi < dat.rsf > signal.rsf sfilt=spef.rsf nfilt=npef.rsf eps= niter=20 slag= nlag=''','''
Signal and noise separation by inversion (super-deconvolution).
Uses the helix and patching technologies.
''')
rsf.doc.progs['sflosignoi']=sflosignoi

