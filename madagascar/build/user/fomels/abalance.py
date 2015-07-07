sfabalance = rsf.doc.rsfprog('sfabalance','user/fomels/Mabalance.c','''Amplitude balancing. ''')
sfabalance.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfabalance.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfabalance.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfabalance.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfabalance.version('1.7 Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfabalance.synopsis('''sfabalance < in.rsf other=ref.rsf > out.rsf niter=100 order=100 ref=1.''','''''')
rsf.doc.progs['sfabalance']=sfabalance

