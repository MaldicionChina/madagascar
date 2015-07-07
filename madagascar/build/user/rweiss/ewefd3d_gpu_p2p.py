sfewefd3d_gpu_p2p = rsf.doc.rsfprog('sfewefd3d_gpu_p2p','user/rweiss/Mewefd3d_gpu_p2p.cu','''3D elastic time-domain FD modeling with GPU (For use in single node with one or more GPUs)''')
sfewefd3d_gpu_p2p.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd3d_gpu_p2p.par('ngpu',rsf.doc.rsfpar('int','1','','''how many local GPUs to use '''))
sfewefd3d_gpu_p2p.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd3d_gpu_p2p.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd3d_gpu_p2p.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd3d_gpu_p2p.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd3d_gpu_p2p.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd3d_gpu_p2p.par('interp',rsf.doc.rsfpar('bool','y','','''perform linear interpolation on receiver data '''))
sfewefd3d_gpu_p2p.par('nbell',rsf.doc.rsfpar('int','5','','''bell size '''))
sfewefd3d_gpu_p2p.par('jdata',rsf.doc.rsfpar('int','1','','''extract receiver data every jdata time steps '''))
sfewefd3d_gpu_p2p.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every jsnap time steps '''))
sfewefd3d_gpu_p2p.version('1.7')
sfewefd3d_gpu_p2p.synopsis('''sfewefd3d_gpu_p2p < Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf ngpu=1 verb=n snap=n free=n ssou=n dabc=n interp=y nbell=5 jdata=1 jsnap=nt''','''''')
rsf.doc.progs['sfewefd3d_gpu_p2p']=sfewefd3d_gpu_p2p

