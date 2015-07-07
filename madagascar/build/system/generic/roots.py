sfroots = rsf.doc.rsfprog('sfroots','system/generic/Mroots.c','''Find roots of a complex polynomial. ''')
sfroots.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfroots.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''tolerance for convergence '''))
sfroots.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfroots.par('sort',rsf.doc.rsfpar('string ',desc='''attribute for sorting (phase,amplitude,real,imaginary) '''))
sfroots.version('1.7')
sfroots.synopsis('''sfroots < poly.rsf > root.rsf niter=10 tol=1.0e-6 verb=y sort=''','''''')
rsf.doc.progs['sfroots']=sfroots

