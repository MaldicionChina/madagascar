sflinear = rsf.doc.rsfprog('sflinear','system/generic/Mlinear.c','''1-D linear interpolation.''')
sflinear.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflinear.par('sort',rsf.doc.rsfpar('bool','n','','''if y, the coordinates need sorting '''))
sflinear.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sflinear.par('rect',rsf.doc.rsfpar('int','1','','''smoothing regularization '''))
sflinear.par('nw',rsf.doc.rsfpar('int','2','','''interpolator size '''))
sflinear.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflinear.version('1.7')
sflinear.synopsis('''sflinear < in.rsf > out.rsf pattern=pattern.rsf sort=n niter=0 rect=1 nw=2''','''
The input should have n2=2 (coordinates,values)

For output, specify either n1= o1= d1= or pattern=
''')
rsf.doc.progs['sflinear']=sflinear

