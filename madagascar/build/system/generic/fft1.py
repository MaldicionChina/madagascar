sffft1 = rsf.doc.rsfprog('sffft1','system/generic/Mfft1.c','''Fast Fourier Transform along the first axis. ''')
sffft1.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sffft1.par('inv',rsf.doc.rsfpar('bool','n','','''y, perform inverse transform '''))
sffft1.par('sym',rsf.doc.rsfpar('bool','n','','''y, symmetric scaling for Hermitian FFT '''))
sffft1.par('opt',rsf.doc.rsfpar('bool','y','','''y, determine optimal size for efficiency '''))
sffft1.par('memsize',rsf.doc.rsfpar('float','1000.0','',''''''))
sffft1.version('1.7')
sffft1.synopsis('''sffft1 < Fin.rsf > Fou.rsf verb=n inv=n sym=n opt=y memsize=1000.0''','''''')
rsf.doc.progs['sffft1']=sffft1

