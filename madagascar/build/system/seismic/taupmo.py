sftaupmo = rsf.doc.rsfprog('sftaupmo','system/seismic/Mtaupmo.c','''Normal moveout in tau-p domain. ''')
sftaupmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupmo.par('slope',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupmo.par('velx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupmo.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sftaupmo.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch '''))
sftaupmo.par('extend',rsf.doc.rsfpar('int','4','','''interpolation accuracy '''))
sftaupmo.par('interval',rsf.doc.rsfpar('bool','y','','''use interval velocity '''))
sftaupmo.par('slope',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftaupmo.par('velx',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftaupmo.version('1.7')
sftaupmo.synopsis('''sftaupmo < taup.rsf velocity=velocity.rsf > nmod.rsf slope=slope.rsf velx=velocityx.rsf mute=12 str=0.5 extend=4 interval=y''','''''')
rsf.doc.progs['sftaupmo']=sftaupmo

