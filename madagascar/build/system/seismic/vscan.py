sfvscan = rsf.doc.rsfprog('sfvscan','system/seismic/Mvscan.c','''Velocity analysis.''')
sfvscan.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvscan.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvscan.par('grad',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvscan.par('semblance',rsf.doc.rsfpar('bool','n','','''if y, compute semblance; if n, stack '''))
sfvscan.par('diffsemblance',rsf.doc.rsfpar('bool','n','','''if y, compute differential semblance '''))
sfvscan.par('avosemblance',rsf.doc.rsfpar('bool','n','','''if y, compute AVO-friendly semblance '''))
sfvscan.par('nb',rsf.doc.rsfpar('int','2','','''semblance averaging '''))
sfvscan.par('weight',rsf.doc.rsfpar('bool','y','','''if y, apply pseudo-unitary weighting '''))
sfvscan.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfvscan.par('smax',rsf.doc.rsfpar('float','2.0','','''maximum heterogeneity '''))
sfvscan.par('ns',rsf.doc.rsfpar('int','1','','''number of heterogeneity scans '''))
sfvscan.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfvscan.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfvscan.par('v1',rsf.doc.rsfpar('float','','','''( v1 reference velocity )'''))
sfvscan.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfvscan.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfvscan.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfvscan.par('v0',rsf.doc.rsfpar('float','','','''first scanned velocity '''))
sfvscan.par('dv',rsf.doc.rsfpar('float','','','''step in velocity '''))
sfvscan.par('nv',rsf.doc.rsfpar('int','','','''number of scanned velocities '''))
sfvscan.par('v1',rsf.doc.rsfpar('float','','','''reference velocity '''))
sfvscan.par('type',rsf.doc.rsfpar('string ',desc='''type of semblance (avo,diff,sembl,power,weighted) '''))
sfvscan.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfvscan.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file (auxiliary input file name)'''))
sfvscan.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfvscan.version('1.7')
sfvscan.synopsis('''sfvscan < cmp.rsf > scan.rsf offset=offset.rsf mask=msk.rsf grad=grd.rsf semblance=n diffsemblance=n avosemblance=n nb=2 weight=y half=y smax=2.0 ns=1 slowness=n squared=n v1= extend=4 mute=12 str=0.5 v0= dv= nv= v1= type=''','''
Inverse of sfvelmod.

May 2013 program of the month:
http://www.ahay.org/rsflog/index.php?/archives/338-Program-of-the-month-sfvscan.html
''')
rsf.doc.progs['sfvscan']=sfvscan

