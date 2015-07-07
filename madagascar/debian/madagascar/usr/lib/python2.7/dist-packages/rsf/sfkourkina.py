import rsf.doc

sfcameron2d = rsf.doc.rsfprog('sfcameron2d','user/kourkina/Mcameron2d.c','''Convert Dix velocity to interval velocity. ''')
sfcameron2d.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcameron2d.par('t0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcameron2d.par('nz',rsf.doc.rsfpar('int','','',''''''))
sfcameron2d.par('dz',rsf.doc.rsfpar('float','','',''''''))
sfcameron2d.par('nc',rsf.doc.rsfpar('int','100','','''number of chebyshev coefficients '''))
sfcameron2d.par('neval',rsf.doc.rsfpar('int','20','','''numvber of used chebyshev coefficients '''))
sfcameron2d.par('method',rsf.doc.rsfpar('string ',desc='''method (chebyshev,lax-friedrichs) '''))
sfcameron2d.version('1.7')
sfcameron2d.synopsis('''sfcameron2d < fv.rsf > fv2.rsf x0=fx.rsf t0=ft.rsf nz= dz= nc=100 neval=20 method=''','''
Input in (x0,t0), output in (x,z).
''')
rsf.doc.progs['sfcameron2d']=sfcameron2d

sfve2d = rsf.doc.rsfprog('sfve2d','user/kourkina/Mve2d.c','''Convert interval velocity to Dix velocity ''')
sfve2d.par('x',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfve2d.par('z',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfve2d.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfve2d.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfve2d.par('order',rsf.doc.rsfpar('int','4','','''interpolation order '''))
sfve2d.version('1.7')
sfve2d.synopsis('''sfve2d < fsc.rsf > fid.rsf x=fx.rsf z=fy.rsf nt= dt= order=4''','''''')
rsf.doc.progs['sfve2d']=sfve2d

sfspiral = rsf.doc.rsfprog('sfspiral','user/kourkina/Mspiral.c','''Spiral function ''')
sfspiral.par('nx',rsf.doc.rsfpar('int','500','',''''''))
sfspiral.par('ny',rsf.doc.rsfpar('int','200','',''''''))
sfspiral.par('xmax',rsf.doc.rsfpar('float','20.','',''''''))
sfspiral.par('ymax',rsf.doc.rsfpar('float','3.','',''''''))
sfspiral.par('xmin',rsf.doc.rsfpar('float','0.','',''''''))
sfspiral.par('ymin',rsf.doc.rsfpar('float','0.','',''''''))
sfspiral.par('dx',rsf.doc.rsfpar('float','(xmax-xmin)/(nx-1)','',''''''))
sfspiral.par('dy',rsf.doc.rsfpar('float','(ymax-ymin)/(ny-1)','',''''''))
sfspiral.par('xc',rsf.doc.rsfpar('float','10.','',''''''))
sfspiral.par('yc',rsf.doc.rsfpar('float','5.','',''''''))
sfspiral.par('eps',rsf.doc.rsfpar('float','1.0e-6','',''''''))
sfspiral.par('v0',rsf.doc.rsfpar('float','2.0','',''''''))
sfspiral.par('v1',rsf.doc.rsfpar('float','2.0','',''''''))
sfspiral.par('r0',rsf.doc.rsfpar('float','1.0','',''''''))
sfspiral.par('r1',rsf.doc.rsfpar('float','0.4','','''paramters of original shape '''))
sfspiral.par('b',rsf.doc.rsfpar('float','0.1','','''exponential decay factor '''))
sfspiral.par('fac',rsf.doc.rsfpar('float','0.2','',''''''))
sfspiral.par('sp_r',rsf.doc.rsfpar('float','1.','','''speed in radius '''))
sfspiral.par('sp_t',rsf.doc.rsfpar('float','0.05','','''speed in angle '''))
sfspiral.version('1.7')
sfspiral.synopsis('''sfspiral > spiral.rsf nx=500 ny=200 xmax=20. ymax=3. xmin=0. ymin=0. dx=(xmax-xmin)/(nx-1) dy=(ymax-ymin)/(ny-1) xc=10. yc=5. eps=1.0e-6 v0=2.0 v1=2.0 r0=1.0 r1=0.4 b=0.1 fac=0.2 sp_r=1. sp_t=0.05''','''''')
rsf.doc.progs['sfspiral']=sfspiral

