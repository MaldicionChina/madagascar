import rsf.doc

sfapef = rsf.doc.rsfprog('sfapef','user/yliu/Mapef.c','''Estimate adaptive nonstationary PEF on aliased traces. ''')
sfapef.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfapef.par('maskin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfapef.par('maskout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfapef.par('a',rsf.doc.rsfpar('ints','','',''' [ndim]'''))
sfapef.par('jump',rsf.doc.rsfpar('int','2','','''Jump parameter '''))
sfapef.par('dim',rsf.doc.rsfpar('int','mdim','','''number of dimensions '''))
sfapef.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfapef.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfapef.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfapef.par('maskin',rsf.doc.rsfpar('string ',desc='''optional input mask file (auxiliary input file name)'''))
sfapef.par('maskout',rsf.doc.rsfpar('string ',desc='''optional output mask file (auxiliary output file name)'''))
sfapef.version('1.7 Mapef.c 12892 2014-06-26 01:10:04Z sfomel')
sfapef.synopsis('''sfapef < mat.rsf > flt.rsf pred=pre.rsf maskin=maskin.rsf maskout=maskout.rsf a= jump=2 dim=mdim niter=100 verb=n''','''''')
rsf.doc.progs['sfapef']=sfapef

sfdifference = rsf.doc.rsfprog('sfdifference','user/yliu/Mdifference.c','''Difference profile of two data ''')
sfdifference.par('subtracter',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdifference.version('1.7 Mdifference.c 4796 2009-09-29 19:39:07Z ivlad')
sfdifference.synopsis('''sfdifference < in.rsf > out.rsf subtracter=sub.rsf''','''''')
rsf.doc.progs['sfdifference']=sfdifference

sffkoclet = rsf.doc.rsfprog('sffkoclet','user/yliu/Mfkoclet.c','''1-D seislet transform using omega-wavenumber offset continuation ''')
sffkoclet.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sffkoclet.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sffkoclet.par('dwt',rsf.doc.rsfpar('bool','n','','''if y, do wavelet transform '''))
sffkoclet.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffkoclet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sffkoclet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sffkoclet.version('1.7 Mfkoclet.c 9673 2012-12-13 04:51:41Z yang_liu')
sffkoclet.synopsis('''sffkoclet < in.rsf > out.rsf inv=n adj=n dwt=n verb=y eps=0.01 type=''','''Forward transform (adj=n inv=y/n) m=T[d]
Inverse transform (adj=y inv=y)   d=T^(-1)[d]
Adjoint transform (adj=y inv=n)   d=T'[d]
''')
rsf.doc.progs['sffkoclet']=sffkoclet

sffourmis2 = rsf.doc.rsfprog('sffourmis2','user/yliu/Mfourmis2.c','''Missing data interpolation in 2-D using Fourier transform and compressive sensing. ''')
sffourmis2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffourmis2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffourmis2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sffourmis2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffourmis2.par('error',rsf.doc.rsfpar('bool','n','','''error verbosity flag '''))
sffourmis2.par('cut',rsf.doc.rsfpar('bool','n','','''cutting verbosity flag, the default is soft-thresholding '''))
sffourmis2.par('f0',rsf.doc.rsfpar('float','0.','','''initial cutting frequency '''))
sffourmis2.par('k0',rsf.doc.rsfpar('float','0.','','''initial cutting wavenumber '''))
sffourmis2.par('parf',rsf.doc.rsfpar('float','0.','','''Ajustable parameter for frequency window, default is fixed window '''))
sffourmis2.par('parw',rsf.doc.rsfpar('float','0.','','''Ajustable parameter for wavenumber window, default is fixed window '''))
sffourmis2.par('orderf',rsf.doc.rsfpar('float','1.','','''Curve order for frequency window, default is linear '''))
sffourmis2.par('orderw',rsf.doc.rsfpar('float','1.','','''Curve order for frequency window, default is linear '''))
sffourmis2.par('perc',rsf.doc.rsfpar('float','99.','','''percentage for soft-thresholding '''))
sffourmis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding parameter, default is linear '''))
sffourmis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding parameter, default is linear '''))
sffourmis2.par('oper',rsf.doc.rsfpar('string ',desc='''[shaping,pocs,bregman] method, the default is shaping '''))
sffourmis2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.version('1.7 Mfourmis2.c 7291 2011-06-20 05:32:40Z yang_liu')
sffourmis2.synopsis('''sffourmis2 < in.rsf > out.rsf mask=mask.rsf res=res.rsf ref=ref.rsf niter=20 verb=n error=n cut=n f0=0. k0=0. parf=0. parw=0. orderf=1. orderw=1. perc=99. ordert=1. ordert=1. oper=''','''''')
rsf.doc.progs['sffourmis2']=sffourmis2

