sffkdmo = rsf.doc.rsfprog('sffkdmo','system/seismic/Mfkdmo.c','''Offset continuation by log-stretch F-K operator. ''')
sffkdmo.par('h',rsf.doc.rsfpar('float','','','''final offset '''))
sffkdmo.par('nh',rsf.doc.rsfpar('int','1','','''number of offset steps '''))
sffkdmo.par('h0',rsf.doc.rsfpar('float','0.','','''initial offset '''))
sffkdmo.version('1.7')
sffkdmo.synopsis('''sffkdmo < in.rsf > out.rsf h= nh=1 h0=0.''','''''')
rsf.doc.progs['sffkdmo']=sffkdmo

