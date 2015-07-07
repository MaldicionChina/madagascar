sffftexp3 = rsf.doc.rsfprog('sffftexp3','user/fomels/Mfftexp3.c','''3-D FFT-based zero-offset exploding reflector modeling/migration  ''')
sffftexp3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp3.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp3.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sffftexp3.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sffftexp3.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sffftexp3.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sffftexp3.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sffftexp3.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sffftexp3.version('1.7')
sffftexp3.synopsis('''sffftexp3 < data.rsf > image.rsf left=left.rsf right=right.rsf mig=n ompchunk=1 nz= dz= nt= dt=''','''''')
rsf.doc.progs['sffftexp3']=sffftexp3