sffreshape = rsf.doc.rsfprog('sffreshape','user/yliu/Mfreshape.c','''Nonstationary spectral balancing in frequency domain. ''')
sffreshape.par('in2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('ma2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('out2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffreshape.par('dim',rsf.doc.rsfpar('int','1','','''data dimensionality '''))
sffreshape.par('in2',rsf.doc.rsfpar('string ',desc='''optional second input file (auxiliary input file name)'''))
sffreshape.version('1.7 Mfreshape.c 7107 2011-04-10 02:04:14Z ivlad')
sffreshape.synopsis('''sffreshape < in.rsf in2=in2.rsf ma=ma.rsf ma2=ma2.rsf > out.rsf out2=out2.rsf dim=1''','''''')
rsf.doc.progs['sffreshape']=sffreshape

sfltft = rsf.doc.rsfprog('sfltft','user/yliu/Mltft.c','''Local time-frequency transform (LTFT). ''')
sfltft.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfltft.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfltft.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfltft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfltft.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfltft.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sfltft.par('dw',rsf.doc.rsfpar('float','','','''frequency step '''))
sfltft.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sfltft.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius (in time, samples) '''))
sfltft.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sfltft.par('alpha',rsf.doc.rsfpar('float','0.','','''frequency adaptivity '''))
sfltft.par('basis',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfltft.par('mask',rsf.doc.rsfpar('string ',desc='''data weight (auxiliary input file name)'''))
sfltft.par('weight',rsf.doc.rsfpar('string ',desc='''model weight (auxiliary input file name)'''))
sfltft.version('1.7 Mltft.c 12981 2014-07-14 14:28:02Z sfomel')
sfltft.synopsis('''sfltft < in.rsf > out.rsf basis=basis.rsf mask=mask.rsf weight=weight.rsf inv=n verb=n nw= dw= w0=0. rect=10 niter=100 alpha=0.''','''
July 2014 program of the month:
ahay.org/rsflog/index.php?/archives/396-Program-of-the-month-sfltft.html
''')
rsf.doc.progs['sfltft']=sfltft

sflum = rsf.doc.rsfprog('sflum','user/yliu/Mlum.c','''1D LUM filter''')
sflum.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sflum.par('smnclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''smoother tuning parameter (1 <= smnclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflum.par('shnclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''sharpener tuning parameter (1 <= shnclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflum.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflum.version('1.7 Mlum.c 7107 2011-04-10 02:04:14Z ivlad')
sflum.synopsis('''sflum < in.rsf > out.rsf nfw= smnclip=(nfw+1)/2 shnclip=(nfw+1)/2 boundary=n''','''''')
rsf.doc.progs['sflum']=sflum

sfmf = rsf.doc.rsfprog('sfmf','user/yliu/Mmf.c','''1D median filtering. ''')
sfmf.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmf.version('1.7 Mmf.c 13867 2015-03-03 00:18:28Z sfomel')
sfmf.synopsis('''sfmf < in.rsf > out.rsf nfw= boundary=n''','''
January 2015 program of the month:
http://ahay.org/rsflog/index.php?/archives/425-Program-of-the-month-sfmf.html
''')
rsf.doc.progs['sfmf']=sfmf

sfmig2 = rsf.doc.rsfprog('sfmig2','user/yliu/Mmig2.c','''2-D Prestack Kirchhoff time migration with antialiasing. ''')
sfmig2.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig2.par('gather',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmig2.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig2.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfmig2.par('apt',rsf.doc.rsfpar('int','nx','','''integral aperture '''))
sfmig2.par('angle',rsf.doc.rsfpar('float','90.0','','''angle aperture '''))
sfmig2.par('half',rsf.doc.rsfpar('bool','y','','''if y, the third axis is half-offset instead of full offset '''))
sfmig2.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfmig2.par('rho',rsf.doc.rsfpar('float','1.-1./nt','','''Leaky integration constant '''))
sfmig2.par('gather',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfmig2.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmig2.version('1.7 Mmig2.c 13985 2015-03-26 13:56:59Z sfomel')
sfmig2.synopsis('''sfmig2 < inp.rsf vel=vel.rsf > mig.rsf gather=gather.rsf offset=offset.rsf antialias=1.0 apt=nx angle=90.0 half=y verb=y rho=1.-1./nt''','''The axes in the input are {time,midpoint,offset}
The axes in the offset are {1,midpoint,offset}
The axes in the output are {time,midpoint}
The axes in the "image gather" are {time,midpoint,offset}
''')
rsf.doc.progs['sfmig2']=sfmig2

sfmiss4 = rsf.doc.rsfprog('sfmiss4','user/yliu/Mmiss4.c','''Missing data interpolation with adaptive PEFs. ''')
sfmiss4.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss4.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss4.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss4.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfmiss4.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfmiss4.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmiss4.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss4.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss4.version('1.7 Mmiss4.c 7107 2011-04-10 02:04:14Z ivlad')
sfmiss4.synopsis('''sfmiss4 < in.rsf filt=fil.rsf > out.rsf mask=mask.rsf niter=100 exact=y eps=0. verb=n''','''''')
rsf.doc.progs['sfmiss4']=sfmiss4

sfmiss43 = rsf.doc.rsfprog('sfmiss43','user/yliu/Mmiss43.c','''3-D missing data interpolation with adaptive PEFs. ''')
sfmiss43.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss43.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss43.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss43.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfmiss43.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfmiss43.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmiss43.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss43.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss43.version('1.7 Mmiss43.c 7107 2011-04-10 02:04:14Z ivlad')
sfmiss43.synopsis('''sfmiss43 < in.rsf filt=fil.rsf > out.rsf mask=mask.rsf niter=100 exact=y eps=0. verb=n''','''''')
rsf.doc.progs['sfmiss43']=sfmiss43

sfsaltpepper = rsf.doc.rsfprog('sfsaltpepper','user/yliu/Msaltpepper.c','''Add salt and pepper noise to the data.''')
sfsaltpepper.par('den',rsf.doc.rsfpar('float','10.','','''noise density (percent, default=10, Min=0, Max=100) '''))
sfsaltpepper.par('inten',rsf.doc.rsfpar('float','0.1','','''noise intensity (multiple peak value of data, default=0.1) '''))
sfsaltpepper.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfsaltpepper.par('allpos',rsf.doc.rsfpar('bool','n','','''if y, assume positive noise '''))
sfsaltpepper.par('noise',rsf.doc.rsfpar('bool','n','','''if y, output noise only '''))
sfsaltpepper.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfsaltpepper.version('1.7 Msaltpepper.c 7107 2011-04-10 02:04:14Z ivlad')
sfsaltpepper.synopsis('''sfsaltpepper < in.rsf > out.rsf den=10. inten=0.1 rep=n allpos=n noise=n seed=time(NULL)''','''''')
rsf.doc.progs['sfsaltpepper']=sfsaltpepper

sfst = rsf.doc.rsfprog('sfst','user/yliu/Mst.c','''S transform ''')
sfst.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfst.par('flo',rsf.doc.rsfpar('float','','','''Low frequency in band, default is 0 '''))
sfst.par('fhi',rsf.doc.rsfpar('float','','','''High frequency in band, default is Nyquist '''))
sfst.version('1.7 Mst.c 8858 2012-07-23 16:33:06Z saragiotis')
sfst.synopsis('''sfst < in.rsf > out.rsf inv=n flo= fhi=''','''''')
rsf.doc.progs['sfst']=sfst

sfstft = rsf.doc.rsfprog('sfstft','user/yliu/Mstft.c','''Short-time Fourier transform (STFT). ''')
sfstft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse transform '''))
sfstft.par('sym',rsf.doc.rsfpar('bool','n','','''if y, apply symmetric scaling to make the FFT operator Hermitian '''))
sfstft.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfstft.par('ntw',rsf.doc.rsfpar('int','7','','''time-window length '''))
sfstft.version('1.7 Mstft.c 7202 2011-05-03 02:13:48Z yang_liu')
sfstft.synopsis('''sfstft < in.rsf > out.rsf inv=n sym=n opt=y ntw=7''','''''')
rsf.doc.progs['sfstft']=sfstft

sfthreshold2 = rsf.doc.rsfprog('sfthreshold2','user/yliu/Mthreshold2.c','''2-D Soft thresholding. ''')
sfthreshold2.par('thr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthreshold2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfthreshold2.par('pclip',rsf.doc.rsfpar('float','99.','',''''''))
sfthreshold2.par('thr',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfthreshold2.version('1.7 Mthreshold2.c 13869 2015-03-03 03:58:51Z zhiguang0810')
sfthreshold2.synopsis('''sfthreshold2 < in.rsf > out.rsf thr=thr.rsf verb=n pclip=99.''','''''')
rsf.doc.progs['sfthreshold2']=sfthreshold2

sftvmf = rsf.doc.rsfprog('sftvmf','user/yliu/Mtvmf.c','''1D Time-varying median filtering. ''')
sftvmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sftvmf.par('nfw',rsf.doc.rsfpar('int','','','''reference filter-window length (>delta, positive and odd integer)'''))
sftvmf.par('alpha',rsf.doc.rsfpar('int','2','','''time-varying window parameter "alpha" (default=2)'''))
sftvmf.par('beta',rsf.doc.rsfpar('int','0','','''time-varying window parameter "beta" (default=0)'''))
sftvmf.par('gamma',rsf.doc.rsfpar('int','2','','''time-varying window parameter "gamma" (default=2)'''))
sftvmf.par('delta',rsf.doc.rsfpar('int','4','','''time-varying window parameter "delta" (default=4)'''))
sftvmf.version('1.7')
sftvmf.synopsis('''sftvmf < in.rsf > out.rsf boundary=n nfw= alpha=2 beta=0 gamma=2 delta=4''','''''')
rsf.doc.progs['sftvmf']=sftvmf

sftxrna2 = rsf.doc.rsfprog('sftxrna2','user/yliu/Mtxrna2.c','''2D space-noncausal t-x nonstationary regularized autoregression. ''')
sftxrna2.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna2.version('1.7 Mtxrna2.c 11561 2014-01-05 05:16:51Z yang_liu')
sftxrna2.synopsis('''sftxrna2 < mat.rsf > pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna2']=sftxrna2

sftxrna3 = rsf.doc.rsfprog('sftxrna3','user/yliu/Mtxrna3.c','''3D space-noncausal t-x-y nonstationary regularized autoregression. ''')
sftxrna3.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna3.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna3.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna3.version('1.7 Mtxrna3.c 11561 2014-01-05 05:16:51Z yang_liu')
sftxrna3.synopsis('''sftxrna3 < mat.rsf > pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna3']=sftxrna3

