sfconjgrad = rsf.doc.rsfprog('sfconjgrad','system/main/conjgrad.c','''Generic conjugate-gradient solver for linear inversion ''')
sfconjgrad.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconjgrad.par('mwt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconjgrad.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconjgrad.par('niter',rsf.doc.rsfpar('int','1','','''number of iterations '''))
sfconjgrad.par('mwt',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfconjgrad.par('x0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfconjgrad.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfconjgrad')
sfconjgrad.version('1.7')
sfconjgrad.synopsis('''sfconjgrad < dat.rsf mod=mod.rsf mwt=mwt.rsf x0=x0.rsf > to.rsf < from.rsf > out.rsf niter=1''','''''')
rsf.doc.progs['sfconjgrad']=sfconjgrad

