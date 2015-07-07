sfexplanesignoi = rsf.doc.rsfprog('sfexplanesignoi','user/pwd/Mexplanesignoi.c','''Signal and noise separation using both frequency components and dips. ''')
sfexplanesignoi.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfexplanesignoi.par('ndip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfexplanesignoi.par('sdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfexplanesignoi.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfexplanesignoi.par('eps',rsf.doc.rsfpar('float','1.','','''regularization parameter '''))
sfexplanesignoi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfexplanesignoi.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfexplanesignoi.par('nj1',rsf.doc.rsfpar('int','1','','''antialiasing for first dip '''))
sfexplanesignoi.par('nj2',rsf.doc.rsfpar('int','1','','''antialiasing for second dip '''))
sfexplanesignoi.version('1.7')
sfexplanesignoi.synopsis('''sfexplanesignoi < in.rsf freq=freq.rsf ndip=ndip.rsf sdip=sdip.rsf > out.rsf niter=50 eps=1. verb=n order=1 nj1=1 nj2=1''',''' ''')
rsf.doc.progs['sfexplanesignoi']=sfexplanesignoi

