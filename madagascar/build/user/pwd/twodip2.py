sftwodip2 = rsf.doc.rsfprog('sftwodip2','user/pwd/Mtwodip2.c','''2-D two dip estimation by plane wave destruction.''')
sftwodip2.par('dip1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftwodip2.par('dip2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftwodip2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftwodip2.par('niter',rsf.doc.rsfpar('int','5','','''number of iterations '''))
sftwodip2.par('eps',rsf.doc.rsfpar('float','1','','''vertical smoothness '''))
sftwodip2.par('lam',rsf.doc.rsfpar('float','1','','''horizontal smoothness '''))
sftwodip2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sftwodip2.par('nj1',rsf.doc.rsfpar('int','1','','''antialiasing for first dip '''))
sftwodip2.par('nj2',rsf.doc.rsfpar('int','1','','''antialiasing for second dip '''))
sftwodip2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftwodip2.par('sign',rsf.doc.rsfpar('bool','n','','''if y, keep dip sign constant '''))
sftwodip2.par('gauss',rsf.doc.rsfpar('bool','n','','''if y, use exact Gaussian for smoothing '''))
sftwodip2.par('both',rsf.doc.rsfpar('bool','y','','''if y, estimate both dips '''))
sftwodip2.par('p0',rsf.doc.rsfpar('float','1.','','''initial first dip '''))
sftwodip2.par('q0',rsf.doc.rsfpar('float','0.','','''initial second dip '''))
sftwodip2.par('dip1',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftwodip2.par('dip2',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftwodip2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftwodip2.version('1.7 Mtwodip2.c 10160 2013-04-10 20:11:15Z sfomel')
sftwodip2.synopsis('''sftwodip2 < in.rsf > out.rsf dip1=dip1.rsf dip2=dip2.rsf mask=mask.rsf niter=5 eps=1 lam=1 order=1 nj1=1 nj2=1 verb=n sign=n gauss=n both=y p0=1. q0=0. < data.rsf > dip.rsf''','''''')
rsf.doc.progs['sftwodip2']=sftwodip2

