import rsf.doc

sfawefd2d = rsf.doc.rsfprog('sfawefd2d','user/cwp/Mawefd2d.c','''2D acoustic time-domain FD modeling ''')
sfawefd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd2d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfawefd2d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfawefd2d.par('expl',rsf.doc.rsfpar('bool','n','','''Multiple sources, one wvlt'''))
sfawefd2d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfawefd2d.par('cden',rsf.doc.rsfpar('bool','n','','''Constant density '''))
sfawefd2d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfawefd2d.par('fsrf',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfawefd2d.par('nbell',rsf.doc.rsfpar('int','5','','''gaussian for source injection '''))
sfawefd2d.par('optfd',rsf.doc.rsfpar('bool','n','','''optimized FD coefficients flag '''))
sfawefd2d.par('fdorder',rsf.doc.rsfpar('int','4','','''spatial FD order '''))
sfawefd2d.par('hybridbc',rsf.doc.rsfpar('bool','n','','''hybrid Absorbing BC '''))
sfawefd2d.par('sinc',rsf.doc.rsfpar('bool','n','','''sinc source injection '''))
sfawefd2d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfawefd2d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfawefd2d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfawefd2d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfawefd2d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfawefd2d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfawefd2d.par('dqz',rsf.doc.rsfpar('float','sf_d(az)','','''Saved wfld window dz '''))
sfawefd2d.par('dqx',rsf.doc.rsfpar('float','sf_d(ax)','','''Saved wfld window dx '''))
sfawefd2d.par('cden',rsf.doc.rsfpar('string ',desc='''Constant density'''))
sfawefd2d.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfawefd2d')
sfawefd2d.version('1.7')
sfawefd2d.synopsis('''sfawefd2d < file_wav.rsf vel=file_vel.rsf sou=file_src.rsf rec=file_rec.rsf > file_dat.rsf wfl=file_wfl.rsf den=file_den.rsf verb=n snap=n expl=n dabc=n cden=n adj=n fsrf=n nbell=5 optfd=n fdorder=4 hybridbc=n sinc=n jsnap=nt jdata=1 nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax) dqz=sf_d(az) dqx=sf_d(ax)''','''   2Nth order in space, 2nd order in time
   with optimized FD scheme option and hybrid one-way ABC option 
   adj flag indicates backwards source injection, not exact adjoint propagator
''')
rsf.doc.progs['sfawefd2d']=sfawefd2d

sfawefd3d = rsf.doc.rsfprog('sfawefd3d','user/cwp/Mawefd3d.c','''3D acoustic time-domain FD modeling ''')
sfawefd3d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd3d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfawefd3d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfawefd3d.par('expl',rsf.doc.rsfpar('bool','n','','''Multiple sources, one wvlt'''))
sfawefd3d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfawefd3d.par('cden',rsf.doc.rsfpar('bool','n','','''Constant density '''))
sfawefd3d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfawefd3d.par('fsrf',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfawefd3d.par('nbell',rsf.doc.rsfpar('int','5','','''gaussian for source injection '''))
sfawefd3d.par('optfd',rsf.doc.rsfpar('bool','n','','''optimized FD coefficients flag '''))
sfawefd3d.par('fdorder',rsf.doc.rsfpar('int','4','','''spatial FD order '''))
sfawefd3d.par('hybridbc',rsf.doc.rsfpar('bool','n','','''hybrid Absorbing BC '''))
sfawefd3d.par('sinc',rsf.doc.rsfpar('bool','n','','''sinc source injection '''))
sfawefd3d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfawefd3d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfawefd3d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfawefd3d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfawefd3d.par('nqy',rsf.doc.rsfpar('int','sf_n(ay)','','''Saved wfld window ny '''))
sfawefd3d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfawefd3d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfawefd3d.par('oqy',rsf.doc.rsfpar('float','sf_o(ay)','','''Saved wfld window oy '''))
sfawefd3d.par('dqz',rsf.doc.rsfpar('float','sf_d(az)','','''Saved wfld window dz '''))
sfawefd3d.par('dqx',rsf.doc.rsfpar('float','sf_d(ax)','','''Saved wfld window dx '''))
sfawefd3d.par('dqy',rsf.doc.rsfpar('float','sf_d(ay)','','''Saved wfld window dy '''))
sfawefd3d.par('cden',rsf.doc.rsfpar('string ',desc='''Constant density'''))
sfawefd3d.version('1.7')
sfawefd3d.synopsis('''sfawefd3d < file_wav.rsf vel=file_vel.rsf sou=file_src.rsf rec=file_rec.rsf > file_dat.rsf wfl=file_wfl.rsf den=file_den.rsf verb=n snap=n expl=n dabc=n cden=n adj=n fsrf=n nbell=5 optfd=n fdorder=4 hybridbc=n sinc=n jsnap=nt jdata=1 nqz=sf_n(az) nqx=sf_n(ax) nqy=sf_n(ay) oqz=sf_o(az) oqx=sf_o(ax) oqy=sf_o(ay) dqz=sf_d(az) dqx=sf_d(ax) dqy=sf_d(ay)''','''   2Nth order in space, 2nd order in time
   with optimized FD scheme option and hybrid one-way ABC option 
   adj flag indicates backwards source injection, not exact adjoint propagator
''')
rsf.doc.progs['sfawefd3d']=sfawefd3d

sfdbmerge = rsf.doc.rsfprog('sfdbmerge','user/cwp/Mdbmerge.py','''''')
sfdbmerge.version('1.7')
sfdbmerge.synopsis('''sfdbmerge''','''A program that can be used to merge separate SCons databases together.  Typically used when an SConstruct is split
into multiple pieces (e.g. on a cluster).

args:
    outdb - path of the output database

    strings - names of the databases to merge together
''')
rsf.doc.progs['sfdbmerge']=sfdbmerge

