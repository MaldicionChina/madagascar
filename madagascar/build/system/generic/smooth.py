sfsmooth = rsf.doc.rsfprog('sfsmooth','system/generic/Msmooth.c','''Multi-dimensional triangle smoothing. ''')
sfsmooth.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfsmooth.par('adj',rsf.doc.rsfpar('bool','n','','''run in the adjoint mode '''))
sfsmooth.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmooth.par('diff#',rsf.doc.rsfpar('bool','(n,n,...)','','''differentiation on #-th axis '''))
sfsmooth.version('1.7 Msmooth.c 9744 2013-01-19 17:12:34Z sfomel')
sfsmooth.synopsis('''sfsmooth < in.rsf > out.rsf repeat=1 adj=n rect#=(1,1,...) diff#=(n,n,...)''','''
January 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/280-Program-of-the-month-sfsmooth.html
''')
rsf.doc.progs['sfsmooth']=sfsmooth

