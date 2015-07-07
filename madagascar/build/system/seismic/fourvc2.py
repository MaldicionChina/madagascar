sffourvc2 = rsf.doc.rsfprog('sffourvc2','system/seismic/Mfourvc2.c','''Velocity continuation with semblance computation. ''')
sffourvc2.par('nb',rsf.doc.rsfpar('int','2','',''''''))
sffourvc2.par('eps',rsf.doc.rsfpar('float','0.01','',''''''))
sffourvc2.par('pad',rsf.doc.rsfpar('int','n1','',''''''))
sffourvc2.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','',''''''))
sffourvc2.par('nv',rsf.doc.rsfpar('int','','',''''''))
sffourvc2.par('dv',rsf.doc.rsfpar('float','','',''''''))
sffourvc2.par('semblance',rsf.doc.rsfpar('bool','y','','''if y, compute semblance; if n, stack '''))
sffourvc2.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sffourvc2.version('1.7')
sffourvc2.synopsis('''sffourvc2 < in.rsf > out.rsf nb=2 eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) nv= dv= semblance=y extend=4''','''''')
rsf.doc.progs['sffourvc2']=sffourvc2

