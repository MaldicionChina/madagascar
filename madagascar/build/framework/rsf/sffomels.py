import rsf.doc

sfabalance = rsf.doc.rsfprog('sfabalance','user/fomels/Mabalance.c','''Amplitude balancing. ''')
sfabalance.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfabalance.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfabalance.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfabalance.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfabalance.version('1.7 Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfabalance.synopsis('''sfabalance < in.rsf other=ref.rsf > out.rsf niter=100 order=100 ref=1.''','''''')
rsf.doc.progs['sfabalance']=sfabalance

sfangle = rsf.doc.rsfprog('sfangle','user/fomels/Mangle.c','''Illustration of angle gathers.''')
sfangle.par('nw',rsf.doc.rsfpar('int','513','',''''''))
sfangle.par('nm',rsf.doc.rsfpar('int','257','',''''''))
sfangle.par('nh',rsf.doc.rsfpar('int','257','',''''''))
sfangle.par('dw',rsf.doc.rsfpar('float','1./(2*(nw-1)*0.004)','',''''''))
sfangle.par('dm',rsf.doc.rsfpar('float','1./(2*(nm-1)*0.01)','',''''''))
sfangle.par('dh',rsf.doc.rsfpar('float','1./(2*(nh-1)*0.01)','',''''''))
sfangle.par('w0',rsf.doc.rsfpar('float','dw','',''''''))
sfangle.par('vel',rsf.doc.rsfpar('float','2.','',''''''))
sfangle.version('1.7 Mangle.c 7884 2011-11-17 02:52:47Z sfomel')
sfangle.synopsis('''sfangle > angle.rsf nw=513 nm=257 nh=257 dw=1./(2*(nw-1)*0.004) dm=1./(2*(nm-1)*0.01) dh=1./(2*(nh-1)*0.01) w0=dw vel=2.''','''''')
rsf.doc.progs['sfangle']=sfangle

sfangle2 = rsf.doc.rsfprog('sfangle2','user/fomels/Mangle2.c','''Another illustration of angle gathers.''')
sfangle2.par('nx',rsf.doc.rsfpar('int','451','',''''''))
sfangle2.par('ny',rsf.doc.rsfpar('int','451','',''''''))
sfangle2.par('dx',rsf.doc.rsfpar('float','0.1','',''''''))
sfangle2.par('dy',rsf.doc.rsfpar('float','0.1','',''''''))
sfangle2.par('zx',rsf.doc.rsfpar('float','0.','',''''''))
sfangle2.par('zy',rsf.doc.rsfpar('float','0.','',''''''))
sfangle2.version('1.7 Mangle2.c 7107 2011-04-10 02:04:14Z ivlad')
sfangle2.synopsis('''sfangle2 > angle.rsf nx=451 ny=451 dx=0.1 dy=0.1 zx=0. zy=0.''','''''')
rsf.doc.progs['sfangle2']=sfangle2

sfbilat2 = rsf.doc.rsfprog('sfbilat2','user/fomels/Mbilat2.c','''2-D bilateral filtering ''')
sfbilat2.par('r1',rsf.doc.rsfpar('int','1','','''vertical smoothing radius '''))
sfbilat2.par('r2',rsf.doc.rsfpar('int','1','','''horizontal smoothing radius '''))
sfbilat2.par('a1',rsf.doc.rsfpar('float','0.0f','','''vertical attenuation factor '''))
sfbilat2.par('a2',rsf.doc.rsfpar('float','a1','','''horizontal attenuation factor '''))
sfbilat2.par('a3',rsf.doc.rsfpar('float','0.0f','','''data attenuation factor '''))
sfbilat2.par('repeat',rsf.doc.rsfpar('int','1','','''repeat the operation '''))
sfbilat2.version('1.7')
sfbilat2.synopsis('''sfbilat2 < inp.rsf > out.rsf r1=1 r2=1 a1=0.0f a2=a1 a3=0.0f repeat=1''','''''')
rsf.doc.progs['sfbilat2']=sfbilat2

sfcdivn = rsf.doc.rsfprog('sfcdivn','user/fomels/Mcdivn.c','''Smooth division for complex data. ''')
sfcdivn.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdivn.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfcdivn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfcdivn.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfcdivn.version('1.7')
sfcdivn.synopsis('''sfcdivn < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sfcdivn']=sfcdivn

sfchebvc = rsf.doc.rsfprog('sfchebvc','user/fomels/Mchebvc.c','''Post-stack 2-D velocity continuation by Chebyshev-tau method. ''')
sfchebvc.par('nv',rsf.doc.rsfpar('int','','',''''''))
sfchebvc.par('vel',rsf.doc.rsfpar('float','','',''''''))
sfchebvc.version('1.7')
sfchebvc.synopsis('''sfchebvc < in.rsf > out.rsf nv= vel=''','''''')
rsf.doc.progs['sfchebvc']=sfchebvc

sfclpf = rsf.doc.rsfprog('sfclpf','user/fomels/Mclpf.c','''Local prediction filter for complex numbers (n-dimensional). ''')
sfclpf.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfclpf.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfclpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfclpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfclpf.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfclpf.version('1.7')
sfclpf.synopsis('''sfclpf < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y''','''''')
rsf.doc.progs['sfclpf']=sfclpf

sfcltft = rsf.doc.rsfprog('sfcltft','user/fomels/Mcltft.c','''Complex local time-frequency transform. ''')
sfcltft.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcltft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfcltft.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfcltft.par('dip',rsf.doc.rsfpar('bool','n','','''if y, do dip decomposition '''))
sfcltft.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius (in time, samples) '''))
sfcltft.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sfcltft.par('np',rsf.doc.rsfpar('int','','','''number of slopes '''))
sfcltft.par('dp',rsf.doc.rsfpar('float','','','''slope step '''))
sfcltft.par('p0',rsf.doc.rsfpar('float','','','''first slope '''))
sfcltft.par('nw',rsf.doc.rsfpar('int','kiss_fft_next_fast_size(n1)','','''number of frequencies '''))
sfcltft.par('dw',rsf.doc.rsfpar('float','1./(nw*d1)','','''frequency step '''))
sfcltft.par('w0',rsf.doc.rsfpar('float','-0.5/d1','','''first frequency '''))
sfcltft.par('basis',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfcltft.version('1.7')
sfcltft.synopsis('''sfcltft < in.rsf > out.rsf basis=basis.rsf inv=n verb=n dip=n rect=10 niter=100 np= dp= p0= nw=kiss_fft_next_fast_size(n1) dw=1./(nw*d1) w0=-0.5/d1''','''''')
rsf.doc.progs['sfcltft']=sfcltft

sfcpef = rsf.doc.rsfprog('sfcpef','user/fomels/Mcpef.c','''1-D prediction-error filter estimation from complex data ''')
sfcpef.par('single',rsf.doc.rsfpar('bool','y','','''single channel or multichannel '''))
sfcpef.par('nf',rsf.doc.rsfpar('int','','','''filter length '''))
sfcpef.version('1.7')
sfcpef.synopsis('''sfcpef < in.rsf > out.rsf single=y nf=''','''''')
rsf.doc.progs['sfcpef']=sfcpef

sfdeblur = rsf.doc.rsfprog('sfdeblur','user/fomels/Mdeblur.c','''Non-stationary debluring by inversion ''')
sfdeblur.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdeblur.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdeblur.par('nliter',rsf.doc.rsfpar('int','1','','''number of nonlinear iterations '''))
sfdeblur.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdeblur.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfdeblur.version('1.7')
sfdeblur.synopsis('''sfdeblur < in.rsf > out.rsf rect=rect.rsf niter=100 nliter=1 verb=n eps=0.''','''''')
rsf.doc.progs['sfdeblur']=sfdeblur

sfdivn = rsf.doc.rsfprog('sfdivn','user/fomels/Mdivn.c','''Smooth division. ''')
sfdivn.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdivn.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdivn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfdivn.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfdivn.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdivn.version('1.7')
sfdivn.synopsis('''sfdivn < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfdivn']=sfdivn

sfdix = rsf.doc.rsfprog('sfdix','user/fomels/Mdix.c','''Convert RMS to interval velocity using LS and shaping regularization. ''')
sfdix.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdix.par('vrmsout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdix.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfdix.par('rect#',rsf.doc.rsfpar('string','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdix.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdix.par('vrmsout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted vrms (auxiliary output file name)'''))
sfdix.version('1.7 Mdix.c 7107 2011-04-10 02:04:14Z ivlad')
sfdix.synopsis('''sfdix < vrms.rsf > vint.rsf weight=weight.rsf vrmsout=vout.rsf niter=100 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfdix']=sfdix

sfeikonal = rsf.doc.rsfprog('sfeikonal','user/fomels/Meikonal.c','''Fast marching eikonal solver (3-D). ''')
sfeikonal.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeikonal.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfeikonal.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfeikonal.par('sweep',rsf.doc.rsfpar('bool','n','','''if y, use fast sweeping instead of fast marching '''))
sfeikonal.par('br1',rsf.doc.rsfpar('float','d1','',''''''))
sfeikonal.par('br2',rsf.doc.rsfpar('float','d2','',''''''))
sfeikonal.par('br3',rsf.doc.rsfpar('float','d3','','''Constant-velocity box around the source (in physical dimensions) '''))
sfeikonal.par('plane1',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonal.par('plane2',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonal.par('plane3',rsf.doc.rsfpar('bool','n','','''plane-wave source '''))
sfeikonal.par('b1',rsf.doc.rsfpar('int','plane[2]? n1: (int) (br1/d1+0.5)','',''''''))
sfeikonal.par('b2',rsf.doc.rsfpar('int','plane[1]? n2: (int) (br2/d2+0.5)','',''''''))
sfeikonal.par('b3',rsf.doc.rsfpar('int','plane[0]? n3: (int) (br3/d3+0.5)','','''Constant-velocity box around the source (in samples) '''))
sfeikonal.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikonal.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikonal.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikonal.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)'''))
sfeikonal.version('1.7 Meikonal.c 12827 2014-06-12 04:04:58Z sfomel')
sfeikonal.synopsis('''sfeikonal < vel.rsf > time.rsf shotfile=shots.rsf vel=y order=2 sweep=n br1=d1 br2=d2 br3=d3 plane1=n plane2=n plane3=n b1=plane[2]? n1: (int) (br1/d1+0.5) b2=plane[1]? n2: (int) (br2/d2+0.5) b3=plane[0]? n3: (int) (br3/d3+0.5) zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3''','''
June 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/392-Program-of-the-month-sfeikonal.html
''')
rsf.doc.progs['sfeikonal']=sfeikonal

sfeikonalvti = rsf.doc.rsfprog('sfeikonalvti','user/fomels/Meikonalvti.c','''Fast marching eikonal solver in VTI media. ''')
sfeikonalvti.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeikonalvti.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfeikonalvti.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfeikonalvti.par('br1',rsf.doc.rsfpar('float','d1','',''''''))
sfeikonalvti.par('br2',rsf.doc.rsfpar('float','d2','',''''''))
sfeikonalvti.par('br3',rsf.doc.rsfpar('float','d3','','''Constant-velocity box around the source (in physical dimensions) '''))
sfeikonalvti.par('plane1',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonalvti.par('plane2',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonalvti.par('plane3',rsf.doc.rsfpar('bool','n','','''plane-wave source '''))
sfeikonalvti.par('b1',rsf.doc.rsfpar('int','plane[2]? n1: (int) (br1/d1+0.5)','',''''''))
sfeikonalvti.par('b2',rsf.doc.rsfpar('int','plane[1]? n2: (int) (br2/d2+0.5)','',''''''))
sfeikonalvti.par('b3',rsf.doc.rsfpar('int','plane[0]? n3: (int) (br3/d3+0.5)','','''Constant-velocity box around the source (in samples) '''))
sfeikonalvti.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikonalvti.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikonalvti.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikonalvti.par('vx',rsf.doc.rsfpar('string ',desc=''''''))
sfeikonalvti.par('eta',rsf.doc.rsfpar('string ',desc=''''''))
sfeikonalvti.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)'''))
sfeikonalvti.version('1.7 Meikonal.c 1507 2005-10-22 04:01:28Z savap')
sfeikonalvti.synopsis('''sfeikonalvti < vzf.rsf > time.rsf shotfile=shots.rsf vel=y order=2 br1=d1 br2=d2 br3=d3 plane1=n plane2=n plane3=n b1=plane[2]? n1: (int) (br1/d1+0.5) b2=plane[1]? n2: (int) (br2/d2+0.5) b3=plane[0]? n3: (int) (br3/d3+0.5) zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3 vx= eta=''','''''')
rsf.doc.progs['sfeikonalvti']=sfeikonalvti

sferf = rsf.doc.rsfprog('sferf','user/fomels/Merf.c','''Bandpass filtering using erf function. ''')
sferf.par('flo',rsf.doc.rsfpar('float','-1.','','''low frequency in band '''))
sferf.par('fhi',rsf.doc.rsfpar('float','-1.','','''high frequency in band '''))
sferf.par('rect',rsf.doc.rsfpar('float','1','','''filter sharpness '''))
sferf.par('spline',rsf.doc.rsfpar('bool','n','','''if use B-spline erf '''))
sferf.par('der',rsf.doc.rsfpar('bool','n','','''compute derivative '''))
sferf.version('1.7')
sferf.synopsis('''sferf < in.rsf > out.rsf flo=-1. fhi=-1. rect=1 spline=n der=n''','''''')
rsf.doc.progs['sferf']=sferf

sfexgr = rsf.doc.rsfprog('sfexgr','user/fomels/Mexgr.c','''Exact group velocity in VTI media ''')
sfexgr.par('aq',rsf.doc.rsfpar('float','14.47','',''''''))
sfexgr.par('bq',rsf.doc.rsfpar('float','2.28','',''''''))
sfexgr.par('cq',rsf.doc.rsfpar('float','9.57','',''''''))
sfexgr.par('dq',rsf.doc.rsfpar('float','4.51','',''''''))
sfexgr.version('1.7')
sfexgr.synopsis('''sfexgr > out.rsf aq=14.47 bq=2.28 cq=9.57 dq=4.51''','''''')
rsf.doc.progs['sfexgr']=sfexgr

sffftexp0 = rsf.doc.rsfprog('sffftexp0','user/fomels/Mfftexp0.c','''2-D FFT-based zero-offset exploding reflector modeling/migration  ''')
sffftexp0.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftexp0.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp0.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp0.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sffftexp0.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftexp0.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftexp0.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sffftexp0.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sffftexp0.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sffftexp0.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sffftexp0.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftexp0.version('1.7')
sffftexp0.synopsis('''sffftexp0 < data.rsf > image.rsf snaps=snaps.rsf left=left.rsf right=right.rsf mig=n cmplx=n pad1=1 nz= dz= nt= dt= snap=0''','''''')
rsf.doc.progs['sffftexp0']=sffftexp0

sffftexp3 = rsf.doc.rsfprog('sffftexp3','user/fomels/Mfftexp3.c','''3-D FFT-based zero-offset exploding reflector modeling/migration  ''')
sffftexp3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp3.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp3.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sffftexp3.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sffftexp3.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sffftexp3.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sffftexp3.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sffftexp3.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sffftexp3.version('1.7')
sffftexp3.synopsis('''sffftexp3 < data.rsf > image.rsf left=left.rsf right=right.rsf mig=n ompchunk=1 nz= dz= nt= dt=''','''''')
rsf.doc.progs['sffftexp3']=sffftexp3

sffftwave1 = rsf.doc.rsfprog('sffftwave1','user/fomels/Mfftwave1.c','''1-D FFT wave extrapolation ''')
sffftwave1.par('prop',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave1.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffftwave1.par('dt',rsf.doc.rsfpar('float','','',''''''))
sffftwave1.par('sub',rsf.doc.rsfpar('bool','y','','''if -1 is included in the matrix '''))
sffftwave1.par('step',rsf.doc.rsfpar('bool','y','','''if two-step propagation '''))
sffftwave1.par('nsps',rsf.doc.rsfpar('bool','n','','''if using NSPS '''))
sffftwave1.par('right',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffftwave1.version('1.7')
sffftwave1.synopsis('''sffftwave1 < inp.rsf > out.rsf prop=prop.rsf right=right.rsf nt= dt= sub=y step=y nsps=n''','''''')
rsf.doc.progs['sffftwave1']=sffftwave1

sffftwave2 = rsf.doc.rsfprog('sffftwave2','user/fomels/Mfftwave2.c','''Simple 2-D wave propagation ''')
sffftwave2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftwave2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffftwave2.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftwave2.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftwave2.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftwave2.version('1.7')
sffftwave2.synopsis('''sffftwave2 < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf verb=n snap=0 cmplx=n pad1=1''','''''')
rsf.doc.progs['sffftwave2']=sffftwave2

sffftwave3 = rsf.doc.rsfprog('sffftwave3','user/fomels/Mfftwave3.c','''Simple 3-D wave propagation ''')
sffftwave3.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftwave3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sffftwave3.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftwave3.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftwave3.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftwave3.version('1.7')
sffftwave3.synopsis('''sffftwave3 < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf verb=y cmplx=n pad1=1 snap=0''','''''')
rsf.doc.progs['sffftwave3']=sffftwave3

sffocus = rsf.doc.rsfprog('sffocus','user/fomels/Mfocus.c','''Focusing indicator. ''')
sffocus.par('dim',rsf.doc.rsfpar('int','','','''dimensionality '''))
sffocus.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sffocus.par('verb',rsf.doc.rsfpar('bool','y','',''''''))
sffocus.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sffocus.version('1.7')
sffocus.synopsis('''sffocus < in.rsf > out.rsf dim= niter=100 verb=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sffocus']=sffocus

sfiphase = rsf.doc.rsfprog('sfiphase','user/fomels/Miphase.c','''Smooth estimate of instantaneous frequency. ''')
sfiphase.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfiphase.par('complex',rsf.doc.rsfpar('bool','n','','''if y, use complex-valued computations '''))
sfiphase.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfiphase.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfiphase.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfiphase.par('hertz',rsf.doc.rsfpar('bool','n','','''if y, convert output to Hertz '''))
sfiphase.par('band',rsf.doc.rsfpar('bool','n','','''if y, compute instantaneous bandwidth '''))
sfiphase.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfiphase.version('1.7 Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfiphase.synopsis('''sfiphase < in.rsf > out.rsf verb=n complex=n niter=100 order=100 ref=1. hertz=n band=n rect#=(1,1,...)''','''''')
rsf.doc.progs['sfiphase']=sfiphase

sflocalskew = rsf.doc.rsfprog('sflocalskew','user/fomels/Mlocalskew.c','''Rotate phase and compute local skewness. ''')
sflocalskew.par('na',rsf.doc.rsfpar('int','360','','''number of angles '''))
sflocalskew.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sflocalskew.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle '''))
sflocalskew.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sflocalskew.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sflocalskew.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflocalskew.par('inv',rsf.doc.rsfpar('bool','y','','''inverse similarity '''))
sflocalskew.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sflocalskew.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sflocalskew.par('const',rsf.doc.rsfpar('bool','n','','''if y, compute inverse varimax '''))
sflocalskew.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflocalskew.version('1.7')
sflocalskew.synopsis('''sflocalskew < inp.rsf > sim.rsf na=360 da=1.0 a0=-180. order=100 ref=1. verb=y inv=y niter=20 rect=3 const=n eps=0.0f''','''''')
rsf.doc.progs['sflocalskew']=sflocalskew

sflpf = rsf.doc.rsfprog('sflpf','user/fomels/Mlpf.c','''Local prediction filter (n-dimensional). ''')
sflpf.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflpf.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sflpf.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflpf.par('pef',rsf.doc.rsfpar('string ',desc='''signal PEF file (optional) '''))
sflpf.par('lag',rsf.doc.rsfpar('string ',desc='''file with PEF lags (optional) '''))
sflpf.version('1.7')
sflpf.synopsis('''sflpf < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y pef= lag=''','''''')
rsf.doc.progs['sflpf']=sflpf

sflsfit = rsf.doc.rsfprog('sflsfit','user/fomels/Mlsfit.c','''Simple least-squares regression. ''')
sflsfit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsfit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflsfit.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsfit.par('linear',rsf.doc.rsfpar('bool','y','','''if linear LS '''))
sflsfit.par('dim',rsf.doc.rsfpar('int','dim','','''number of dimensions '''))
sflsfit.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization parameter '''))
sflsfit.par('coef',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflsfit.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflsfit.version('1.7')
sflsfit.synopsis('''sflsfit < inp.rsf fit=fit.rsf > out.rsf coef=coef.rsf weight=wht.rsf linear=y dim=dim eps=0.0f''','''''')
rsf.doc.progs['sflsfit']=sflsfit

sfmffit = rsf.doc.rsfprog('sfmffit','user/fomels/Mmffit.c','''Fitting multi-focusing approximations ''')
sfmffit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmffit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmffit.par('x0',rsf.doc.rsfpar('float','m0','','''central midpoint '''))
sfmffit.par('type',rsf.doc.rsfpar('string ',desc='''Type of approximation (crs,mf,nonhyperbolic) '''))
sfmffit.version('1.7')
sfmffit.synopsis('''sfmffit < in.rsf coef=coef.rsf > out.rsf fit=fit.rsf x0=m0 type=''','''''')
rsf.doc.progs['sfmffit']=sfmffit

sfmig3 = rsf.doc.rsfprog('sfmig3','user/fomels/Mmig3.c','''3-D Kirchhoff time migration with antialiasing. ''')
sfmig3.par('hdr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig3.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('d2',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('o2',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('n3',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('d3',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('o3',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('vel',rsf.doc.rsfpar('float','','','''migration velocity '''))
sfmig3.par('antialias',rsf.doc.rsfpar('string ',desc='''antialiasing type [triangle,flat,steep,none] '''))
sfmig3.version('1.7')
sfmig3.synopsis('''sfmig3 < in.rsf hdr=head.rsf > mig.rsf n2= d2= o2= n3= d3= o3= n1= vel= antialias=''','''''')
rsf.doc.progs['sfmig3']=sfmig3

sfnsmooth1 = rsf.doc.rsfprog('sfnsmooth1','user/fomels/Mnsmooth1.c','''1-D non-stationary smoothing. ''')
sfnsmooth1.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnsmooth1.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfnsmooth1.version('1.7 Msmooth.c 691 2004-07-04 19:28:08Z fomels')
sfnsmooth1.synopsis('''sfnsmooth1 < in.rsf > out.rsf rect=rect.rsf repeat=1''','''''')
rsf.doc.progs['sfnsmooth1']=sfnsmooth1

sfocparcel = rsf.doc.rsfprog('sfocparcel','user/fomels/Mocparcel.c','''Patching test for out-of-core patching. ''')
sfocparcel.par('w',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfocparcel.par('k',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfocparcel.version('1.7 Mparcel.c 691 2004-07-04 19:28:08Z fomels')
sfocparcel.synopsis('''sfocparcel < in.rsf > out.rsf w= k=''','''''')
rsf.doc.progs['sfocparcel']=sfocparcel

sfoctentwt = rsf.doc.rsfprog('sfoctentwt','user/fomels/Moctentwt.c','''Tent-like weight for out-of-core patching. ''')
sfoctentwt.par('windwt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfoctentwt.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sfoctentwt.par('k',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sfoctentwt.par('a',rsf.doc.rsfpar('ints','','','''filter size  [dim]'''))
sfoctentwt.par('center',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfoctentwt.par('dim',rsf.doc.rsfpar('int','2','','''number of dimensions '''))
sfoctentwt.version('1.7 Mtentwt.c 691 2004-07-04 19:28:08Z fomels')
sfoctentwt.synopsis('''sfoctentwt > wallwt.rsf windwt=windwt.rsf w= k= a= center= dim=2''','''''')
rsf.doc.progs['sfoctentwt']=sfoctentwt

sfofilp = rsf.doc.rsfprog('sfofilp','user/fomels/Mofilp.c','''2-D missing data interpolation by differential offset continuation. ''')
sfofilp.par('known',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofilp.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfofilp.par('simple',rsf.doc.rsfpar('bool','n','','''if y, use simple h derivative for regularization '''))
sfofilp.version('1.7 Mofilp.c 7107 2011-04-10 02:04:14Z ivlad')
sfofilp.synopsis('''sfofilp < in.rsf > out.rsf known=known.rsf niter=10 simple=n''','''''')
rsf.doc.progs['sfofilp']=sfofilp

sfortho = rsf.doc.rsfprog('sfortho','user/fomels/Mortho.c','''Orthogonolize signal and noise. ''')
sfortho.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfortho.par('sig2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortho.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfortho.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfortho.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfortho.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfortho.version('1.7')
sfortho.synopsis('''sfortho < fnoi.rsf sig=fsig.rsf > fnoi2.rsf sig2=fsig2.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfortho']=sfortho

sfpatch = rsf.doc.rsfprog('sfpatch','user/fomels/Mpatch.c','''Patching (N-dimensional). ''')
sfpatch.par('n0',rsf.doc.rsfpar('ints','','','''data dimensions (for inv=y)  [dim]'''))
sfpatch.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sfpatch.par('p',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sfpatch.par('inv',rsf.doc.rsfpar('bool','n','','''inverse or forward operation '''))
sfpatch.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpatch.par('weight',rsf.doc.rsfpar('bool','n','','''if y, apply weighting to each patch '''))
sfpatch.par('dim',rsf.doc.rsfpar('int','dim0','',''''''))
sfpatch.version('1.7')
sfpatch.synopsis('''sfpatch < in.rsf > out.rsf n0= w= p= inv=n verb=n weight=n dim=dim0''','''
w is window size (defaults to n1,n2,...)
p is number of patches in different dimensions (defaults to 1,1,...)

If inv=n, the number of output dimensions is twice the number of input dimensions.
If inv=y, the number of output dimensions is half the number of input dimensions.

September 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/357-Program-of-the-month-sfpatch.html
''')
rsf.doc.progs['sfpatch']=sfpatch

sfphaserot = rsf.doc.rsfprog('sfphaserot','user/fomels/Mphaserot.c','''Non-stationary phase rotation. ''')
sfphaserot.par('phase',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfphaserot.par('na',rsf.doc.rsfpar('int','721','','''number of angles '''))
sfphaserot.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sfphaserot.par('a0',rsf.doc.rsfpar('float','-360.','','''first angle '''))
sfphaserot.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfphaserot.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfphaserot.version('1.7')
sfphaserot.synopsis('''sfphaserot < inp.rsf phase=pha.rsf > out.rsf na=721 da=1.0 a0=-360. order=100 ref=1.''','''''')
rsf.doc.progs['sfphaserot']=sfphaserot

sfpick = rsf.doc.rsfprog('sfpick','user/fomels/Mpick.c','''Automatic picking  from semblance-like panels. ''')
sfpick.par('vel0',rsf.doc.rsfpar('float','o2','','''surface velocity '''))
sfpick.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick.par('an',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick.par('gate',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfpick.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfpick')
sfpick.version('1.7')
sfpick.synopsis('''sfpick < scn.rsf > pik.rsf vel0=o2 niter=100 an=1. gate=3 smooth=y rect#=(1,1,...) rect1=1 rect2=1 ...''','''rectN defines the size of the smoothing stencil in N-th dimension.

Theory in Appendix B of:
S. Fomel, 2009, 
Velocity analysis using AB semblance: Geophysical Prospecting, v. 57, 311-321.
Reproducible version in RSFSRC/book/tccs/avo 
http://ahay.org/RSF/book/tccs/avo/paper_html/

August 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/302-Program-of-the-month-sfpick.html
''')
rsf.doc.progs['sfpick']=sfpick

sfpick3 = rsf.doc.rsfprog('sfpick3','user/fomels/Mpick3.c','''Automatic picking  from 3-D semblance-like panels. ''')
sfpick3.par('vel1',rsf.doc.rsfpar('float','o2','',''''''))
sfpick3.par('vel2',rsf.doc.rsfpar('float','o3','','''surface velocity '''))
sfpick3.par('rect1',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sfpick3.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick3.par('an1',rsf.doc.rsfpar('float','1.','',''''''))
sfpick3.par('an2',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick3.par('gate1',rsf.doc.rsfpar('int','3','',''''''))
sfpick3.par('gate2',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick3.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick3.version('1.7')
sfpick3.synopsis('''sfpick3 < scn.rsf > pik.rsf vel1=o2 vel2=o3 rect1=1 niter=100 an1=1. an2=1. gate1=3 gate2=3 smooth=y''','''''')
rsf.doc.progs['sfpick3']=sfpick3

sfplane = rsf.doc.rsfprog('sfplane','user/fomels/Mplane.c','''Generating plane waves with steering filters. ''')
sfplane.par('p',rsf.doc.rsfpar('float','0.7','','''plane wave slope '''))
sfplane.par('a1',rsf.doc.rsfpar('int','2','','''filter length '''))
sfplane.par('b1',rsf.doc.rsfpar('int','1','','''denominator length '''))
sfplane.par('hyp',rsf.doc.rsfpar('bool','n','','''generate hyperbolas '''))
sfplane.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfplane.version('1.7')
sfplane.synopsis('''sfplane < inp.rsf > out.rsf p=0.7 a1=2 b1=1 hyp=n lag=''','''''')
rsf.doc.progs['sfplane']=sfplane

sfshapeagc = rsf.doc.rsfprog('sfshapeagc','user/fomels/Mshapeagc.c','''Automatic gain control by shaping regularization. ''')
sfshapeagc.par('gain',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfshapeagc.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshapeagc.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfshapeagc.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfshapeagc.par('rect#',rsf.doc.rsfpar('int','(125,1,1,...)','','''smoothing radius on #-th axis '''))
sfshapeagc.par('gain',rsf.doc.rsfpar('string ',desc='''output gain file (optional) (auxiliary output file name)'''))
sfshapeagc.version('1.7')
sfshapeagc.synopsis('''sfshapeagc < in.rsf > out.rsf gain=fgain.rsf niter=100 eps=0.0f verb=n rect#=(125,1,1,...)''','''''')
rsf.doc.progs['sfshapeagc']=sfshapeagc

sfshapefill = rsf.doc.rsfprog('sfshapefill','user/fomels/Mshapefill.c','''Missing data interpolation in 2-D by Laplacian regularization. ''')
sfshapefill.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfshapefill.par('niter',rsf.doc.rsfpar('int','200','','''number of iterations '''))
sfshapefill.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfshapefill.par('dim',rsf.doc.rsfpar('int','dim','','''dimensionality '''))
sfshapefill.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfshapefill.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file with zeroes for missing data locations (auxiliary input file name)'''))
sfshapefill.version('1.7')
sfshapefill.synopsis('''sfshapefill < in.rsf > out.rsf mask=mask.rsf niter=200 verb=n dim=dim rect#=(1,1,...)''','''''')
rsf.doc.progs['sfshapefill']=sfshapefill

sfshearer = rsf.doc.rsfprog('sfshearer','user/fomels/Mshearer.c','''Preconditioning for traveltime picking. ''')
sfshearer.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshearer.par('order',rsf.doc.rsfpar('int','10','','''Hilbert transformer order '''))
sfshearer.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfshearer.par('short',rsf.doc.rsfpar('int','1','','''short smoothing radius '''))
sfshearer.par('long',rsf.doc.rsfpar('int','10','','''long smoothing radius '''))
sfshearer.version('1.7 Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfshearer.synopsis('''sfshearer < in.rsf > out.rsf niter=100 order=10 ref=1. short=1 long=10 rect1=1 rect2=1 ... ''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfshearer']=sfshearer

sfshift1 = rsf.doc.rsfprog('sfshift1','user/fomels/Mshift1.c','''Generate shifts for 1-D regularized autoregression. ''')
sfshift1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshift1.version('1.7')
sfshift1.synopsis('''sfshift1 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshift1']=sfshift1

sfsimenv = rsf.doc.rsfprog('sfsimenv','user/fomels/Msimenv.c','''Rotate phase and compute similarity with enevelope. ''')
sfsimenv.par('na',rsf.doc.rsfpar('int','360','','''number of angles '''))
sfsimenv.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sfsimenv.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle '''))
sfsimenv.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfsimenv.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfsimenv.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimenv.par('inv',rsf.doc.rsfpar('bool','y','','''inverse similarity '''))
sfsimenv.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimenv.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfsimenv.version('1.7')
sfsimenv.synopsis('''sfsimenv < inp.rsf > sim.rsf na=360 da=1.0 a0=-180. order=100 ref=1. verb=y inv=y niter=20 rect=3''','''''')
rsf.doc.progs['sfsimenv']=sfsimenv

sfsimilarity = rsf.doc.rsfprog('sfsimilarity','user/fomels/Msimilarity.c','''Local similarity measure between two datasets. ''')
sfsimilarity.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimilarity.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimilarity.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimilarity.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfsimilarity.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsimilarity.version('1.7')
sfsimilarity.synopsis('''sfsimilarity < in.rsf > out.rsf other=other.rsf verb=y niter=20 eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfsimilarity']=sfsimilarity

sfsmoothreg = rsf.doc.rsfprog('sfsmoothreg','user/fomels/Msmoothreg.c','''Smoothing in 1-D by simple regularization.''')
sfsmoothreg.par('eps',rsf.doc.rsfpar('float','1.','','''smoothness parameter '''))
sfsmoothreg.par('repeat',rsf.doc.rsfpar('int','1','','''repeat smoothing '''))
sfsmoothreg.version('1.7 Msmoothreg.c 7107 2011-04-10 02:04:14Z ivlad')
sfsmoothreg.synopsis('''sfsmoothreg < in.rsf > smooth.rsf eps=1. repeat=1''','''''')
rsf.doc.progs['sfsmoothreg']=sfsmoothreg

sftimefreq = rsf.doc.rsfprog('sftimefreq','user/fomels/Mtimefreq.c','''Time-frequency analysis using local attributes. ''')
sftimefreq.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftimefreq.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sftimefreq.par('dw',rsf.doc.rsfpar('float','','','''f	requency step '''))
sftimefreq.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sftimefreq.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius '''))
sftimefreq.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sftimefreq.par('phase',rsf.doc.rsfpar('bool','n','','''output phase instead of amplitude '''))
sftimefreq.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftimefreq.version('1.7')
sftimefreq.synopsis('''sftimefreq < time.rsf > timefreq.rsf mask=mask.rsf nw= dw= w0=0. rect=10 niter=100 phase=n''','''''')
rsf.doc.progs['sftimefreq']=sftimefreq

sftwofreq2 = rsf.doc.rsfprog('sftwofreq2','user/fomels/Mtwofreq2.c','''2-D two spectral component estimation.''')
sftwofreq2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftwofreq2.par('niter',rsf.doc.rsfpar('int','5','','''number of iterations '''))
sftwofreq2.par('eps',rsf.doc.rsfpar('float','1','','''vertical smoothness '''))
sftwofreq2.par('lam',rsf.doc.rsfpar('float','1','','''horizontal smoothness '''))
sftwofreq2.par('p0',rsf.doc.rsfpar('float','1.','','''initial first component '''))
sftwofreq2.par('q0',rsf.doc.rsfpar('float','1.','','''initial first component '''))
sftwofreq2.par('p1',rsf.doc.rsfpar('float','-1.','','''initial second component '''))
sftwofreq2.par('q1',rsf.doc.rsfpar('float','1.','','''initial second component '''))
sftwofreq2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftwofreq2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftwofreq2.version('1.7 Mtwofreq2.c 704 2004-07-13 18:22:06Z fomels')
sftwofreq2.synopsis('''sftwofreq2 < in.rsf > out.rsf mask=mask.rsf niter=5 eps=1 lam=1 p0=1. q0=1. p1=-1. q1=1. verb=n < data.rsf > dip.rsf''','''''')
rsf.doc.progs['sftwofreq2']=sftwofreq2

sfvelcon = rsf.doc.rsfprog('sfvelcon','user/fomels/Mvelcon.c','''Post-stack velocity continuation by implicit finite differences ''')
sfvelcon.par('vel',rsf.doc.rsfpar('float','0.75','','''final velocity '''))
sfvelcon.par('v0',rsf.doc.rsfpar('float','0.','','''starting velocity '''))
sfvelcon.par('nv',rsf.doc.rsfpar('int','n1','','''number of steps '''))
sfvelcon.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfvelcon.par('add',rsf.doc.rsfpar('bool','n','','''addition flag '''))
sfvelcon.par('inv',rsf.doc.rsfpar('int','0','','''amplitude type '''))
sfvelcon.version('1.7')
sfvelcon.synopsis('''sfvelcon < in.rsf > out.rsf vel=0.75 v0=0. nv=n1 adj=n add=n inv=0''','''''')
rsf.doc.progs['sfvelcon']=sfvelcon

sfwarp1 = rsf.doc.rsfprog('sfwarp1','user/fomels/Mwarp1.c','''Multicomponent data registration by 1-D warping. ''')
sfwarp1.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarp1.par('warpout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwarp1.par('amplout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwarp1.par('warpin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarp1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwarp1.par('noamp',rsf.doc.rsfpar('bool','n','','''if y, don't correct amplitudes '''))
sfwarp1.par('accuracy',rsf.doc.rsfpar('int','','[1-4]','''interpolation accuracy '''))
sfwarp1.par('nliter',rsf.doc.rsfpar('int','10','','''number of non-linear iterations '''))
sfwarp1.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of linear iterations '''))
sfwarp1.par('warpin',rsf.doc.rsfpar('string ',desc='''optional initial warp file (auxiliary input file name)'''))
sfwarp1.version('1.7 Mwarp1.c 13985 2015-03-26 13:56:59Z sfomel')
sfwarp1.synopsis('''sfwarp1 < in.rsf > warped.rsf other=other.rsf warpout=warpout.rsf amplout=amplout.rsf warpin=warpin.rsf verb=n noamp=n accuracy= nliter=10 niter=100''','''''')
rsf.doc.progs['sfwarp1']=sfwarp1

sfwarpadd = rsf.doc.rsfprog('sfwarpadd','user/fomels/Mwarpadd.c','''Add a perturbation to the warping function.''')
sfwarpadd.par('add',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpadd.par('accuracy',rsf.doc.rsfpar('int','','','''Interpolation accuracy order '''))
sfwarpadd.par('m1',rsf.doc.rsfpar('int','n1*2','','''Trace pading '''))
sfwarpadd.version('1.7 Mwarpadd.c 7107 2011-04-10 02:04:14Z ivlad')
sfwarpadd.synopsis('''sfwarpadd < in.rsf add=add.rsf > sum.rsf accuracy= m1=n1*2''','''''')
rsf.doc.progs['sfwarpadd']=sfwarpadd

sfwarpscan = rsf.doc.rsfprog('sfwarpscan','user/fomels/Mwarpscan.c','''Multicomponent data registration analysis. ''')
sfwarpscan.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpscan.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfwarpscan.par('ng',rsf.doc.rsfpar('int','1','','''number of gamma values '''))
sfwarpscan.par('g0',rsf.doc.rsfpar('float','','','''gamma origin '''))
sfwarpscan.par('dg',rsf.doc.rsfpar('float','g0','','''gamma sampling '''))
sfwarpscan.par('rect1',rsf.doc.rsfpar('int','1','','''vertical smoothing '''))
sfwarpscan.par('rect2',rsf.doc.rsfpar('int','1','','''gamma smoothing '''))
sfwarpscan.par('rect3',rsf.doc.rsfpar('int','1','','''in-line smoothing '''))
sfwarpscan.par('rect4',rsf.doc.rsfpar('int','1','','''cross-line smoothing '''))
sfwarpscan.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfwarpscan.par('accuracy',rsf.doc.rsfpar('int','','[1-4]','''interpolation accuracy '''))
sfwarpscan.version('1.7 Mwarpscan.c 744 2004-08-17 18:46:07Z fomels')
sfwarpscan.synopsis('''sfwarpscan < in.rsf > warped.rsf other=other.rsf verb=y ng=1 g0= dg=g0 rect1=1 rect2=1 rect3=1 rect4=1 niter=10 accuracy=''','''''')
rsf.doc.progs['sfwarpscan']=sfwarpscan

sfanisolr2 = rsf.doc.rsfprog('sfanisolr2','user/fomels/Manisolr2.cc','''Lowrank decomposition for 2-D anisotropic wave propagation (Real number).''')
sfanisolr2.par('vels',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('xtap',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('ktap',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfanisolr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfanisolr2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfanisolr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfanisolr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfanisolr2.par('approx',rsf.doc.rsfpar('','2','','''Type of approximation (0=exact 1=zone 2=acoustic)'''))
sfanisolr2.par('relation',rsf.doc.rsfpar('','3','','''Type of q relationship (0=shale, 1=sand, 2=carbonate, default being smallest error)'''))
sfanisolr2.par('xtaper',rsf.doc.rsfpar('','false','','''if taper in x'''))
sfanisolr2.par('ktaper',rsf.doc.rsfpar('','false','','''if taper in k'''))
sfanisolr2.version('1.7')
sfanisolr2.synopsis('''sfanisolr2 < velz.rsf vels=vels.rsf fft=fft.rsf xtap=fxtap.rsf ktap=fktap.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt= approx=2 relation=3 xtaper=false ktaper=false''','''''')
rsf.doc.progs['sfanisolr2']=sfanisolr2

sfisolr2 = rsf.doc.rsfprog('sfisolr2','user/fomels/Misolr2.cc','''Lowrank decomposition for 2-D isotropic wave propagation. ''')
sfisolr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr2.version('1.7')
sfisolr2.synopsis('''sfisolr2 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr2']=sfisolr2

sfisolr3 = rsf.doc.rsfprog('sfisolr3','user/fomels/Misolr3.cc','''Lowrank decomposition for 3-D isotropic wave propagation. ''')
sfisolr3.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr3.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr3.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr3.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr3.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr3.version('1.7')
sfisolr3.synopsis('''sfisolr3 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr3']=sfisolr3

sfbyte2jpg = rsf.doc.rsfprog('sfbyte2jpg','user/fomels/_byte2jpg.c','''Convert byte RSF to a JPEG image. ''')
sfbyte2jpg.par('color',rsf.doc.rsfpar('bool','(bool)(3==n1)','',''''''))
sfbyte2jpg.version('1.7')
sfbyte2jpg.synopsis('''sfbyte2jpg < in.rsf color=(bool)(3==n1)''','''''')
rsf.doc.progs['sfbyte2jpg']=sfbyte2jpg

sfjpg2byte = rsf.doc.rsfprog('sfjpg2byte','user/fomels/_jpg2byte.c','''Convert JPEG image to byte RSF. ''')
sfjpg2byte.version('1.7')
sfjpg2byte.synopsis('''sfjpg2byte > out.rsf < file.jpeg ''','''''')
rsf.doc.progs['sfjpg2byte']=sfjpg2byte

sfbyte2tif = rsf.doc.rsfprog('sfbyte2tif','user/fomels/_byte2tif.c','''Convert byte RSF to a TIFF image. ''')
sfbyte2tif.par('color',rsf.doc.rsfpar('bool','(bool)(3==n1)','',''''''))
sfbyte2tif.version('1.7')
sfbyte2tif.synopsis('''sfbyte2tif < in.rsf color=(bool)(3==n1)''','''''')
rsf.doc.progs['sfbyte2tif']=sfbyte2tif

sftif2byte = rsf.doc.rsfprog('sftif2byte','user/fomels/_tif2byte.c','''Convert TIFF image to byte RSF. ''')
sftif2byte.version('1.7')
sftif2byte.synopsis('''sftif2byte > out.rsf < file.tiff ''','''''')
rsf.doc.progs['sftif2byte']=sftif2byte

sfcgi = rsf.doc.rsfprog('sfcgi','user/fomels/Mcgi.py','''A generic CGI script''')
sfcgi.version('1.7')
sfcgi.synopsis('''sfcgi''','''''')
rsf.doc.progs['sfcgi']=sfcgi

sffft = rsf.doc.rsfprog('sffft','user/fomels/Mfft.py','''Fourier transform as a linear operator''')
sffft.version('1.7')
sffft.synopsis('''sffft''','''''')
rsf.doc.progs['sffft']=sffft

sfipick = rsf.doc.rsfprog('sfipick','user/fomels/Mipick.py','''Simple interactive picking''')
sfipick.version('1.7')
sfipick.synopsis('''sfipick''','''''')
rsf.doc.progs['sfipick']=sfipick

sflas2rsf = rsf.doc.rsfprog('sflas2rsf','user/fomels/Mlas2rsf.py','''Convert LAS-2 well logs to RSF''')
sflas2rsf.version('1.7')
sflas2rsf.synopsis('''sflas2rsf''','''''')
rsf.doc.progs['sflas2rsf']=sflas2rsf

sfresults = rsf.doc.rsfprog('sfresults','user/fomels/Mresults.py','''Explore project results''')
sfresults.version('1.7')
sfresults.synopsis('''sfresults''','''''')
rsf.doc.progs['sfresults']=sfresults

sfwxresults = rsf.doc.rsfprog('sfwxresults','user/fomels/Mwxresults.py','''Explore project results''')
sfwxresults.version('1.7')
sfwxresults.synopsis('''sfwxresults''','''''')
rsf.doc.progs['sfwxresults']=sfwxresults

sfzoom = rsf.doc.rsfprog('sfzoom','user/fomels/Mzoom.py','''Show data with zoom''')
sfzoom.version('1.7')
sfzoom.synopsis('''sfzoom''','''''')
rsf.doc.progs['sfzoom']=sfzoom

