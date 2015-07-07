sfzomiso = rsf.doc.rsfprog('sfzomiso','user/xuxin/Mzomiso.c','''zero-offset isotropic reverse-time migration''')
sfzomiso.par('velo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomiso.par('cr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomiso.par('wave',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfzomiso.par('vmap',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomiso.par('sigm',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomiso.par('inv',rsf.doc.rsfpar('bool','n','','''if y, modeling; if n, migration '''))
sfzomiso.par('tau',rsf.doc.rsfpar('bool','n','','''if y, tau domain; if n, cartesian '''))
sfzomiso.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfzomiso.par('opt',rsf.doc.rsfpar('bool','n','','''optimze fft size '''))
sfzomiso.par('nt',rsf.doc.rsfpar('int','1','','''time n (if inv=y) '''))
sfzomiso.par('dt',rsf.doc.rsfpar('float','1.','','''time d (if inv=y) '''))
sfzomiso.par('bzl',rsf.doc.rsfpar('int','0','',''''''))
sfzomiso.par('bzh',rsf.doc.rsfpar('int','0','',''''''))
sfzomiso.par('bxl',rsf.doc.rsfpar('int','0','',''''''))
sfzomiso.par('bxh',rsf.doc.rsfpar('int','0','',''''''))
sfzomiso.par('czl',rsf.doc.rsfpar('float','1.','',''''''))
sfzomiso.par('czh',rsf.doc.rsfpar('float','1.','',''''''))
sfzomiso.par('cxl',rsf.doc.rsfpar('float','1.','',''''''))
sfzomiso.par('cxh',rsf.doc.rsfpar('float','1.','',''''''))
sfzomiso.par('n3',rsf.doc.rsfpar('int','nt','','''wave time n '''))
sfzomiso.par('eps',rsf.doc.rsfpar('float','1','','''regularize sigma '''))
sfzomiso.version('1.7')
sfzomiso.synopsis('''sfzomiso velo=Fvelo.rsf cr=Fcr.rsf wave=Fwave.rsf < Fimag.rsf > Fdata.rsf vmap=Fvmap.rsf sigm=Fsigm.rsf inv=n tau=n verb=n opt=n nt=1 dt=1. bzl=0 bzh=0 bxl=0 bxh=0 czl=1. czh=1. cxl=1. cxh=1. n3=nt eps=1''',''' * exploding reflector modeling : < imag.rsf sfzomiso inv=y > data.rsf
 * zero-offset migration        : < data.rsf sfzomiso inv=n > imag.rsf
 * forward modeling             : < data.rsf sfzomiso inv=n > imag.rsf 
 Need (1) velo *= 2 (2) nr=1 (3) imag.rsf is useless ''')
rsf.doc.progs['sfzomiso']=sfzomiso

