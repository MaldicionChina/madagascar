sfspline = rsf.doc.rsfprog('sfspline','system/generic/Mspline.c','''1-D cubic spline interpolation.''')
sfspline.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfspline.par('fp',rsf.doc.rsfpar('floats','','','''end-point derivatives  [2]'''))
sfspline.par('sort',rsf.doc.rsfpar('bool','n','','''if y, the coordinates need sorting '''))
sfspline.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfspline.version('1.7')
sfspline.synopsis('''sfspline < in.rsf > out.rsf pattern=pattern.rsf fp= sort=n''','''
Specify either n1= o1= d1= or pattern=
''')
rsf.doc.progs['sfspline']=sfspline

