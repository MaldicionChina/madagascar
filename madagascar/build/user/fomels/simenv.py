sfsimenv = rsf.doc.rsfprog('sfsimenv','user/fomels/Msimenv.c','''Rotate phase and compute similarity with enevelope. ''')
sfsimenv.par('na',rsf.doc.rsfpar('int','360','','''number of angles '''))
sfsimenv.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sfsimenv.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle '''))
sfsimenv.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfsimenv.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfsimenv.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimenv.par('inv',rsf.doc.rsfpar('bool','y','','''inverse similarity '''))
sfsimenv.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimenv.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfsimenv.version('1.7')
sfsimenv.synopsis('''sfsimenv < inp.rsf > sim.rsf na=360 da=1.0 a0=-180. order=100 ref=1. verb=y inv=y niter=20 rect=3''','''''')
rsf.doc.progs['sfsimenv']=sfsimenv

