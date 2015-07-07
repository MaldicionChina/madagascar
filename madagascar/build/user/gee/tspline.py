sftspline = rsf.doc.rsfprog('sftspline','user/gee/Mtspline.c','''Helix filters for spline in tension ''')
sftspline.par('tension',rsf.doc.rsfpar('float','0.','','''spline tension '''))
sftspline.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftspline.par('eps',rsf.doc.rsfpar('float','FLT_EPSILON','','''tolerance for filter compressing '''))
sftspline.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sftspline.version('1.7')
sftspline.synopsis('''sftspline > flt.rsf tension=0. niter=20 eps=FLT_EPSILON lag=''','''''')
rsf.doc.progs['sftspline']=sftspline

