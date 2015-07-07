sfewefd3dtti = rsf.doc.rsfprog('sfewefd3dtti','user/jyan/Mewefd3dtti.c','''3D elastic time-domain FD modeling ''')
sfewefd3dtti.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3dtti.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3dtti.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3dtti.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3dtti.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd3dtti.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd3dtti.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd3dtti.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd3dtti.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd3dtti.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd3dtti.par('nbell',rsf.doc.rsfpar('int','1','','''bell size '''))
sfewefd3dtti.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfewefd3dtti.par('jsnap',rsf.doc.rsfpar('int','nt','',''''''))
sfewefd3dtti.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','',''''''))
sfewefd3dtti.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','',''''''))
sfewefd3dtti.par('nqy',rsf.doc.rsfpar('int','sf_n(ay)','',''''''))
sfewefd3dtti.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','',''''''))
sfewefd3dtti.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','',''''''))
sfewefd3dtti.par('oqy',rsf.doc.rsfpar('float','sf_o(ay)','',''''''))
sfewefd3dtti.version('1.7')
sfewefd3dtti.synopsis('''sfewefd3dtti < Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf verb=n snap=n free=n ssou=n dabc=n nbell=1 jdata=1 jsnap=nt nqz=sf_n(az) nqx=sf_n(ax) nqy=sf_n(ay) oqz=sf_o(az) oqx=sf_o(ax) oqy=sf_o(ay)''','''''')
rsf.doc.progs['sfewefd3dtti']=sfewefd3dtti

