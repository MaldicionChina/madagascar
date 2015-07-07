sfungrad = rsf.doc.rsfprog('sfungrad','user/gee/Mungrad.c','''Phase unwrapping by least squares. ''')
sfungrad.par('badness',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfungrad.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfungrad.par('badness',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfungrad.version('1.7')
sfungrad.synopsis('''sfungrad < inp.rsf > out.rsf badness=bad.rsf niter=0''','''''')
rsf.doc.progs['sfungrad']=sfungrad

