sfxcor2d = rsf.doc.rsfprog('sfxcor2d','user/psava/Mxcor2d.c','''OpenMP time- or freq-domain cross-correlation on axes 1,2,3 ''')
sfxcor2d.par('uu',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfxcor2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfxcor2d.par('axis',rsf.doc.rsfpar('int','2','','''stack axis '''))
sfxcor2d.par('nbuf',rsf.doc.rsfpar('int','1','','''buffer size '''))
sfxcor2d.version('1.7')
sfxcor2d.synopsis('''sfxcor2d < Fs.rsf uu=Fr.rsf > Fi.rsf verb=n axis=2 nbuf=1''','''''')
rsf.doc.progs['sfxcor2d']=sfxcor2d

