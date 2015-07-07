sfconvolve2 = rsf.doc.rsfprog('sfconvolve2','user/jyan/Mconvolve2.c','''2D convolution with arbitrary filter ''')
sfconvolve2.par('flt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvolve2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfconvolve2.par('stat',rsf.doc.rsfpar('bool','y','','''stationary operator '''))
sfconvolve2.version('1.7')
sfconvolve2.synopsis('''sfconvolve2 < Fx.rsf > Fy.rsf flt=Ff.rsf verb=n stat=y''','''''')
rsf.doc.progs['sfconvolve2']=sfconvolve2

