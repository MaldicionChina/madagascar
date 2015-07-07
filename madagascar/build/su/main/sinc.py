sfsinc = rsf.doc.rsfprog('sfsinc','su/main/sinc.c','''1-D sinc interpolation.''')
sfsinc.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsinc.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsinc.version('1.7')
sfsinc.synopsis('''sfsinc < in.rsf > out.rsf pattern=pattern.rsf''','''
Specify either n1= o1= d1= or pattern=
''')
rsf.doc.progs['sfsinc']=sfsinc

