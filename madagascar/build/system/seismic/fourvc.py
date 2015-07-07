sffourvc = rsf.doc.rsfprog('sffourvc','system/seismic/Mfourvc.c','''Prestack velocity continuation. ''')
sffourvc.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sffourvc.par('pad',rsf.doc.rsfpar('int','n1','','''padding for stretch '''))
sffourvc.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sffourvc.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffourvc.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sffourvc.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sffourvc.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sffourvc.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sffourvc.version('1.7')
sffourvc.synopsis('''sffourvc < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=n nv= dv= extend=4 v0=''','''''')
rsf.doc.progs['sffourvc']=sffourvc

