sfwigner = rsf.doc.rsfprog('sfwigner','user/psava/Mwigner.c','''Assymptotic Wigner distribution in space-time ''')
sfwigner.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sfwigner.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwigner.par('nh1',rsf.doc.rsfpar('int','0','',''''''))
sfwigner.par('nh2',rsf.doc.rsfpar('int','0','',''''''))
sfwigner.par('nh3',rsf.doc.rsfpar('int','0','',''''''))
sfwigner.par('wk',rsf.doc.rsfpar('float','0.0','',''''''))
sfwigner.version('1.7')
sfwigner.synopsis('''sfwigner < Fu.rsf > Fw.rsf ompchunk=1 verb=n nh1=0 nh2=0 nh3=0 wk=0.0''','''''')
rsf.doc.progs['sfwigner']=sfwigner

