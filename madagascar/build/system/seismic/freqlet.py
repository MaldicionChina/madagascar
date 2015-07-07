sffreqlet = rsf.doc.rsfprog('sffreqlet','system/seismic/Mfreqlet.c','''1-D seislet frame ''')
sffreqlet.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreqlet.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sffreqlet.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffreqlet.par('decomp',rsf.doc.rsfpar('bool','n','','''do decomposition '''))
sffreqlet.par('ncycle',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sffreqlet.par('niter',rsf.doc.rsfpar('int','1','','''number of Bregman iterations '''))
sffreqlet.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sffreqlet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sffreqlet.version('1.7')
sffreqlet.synopsis('''sffreqlet < in.rsf > out.rsf freq=w.rsf inv=n verb=y decomp=n ncycle=0 niter=1 perc=50.0 type=''','''''')
rsf.doc.progs['sffreqlet']=sffreqlet

