sfexpsignoi = rsf.doc.rsfprog('sfexpsignoi','user/pwd/Mexpsignoi.c','''Signal and noise separation using frequency components. ''')
sfexpsignoi.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfexpsignoi.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfexpsignoi.par('eps',rsf.doc.rsfpar('float','1.','','''regularization parameter '''))
sfexpsignoi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfexpsignoi.version('1.7')
sfexpsignoi.synopsis('''sfexpsignoi < in.rsf freq=freq.rsf > out.rsf niter=50 eps=1. verb=n''',''' ''')
rsf.doc.progs['sfexpsignoi']=sfexpsignoi

