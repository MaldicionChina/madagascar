sfmig2 = rsf.doc.rsfprog('sfmig2','user/yliu/Mmig2.c','''2-D Prestack Kirchhoff time migration with antialiasing. ''')
sfmig2.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig2.par('gather',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmig2.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig2.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfmig2.par('apt',rsf.doc.rsfpar('int','nx','','''integral aperture '''))
sfmig2.par('angle',rsf.doc.rsfpar('float','90.0','','''angle aperture '''))
sfmig2.par('half',rsf.doc.rsfpar('bool','y','','''if y, the third axis is half-offset instead of full offset '''))
sfmig2.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfmig2.par('rho',rsf.doc.rsfpar('float','1.-1./nt','','''Leaky integration constant '''))
sfmig2.par('gather',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfmig2.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmig2.version('1.7 Mmig2.c 13985 2015-03-26 13:56:59Z sfomel')
sfmig2.synopsis('''sfmig2 < inp.rsf vel=vel.rsf > mig.rsf gather=gather.rsf offset=offset.rsf antialias=1.0 apt=nx angle=90.0 half=y verb=y rho=1.-1./nt''','''The axes in the input are {time,midpoint,offset}
The axes in the offset are {1,midpoint,offset}
The axes in the output are {time,midpoint}
The axes in the "image gather" are {time,midpoint,offset}
''')
rsf.doc.progs['sfmig2']=sfmig2

