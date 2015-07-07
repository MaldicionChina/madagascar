sflinefit = rsf.doc.rsfprog('sflinefit','system/generic/Mlinefit.c','''Fit a line to a set of points in 2-D.''')
sflinefit.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflinefit.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflinefit.version('1.7')
sflinefit.synopsis('''sflinefit < in.rsf > out.rsf pattern=pattern.rsf''','''''')
rsf.doc.progs['sflinefit']=sflinefit

