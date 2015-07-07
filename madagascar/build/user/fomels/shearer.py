sfshearer = rsf.doc.rsfprog('sfshearer','user/fomels/Mshearer.c','''Preconditioning for traveltime picking. ''')
sfshearer.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshearer.par('order',rsf.doc.rsfpar('int','10','','''Hilbert transformer order '''))
sfshearer.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfshearer.par('short',rsf.doc.rsfpar('int','1','','''short smoothing radius '''))
sfshearer.par('long',rsf.doc.rsfpar('int','10','','''long smoothing radius '''))
sfshearer.version('1.7 Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfshearer.synopsis('''sfshearer < in.rsf > out.rsf niter=100 order=10 ref=1. short=1 long=10 rect1=1 rect2=1 ... ''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfshearer']=sfshearer

