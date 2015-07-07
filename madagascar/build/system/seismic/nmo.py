sfnmo = rsf.doc.rsfprog('sfnmo','system/seismic/Mnmo.c','''Normal moveout.''')
sfnmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('s',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfnmo.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfnmo.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfnmo.par('CDPtype',rsf.doc.rsfpar('int','','',''''''))
sfnmo.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfnmo.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfnmo.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfnmo.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfnmo.par('s',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo.par('a',rsf.doc.rsfpar('string ',desc=''''''))
sfnmo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo.version('1.7 Mnmo.c 14036 2015-04-03 15:29:04Z sfomel')
sfnmo.synopsis('''sfnmo < cmp.rsf velocity=velocity.rsf > nmod.rsf s=het.rsf offset=offset.rsf mask=msk.rsf half=y str=0.5 mute=12 CDPtype= slowness=n squared=n h0=0. extend=4 a=''','''
Compatible with sfvscan.

April 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/334-Program-of-the-month-sfnmo.html
''')
rsf.doc.progs['sfnmo']=sfnmo

