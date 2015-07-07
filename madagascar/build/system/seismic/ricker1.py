sfricker1 = rsf.doc.rsfprog('sfricker1','system/seismic/Mricker1.c','''Convolution with a Ricker wavelet. ''')
sfricker1.par('frequency',rsf.doc.rsfpar('float','','','''peak frequency for Ricker wavelet (in Hz) '''))
sfricker1.par('freq',rsf.doc.rsfpar('float','0.2','','''peak frequency for Ricker wavelet (as fraction of Nyquist) '''))
sfricker1.par('deriv',rsf.doc.rsfpar('bool','n','','''apply a half-order derivative filter '''))
sfricker1.version('1.7')
sfricker1.synopsis('''sfricker1 < in.rsf > out.rsf frequency= freq=0.2 deriv=n''','''
January 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/318-Program-of-the-month-sfricker1.html
''')
rsf.doc.progs['sfricker1']=sfricker1

