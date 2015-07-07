sfagmig = rsf.doc.rsfprog('sfagmig','system/seismic/Magmig.c','''Angle-gather constant-velocity time migration. ''')
sfagmig.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfagmig.par('ng',rsf.doc.rsfpar('int','','','''number of reflection angles '''))
sfagmig.par('dg',rsf.doc.rsfpar('float','','','''reflection angle sampling '''))
sfagmig.par('g0',rsf.doc.rsfpar('float','','','''reflection angle origin '''))
sfagmig.par('na',rsf.doc.rsfpar('int','nx','','''number of dip angles '''))
sfagmig.par('a',rsf.doc.rsfpar('float','80.','','''maximum dip angle '''))
sfagmig.version('1.7')
sfagmig.synopsis('''sfagmig < in.rsf > out.rsf vel= ng= dg= g0= na=nx a=80.''','''''')
rsf.doc.progs['sfagmig']=sfagmig

