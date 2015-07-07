sfsum = rsf.doc.rsfprog('sfsum','user/jingwei/Msum.cc','''adjoint test ''')
sfsum.par('input2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.par('input3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.par('input4',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.version('1.7')
sfsum.synopsis('''sfsum < input1.rsf input2=input2.rsf input3=input3.rsf input4=input4.rsf > output.rsf''','''''')
rsf.doc.progs['sfsum']=sfsum

