sfricker = rsf.doc.rsfprog('sfricker','system/seismic/Mricker.c','''Ricker wavelet estimation. ''')
sfricker.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfricker.par('m',rsf.doc.rsfpar('float','f0+0.25*(na-1)*df','','''initial frequency '''))
sfricker.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfricker.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfricker.version('1.7 Mricker.c 7956 2011-12-08 16:56:49Z sfomel')
sfricker.synopsis('''sfricker < in.rsf > out.rsf ma=ma.rsf m=f0+0.25*(na-1)*df niter=100 verb=n''','''''')
rsf.doc.progs['sfricker']=sfricker

