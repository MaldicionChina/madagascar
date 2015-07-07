sfkarlpocs = rsf.doc.rsfprog('sfkarlpocs','user/karl/Mkarlpocs.c','''n-D POCS interpolation using a general Lp-norm optimization''')
sfkarlpocs.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkarlpocs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfkarlpocs.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfkarlpocs.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 99)'''))
sfkarlpocs.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfkarlpocs.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkarlpocs.version('1.7')
sfkarlpocs.synopsis('''sfkarlpocs < in.rsf > out.rsf mask=Fmask.rsf verb=n niter=100 pclip=10. n#=''','''   Note: Acquistion geometry represented by mask operator.
''')
rsf.doc.progs['sfkarlpocs']=sfkarlpocs

