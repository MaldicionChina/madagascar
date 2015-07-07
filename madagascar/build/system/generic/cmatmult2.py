sfcmatmult2 = rsf.doc.rsfprog('sfcmatmult2','system/generic/Mcmatmult2.c','''Multiplication of two complex matrices ''')
sfcmatmult2.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcmatmult2.version('1.7')
sfcmatmult2.synopsis('''sfcmatmult2 < in.rsf > out.rsf mat=mat.rsf''','''''')
rsf.doc.progs['sfcmatmult2']=sfcmatmult2

