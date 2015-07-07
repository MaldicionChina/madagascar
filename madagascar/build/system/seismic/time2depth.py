sftime2depth = rsf.doc.rsfprog('sftime2depth','system/seismic/Mtime2depth.c','''Time-to-depth conversion in V(z). ''')
sftime2depth.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftime2depth.par('intime',rsf.doc.rsfpar('bool','n','','''y if velocity is in time rather than depth '''))
sftime2depth.par('nz',rsf.doc.rsfpar('int','','','''Number of depth samples (default: n1) '''))
sftime2depth.par('dz',rsf.doc.rsfpar('float','','','''Depth sampling (default: d1) '''))
sftime2depth.par('z0',rsf.doc.rsfpar('float','0.','','''Depth origin '''))
sftime2depth.par('extend',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sftime2depth.par('slow',rsf.doc.rsfpar('bool','n','','''If y, input slowness; if n, velocity '''))
sftime2depth.par('twoway',rsf.doc.rsfpar('bool','y','','''if y, two-way traveltime '''))
sftime2depth.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sftime2depth.version('1.7 Mtime2depth.c 10817 2013-08-03 16:36:21Z sfomel')
sftime2depth.synopsis('''sftime2depth < in.rsf velocity=velocity.rsf > out.rsf intime=n nz= dz= z0=0. extend=4 slow=n twoway=y eps=0.01''','''
July 2013 program of the month:
http://www.ahay.org/rsflog/index.php?/archives/345-Program-of-the-month-sftime2depth.html
''')
rsf.doc.progs['sftime2depth']=sftime2depth

