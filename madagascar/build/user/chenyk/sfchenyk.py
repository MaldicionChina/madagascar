import rsf.doc

sfblend = rsf.doc.rsfprog('sfblend','user/chenyk/Mblend.c','''Seismic blending operator.''')
sfblend.par('verbose',rsf.doc.rsfpar('int','1','','''0 terse, 1 informative, 2 chatty, 3 debug '''))
sfblend.par('shot_time_in',rsf.doc.rsfpar('string ',desc=''''''))
sfblend.par('shot_time_out',rsf.doc.rsfpar('string ',desc=''''''))
sfblend.version('1.7')
sfblend.synopsis('''sfblend < in.rsf > out.rsf verbose=1 shot_time_in= shot_time_out=''',''' Custom program to blend the seismic data.
''')
rsf.doc.progs['sfblend']=sfblend

sfcabs = rsf.doc.rsfprog('sfcabs','user/chenyk/Mcabs.c','''Absolute value complex data. ''')
sfcabs.version('1.7')
sfcabs.synopsis('''sfcabs < fin.rsf > fout.rsf''','''''')
rsf.doc.progs['sfcabs']=sfcabs

sfdiff = rsf.doc.rsfprog('sfdiff','user/chenyk/Mdiff.c','''Compare the difference of two rsf data sets with the same size. ''')
sfdiff.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiff.version('1.7')
sfdiff.synopsis('''sfdiff < inp1.rsf match=inp2.rsf > dif.rsf''','''''')
rsf.doc.progs['sfdiff']=sfdiff

sfemd = rsf.doc.rsfprog('sfemd','user/chenyk/Memd.c','''Empirical Mode Decomposition ''')
sfemd.par('threshold',rsf.doc.rsfpar('float','DEFAULT_THRESHOLD','','''Sifting stoping parameter: threshold, the default is 0.05. '''))
sfemd.par('tolerance',rsf.doc.rsfpar('float','DEFAULT_TOLERANCE','','''Sifting stoping parameter: tolerance, the default is 0.05. '''))
sfemd.par('miter',rsf.doc.rsfpar('int','MAX_ITERATIONS','','''Maximum number of iterations during sifting, the default is 1000. '''))
sfemd.par('mimf',rsf.doc.rsfpar('int','0','','''Maximum number of IMFs, the default is as many as possible. '''))
sfemd.version('1.7')
sfemd.synopsis('''sfemd < inp.rsf > outp.rsf threshold=DEFAULT_THRESHOLD tolerance=DEFAULT_TOLERANCE miter=MAX_ITERATIONS mimf=0''','''''')
rsf.doc.progs['sfemd']=sfemd

sffxdecon = rsf.doc.rsfprog('sffxdecon','user/chenyk/Mfxdecon.c','''Random noise attenuation using f-x deconvolution ''')
sffxdecon.par('verb',rsf.doc.rsfpar('bool','n','','''flag to get advisory messages '''))
sffxdecon.par('taper',rsf.doc.rsfpar('float','.1','','''length of taper '''))
sffxdecon.par('fmin',rsf.doc.rsfpar('float','1.','','''minimum frequency to process in Hz '''))
sffxdecon.par('fmax',rsf.doc.rsfpar('float','1./(2*dt)','','''maximum frequency to process in Hz '''))
sffxdecon.par('twlen',rsf.doc.rsfpar('float','(float)(n1-1)*dt','','''time window length '''))
sffxdecon.par('n2w',rsf.doc.rsfpar('int','10','','''number of traces in window '''))
sffxdecon.par('lenf',rsf.doc.rsfpar('int','4','','''number of traces for filter '''))
sffxdecon.version('1.7')
sffxdecon.synopsis('''sffxdecon < in.rsf > out.rsf verb=n taper=.1 fmin=1. fmax=1./(2*dt) twlen=(float)(n1-1)*dt n2w=10 lenf=4''','''''')
rsf.doc.progs['sffxdecon']=sffxdecon

