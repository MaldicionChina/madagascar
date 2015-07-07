sfemd = rsf.doc.rsfprog('sfemd','user/chenyk/Memd.c','''Empirical Mode Decomposition ''')
sfemd.par('threshold',rsf.doc.rsfpar('float','DEFAULT_THRESHOLD','','''Sifting stoping parameter: threshold, the default is 0.05. '''))
sfemd.par('tolerance',rsf.doc.rsfpar('float','DEFAULT_TOLERANCE','','''Sifting stoping parameter: tolerance, the default is 0.05. '''))
sfemd.par('miter',rsf.doc.rsfpar('int','MAX_ITERATIONS','','''Maximum number of iterations during sifting, the default is 1000. '''))
sfemd.par('mimf',rsf.doc.rsfpar('int','0','','''Maximum number of IMFs, the default is as many as possible. '''))
sfemd.version('1.7')
sfemd.synopsis('''sfemd < inp.rsf > outp.rsf threshold=DEFAULT_THRESHOLD tolerance=DEFAULT_TOLERANCE miter=MAX_ITERATIONS mimf=0''','''''')
rsf.doc.progs['sfemd']=sfemd

