sfsignoi = rsf.doc.rsfprog('sfsignoi','user/gee/Msignoi.c','''Signal and noise separation (N-dimensional). ''')
sfsignoi.par('sfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsignoi.par('nfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsignoi.par('epsilon',rsf.doc.rsfpar('float','','','''regularization parameter '''))
sfsignoi.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfsignoi.par('spitz',rsf.doc.rsfpar('bool','n','','''if use Spitz method '''))
sfsignoi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfsignoi.par('slag',rsf.doc.rsfpar('string ',desc=''''''))
sfsignoi.par('nlag',rsf.doc.rsfpar('string ',desc=''''''))
sfsignoi.version('1.7 Msignoi.c 7591 2011-08-15 17:11:55Z sfomel')
sfsignoi.synopsis('''sfsignoi < dat.rsf > signoi.rsf sfilt=spef.rsf nfilt=npef.rsf epsilon= niter=20 spitz=n verb=n slag= nlag=''','''''')
rsf.doc.progs['sfsignoi']=sfsignoi

