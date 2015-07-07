import rsf.doc

sfaddevent = rsf.doc.rsfprog('sfaddevent','user/chen/Maddevent.c','''Add a dispersive event to a seismic profile ''')
sfaddevent.par('wvtype',rsf.doc.rsfpar('int','0','','''0: ricker; 1: sinc; x: not support '''))
sfaddevent.par('w0',rsf.doc.rsfpar('float','35.0','','''central frequency of Ricker wavelet or bandwidth of sinc wavelet '''))
sfaddevent.par('event',rsf.doc.rsfpar('int','2','','''0: linear; 1: parabolic; 2:hyperbolic '''))
sfaddevent.par('nfft',rsf.doc.rsfpar('int','','','''fft length '''))
sfaddevent.par('t0',rsf.doc.rsfpar('float','0.3','','''event travel time at x=0 '''))
sfaddevent.par('v0',rsf.doc.rsfpar('float','1500.0','','''event velocity at x=0, for reference frequency f0 '''))
sfaddevent.par('a0',rsf.doc.rsfpar('float','1.0','','''event amplitude at t=a0ref (x=0) '''))
sfaddevent.par('qv',rsf.doc.rsfpar('float','-1.0','','''Q factor for velocity dispersion '''))
sfaddevent.par('qa',rsf.doc.rsfpar('float','qv','','''Q factor for amplitude attenuation '''))
sfaddevent.par('f0',rsf.doc.rsfpar('float','w0','','''reference frequency for velocity dispersion and amplitude attenuation '''))
sfaddevent.par('a0ref',rsf.doc.rsfpar('int','0','','''reference point for a0: 0 - t0; 1 - a0 '''))
sfaddevent.version('1.7')
sfaddevent.synopsis('''sfaddevent < in.rsf > out.rsf wvtype=0 w0=35.0 event=2 nfft= t0=0.3 v0=1500.0 a0=1.0 qv=-1.0 qa=qv f0=w0 a0ref=0''','''''')
rsf.doc.progs['sfaddevent']=sfaddevent

sfcomp = rsf.doc.rsfprog('sfcomp','user/chen/Mcomp.c','''Compare 2 data set ''')
sfcomp.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcomp.par('mode',rsf.doc.rsfpar('int','0','','''compare method: 
	0 - normalized xcorrelation; 
	1 - mean square error '''))
sfcomp.version('1.7')
sfcomp.synopsis('''sfcomp < in.rsf > out.rsf ref=ref.rsf mode=0''','''''')
rsf.doc.progs['sfcomp']=sfcomp

