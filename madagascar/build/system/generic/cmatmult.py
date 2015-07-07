sfcmatmult = rsf.doc.rsfprog('sfcmatmult','system/generic/Mcmatmult.c','''Simple matrix multiplication for complex matrices ''')
sfcmatmult.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcmatmult.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfcmatmult.version('1.7')
sfcmatmult.synopsis('''sfcmatmult < in.rsf > out.rsf mat=mat.rsf adj=n''','''''')
rsf.doc.progs['sfcmatmult']=sfcmatmult

