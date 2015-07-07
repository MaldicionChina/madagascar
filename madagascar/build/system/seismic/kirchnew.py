sfkirchnew = rsf.doc.rsfprog('sfkirchnew','system/seismic/Mkirchnew.c','''Kirchhoff 2-D post-stack time migration and modeling with antialiasing. ''')
sfkirchnew.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchnew.par('adj',rsf.doc.rsfpar('bool','y','','''yes: migration, no: modeling '''))
sfkirchnew.par('hd',rsf.doc.rsfpar('bool','y','','''if y, apply half-derivative filter '''))
sfkirchnew.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfkirchnew.par('v0',rsf.doc.rsfpar('float','','','''constant velocity (if no velocity=) '''))
sfkirchnew.par('velocity',rsf.doc.rsfpar('string ',desc='''velocity file (auxiliary input file name)'''))
sfkirchnew.version('1.7')
sfkirchnew.synopsis('''sfkirchnew < in.rsf > out.rsf velocity=vel.rsf adj=y hd=y sw=0 v0=''','''
 Antialiasing by reparameterization. ''')
rsf.doc.progs['sfkirchnew']=sfkirchnew

