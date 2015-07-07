import rsf.doc

sfspecfac = rsf.doc.rsfprog('sfspecfac','user/ridder/Mspecfac.f90','''(Maximum dimension is 3)''')
sfspecfac.par('acfile',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfspecfac.version('1.7')
sfspecfac.synopsis('''sfspecfac < in.rsf > out.rsf acfile=acfile.rsf''','''''')
rsf.doc.progs['sfspecfac']=sfspecfac

