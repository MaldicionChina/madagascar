sfpad2nextfastsize = rsf.doc.rsfprog('sfpad2nextfastsize','user/ivlad/Mpad2nextfastsize.c','''How much to pad to get to next fast c2c FFT size (factors: 2,3 and 5)''')
sfpad2nextfastsize.par('n',rsf.doc.rsfpar('int','','',''''''))
sfpad2nextfastsize.version('1.7')
sfpad2nextfastsize.synopsis('''sfpad2nextfastsize n=''','''Wrapper for kiss_fft_next_fast_size. ''')
rsf.doc.progs['sfpad2nextfastsize']=sfpad2nextfastsize

