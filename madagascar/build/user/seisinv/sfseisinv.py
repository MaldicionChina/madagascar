import rsf.doc

sfkirchinvs = rsf.doc.rsfprog('sfkirchinvs','user/seisinv/Mkirchinvs.c','''Kirchhoff 2-D post-stack least-squares time migration with sparse constrains. ''')
sfkirchinvs.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchinvs.par('hd',rsf.doc.rsfpar('bool','y','','''if y, apply half-derivative filter '''))
sfkirchinvs.par('ps',rsf.doc.rsfpar('bool','y','','''if y, apply pseudo-unitary weighting '''))
sfkirchinvs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkirchinvs.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfkirchinvs.par('niter',rsf.doc.rsfpar('int','5','','''number of non-linear iterations, when niter=1, it's linear '''))
sfkirchinvs.par('liter',rsf.doc.rsfpar('int','5','','''number of linear iterations '''))
sfkirchinvs.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameters '''))
sfkirchinvs.par('err',rsf.doc.rsfpar('string ',desc='''output file for error '''))
sfkirchinvs.version('1.7')
sfkirchinvs.synopsis('''sfkirchinvs < in.rsf > out.rsf velocity=vel.rsf hd=y ps=y verb=n sw=0 niter=5 liter=5 eps=0. err=''','''
 Antialiasing by reparameterization. ''')
rsf.doc.progs['sfkirchinvs']=sfkirchinvs

