import rsf.doc

sfmpihello = rsf.doc.rsfprog('sfmpihello','user/bash/Mmpihello.c','''MPI example, summation of vectors c = a + b ''')
sfmpihello.par('input',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpihello.par('b',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpihello.version('1.7')
sfmpihello.synopsis('''sfmpihello input=ain.rsf b=bin.rsf > cout.rsf''','''''')
rsf.doc.progs['sfmpihello']=sfmpihello

