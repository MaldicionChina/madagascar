sfpfactor2 = rsf.doc.rsfprog('sfpfactor2','user/gee/Mpfactor2.c','''Plane prediction filter on a helix. ''')
sfpfactor2.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfpfactor2.par('nx',rsf.doc.rsfpar('int','','',''''''))
sfpfactor2.par('p',rsf.doc.rsfpar('float','','',''''''))
sfpfactor2.par('q',rsf.doc.rsfpar('float','','',''''''))
sfpfactor2.par('niter',rsf.doc.rsfpar('int','20','','''number of factorization iterations '''))
sfpfactor2.par('na',rsf.doc.rsfpar('int','25','','''filter size '''))
sfpfactor2.par('eps',rsf.doc.rsfpar('float','FLT_EPSILON','','''compression tolerance '''))
sfpfactor2.par('fixed',rsf.doc.rsfpar('bool','y','','''if fixed size '''))
sfpfactor2.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfpfactor2.version('1.7')
sfpfactor2.synopsis('''sfpfactor2 > filt.rsf nt= nx= p= q= niter=20 na=25 eps=FLT_EPSILON fixed=y lag=''','''''')
rsf.doc.progs['sfpfactor2']=sfpfactor2

