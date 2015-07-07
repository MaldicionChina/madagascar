sffxdecon = rsf.doc.rsfprog('sffxdecon','user/chenyk/Mfxdecon.c','''Random noise attenuation using f-x deconvolution ''')
sffxdecon.par('verb',rsf.doc.rsfpar('bool','n','','''flag to get advisory messages '''))
sffxdecon.par('taper',rsf.doc.rsfpar('float','.1','','''length of taper '''))
sffxdecon.par('fmin',rsf.doc.rsfpar('float','1.','','''minimum frequency to process in Hz '''))
sffxdecon.par('fmax',rsf.doc.rsfpar('float','1./(2*dt)','','''maximum frequency to process in Hz '''))
sffxdecon.par('twlen',rsf.doc.rsfpar('float','(float)(n1-1)*dt','','''time window length '''))
sffxdecon.par('n2w',rsf.doc.rsfpar('int','10','','''number of traces in window '''))
sffxdecon.par('lenf',rsf.doc.rsfpar('int','4','','''number of traces for filter '''))
sffxdecon.version('1.7')
sffxdecon.synopsis('''sffxdecon < in.rsf > out.rsf verb=n taper=.1 fmin=1. fmax=1./(2*dt) twlen=(float)(n1-1)*dt n2w=10 lenf=4''','''''')
rsf.doc.progs['sffxdecon']=sffxdecon

