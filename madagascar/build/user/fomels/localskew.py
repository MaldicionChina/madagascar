sflocalskew = rsf.doc.rsfprog('sflocalskew','user/fomels/Mlocalskew.c','''Rotate phase and compute local skewness. ''')
sflocalskew.par('na',rsf.doc.rsfpar('int','360','','''number of angles '''))
sflocalskew.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sflocalskew.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle '''))
sflocalskew.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sflocalskew.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sflocalskew.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflocalskew.par('inv',rsf.doc.rsfpar('bool','y','','''inverse similarity '''))
sflocalskew.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sflocalskew.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sflocalskew.par('const',rsf.doc.rsfpar('bool','n','','''if y, compute inverse varimax '''))
sflocalskew.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflocalskew.version('1.7')
sflocalskew.synopsis('''sflocalskew < inp.rsf > sim.rsf na=360 da=1.0 a0=-180. order=100 ref=1. verb=y inv=y niter=20 rect=3 const=n eps=0.0f''','''''')
rsf.doc.progs['sflocalskew']=sflocalskew

