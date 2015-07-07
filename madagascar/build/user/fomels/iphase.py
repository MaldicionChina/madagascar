sfiphase = rsf.doc.rsfprog('sfiphase','user/fomels/Miphase.c','''Smooth estimate of instantaneous frequency. ''')
sfiphase.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfiphase.par('complex',rsf.doc.rsfpar('bool','n','','''if y, use complex-valued computations '''))
sfiphase.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfiphase.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfiphase.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfiphase.par('hertz',rsf.doc.rsfpar('bool','n','','''if y, convert output to Hertz '''))
sfiphase.par('band',rsf.doc.rsfpar('bool','n','','''if y, compute instantaneous bandwidth '''))
sfiphase.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfiphase.version('1.7 Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfiphase.synopsis('''sfiphase < in.rsf > out.rsf verb=n complex=n niter=100 order=100 ref=1. hertz=n band=n rect#=(1,1,...)''','''''')
rsf.doc.progs['sfiphase']=sfiphase

