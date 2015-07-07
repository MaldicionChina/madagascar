sfinttest2 = rsf.doc.rsfprog('sfinttest2','system/generic/Minttest2.c','''Interpolation from a regular grid in 2-D. ''')
sfinttest2.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinttest2.par('nw',rsf.doc.rsfpar('int','','','''interpolator size '''))
sfinttest2.par('kai',rsf.doc.rsfpar('float','4.0','','''Kaiser window parameter '''))
sfinttest2.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline) '''))
sfinttest2.version('1.7')
sfinttest2.synopsis('''sfinttest2 < in.rsf > out.rsf coord=crd.rsf nw= kai=4.0 interp=''','''''')
rsf.doc.progs['sfinttest2']=sfinttest2

