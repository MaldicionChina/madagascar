sfsignal = rsf.doc.rsfprog('sfsignal','user/chen/Msignal.c','''Generate signal series ''')
sfsignal.par('para',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfsignal.par('n',rsf.doc.rsfpar('int','100','','''length '''))
sfsignal.par('o',rsf.doc.rsfpar('float','0.0','','''original '''))
sfsignal.par('d',rsf.doc.rsfpar('float','0.004','','''interval '''))
sfsignal.par('waveform',rsf.doc.rsfpar('string ',desc='''waveform: ricker,sinc,harmonic,randn,rand '''))
sfsignal.version('1.7')
sfsignal.synopsis('''sfsignal > out.rsf para= n=100 o=0.0 d=0.004 waveform=''','''''')
rsf.doc.progs['sfsignal']=sfsignal

