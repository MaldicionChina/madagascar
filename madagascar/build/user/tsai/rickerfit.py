sfrickerfit = rsf.doc.rsfprog('sfrickerfit','user/tsai/Mrickerfit.c','''Model wavelet spectrum by fitting spectral components of ricker wavelet.''')
sfrickerfit.par('ma1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrickerfit.par('ma2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrickerfit.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickerfit.par('n',rsf.doc.rsfpar('int','','',''''''))
sfrickerfit.par('niter',rsf.doc.rsfpar('int','100','',''''''))
sfrickerfit.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrickerfit.version('1.7')
sfrickerfit.synopsis('''sfrickerfit < in.rsf > out.rsf ma1=ma1.rsf ma2=ma2.rsf m= n= niter=100 verb=n''','''
   n is the number of components. ma1 is amplitude, ma2 is peak frequency.
''')
rsf.doc.progs['sfrickerfit']=sfrickerfit

