sfmiss43 = rsf.doc.rsfprog('sfmiss43','user/yliu/Mmiss43.c','''3-D missing data interpolation with adaptive PEFs. ''')
sfmiss43.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss43.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss43.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss43.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfmiss43.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfmiss43.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmiss43.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss43.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss43.version('1.7 Mmiss43.c 7107 2011-04-10 02:04:14Z ivlad')
sfmiss43.synopsis('''sfmiss43 < in.rsf filt=fil.rsf > out.rsf mask=mask.rsf niter=100 exact=y eps=0. verb=n''','''''')
rsf.doc.progs['sfmiss43']=sfmiss43

