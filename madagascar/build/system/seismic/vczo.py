sfvczo = rsf.doc.rsfprog('sfvczo','system/seismic/Mvczo.c','''Post-stack 2-D velocity continuation. ''')
sfvczo.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfvczo.par('pad',rsf.doc.rsfpar('int','n1','','''padding for stretch '''))
sfvczo.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sfvczo.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfvczo.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfvczo.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfvczo.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfvczo.version('1.7')
sfvczo.synopsis('''sfvczo < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=y nv= dv= v0=''','''''')
rsf.doc.progs['sfvczo']=sfvczo

