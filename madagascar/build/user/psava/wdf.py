sfwdf = rsf.doc.rsfprog('sfwdf','user/psava/Mwdf.c','''Assymptotic Wigner distribution ''')
sfwdf.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sfwdf.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwdf.par('nh1',rsf.doc.rsfpar('int','0','',''''''))
sfwdf.par('nh2',rsf.doc.rsfpar('int','0','',''''''))
sfwdf.par('nh3',rsf.doc.rsfpar('int','0','',''''''))
sfwdf.version('1.7')
sfwdf.synopsis('''sfwdf < Fu.rsf > Fw.rsf ompchunk=1 verb=n nh1=0 nh2=0 nh3=0''','''''')
rsf.doc.progs['sfwdf']=sfwdf

