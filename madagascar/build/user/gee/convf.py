sfconvf = rsf.doc.rsfprog('sfconvf','user/gee/Mconvf.c','''1-D convolution, adjoint is the filter. ''')
sfconvf.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvf.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfconvf.par('nf',rsf.doc.rsfpar('int','','','''filter size '''))
sfconvf.par('lag',rsf.doc.rsfpar('int','1','','''lag for internal convolution '''))
sfconvf.version('1.7')
sfconvf.synopsis('''sfconvf < inp.rsf > out.rsf other=oth.rsf adj=n nf= lag=1''','''''')
rsf.doc.progs['sfconvf']=sfconvf

