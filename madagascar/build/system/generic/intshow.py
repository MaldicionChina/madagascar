sfintshow = rsf.doc.rsfprog('sfintshow','system/generic/Mintshow.c','''Output interpolation filter. ''')
sfintshow.par('nw',rsf.doc.rsfpar('int','','','''interpolator size '''))
sfintshow.par('x',rsf.doc.rsfpar('float','','','''interpolation shift '''))
sfintshow.par('kai',rsf.doc.rsfpar('float','4.0','','''Kaiser window parameter '''))
sfintshow.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline,mom) '''))
sfintshow.version('1.7')
sfintshow.synopsis('''sfintshow > filt.rsf nw= x= kai=4.0 interp=''','''
See also: inttest1.
''')
rsf.doc.progs['sfintshow']=sfintshow

