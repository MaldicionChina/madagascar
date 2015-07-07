sfpocs = rsf.doc.rsfprog('sfpocs','user/pyang/Mpocs.c','''n-D POCS interpolation using a hard thresholding''')
sfpocs.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpocs.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfpocs.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 99)'''))
sfpocs.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfpocs.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocs.version('1.7')
sfpocs.synopsis('''sfpocs < in.rsf > out.rsf mask=Fmask.rsf verb=n niter=100 pclip=10. n#=''','''Note: Acquistion geometry specified by mask operator.
''')
rsf.doc.progs['sfpocs']=sfpocs

