sfkirchinv = rsf.doc.rsfprog('sfkirchinv','system/seismic/Mkirchinv.c','''Kirchhoff 2-D post-stack least-squares time migration with antialiasing. ''')
sfkirchinv.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchinv.par('hd',rsf.doc.rsfpar('bool','y','','''if y, apply half-derivative filter '''))
sfkirchinv.par('ps',rsf.doc.rsfpar('bool','y','','''if y, apply pseudo-unitary weighting '''))
sfkirchinv.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfkirchinv.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfkirchinv.par('err',rsf.doc.rsfpar('string ',desc='''output file for error '''))
sfkirchinv.version('1.7')
sfkirchinv.synopsis('''sfkirchinv < in.rsf > out.rsf velocity=vel.rsf hd=y ps=y sw=0 niter=10 err=''','''
 Antialiasing by reparameterization. ''')
rsf.doc.progs['sfkirchinv']=sfkirchinv

