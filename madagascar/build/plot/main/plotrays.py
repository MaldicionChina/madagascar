sfplotrays = rsf.doc.rsfprog('sfplotrays','plot/main/plotrays.c','''Plot rays.''')
sfplotrays.par('frame',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfplotrays.par('nt',rsf.doc.rsfpar('int','n1*n2','','''maximum ray length '''))
sfplotrays.par('jr',rsf.doc.rsfpar('int','1','','''skip rays '''))
sfplotrays.par('frame',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfplotrays.version('1.7')
sfplotrays.synopsis('''sfplotrays frame=frame.rsf nt=n1*n2 jr=1 < rays.rsf > plot.vpl''','''Run "sfdoc stdplot" for more parameters.
''')
rsf.doc.progs['sfplotrays']=sfplotrays

