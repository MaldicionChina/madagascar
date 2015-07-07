sfdiff = rsf.doc.rsfprog('sfdiff','user/chenyk/Mdiff.c','''Compare the difference of two rsf data sets with the same size. ''')
sfdiff.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiff.version('1.7')
sfdiff.synopsis('''sfdiff < inp1.rsf match=inp2.rsf > dif.rsf''','''''')
rsf.doc.progs['sfdiff']=sfdiff

