sfcconjgrad = rsf.doc.rsfprog('sfcconjgrad','system/main/cconjgrad.c','''Generic conjugate-gradient solver for linear inversion with complex data ''')
sfcconjgrad.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcconjgrad.par('niter',rsf.doc.rsfpar('int','1','','''number of iterations '''))
sfcconjgrad.version('1.7')
sfcconjgrad.synopsis('''sfcconjgrad < dat.rsf mod=mod.rsf > to.rsf < from.rsf > out.rsf niter=1''','''''')
rsf.doc.progs['sfcconjgrad']=sfcconjgrad

