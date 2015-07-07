sfmutter = rsf.doc.rsfprog('sfmutter','system/generic/Mmutter.c','''Muting.''')
sfmutter.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmutter.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfmutter.par('nan',rsf.doc.rsfpar('bool','n','','''if y, put  nans instead of zeros '''))
sfmutter.par('tp',rsf.doc.rsfpar('float','0.150','','''end time '''))
sfmutter.par('t0',rsf.doc.rsfpar('float','0.','','''starting time '''))
sfmutter.par('v0',rsf.doc.rsfpar('float','1.45','','''velocity '''))
sfmutter.par('slope0',rsf.doc.rsfpar('float','1./v0','','''slope '''))
sfmutter.par('slopep',rsf.doc.rsfpar('float','slope0','','''end slope '''))
sfmutter.par('x0',rsf.doc.rsfpar('float','0.','','''starting space '''))
sfmutter.par('abs',rsf.doc.rsfpar('bool','y','','''if y, use absolute value |x-x0| '''))
sfmutter.par('inner',rsf.doc.rsfpar('bool','n','','''if y, do inner muter '''))
sfmutter.par('hyper',rsf.doc.rsfpar('bool','n','','''if y, do hyperbolic mute '''))
sfmutter.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmutter.version('1.7 Mmutter.c 7107 2011-04-10 02:04:14Z ivlad')
sfmutter.synopsis('''sfmutter < in.rsf > out.rsf offset=offset.rsf half=y nan=n tp=0.150 t0=0. v0=1.45 slope0=1./v0 slopep=slope0 x0=0. abs=y inner=n hyper=n''','''   
Data is smoothly weighted inside the mute zone.
The weight is zero for t <       (x-x0) * slope0
The weight is one  for t >  tp + (x-x0) * slopep

The signs are reversed for inner=y.
''')
rsf.doc.progs['sfmutter']=sfmutter

