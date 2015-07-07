sfkarman = rsf.doc.rsfprog('sfkarman','user/browaeys/Mkarman.c','''Estimation of von Karman autocorrelation 1D spectrum. ''')
sfkarman.par('x0',rsf.doc.rsfpar('float','1.','','''initial squared length scale '''))
sfkarman.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfkarman.par('nliter',rsf.doc.rsfpar('int','1','','''number of reweighting iterations '''))
sfkarman.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkarman.version('1.7')
sfkarman.synopsis('''sfkarman < in.rsf > out.rsf x0=1. niter=100 nliter=1 verb=n''','''''')
rsf.doc.progs['sfkarman']=sfkarman