sfldip = rsf.doc.rsfprog('sfldip','user/chen/Mldip.c','''dip estimation by line interpolating pwd ''')
sfldip.par('idip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfldip.par('m',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sfldip.par('n',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sfldip.par('rect1',rsf.doc.rsfpar('int','0','','''dip smoothness on 1st axis '''))
sfldip.par('rect2',rsf.doc.rsfpar('int','0','','''dip smoothness on 2nd axis '''))
sfldip.par('niter',rsf.doc.rsfpar('int','5','','''number of iterations '''))
sfldip.par('liter',rsf.doc.rsfpar('int','20','','''number of linear iterations '''))
sfldip.par('eta',rsf.doc.rsfpar('float','1.0','','''steps for iteration '''))
sfldip.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfldip.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation method: maxflat lagrange bspline '''))
sfldip.par('idip',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfldip.version('1.7')
sfldip.synopsis('''sfldip < in.rsf > out.rsf idip=p0.rsf m=1 n=1 rect1=0 rect2=0 niter=5 liter=20 eta=1.0 verb=n interp=''','''''')
rsf.doc.progs['sfldip']=sfldip

sflphfreq = rsf.doc.rsfprog('sflphfreq','user/chen/Mlphfreq.c','''frequency response of linear phase approximators ''')
sflphfreq.par('m',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sflphfreq.par('n',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sflphfreq.par('iir',rsf.doc.rsfpar('bool','y','','''y:iir,  n:fir '''))
sflphfreq.par('n1',rsf.doc.rsfpar('int','50','','''samples in frequency domain between (0:f_c] '''))
sflphfreq.par('o2',rsf.doc.rsfpar('float','0.1','','''first phase shift '''))
sflphfreq.par('d2',rsf.doc.rsfpar('float','0.3','','''phase shift increment '''))
sflphfreq.par('n2',rsf.doc.rsfpar('int','1','','''number of phase shift '''))
sflphfreq.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation method: maxflat lagrange bspline '''))
sflphfreq.version('1.7')
sflphfreq.synopsis('''sflphfreq > out.rsf m=1 n=1 iir=y n1=50 o2=0.1 d2=0.3 n2=1 interp=''','''''')
rsf.doc.progs['sflphfreq']=sflphfreq

sfmflt = rsf.doc.rsfprog('sfmflt','user/chen/Mmflt.c','''3D Recursive median filter ''')
sfmflt.par('rect1',rsf.doc.rsfpar('int','1','','''filter length on 1st axis '''))
sfmflt.par('rect2',rsf.doc.rsfpar('int','0','','''filter length on 2nd axis '''))
sfmflt.par('rect3',rsf.doc.rsfpar('int','0','','''filter length on 3nd axis '''))
sfmflt.version('1.7')
sfmflt.synopsis('''sfmflt < in.rsf > out.rsf rect1=1 rect2=0 rect3=0''','''''')
rsf.doc.progs['sfmflt']=sfmflt

sfodip = rsf.doc.rsfprog('sfodip','user/chen/Modip.c','''omnidirectional dip estimation  ''')
sfodip.par('m',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sfodip.par('n',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sfodip.par('rect1',rsf.doc.rsfpar('int','0','','''dip smoothness on 1st axis '''))
sfodip.par('rect2',rsf.doc.rsfpar('int','0','','''dip smoothness on 2nd axis '''))
sfodip.par('niter',rsf.doc.rsfpar('int','5','','''number of iterations '''))
sfodip.par('liter',rsf.doc.rsfpar('int','20','','''number of linear iterations '''))
sfodip.par('radius',rsf.doc.rsfpar('float','1.0','','''interpolating radius for opwd '''))
sfodip.par('eta',rsf.doc.rsfpar('float','0.5','','''steps for iteration '''))
sfodip.par('dip0',rsf.doc.rsfpar('float','0.0','','''starting dip '''))
sfodip.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfodip.par('slope',rsf.doc.rsfpar('bool','n','','''slope (y) or dip (n) estimation '''))
sfodip.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation method: maxflat lagrange bspline '''))
sfodip.version('1.7')
sfodip.synopsis('''sfodip < in.rsf > out.rsf m=1 n=1 rect1=0 rect2=0 niter=5 liter=20 radius=1.0 eta=0.5 dip0=0.0 verb=n slope=n interp=''','''''')
rsf.doc.progs['sfodip']=sfodip

sfpca = rsf.doc.rsfprog('sfpca','user/chen/Mpca.c','''KL transform. ''')
sfpca.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfpca.par('nc',rsf.doc.rsfpar('int','n1','','''number of components [ 0 < nc < n1 ] '''))
sfpca.par('eta',rsf.doc.rsfpar('float','0.9','','''energy ratio for signal subspace [ 0 eta < 1 ]'''))
sfpca.version('1.7')
sfpca.synopsis('''sfpca < in.rsf > out.rsf verb=y nc=n1 eta=0.9''','''''')
rsf.doc.progs['sfpca']=sfpca

sfpscefd = rsf.doc.rsfprog('sfpscefd','user/chen/Mpscefd.c','''EFD phase shift wave extrapolation. ''')
sfpscefd.par('data',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpscefd.par('wave',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpscefd.par('jt',rsf.doc.rsfpar('int','40','','''time step for wave data '''))
sfpscefd.par('nz',rsf.doc.rsfpar('int','nz0','','''depth number '''))
sfpscefd.version('1.7')
sfpscefd.synopsis('''sfpscefd < modl.rsf > imag.rsf data=data.rsf wave=wave.rsf jt=40 nz=nz0''','''''')
rsf.doc.progs['sfpscefd']=sfpscefd

sfpwdfreq = rsf.doc.rsfprog('sfpwdfreq','user/chen/Mpwdfreq.c','''frequency response of PWD operator ''')
sfpwdfreq.par('n1',rsf.doc.rsfpar('int','50','','''samples in frequency domain between (0:f_c] '''))
sfpwdfreq.par('order',rsf.doc.rsfpar('int','1','','''order of PWD '''))
sfpwdfreq.par('o3',rsf.doc.rsfpar('float','20','','''first dip angle '''))
sfpwdfreq.par('d3',rsf.doc.rsfpar('float','30','','''dip angle increment '''))
sfpwdfreq.par('n3',rsf.doc.rsfpar('int','1','','''number dip angle '''))
sfpwdfreq.par('iir',rsf.doc.rsfpar('bool','n','','''y: iir; n: fir '''))
sfpwdfreq.par('opwd',rsf.doc.rsfpar('bool','y','','''y: circle interpolating pwd; n: line interpolating pwd '''))
sfpwdfreq.par('radius',rsf.doc.rsfpar('float','1.0','','''radius for circle interpolating pwd '''))
sfpwdfreq.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation method: maxflat lagrange bspline '''))
sfpwdfreq.version('1.7')
sfpwdfreq.synopsis('''sfpwdfreq > out.rsf n1=50 order=1 o3=20 d3=30 n3=1 iir=n opwd=y radius=1.0 interp=''','''''')
rsf.doc.progs['sfpwdfreq']=sfpwdfreq

sfsignal = rsf.doc.rsfprog('sfsignal','user/chen/Msignal.c','''Generate signal series ''')
sfsignal.par('para',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfsignal.par('n',rsf.doc.rsfpar('int','100','','''length '''))
sfsignal.par('o',rsf.doc.rsfpar('float','0.0','','''original '''))
sfsignal.par('d',rsf.doc.rsfpar('float','0.004','','''interval '''))
sfsignal.par('waveform',rsf.doc.rsfpar('string ',desc='''waveform: ricker,sinc,harmonic,randn,rand '''))
sfsignal.version('1.7')
sfsignal.synopsis('''sfsignal > out.rsf para= n=100 o=0.0 d=0.004 waveform=''','''''')
rsf.doc.progs['sfsignal']=sfsignal

sfwavmod = rsf.doc.rsfprog('sfwavmod','user/chen/Mwavmod.c','''1-2-3D finite difference modeling ''')
sfwavmod.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavmod.par('sgrid',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavmod.par('ggrid',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavmod.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwavmod.par('jt',rsf.doc.rsfpar('int','1','','''time interval in observation system '''))
sfwavmod.par('jtm',rsf.doc.rsfpar('int','100','','''time interval of wave movie '''))
sfwavmod.par('ot',rsf.doc.rsfpar('float','0.0','','''time delay '''))
sfwavmod.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfwavmod.par('wfl',rsf.doc.rsfpar('string ',desc='''wavefield movie file (auxiliary output file name)'''))
sfwavmod.version('1.7')
sfwavmod.synopsis('''sfwavmod < in.rsf vel=vel.rsf sgrid=sgrid.rsf ggrid=ggrid.rsf > dat.rsf wfl=wfl.rsf jt=1 jtm=100 ot=0.0 verb=n''','''''')
rsf.doc.progs['sfwavmod']=sfwavmod

sfshuffle = rsf.doc.rsfprog('sfshuffle','user/chen/Mshuffle.py','''shuffle the data''')
sfshuffle.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfshuffle.par('seed',rsf.doc.rsfpar('int','n2','',''''''))
sfshuffle.par('inv',rsf.doc.rsfpar('bool','n','',''''''))
sfshuffle.version('1.7')
sfshuffle.synopsis('''sfshuffle < pi.rsf > po.rsf axis=2 seed=n2 inv=n''','''''')
rsf.doc.progs['sfshuffle']=sfshuffle

