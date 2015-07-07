sfvczo3 = rsf.doc.rsfprog('sfvczo3','system/seismic/Mvczo3.c','''Post-stack 3-D velocity continuation. ''')
sfvczo3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfvczo3.par('pad',rsf.doc.rsfpar('int','n1','','''padding for stretch '''))
sfvczo3.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sfvczo3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfvczo3.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfvczo3.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfvczo3.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfvczo3.version('1.7')
sfvczo3.synopsis('''sfvczo3 < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=y nv= dv= v0=''','''''')
rsf.doc.progs['sfvczo3']=sfvczo3

