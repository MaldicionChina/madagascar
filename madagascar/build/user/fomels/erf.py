sferf = rsf.doc.rsfprog('sferf','user/fomels/Merf.c','''Bandpass filtering using erf function. ''')
sferf.par('flo',rsf.doc.rsfpar('float','-1.','','''low frequency in band '''))
sferf.par('fhi',rsf.doc.rsfpar('float','-1.','','''high frequency in band '''))
sferf.par('rect',rsf.doc.rsfpar('float','1','','''filter sharpness '''))
sferf.par('spline',rsf.doc.rsfpar('bool','n','','''if use B-spline erf '''))
sferf.par('der',rsf.doc.rsfpar('bool','n','','''compute derivative '''))
sferf.version('1.7')
sferf.synopsis('''sferf < in.rsf > out.rsf flo=-1. fhi=-1. rect=1 spline=n der=n''','''''')
rsf.doc.progs['sferf']=sferf

