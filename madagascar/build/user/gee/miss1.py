sfmiss1 = rsf.doc.rsfprog('sfmiss1','user/gee/Mmiss1.c','''Missing data interpolation in 1-D. ''')
sfmiss1.par('filtin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss1.par('niter',rsf.doc.rsfpar('int','n1','','''number of iterations '''))
sfmiss1.par('diter',rsf.doc.rsfpar('int','niter','','''iteration step '''))
sfmiss1.par('filtin',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmiss1.par('step',rsf.doc.rsfpar('string ',desc='''linear solver type '''))
sfmiss1.version('1.7 Mmiss1.c 12370 2014-05-04 11:49:34Z sfomel')
sfmiss1.synopsis('''sfmiss1 < in.rsf > out.rsf filtin=filt.rsf niter=n1 diter=niter step=''','''''')
rsf.doc.progs['sfmiss1']=sfmiss1