sflow = rsf.doc.rsfprog('sflow','user/chenyk/Mlow.c','''Calculating local (signal-and-noise) orthogonalization weight (LOW)  ''')
sflow.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflow.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflow.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflow.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflow.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sflow.version('1.7')
sflow.synopsis('''sflow < fnoi.rsf sig=fsig.rsf > flow.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sflow']=sflow

sfprekirch = rsf.doc.rsfprog('sfprekirch','user/chenyk/Mprekirch.c','''2-D Prestack Kirchhoff time migration with antialiasing. ''')
sfprekirch.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfprekirch.par('nz',rsf.doc.rsfpar('int','nt','',''''''))
sfprekirch.par('dz',rsf.doc.rsfpar('float','dt','',''''''))
sfprekirch.par('z0',rsf.doc.rsfpar('float','t0','',''''''))
sfprekirch.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfprekirch.version('1.7')
sfprekirch.synopsis('''sfprekirch < inp.rsf vel=vel.rsf > mig.rsf nz=nt dz=dt z0=t0 antialias=1.0''','''The axes in the input are {time,midpoint,offset}
The axes in the output are {time,midpoint}
''')
rsf.doc.progs['sfprekirch']=sfprekirch

sfsimidenoise = rsf.doc.rsfprog('sfsimidenoise','user/chenyk/Msimidenoise.c','''Random noise attenuation using local similarity ''')
sfsimidenoise.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimidenoise.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfsimidenoise.version('1.7')
sfsimidenoise.synopsis('''sfsimidenoise < in.rsf > out.rsf similarity=simi.rsf thr=''','''''')
rsf.doc.progs['sfsimidenoise']=sfsimidenoise

sfsimidenoise1 = rsf.doc.rsfprog('sfsimidenoise1','user/chenyk/Msimidenoise1.c','''Random noise attenuation using local similarity (different weighting approach) ''')
sfsimidenoise1.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimidenoise1.par('s1',rsf.doc.rsfpar('float','','','''thresholding level 1 '''))
sfsimidenoise1.par('s2',rsf.doc.rsfpar('float','','','''thresholding level 2 '''))
sfsimidenoise1.version('1.7')
sfsimidenoise1.synopsis('''sfsimidenoise1 < in.rsf > out.rsf similarity=simi.rsf s1= s2=''','''The weighting function is defined as
W(s) = 1				if s>s2
	 = (s-s1)/(s2-s1)	if s1<=s<=s2
	 = 0				if s<s1
''')
rsf.doc.progs['sfsimidenoise1']=sfsimidenoise1

sfsnr2 = rsf.doc.rsfprog('sfsnr2','user/chenyk/Msnr2.c','''Compute signal-noise-ratio.''')
sfsnr2.par('noise',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsnr2.version('1.7')
sfsnr2.synopsis('''sfsnr2 < signal.rsf noise=noise.rsf > snrf.rsf''','''SNR=10 log10(sum(clean)/sum(noise))''')
rsf.doc.progs['sfsnr2']=sfsnr2

sfthreshold1 = rsf.doc.rsfprog('sfthreshold1','user/chenyk/Mthreshold1.c','''Soft or hard thresholding using exact-value or percentile thresholding.''')
sfthreshold1.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfthreshold1.par('ifperc',rsf.doc.rsfpar('int','1','','''0, exact-value thresholding; 1, percentile thresholding. '''))
sfthreshold1.par('ifverb',rsf.doc.rsfpar('int','0','','''0, not print threshold value; 1, print threshold value. '''))
sfthreshold1.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfthreshold1.par('type',rsf.doc.rsfpar('string ',desc='''[soft,hard] thresholding type, the default is soft  '''))
sfthreshold1.par('other',rsf.doc.rsfpar('string ',desc='''If output the difference between the thresholded part and the original one (auxiliary output file name)'''))
sfthreshold1.version('1.7')
sfthreshold1.synopsis('''sfthreshold1 < in.rsf > out.rsf other=other.rsf ifperc=1 ifverb=0 thr= type=''','''   When type=soft and ifperc=1, sfthreshold1 is equal to sfthreshold.
''')
rsf.doc.progs['sfthreshold1']=sfthreshold1

sftsmf = rsf.doc.rsfprog('sftsmf','user/chenyk/Mtsmf.c','''Two-step space varying median filtering. ''')
sftsmf.par('L',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftsmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sftsmf.par('ns',rsf.doc.rsfpar('int','0','','''processing window starting point, corresponding to the temporal axis '''))
sftsmf.par('ne',rsf.doc.rsfpar('int','n2-1','','''processing window ending point, corresponding to the temporal axis, n2 means transposed first-axis dimension. '''))
sftsmf.par('N',rsf.doc.rsfpar('int','(f2-f1+1)*n1','','''average energy level (AEL) computing number '''))
sftsmf.par('ael',rsf.doc.rsfpar('float','0.0','','''get the average energy level (AEL) empirically defined '''))
sftsmf.par('verb',rsf.doc.rsfpar('bool','n','','''if print the computed average energy level (AEL) '''))
sftsmf.par('nfw',rsf.doc.rsfpar('int','','','''reference filter-window length (>l4, positive and odd integer)'''))
sftsmf.par('l1',rsf.doc.rsfpar('int','2','','''space-varying window parameter "l1" (default=2)'''))
sftsmf.par('l2',rsf.doc.rsfpar('int','0','','''space-varying window parameter "l2" (default=0)'''))
sftsmf.par('l3',rsf.doc.rsfpar('int','2','','''space-varying window parameter "l3" (default=2)'''))
sftsmf.par('l4',rsf.doc.rsfpar('int','4','','''space-varying window parameter "l4" (default=4)'''))
sftsmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftsmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftsmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftsmf.version('1.7')
sftsmf.synopsis('''sftsmf < in.rsf > out.rsf L=lengthout.rsf boundary=n ns=0 ne=n2-1 N=(f2-f1+1)*n1 ael=0.0 verb=n nfw= l1=2 l2=0 l3=2 l4=4''','''   In default case, sftsmf is equal to sftvmf.
''')
rsf.doc.progs['sftsmf']=sftsmf

sfpyran = rsf.doc.rsfprog('sfpyran','user/chenyk/Mpyran.py','''Add random noise using python.''')
sfpyran.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfpyran.par('range',rsf.doc.rsfpar('float','1','','''noise range (default=1)'''))
sfpyran.par('seed',rsf.doc.rsfpar('int','n2','','''random seed (default=n2)'''))
sfpyran.par('type',rsf.doc.rsfpar('string','y','','''noise type, y: normal, n: uniform'''))
sfpyran.par('mean',rsf.doc.rsfpar('float','0','','''noise mean (default=0)'''))
sfpyran.par('var',rsf.doc.rsfpar('float','1','','''noise variance (default=1)'''))
sfpyran.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise'''))
sfpyran.version('1.7')
sfpyran.synopsis('''sfpyran < pi.rsf > po.rsf axis=2 range=1 seed=n2 type=y mean=0 var=1 rep=n''','''''')
rsf.doc.progs['sfpyran']=sfpyran

