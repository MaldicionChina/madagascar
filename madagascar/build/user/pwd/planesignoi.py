sfplanesignoi = rsf.doc.rsfprog('sfplanesignoi','user/pwd/Mplanesignoi.c','''Signal and noise separation using plane-wave destruction filters.  ''')
sfplanesignoi.par('ndip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfplanesignoi.par('sdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfplanesignoi.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfplanesignoi.par('eps',rsf.doc.rsfpar('float','1.','','''regularization parameter '''))
sfplanesignoi.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfplanesignoi.par('nj1',rsf.doc.rsfpar('int','1','','''antialiasing for noise dip '''))
sfplanesignoi.par('nj2',rsf.doc.rsfpar('int','1','','''antialiasing for signal dip '''))
sfplanesignoi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfplanesignoi.version('1.7')
sfplanesignoi.synopsis('''sfplanesignoi < in.rsf ndip=ndip.rsf sdip=sdip.rsf > out.rsf niter=50 eps=1. order=1 nj1=1 nj2=1 verb=n''','''
If n3=1 in the output, outputs both signal and noise. Otherwise, only signal.
''')
rsf.doc.progs['sfplanesignoi']=sfplanesignoi

