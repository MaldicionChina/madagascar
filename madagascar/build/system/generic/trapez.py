sftrapez = rsf.doc.rsfprog('sftrapez','system/generic/Mtrapez.c','''Convolution with a trapezoidal filter. ''')
sftrapez.par('frequency',rsf.doc.rsfpar('floats','','','''frequencies (in Hz), default: (0.1,0.15,0.45,0.5)*Nyquist  [4]'''))
sftrapez.version('1.7')
sftrapez.synopsis('''sftrapez < in.rsf > out.rsf frequency=''','''''')
rsf.doc.progs['sftrapez']=sftrapez

