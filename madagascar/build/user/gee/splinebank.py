sfsplinebank = rsf.doc.rsfprog('sfsplinebank','user/gee/Msplinebank.c','''Prepare a filter bank for B-spline plane wave filters ''')
sfsplinebank.par('nt',rsf.doc.rsfpar('int','40','','''length of the fast axis '''))
sfsplinebank.par('np',rsf.doc.rsfpar('int','','','''number of dips '''))
sfsplinebank.par('pmax',rsf.doc.rsfpar('float','2.','','''maximum dip '''))
sfsplinebank.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfsplinebank.par('eps',rsf.doc.rsfpar('float','FLT_EPSILON','','''tolerance '''))
sfsplinebank.par('nh',rsf.doc.rsfpar('string ',desc=''''''))
sfsplinebank.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfsplinebank.version('1.7')
sfsplinebank.synopsis('''sfsplinebank > out.rsf nt=40 np= pmax=2. niter=20 eps=FLT_EPSILON nh= lag=''','''''')
rsf.doc.progs['sfsplinebank']=sfsplinebank

