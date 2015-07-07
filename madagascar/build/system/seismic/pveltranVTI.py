sfpveltranVTI = rsf.doc.rsfprog('sfpveltranVTI','system/seismic/MpveltranVTI.c','''Slope-based tau-p velocity transform for VTI media. ''')
sfpveltranVTI.par('velH',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpveltranVTI.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpveltranVTI.par('cmp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('curv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('tau0t',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('curvt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('map',rsf.doc.rsfpar('bool','n','','''output maps instead of coherency panels '''))
sfpveltranVTI.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfpveltranVTI.par('v0',rsf.doc.rsfpar('float','','','''velocity origin '''))
sfpveltranVTI.par('dv',rsf.doc.rsfpar('float','','','''velocity sampling '''))
sfpveltranVTI.par('nvh',rsf.doc.rsfpar('int','nv','','''number of HOR velocities  '''))
sfpveltranVTI.par('vh0',rsf.doc.rsfpar('float','v0','','''HOR velocity origin '''))
sfpveltranVTI.par('dvh',rsf.doc.rsfpar('float','dv','','''HOR velocity sampling '''))
sfpveltranVTI.par('ne',rsf.doc.rsfpar('int','101','','''number of etas '''))
sfpveltranVTI.par('e0',rsf.doc.rsfpar('float','-0.5','','''eta origin '''))
sfpveltranVTI.par('de',rsf.doc.rsfpar('float','0.01','','''eta sampling '''))
sfpveltranVTI.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfpveltranVTI.par('method',rsf.doc.rsfpar('string ',desc='''method to use (stripping,dix,fowler,effective) '''))
sfpveltranVTI.par('dip',rsf.doc.rsfpar('string ',desc='''slope field (required for method=e and method=d) (auxiliary input file name)'''))
sfpveltranVTI.par('curv',rsf.doc.rsfpar('string ',desc='''curvature field (required for method=e and method=d) (auxiliary input file name)'''))
sfpveltranVTI.par('dipt',rsf.doc.rsfpar('string ',desc='''time derivative of slope field(auxiliary input file name)'''))
sfpveltranVTI.par('tau0t',rsf.doc.rsfpar('string ',desc='''tau0 tau derivative field (required for method=f) (auxiliary input file name)'''))
sfpveltranVTI.par('curvt',rsf.doc.rsfpar('string ',desc='''time derivative of curvature field (required for method=d and method=s) (auxiliary input file name)'''))
sfpveltranVTI.version('1.7')
sfpveltranVTI.synopsis('''sfpveltranVTI < tau0.rsf > velN.rsf velH=velH.rsf eta=eta.rsf cmp=cmp.rsf dip=dip.rsf curv=curv.rsf dipt=dipt.rsf tau0t=tau0t.rsf curvt=curvt.rsf map=n nv= v0= dv= nvh=nv vh0=v0 dvh=dv ne=101 e0=-0.5 de=0.01 nw=4 method=''','''''')
rsf.doc.progs['sfpveltranVTI']=sfpveltranVTI

