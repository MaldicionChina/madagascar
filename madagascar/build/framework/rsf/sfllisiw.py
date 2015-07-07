import rsf.doc

sfdsreiko = rsf.doc.rsfprog('sfdsreiko','user/llisiw/Mdsreiko.c','''Double square-root eikonal solver (2D) ''')
sfdsreiko.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsreiko.par('flag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdsreiko.par('alpha',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdsreiko.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfdsreiko.par('thres',rsf.doc.rsfpar('float','5.e-5','','''threshold (percentage) '''))
sfdsreiko.par('tol',rsf.doc.rsfpar('float','1.e-3','','''tolerance for bisection root-search '''))
sfdsreiko.par('nloop',rsf.doc.rsfpar('int','10','','''number of bisection root-search '''))
sfdsreiko.par('causal',rsf.doc.rsfpar('bool','y','','''if y, neglect non-causal branches of DSR '''))
sfdsreiko.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsreiko.par('flag',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfdsreiko.par('alpha',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfdsreiko.version('1.7')
sfdsreiko.synopsis('''sfdsreiko < in.rsf > out.rsf mask=mask.rsf flag=flag.rsf alpha=alpha.rsf velocity=y thres=5.e-5 tol=1.e-3 nloop=10 causal=y''','''''')
rsf.doc.progs['sfdsreiko']=sfdsreiko

sfdsreiko0 = rsf.doc.rsfprog('sfdsreiko0','user/llisiw/Mdsreiko0.c','''Double square-root eikonal solver (2D + explicit) ''')
sfdsreiko0.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfdsreiko0.version('1.7')
sfdsreiko0.synopsis('''sfdsreiko0 < in.rsf > out.rsf velocity=y''','''''')
rsf.doc.progs['sfdsreiko0']=sfdsreiko0

sfdsrtomo = rsf.doc.rsfprog('sfdsrtomo','user/llisiw/Mdsrtomo.c','''Prestack first-arrival traveltime tomography (DSR) ''')
sfdsrtomo.par('grad',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsrtomo.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsrtomo.par('flag',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsrtomo.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsrtomo.par('prec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsrtomo.par('reco',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsrtomo.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag (for what=linear) '''))
sfdsrtomo.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness-squared '''))
sfdsrtomo.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness-squared '''))
sfdsrtomo.par('shape',rsf.doc.rsfpar('bool','n','','''shaping regularization (default no) '''))
sfdsrtomo.par('scale',rsf.doc.rsfpar('bool','n','','''if y, scale gradient before line-search '''))
sfdsrtomo.par('scale0',rsf.doc.rsfpar('float','0.5','','''gradient scale max ratio (if scale=y) '''))
sfdsrtomo.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdsrtomo.par('niter',rsf.doc.rsfpar('int','5','','''number of inversion iterations '''))
sfdsrtomo.par('cgiter',rsf.doc.rsfpar('int','10','','''number of conjugate-gradient iterations '''))
sfdsrtomo.par('liter',rsf.doc.rsfpar('int','5','','''number of line-search iterations '''))
sfdsrtomo.par('thres',rsf.doc.rsfpar('float','5.e-5','','''threshold (percentage) '''))
sfdsrtomo.par('tol',rsf.doc.rsfpar('float','1.e-3','','''tolerance for bisection root-search '''))
sfdsrtomo.par('nloop',rsf.doc.rsfpar('int','10','','''number of bisection root-search '''))
sfdsrtomo.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfdsrtomo.par('causal',rsf.doc.rsfpar('bool','y','','''if y, neglect non-causal branches of DSR '''))
sfdsrtomo.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdsrtomo.par('what',rsf.doc.rsfpar('string ',desc='''what to compute (default tomography) '''))
sfdsrtomo.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('flag',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('prec',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('reco',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('prec',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsrtomo.version('1.7')
sfdsrtomo.synopsis('''sfdsrtomo < in.rsf > out.rsf grad=grad.rsf time=time.rsf flag=flag.rsf mask=mask.rsf prec=prec.rsf reco=reco.rsf adj=n velocity=y velocity=y shape=n scale=n scale0=0.5 verb=n niter=5 cgiter=10 liter=5 thres=5.e-5 tol=1.e-3 nloop=10 eps=0. causal=y rect#=(1,1,...) what=''','''''')
rsf.doc.progs['sfdsrtomo']=sfdsrtomo

sfeikods = rsf.doc.rsfprog('sfeikods','user/llisiw/Meikods.c','''Fast marching with source perturbation. ''')
sfeikods.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeikods.par('tdl1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfeikods.par('tds1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfeikods.par('tdl2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfeikods.par('tds2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfeikods.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfeikods.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfeikods.par('sweep',rsf.doc.rsfpar('bool','n','','''if y, use fast sweeping instead of fast marching '''))
sfeikods.par('br1',rsf.doc.rsfpar('float','d1','',''''''))
sfeikods.par('br2',rsf.doc.rsfpar('float','d2','',''''''))
sfeikods.par('br3',rsf.doc.rsfpar('float','d3','','''Constant-velocity box around the source (in physical dimensions) '''))
sfeikods.par('plane1',rsf.doc.rsfpar('bool','n','',''''''))
sfeikods.par('plane2',rsf.doc.rsfpar('bool','n','',''''''))
sfeikods.par('plane3',rsf.doc.rsfpar('bool','n','','''plane-wave source '''))
sfeikods.par('b1',rsf.doc.rsfpar('int','plane[2]? n1: (int) (br1/d1+0.5)','',''''''))
sfeikods.par('b2',rsf.doc.rsfpar('int','plane[1]? n2: (int) (br2/d2+0.5)','',''''''))
sfeikods.par('b3',rsf.doc.rsfpar('int','plane[0]? n3: (int) (br3/d3+0.5)','','''Constant-velocity box around the source (in samples) '''))
sfeikods.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikods.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikods.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikods.par('l',rsf.doc.rsfpar('int','1','','''source perturbation direction '''))
sfeikods.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)'''))
sfeikods.par('tdl1',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfeikods.par('tds1',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfeikods.par('tdl2',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfeikods.par('tds2',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfeikods.version('1.7 Meikonal.c 7107 2011-04-10 02:04:14Z ivlad')
sfeikods.synopsis('''sfeikods < vel.rsf > time.rsf shotfile=shots.rsf tdl1=tdl1.rsf tds1=tds1.rsf tdl2=tdl2.rsf tds2=tds2.rsf vel=y order=2 sweep=n br1=d1 br2=d2 br3=d3 plane1=n plane2=n plane3=n b1=plane[2]? n1: (int) (br1/d1+0.5) b2=plane[1]? n2: (int) (br2/d2+0.5) b3=plane[0]? n3: (int) (br3/d3+0.5) zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3 l=1''','''''')
rsf.doc.progs['sfeikods']=sfeikods

sffatomoomp = rsf.doc.rsfprog('sffatomoomp','user/llisiw/Mfatomoomp.c','''First-arrival Traveltime Tomography (OMP) ''')
sffatomoomp.par('shot',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffatomoomp.par('recv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffatomoomp.par('reco',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffatomoomp.par('topo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffatomoomp.par('prec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffatomoomp.par('grad',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffatomoomp.par('rayd',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffatomoomp.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffatomoomp.par('misnorm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffatomoomp.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sffatomoomp.par('shape',rsf.doc.rsfpar('bool','n','','''regularization (default Tikhnov) '''))
sffatomoomp.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffatomoomp.par('order',rsf.doc.rsfpar('int','2','','''fast marching accuracy order '''))
sffatomoomp.par('seg',rsf.doc.rsfpar('int','3','','''maximum number of segments of topography '''))
sffatomoomp.par('niter',rsf.doc.rsfpar('int','1','','''number of slowness inversion iterations '''))
sffatomoomp.par('stiter',rsf.doc.rsfpar('int','100','','''number of inner CG iterations (for both Ticknov and Shaping) '''))
sffatomoomp.par('nstep',rsf.doc.rsfpar('int','10','','''number of linesearch '''))
sffatomoomp.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter (for both Ticknov and Shaping) '''))
sffatomoomp.par('weight',rsf.doc.rsfpar('bool','n','','''data weighting '''))
sffatomoomp.par('pow',rsf.doc.rsfpar('float','2.','','''power raised for data weighting '''))
sffatomoomp.par('tol',rsf.doc.rsfpar('float','1.e-6','','''tolerance for shaping regularization '''))
sffatomoomp.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sffatomoomp.par('what',rsf.doc.rsfpar('string ',desc='''what to compute (default tomography) '''))
sffatomoomp.par('shot',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffatomoomp.par('recv',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffatomoomp.par('reco',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffatomoomp.par('topo',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffatomoomp.par('prec',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffatomoomp.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffatomoomp.par('rayd',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffatomoomp.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffatomoomp.par('misnorm',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffatomoomp.version('1.7')
sffatomoomp.synopsis('''sffatomoomp < sinp.rsf > sout.rsf shot=shot.rsf recv=recv.rsf reco=reco.rsf topo=topo.rsf prec=prec.rsf grad=grad.rsf rayd=rayd.rsf time=time.rsf misnorm=norm.rsf velocity=y shape=n verb=n order=2 seg=3 niter=1 stiter=100 nstep=10 eps=0. weight=n pow=2. tol=1.e-6 rect#=(1,1,...) what=''','''''')
rsf.doc.progs['sffatomoomp']=sffatomoomp

sfftoper = rsf.doc.rsfprog('sfftoper','user/llisiw/Mftoper.c','''First-arrival Traveltime Tomography (linear operator) ''')
sfftoper.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfftoper.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfftoper.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfftoper.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfftoper.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfftoper.version('1.7')
sfftoper.synopsis('''sfftoper < in.rsf > out.rsf time=time.rsf mask=mask.rsf adj=n''','''''')
rsf.doc.progs['sfftoper']=sfftoper

sfirays = rsf.doc.rsfprog('sfirays','user/llisiw/Mirays.c','''Fast marching for image rays ''')
sfirays.par('t0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfirays.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfirays.par('f0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfirays.par('velocity',rsf.doc.rsfpar('bool','y','','''y, inputs are velocity / n, slowness-squared '''))
sfirays.par('order',rsf.doc.rsfpar('int','1','','''fastmarching accuracy order '''))
sfirays.par('thres',rsf.doc.rsfpar('float','10.','','''thresholding for caustics '''))
sfirays.par('t0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfirays.par('x0',rsf.doc.rsfpar('string ',desc='''output upwind neighbor (auxiliary output file name)'''))
sfirays.par('f0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfirays.version('1.7')
sfirays.synopsis('''sfirays < in.rsf > out.rsf t0=ot0.rsf x0=ox0.rsf f0=of0.rsf velocity=y order=1 thres=10.''','''''')
rsf.doc.progs['sfirays']=sfirays

sfkirdatsr = rsf.doc.rsfprog('sfkirdatsr','user/llisiw/Mkirdatsr.c','''2-D Pre-stack Kirchhoff redatuming. ''')
sfkirdatsr.par('sgreen',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirdatsr.par('rgreen',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirdatsr.par('interm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkirdatsr.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkirdatsr.par('sdatum',rsf.doc.rsfpar('float','','','''source datum depth '''))
sfkirdatsr.par('rdatum',rsf.doc.rsfpar('float','','','''receiver datum depth '''))
sfkirdatsr.par('aperture',rsf.doc.rsfpar('int','50','','''aperture (number of traces) '''))
sfkirdatsr.par('taper',rsf.doc.rsfpar('int','10','','''taper (number of traces) '''))
sfkirdatsr.par('length',rsf.doc.rsfpar('float','0.025','','''filter length (in seconds) '''))
sfkirdatsr.par('interm',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfkirdatsr.version('1.7')
sfkirdatsr.synopsis('''sfkirdatsr < in.rsf > out.rsf sgreen=sgreen.rsf rgreen=rgreen.rsf interm=interm.rsf verb=n sdatum= rdatum= aperture=50 taper=10 length=0.025''','''''')
rsf.doc.progs['sfkirdatsr']=sfkirdatsr

sfkirmig0 = rsf.doc.rsfprog('sfkirmig0','user/llisiw/Mkirmig0.c','''2-D Post-stack Kirchhoff depth migration. ''')
sfkirmig0.par('table',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmig0.par('deriv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmig0.par('adj',rsf.doc.rsfpar('bool','y','','''y for migration, n for modeling '''))
sfkirmig0.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfkirmig0.par('ns',rsf.doc.rsfpar('int','','','''midpoint samples '''))
sfkirmig0.par('t0',rsf.doc.rsfpar('float','0.0','','''time origin '''))
sfkirmig0.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfkirmig0.par('s0',rsf.doc.rsfpar('float','0.0','','''midpoint origin '''))
sfkirmig0.par('ds',rsf.doc.rsfpar('float','','','''midpoint sampling '''))
sfkirmig0.par('aperture',rsf.doc.rsfpar('float','90.','','''migration aperture (in degree) '''))
sfkirmig0.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfkirmig0.par('type',rsf.doc.rsfpar('string ',desc='''type of interpolation (default Hermit) '''))
sfkirmig0.version('1.7')
sfkirmig0.synopsis('''sfkirmig0 < dat.rsf > mig.rsf table=tbl.rsf deriv=der.rsf adj=y nt= ns= t0=0.0 dt= s0=0.0 ds= aperture=90. antialias=1.0 type=''','''''')
rsf.doc.progs['sfkirmig0']=sfkirmig0

sfkirmigsr = rsf.doc.rsfprog('sfkirmigsr','user/llisiw/Mkirmigsr.c','''2-D Prestack Kirchhoff depth migration. ''')
sfkirmigsr.par('stable',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmigsr.par('sderiv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmigsr.par('rtable',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmigsr.par('rderiv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmigsr.par('adj',rsf.doc.rsfpar('bool','y','','''y for migration, n for modeling '''))
sfkirmigsr.par('cmp',rsf.doc.rsfpar('bool','y','','''y for CMP gather, n for shot gather '''))
sfkirmigsr.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfkirmigsr.par('nh',rsf.doc.rsfpar('int','1','','''offset samples '''))
sfkirmigsr.par('ns',rsf.doc.rsfpar('int','1','','''shot samples '''))
sfkirmigsr.par('t0',rsf.doc.rsfpar('float','0.0','','''time origin '''))
sfkirmigsr.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfkirmigsr.par('h0',rsf.doc.rsfpar('float','0.0','','''offset origin '''))
sfkirmigsr.par('dh',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfkirmigsr.par('s0',rsf.doc.rsfpar('float','0.0','','''shot origin '''))
sfkirmigsr.par('ds',rsf.doc.rsfpar('float','','','''shot sampling '''))
sfkirmigsr.par('tau',rsf.doc.rsfpar('float','0.','','''static time-shift (in second) '''))
sfkirmigsr.par('aperture',rsf.doc.rsfpar('float','90.','','''migration aperture (in degree) '''))
sfkirmigsr.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfkirmigsr.par('cig',rsf.doc.rsfpar('bool','n','','''y - output common offset gathers '''))
sfkirmigsr.par('type',rsf.doc.rsfpar('string ',desc='''type of interpolation (default Hermit) '''))
sfkirmigsr.version('1.7')
sfkirmigsr.synopsis('''sfkirmigsr < dat.rsf > mig.rsf stable=stim.rsf sderiv=sder.rsf rtable=rtim.rsf rderiv=rder.rsf adj=y cmp=y nt= nh=1 ns=1 t0=0.0 dt= h0=0.0 dh= s0=0.0 ds= tau=0. aperture=90. antialias=1.0 cig=n type=''','''''')
rsf.doc.progs['sfkirmigsr']=sfkirmigsr

sflineiko = rsf.doc.rsfprog('sflineiko','user/llisiw/Mlineiko.c','''Iterative solution of the linearized eikonal equation. ''')
sflineiko.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('squared',rsf.doc.rsfpar('bool','y','','''if slowness is squared '''))
sflineiko.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag (for what=linear) '''))
sflineiko.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag (for what=linear) '''))
sflineiko.par('niter',rsf.doc.rsfpar('int','1','','''maximum number of iterations '''))
sflineiko.par('tol',rsf.doc.rsfpar('float','0.001','','''tolerance for convergence '''))
sflineiko.par('what',rsf.doc.rsfpar('string ',desc='''what to compute '''))
sflineiko.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.version('1.7')
sflineiko.synopsis('''sflineiko < time.rsf > dtime.rsf time=time0.rsf slow=slow.rsf mask=mask.rsf squared=y adj=n inv=n niter=1 tol=0.001 what=''','''''')
rsf.doc.progs['sflineiko']=sflineiko

sfmkrcv = rsf.doc.rsfprog('sfmkrcv','user/llisiw/Mmkrcv.c','''Make topography mask / receiver list / record list for first-arrival traveltime tomography ''')
sfmkrcv.par('reco',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmkrcv.par('shot',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmkrcv.par('topo',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmkrcv.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmkrcv.par('air',rsf.doc.rsfpar('float','0.5','','''air velocity for thresholding topography '''))
sfmkrcv.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfmkrcv.par('order',rsf.doc.rsfpar('int','2','','''fast marching accuracy order '''))
sfmkrcv.par('fix',rsf.doc.rsfpar('bool','n','','''if y, fixed-spread; n, moving acquisition '''))
sfmkrcv.par('plane',rsf.doc.rsfpar('bool','n','','''if y, plane-wave source; n, point source '''))
sfmkrcv.par('offset1',rsf.doc.rsfpar('int','0','','''receiver offset inline '''))
sfmkrcv.par('offset2',rsf.doc.rsfpar('int','0','','''receiver offset crossline '''))
sfmkrcv.par('np',rsf.doc.rsfpar('int','1','','''ray-parameter number '''))
sfmkrcv.par('p0',rsf.doc.rsfpar('float','0.','','''ray-parameter start '''))
sfmkrcv.par('dp',rsf.doc.rsfpar('float','1.','','''ray-parameter increment '''))
sfmkrcv.par('shot',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmkrcv.par('topo',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfmkrcv.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfmkrcv.version('1.7')
sfmkrcv.synopsis('''sfmkrcv < in.rsf > out.rsf reco=reco.rsf shot=shot.rsf topo=topo.rsf time=time.rsf air=0.5 velocity=y order=2 fix=n plane=n offset1=0 offset2=0 np=1 p0=0. dp=1.''','''''')
rsf.doc.progs['sfmkrcv']=sfmkrcv

sft2diter = rsf.doc.rsfprog('sft2diter','user/llisiw/Mt2diter.c','''Time-to-depth conversion (linear operator) ''')
sft2diter.par('s0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('t0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('f0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('prec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('dix',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sft2diter.par('velocity',rsf.doc.rsfpar('bool','y','','''y, inputs are velocity / n, slowness-squared '''))
sft2diter.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sft2diter.par('shape',rsf.doc.rsfpar('bool','n','','''regularization (default Tikhnov) '''))
sft2diter.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sft2diter.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sft2diter.par('tol',rsf.doc.rsfpar('float','1.e-6','','''tolerance for shaping regularization '''))
sft2diter.par('cgiter',rsf.doc.rsfpar('int','200','','''number of CG iterations '''))
sft2diter.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sft2diter.par('what',rsf.doc.rsfpar('string ',desc='''what to compute (default inversion) '''))
sft2diter.par('s0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.par('t0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.par('x0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.par('f0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.par('prec',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.par('dix',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sft2diter.version('1.7')
sft2diter.synopsis('''sft2diter < in.rsf > out.rsf s0=is0.rsf t0=it0.rsf x0=ix0.rsf f0=if0.rsf mask=mask.rsf prec=prec.rsf dix=dix.rsf velocity=y adj=n shape=n eps=0.1 verb=n tol=1.e-6 cgiter=200 rect#=(1,1,...) what=''','''''')
rsf.doc.progs['sft2diter']=sft2diter

sftdconvert = rsf.doc.rsfprog('sftdconvert','user/llisiw/Mtdconvert.c','''Iterative time-to-depth velocity conversion ''')
sftdconvert.par('dix',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftdconvert.par('t0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftdconvert.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftdconvert.par('f0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftdconvert.par('grad',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftdconvert.par('cost',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftdconvert.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftdconvert.par('prec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftdconvert.par('velocity',rsf.doc.rsfpar('bool','y','','''y, input is velocity / n, slowness-squared '''))
sftdconvert.par('order',rsf.doc.rsfpar('int','1','','''fastmarch accuracy order '''))
sftdconvert.par('thres',rsf.doc.rsfpar('float','10.','','''thresholding for caustics '''))
sftdconvert.par('niter',rsf.doc.rsfpar('int','1','','''number of nonlinear updates '''))
sftdconvert.par('cgiter',rsf.doc.rsfpar('int','200','','''number of CG iterations '''))
sftdconvert.par('shape',rsf.doc.rsfpar('bool','n','','''regularization (default Tikhnov) '''))
sftdconvert.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sftdconvert.par('nline',rsf.doc.rsfpar('int','0','','''maximum number of line search (default turned-off) '''))
sftdconvert.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftdconvert.par('tol',rsf.doc.rsfpar('float','1.e-6','','''tolerance for shaping regularization '''))
sftdconvert.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sftdconvert.par('dix',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftdconvert.par('t0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftdconvert.par('x0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftdconvert.par('f0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftdconvert.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftdconvert.par('cost',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftdconvert.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftdconvert.par('mval',rsf.doc.rsfpar('string ',desc=''''''))
sftdconvert.par('prec',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftdconvert.version('1.7')
sftdconvert.synopsis('''sftdconvert < in.rsf > out.rsf dix=dix.rsf t0=t_0.rsf x0=x_0.rsf f0=f_0.rsf grad=grad.rsf cost=cost.rsf mask=mini.rsf prec=prec.rsf velocity=y order=1 thres=10. niter=1 cgiter=200 shape=n eps=0.1 nline=0 verb=n tol=1.e-6 rect#=(1,1,...) mval=''','''''')
rsf.doc.progs['sftdconvert']=sftdconvert

sftinterp = rsf.doc.rsfprog('sftinterp','user/llisiw/Mtinterp.c','''Traveltime interpolation by cubic Hermite spline ''')
sftinterp.par('deriv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftinterp.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftinterp.par('type',rsf.doc.rsfpar('string ',desc='''type of interpolation (default Hermit) '''))
sftinterp.par('deriv',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftinterp.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftinterp.version('1.7')
sftinterp.synopsis('''sftinterp < in.rsf > out.rsf deriv=deriv.rsf pattern=pattern.rsf type=''','''''')
rsf.doc.progs['sftinterp']=sftinterp

