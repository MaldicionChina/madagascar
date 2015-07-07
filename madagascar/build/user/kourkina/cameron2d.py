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

