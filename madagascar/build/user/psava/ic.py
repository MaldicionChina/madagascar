sfic = rsf.doc.rsfprog('sfic','user/psava/Mic.c','''Imaging condition ''')
sfic.par('ur',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfic.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sfic.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfic.par('nbuf',rsf.doc.rsfpar('int','1','','''buffer size '''))
sfic.par('version',rsf.doc.rsfpar('int','0','','''I.C. version (see paper) '''))
sfic.par('eps',rsf.doc.rsfpar('float','1e-6','','''epsilon '''))
sfic.version('1.7')
sfic.synopsis('''sfic < Fs.rsf ur=Fr.rsf > Fi.rsf ompchunk=1 verb=n nbuf=1 version=0 eps=1e-6''','''''')
rsf.doc.progs['sfic']=sfic

