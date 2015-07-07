sfmsmiss = rsf.doc.rsfprog('sfmsmiss','user/gee/Mmsmiss.c','''Multiscale missing data interpolation (N-dimensional). ''')
sfmsmiss.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmsmiss.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmsmiss.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmsmiss.par('lag',rsf.doc.rsfpar('string ',desc='''optional input file with filter lags '''))
sfmsmiss.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmsmiss.version('1.7 Mmsmiss.c 4796 2009-09-29 19:39:07Z ivlad')
sfmsmiss.synopsis('''sfmsmiss < in.rsf filt=filt.rsf > out.rsf mask=mask.rsf niter=100 lag=''','''''')
rsf.doc.progs['sfmsmiss']=sfmsmiss

