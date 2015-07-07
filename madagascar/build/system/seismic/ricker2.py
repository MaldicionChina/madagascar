sfricker2 = rsf.doc.rsfprog('sfricker2','system/seismic/Mricker2.c','''Nonstationary convolution with a Ricker wavelet. Phase and Frequency can be time-varying. ''')
sfricker2.par('tfreq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfricker2.par('tphase',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfricker2.par('frequency',rsf.doc.rsfpar('float','','','''peak frequency for Ricker wavelet (in Hz) '''))
sfricker2.par('freq',rsf.doc.rsfpar('float','0.2','','''peak frequency for Ricker wavelet (as fraction of Nyquist) '''))
sfricker2.par('esp',rsf.doc.rsfpar('float','0.','','''if norm=y, stable parameter'''))
sfricker2.par('norm',rsf.doc.rsfpar('bool','n','',''''''))
sfricker2.par('hiborder',rsf.doc.rsfpar('int','6','','''Hilbert transformer order '''))
sfricker2.par('hibref',rsf.doc.rsfpar('float','1.','',''''''))
sfricker2.par('tphase',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfricker2.version('1.7')
sfricker2.synopsis('''sfricker2 < in.rsf > out.rsf tfreq=tfre.rsf tphase=tpha.rsf frequency= freq=0.2 esp=0. norm=n hiborder=6 hibref=1.''','''''')
rsf.doc.progs['sfricker2']=sfricker2

