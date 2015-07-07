sfmwni2d = rsf.doc.rsfprog('sfmwni2d','user/pyang/Mmwni2d.c','''2-D bandlimited minimum weighted-norm interpolation (MWNI) ''')
sfmwni2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmwni2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfmwni2d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfmwni2d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sfmwni2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmwni2d.version('1.7')
sfmwni2d.synopsis('''sfmwni2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6''',''' implemented with conjugate gradient least squares (CGLS) method
''')
rsf.doc.progs['sfmwni2d']=sfmwni2d

