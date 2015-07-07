sfsplineplane = rsf.doc.rsfprog('sfsplineplane','user/gee/Msplineplane.c','''B-spline plane-wave filter ''')
sfsplineplane.par('lag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsplineplane.par('nw',rsf.doc.rsfpar('int','2','','''filter size '''))
sfsplineplane.par('p',rsf.doc.rsfpar('float','0.','','''plane-wave slope '''))
sfsplineplane.par('niter',rsf.doc.rsfpar('int','20','','''number of spectral decomposition iterations '''))
sfsplineplane.par('eps',rsf.doc.rsfpar('float','SF_EPS','',''''''))
sfsplineplane.par('lag',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfsplineplane.version('1.7')
sfsplineplane.synopsis('''sfsplineplane > out.rsf lag=lag.rsf nw=2 p=0. niter=20 eps=SF_EPS''','''''')
rsf.doc.progs['sfsplineplane']=sfsplineplane

