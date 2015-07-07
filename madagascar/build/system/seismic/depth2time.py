sfdepth2time = rsf.doc.rsfprog('sfdepth2time','system/seismic/Mdepth2time.c','''Conversion from depth to time in a V(z) medium.''')
sfdepth2time.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdepth2time.par('nt',rsf.doc.rsfpar('int','','','''Number of points in time (default is n1) '''))
sfdepth2time.par('dt',rsf.doc.rsfpar('float','','','''Time sampling (default is d1) '''))
sfdepth2time.par('t0',rsf.doc.rsfpar('float','','','''Time origin (default is 0) '''))
sfdepth2time.par('slow',rsf.doc.rsfpar('bool','n','','''y: slowness, n: velocity '''))
sfdepth2time.par('eps',rsf.doc.rsfpar('float','0.01','','''smoothness parameter '''))
sfdepth2time.version('1.7 Mdepth2time.c 7107 2011-04-10 02:04:14Z ivlad')
sfdepth2time.synopsis('''sfdepth2time < in.rsf velocity=velocity.rsf > out.rsf nt= dt= t0= slow=n eps=0.01''','''
Transforms function of z to function of

tau = Integral[2/v[x,n],{n,0,z}]
''')
rsf.doc.progs['sfdepth2time']=sfdepth2time

