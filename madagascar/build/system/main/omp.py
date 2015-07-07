sfomp = rsf.doc.rsfprog('sfomp','system/main/omp.c','''OpenMP wrapper for embarassingly parallel jobs. ''')
sfomp.par('split',rsf.doc.rsfpar('int','ndim','','''axis to split '''))
sfomp.par('join',rsf.doc.rsfpar('int','axis','','''axis to join (0 means add) '''))
sfomp.version('1.7')
sfomp.synopsis('''sfomp < inp.rsf > out.rsf split=ndim join=axis''','''''')
rsf.doc.progs['sfomp']=sfomp

