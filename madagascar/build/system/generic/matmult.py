sfmatmult = rsf.doc.rsfprog('sfmatmult','system/generic/Mmatmult.c','''Simple matrix multiplication ''')
sfmatmult.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmatmult.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfmatmult.version('1.7')
sfmatmult.synopsis('''sfmatmult < in.rsf > out.rsf mat=mat.rsf adj=n''','''''')
rsf.doc.progs['sfmatmult']=sfmatmult

