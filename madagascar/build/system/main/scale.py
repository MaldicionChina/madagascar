sfscale = rsf.doc.rsfprog('sfscale','system/main/scale.c','''Scale data.''')
sfscale.par('axis',rsf.doc.rsfpar('int','0','','''Scale by maximum in the dimensions up to this axis. '''))
sfscale.par('rscale',rsf.doc.rsfpar('float','0.','','''Scale by this factor. '''))
sfscale.par('pclip',rsf.doc.rsfpar('float','100.','','''data clip percentile '''))
sfscale.par('dscale',rsf.doc.rsfpar('float','1.','','''Scale by this factor (works if rscale=0) '''))
sfscale.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfscale')
sfscale.version('1.7')
sfscale.synopsis('''sfscale < in.rsf > out.rsf axis=0 rscale=0. pclip=100. dscale=1.''','''
To scale by a constant factor, you can also use sfmath.
''')
rsf.doc.progs['sfscale']=sfscale

