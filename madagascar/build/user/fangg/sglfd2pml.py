sfsglfd2pml = rsf.doc.rsfprog('sfsglfd2pml','user/fangg/Msglfd2pml.c','''2-D Lowrank Finite-difference wave extrapolation on staggered grid''')
sfsglfd2pml.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfd2pml.par('Gx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('Gz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('sxx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('sxz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('szx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('szz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglfd2pml.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity'''))
sfsglfd2pml.par('srcdecay',rsf.doc.rsfpar('bool','n','','''source decay'''))
sfsglfd2pml.par('srcrange',rsf.doc.rsfpar('int','10','','''source decay range'''))
sfsglfd2pml.par('srctrunc',rsf.doc.rsfpar('float','100','','''trunc source after srctrunc time (s)'''))
sfsglfd2pml.par('snapinter',rsf.doc.rsfpar('int','1','','''snap interval '''))
sfsglfd2pml.par('pmlsize',rsf.doc.rsfpar('int','PMLOUT','','''size of PML layer '''))
sfsglfd2pml.par('pmld0',rsf.doc.rsfpar('int','PMLD0','','''PML parameter '''))
sfsglfd2pml.par('decay',rsf.doc.rsfpar('int','DECAY_FLAG','','''Flag of decay boundary condtion: 1 = use ; 0 = not use '''))
sfsglfd2pml.par('decaybegin',rsf.doc.rsfpar('int','DECAY_BEGIN','','''Begin time of using decay boundary condition '''))
sfsglfd2pml.par('freesurface',rsf.doc.rsfpar('bool','n','','''free surface'''))
sfsglfd2pml.par('slx',rsf.doc.rsfpar('float','-1.0','','''source location x '''))
sfsglfd2pml.par('spx',rsf.doc.rsfpar('int','-1','','''source location x (index)'''))
sfsglfd2pml.par('slz',rsf.doc.rsfpar('float','-1.0','','''source location z '''))
sfsglfd2pml.par('spz',rsf.doc.rsfpar('int','-1','','''source location z (index)'''))
sfsglfd2pml.par('gdep',rsf.doc.rsfpar('float','-1.0','','''recorder depth on grid'''))
sfsglfd2pml.par('gp',rsf.doc.rsfpar('int','0','','''recorder depth on index'''))
sfsglfd2pml.version('1.7')
sfsglfd2pml.synopsis('''sfsglfd2pml < fsource.rsf vel=fvel.rsf den=fden.rsf > fwf.rsf rec=frec.rsf Gx=fGx.rsf Gz=fGz.rsf sxx=fsxx.rsf sxz=fsxz.rsf szx=fszx.rsf szz=fszz.rsf verb=n srcdecay=n srcrange=10 srctrunc=100 snapinter=1 pmlsize=PMLOUT pmld0=PMLD0 decay=DECAY_FLAG decaybegin=DECAY_BEGIN freesurface=n slx=-1.0 spx=-1 slz=-1.0 spz=-1 gdep=-1.0 gp=0''','''''')
rsf.doc.progs['sfsglfd2pml']=sfsglfd2pml

