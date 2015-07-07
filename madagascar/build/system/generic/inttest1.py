sfinttest1 = rsf.doc.rsfprog('sfinttest1','system/generic/Minttest1.c','''Interpolation from a regular grid in 1-D. ''')
sfinttest1.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinttest1.par('nw',rsf.doc.rsfpar('int','','','''interpolator size '''))
sfinttest1.par('same',rsf.doc.rsfpar('bool','y','','''same or different coordinates for each trace '''))
sfinttest1.par('kai',rsf.doc.rsfpar('float','4.0','','''Kaiser window parameter '''))
sfinttest1.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline,mom) '''))
sfinttest1.version('1.7')
sfinttest1.synopsis('''sfinttest1 < in.rsf > out.rsf coord=crd.rsf nw= same=y kai=4.0 interp=''','''
January 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/373-Program-of-the-month-sfinttest1.html
''')
rsf.doc.progs['sfinttest1']=sfinttest1

