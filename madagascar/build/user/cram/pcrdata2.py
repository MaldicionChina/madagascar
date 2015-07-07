sfpcrdata2 = rsf.doc.rsfprog('sfpcrdata2','user/cram/Mpcrdata2.c','''Prepare data for 2-D angle-domain migration. ''')
sfpcrdata2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpcrdata2.par('absoff',rsf.doc.rsfpar('bool','n','','''y - absolute offset (default - relative to shot axis) '''))
sfpcrdata2.par('filter',rsf.doc.rsfpar('bool','y','','''y - antialiasing filter for data '''))
sfpcrdata2.par('KMAH',rsf.doc.rsfpar('bool','y','','''y - account for phase shifts due to KMAH index '''))
sfpcrdata2.par('diff',rsf.doc.rsfpar('bool','y','','''y - apply half-order differentiation '''))
sfpcrdata2.version('1.7')
sfpcrdata2.synopsis('''sfpcrdata2 < data.rsf > out.rsf verb=n absoff=n filter=y KMAH=y diff=y''','''''')
rsf.doc.progs['sfpcrdata2']=sfpcrdata2

