import rsf.doc

sfacd2d = rsf.doc.rsfprog('sfacd2d','user/hpcss/Macd2d.c','''time-domain acoustic FD modeling ''')
sfacd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfacd2d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfacd2d.par('verb',rsf.doc.rsfpar('bool','n','','''setup I/O files '''))
sfacd2d.version('1.7')
sfacd2d.synopsis('''sfacd2d < Fw.rsf > Fo.rsf vel=Fv.rsf ref=Fr.rsf verb=n''','''''')
rsf.doc.progs['sfacd2d']=sfacd2d

sfeacd2d = rsf.doc.rsfprog('sfeacd2d','user/hpcss/Meacd2d.c','''Extended time-domain acoustic FD modeling ''')
sfeacd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeacd2d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeacd2d.par('verb',rsf.doc.rsfpar('bool','n','','''setup I/O files '''))
sfeacd2d.version('1.7')
sfeacd2d.synopsis('''sfeacd2d < Fw.rsf > Fo.rsf vel=Fv.rsf ref=Fr.rsf verb=n''','''''')
rsf.doc.progs['sfeacd2d']=sfeacd2d

sfvam = rsf.doc.rsfprog('sfvam','user/hpcss/Mvam.c','''Create a layered model. ''')
sfvam.par('nz',rsf.doc.rsfpar('int','','','''depth grid '''))
sfvam.par('nx',rsf.doc.rsfpar('int','','','''distance grid '''))
sfvam.par('dz',rsf.doc.rsfpar('float','','','''depth sampling '''))
sfvam.par('dx',rsf.doc.rsfpar('float','','','''distance sampling '''))
sfvam.version('1.7')
sfvam.synopsis('''sfvam > vfile.rsf nz= nx= dz= dx=''','''''')
rsf.doc.progs['sfvam']=sfvam

sfwavedoc = rsf.doc.rsfprog('sfwavedoc','user/hpcss/Mwavedoc.c','''Rice HPCSS seismic modeling and migration. ''')
sfwavedoc.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwavedoc.par('receiver',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwavedoc.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfwavedoc.par('dt',rsf.doc.rsfpar('float','','','''step in t '''))
sfwavedoc.par('nm',rsf.doc.rsfpar('int','0','','''number of time steps to skip between movie frames
       (<=0 for no movie) '''))
sfwavedoc.par('isz',rsf.doc.rsfpar('int','1','','''source depth, in units of dz '''))
sfwavedoc.par('isxbeg',rsf.doc.rsfpar('int','(nx)/2','','''far left source x coord in units of dx '''))
sfwavedoc.par('isxend',rsf.doc.rsfpar('int','(nx)/2','','''far right source x coord in units of dx '''))
sfwavedoc.par('iskip',rsf.doc.rsfpar('int','1','','''interval between sources in units of dx '''))
sfwavedoc.par('igz',rsf.doc.rsfpar('int','1','','''recvr depth, in units of dz '''))
sfwavedoc.par('igxbeg',rsf.doc.rsfpar('int','1','','''far left receiver x coord in units of dx '''))
sfwavedoc.par('igxend',rsf.doc.rsfpar('int','0','','''far right receiver x coord in units of dx '''))
sfwavedoc.par('fpeak',rsf.doc.rsfpar('float','0.01','','''center frequency of Ricker wavelet '''))
sfwavedoc.par('ihmax',rsf.doc.rsfpar('int','0','','''offset radius, units of dx '''))
sfwavedoc.par('imbeg',rsf.doc.rsfpar('int','ihmax','','''midpoint begin '''))
sfwavedoc.par('imend',rsf.doc.rsfpar('int','nx-ihmax-1','','''midpoint end '''))
sfwavedoc.par('imskip',rsf.doc.rsfpar('int','1','','''midpoint skip '''))
sfwavedoc.par('source',rsf.doc.rsfpar('string ',desc='''source movie file (auxiliary output file name)'''))
sfwavedoc.par('receiver',rsf.doc.rsfpar('string ',desc='''receiver movie file (auxiliary output file name)'''))
sfwavedoc.version('1.7')
sfwavedoc.synopsis('''sfwavedoc < vfile.rsf source=mfile.rsf > tfile.rsf receiver=rmfile.rsf > imfile.rsf nt= dt= nm=0 isz=1 isxbeg=(nx)/2 isxend=(nx)/2 iskip=1 igz=1 igxbeg=1 igxend=0 fpeak=0.01 ihmax=0 imbeg=ihmax imend=nx-ihmax-1 imskip=1''','''''')
rsf.doc.progs['sfwavedoc']=sfwavedoc

rsf.doc.progs['sfwave']=sfwavedoc
rsf.doc.progs['sfrtm']=sfwavedoc
rsf.doc.progs['sfwave24']=sfwavedoc
