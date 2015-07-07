sfmiss4 = rsf.doc.rsfprog('sfmiss4','user/yliu/Mmiss4.c','''Missing data interpolation with adaptive PEFs. ''')
sfmiss4.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss4.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss4.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss4.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfmiss4.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfmiss4.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmiss4.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss4.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss4.version('1.7 Mmiss4.c 7107 2011-04-10 02:04:14Z ivlad')
sfmiss4.synopsis('''sfmiss4 < in.rsf filt=fil.rsf > out.rsf mask=mask.rsf niter=100 exact=y eps=0. verb=n''','''''')
rsf.doc.progs['sfmiss4']=sfmiss4

