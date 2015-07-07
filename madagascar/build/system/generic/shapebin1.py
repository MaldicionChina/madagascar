sfshapebin1 = rsf.doc.rsfprog('sfshapebin1','system/generic/Mshapebin1.c','''1-D inverse interpolation with shaping regularization. ''')
sfshapebin1.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfshapebin1.par('nx',rsf.doc.rsfpar('int','','','''number of bins '''))
sfshapebin1.par('xmin',rsf.doc.rsfpar('float','','','''grid size '''))
sfshapebin1.par('xmax',rsf.doc.rsfpar('float','','',''''''))
sfshapebin1.par('x0',rsf.doc.rsfpar('float','xmin','','''grid origin '''))
sfshapebin1.par('dx',rsf.doc.rsfpar('float','','','''grid sampling '''))
sfshapebin1.par('interp',rsf.doc.rsfpar('int','2','[1,2]','''forward interpolation method, 1: nearest neighbor, 2: linear '''))
sfshapebin1.par('filter',rsf.doc.rsfpar('float','3.','','''smoothing length '''))
sfshapebin1.par('niter',rsf.doc.rsfpar('int','nx','','''number of conjugate-gradient iterations '''))
sfshapebin1.par('eps',rsf.doc.rsfpar('float','1./nd','','''regularization parameter '''))
sfshapebin1.par('pef',rsf.doc.rsfpar('bool','n','','''if y, use monofrequency regularization '''))
sfshapebin1.par('gauss',rsf.doc.rsfpar('bool','n','','''if y, use Gaussian shaping '''))
sfshapebin1.par('pad',rsf.doc.rsfpar('int','0','','''padding for Gaussian shaping '''))
sfshapebin1.par('head',rsf.doc.rsfpar('string ',desc=''''''))
sfshapebin1.version('1.7 Mshapebin1.c 13985 2015-03-26 13:56:59Z sfomel')
sfshapebin1.synopsis('''sfshapebin1 < in.rsf > out.rsf verb=y nx= xmin= xmax= x0=xmin dx= interp=2 filter=3. niter=nx eps=1./nd pef=n gauss=n pad=0 head=''','''''')
rsf.doc.progs['sfshapebin1']=sfshapebin1

