sfmpi = rsf.doc.rsfprog('sfmpi','system/main/mpi.c','''MPI wrapper for embarassingly parallel jobs. ''')
sfmpi.par('input',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpi.par('output',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpi.par('split',rsf.doc.rsfpar('int','ndim','','''axis to split '''))
sfmpi.par('join',rsf.doc.rsfpar('int','axis','','''axis to join (0 means add) '''))
sfmpi.par('input',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmpi.version('1.7')
sfmpi.synopsis('''sfmpi input=inp.rsf output=out.rsf split=ndim join=axis''','''''')
rsf.doc.progs['sfmpi']=sfmpi

