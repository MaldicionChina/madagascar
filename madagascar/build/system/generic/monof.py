sfmonof = rsf.doc.rsfprog('sfmonof','system/generic/Mmonof.c','''Mono-frequency wavelet estimation.''')
sfmonof.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmonof.par('a0',rsf.doc.rsfpar('float','1.','','''starting sharpness '''))
sfmonof.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmonof.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmonof.version('1.7')
sfmonof.synopsis('''sfmonof < in.rsf > out.rsf ma=ma.rsf a0=1. niter=100 verb=n''','''''')
rsf.doc.progs['sfmonof']=sfmonof

