import rsf.doc

sfagc = rsf.doc.rsfprog('sfagc','system/generic/Magc.c','''Automatic gain control. ''')
sfagc.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfagc.par('rect#',rsf.doc.rsfpar('int','(125,1,1,...)','','''smoothing radius on #-th axis '''))
sfagc.version('1.7')
sfagc.synopsis('''sfagc < in.rsf > out.rsf repeat=1 rect#=(125,1,1,...)''','''
October 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/271-Program-of-the-month-sfagc.html
''')
rsf.doc.progs['sfagc']=sfagc

sfaliasp = rsf.doc.rsfprog('sfaliasp','system/generic/Maliasp.c','''Aliasing test. ''')
sfaliasp.par('n1',rsf.doc.rsfpar('int','600','',''''''))
sfaliasp.par('n2',rsf.doc.rsfpar('int','24','','''dimensions '''))
sfaliasp.par('cycles',rsf.doc.rsfpar('float','10.','','''wave frequency '''))
sfaliasp.par('ix0',rsf.doc.rsfpar('int','0','','''central trace '''))
sfaliasp.par('slow',rsf.doc.rsfpar('float','0.1','','''slowness '''))
sfaliasp.version('1.7')
sfaliasp.synopsis('''sfaliasp > out.rsf n1=600 n2=24 cycles=10. ix0=0 slow=0.1''','''''')
rsf.doc.progs['sfaliasp']=sfaliasp

sfbandpass = rsf.doc.rsfprog('sfbandpass','system/generic/Mbandpass.c','''Bandpass filtering. ''')
sfbandpass.par('flo',rsf.doc.rsfpar('float','','','''Low frequency in band, default is 0 '''))
sfbandpass.par('fhi',rsf.doc.rsfpar('float','','','''High frequency in band, default is Nyquist '''))
sfbandpass.par('phase',rsf.doc.rsfpar('bool','n','','''y: minimum phase, n: zero phase '''))
sfbandpass.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfbandpass.par('nplo',rsf.doc.rsfpar('int','6','','''number of poles for low cutoff '''))
sfbandpass.par('nphi',rsf.doc.rsfpar('int','6','','''number of poles for high cutoff '''))
sfbandpass.version('1.7')
sfbandpass.synopsis('''sfbandpass < in.rsf > out.rsf flo= fhi= phase=n verb=n nplo=6 nphi=6''','''
November 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/313-Program-of-the-month-sfbandpass.html
''')
rsf.doc.progs['sfbandpass']=sfbandpass

sfbin = rsf.doc.rsfprog('sfbin','system/generic/Mbin.c','''Data binning in 2-D slices. ''')
sfbin.par('fold',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbin.par('xkey',rsf.doc.rsfpar('int','0','','''x key number '''))
sfbin.par('ykey',rsf.doc.rsfpar('int','1','','''y key number '''))
sfbin.par('xmax',rsf.doc.rsfpar('float','','','''x maximum '''))
sfbin.par('xmin',rsf.doc.rsfpar('float','','','''x minimum '''))
sfbin.par('ymax',rsf.doc.rsfpar('float','','','''y maximum '''))
sfbin.par('ymin',rsf.doc.rsfpar('float','','','''y minimum '''))
sfbin.par('x0',rsf.doc.rsfpar('float','xmin','','''x origin '''))
sfbin.par('y0',rsf.doc.rsfpar('float','ymin','','''y origin '''))
sfbin.par('nx',rsf.doc.rsfpar('int','(int) (xmax - xmin + 1.)','','''Number of bins in x '''))
sfbin.par('ny',rsf.doc.rsfpar('int','(int) (ymax - ymin + 1.)','','''Number of bins in y '''))
sfbin.par('dx',rsf.doc.rsfpar('float','','','''bin size in x '''))
sfbin.par('dy',rsf.doc.rsfpar('float','','','''bin size in y '''))
sfbin.par('interp',rsf.doc.rsfpar('int','1','[0,1,2]','''interpolation method;
       0: median, 1: nearest neighbor, 2: bi-linear,  '''))
sfbin.par('norm',rsf.doc.rsfpar('bool','y','','''if normalize '''))
sfbin.par('clip',rsf.doc.rsfpar('float','FLT_EPSILON','','''clip for fold normalization '''))
sfbin.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfbin.par('fold',rsf.doc.rsfpar('string ',desc='''output file for fold (optional) (auxiliary output file name)'''))
sfbin.version('1.7 Mbin.c 13815 2015-02-01 23:48:56Z sfomel')
sfbin.synopsis('''sfbin < in.rsf > out.rsf fold=fold.rsf xkey=0 ykey=1 xmax= xmin= ymax= ymin= x0=xmin y0=ymin nx=(int) (xmax - xmin + 1.) ny=(int) (ymax - ymin + 1.) dx= dy= interp=1 norm=y clip=FLT_EPSILON head=''','''
December 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/419-Program-of-the-month-sfbin.html
''')
rsf.doc.progs['sfbin']=sfbin

sfbin1 = rsf.doc.rsfprog('sfbin1','system/generic/Mbin1.c','''Data binning in 1-D slices. ''')
sfbin1.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbin1.par('fold',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbin1.par('xmin',rsf.doc.rsfpar('float','','','''grid dimensions '''))
sfbin1.par('xmax',rsf.doc.rsfpar('float','','',''''''))
sfbin1.par('nx',rsf.doc.rsfpar('int','','','''Number of bins '''))
sfbin1.par('x0',rsf.doc.rsfpar('float','xmin','','''grid origin '''))
sfbin1.par('dx',rsf.doc.rsfpar('float','','','''grid spacing '''))
sfbin1.par('interp',rsf.doc.rsfpar('int','1','[1,2]','''interpolation method, 1: nearest neighbor, 2: linear '''))
sfbin1.par('clip',rsf.doc.rsfpar('float','FLT_EPSILON','','''clip for fold normalization '''))
sfbin1.par('head',rsf.doc.rsfpar('string ',desc=''''''))
sfbin1.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfbin1.par('fold',rsf.doc.rsfpar('string ',desc='''output fold file (optional) (auxiliary output file name)'''))
sfbin1.version('1.7 Mbin1.c 13985 2015-03-26 13:56:59Z sfomel')
sfbin1.synopsis('''sfbin1 < in.rsf > out.rsf pattern=pattern.rsf fold=fold.rsf xmin= xmax= nx= x0=xmin dx= interp=1 clip=FLT_EPSILON head=''','''''')
rsf.doc.progs['sfbin1']=sfbin1

sfboxsmooth = rsf.doc.rsfprog('sfboxsmooth','system/generic/Mboxsmooth.c','''Multi-dimensional smoothing with boxes. ''')
sfboxsmooth.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfboxsmooth.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfboxsmooth.version('1.7')
sfboxsmooth.synopsis('''sfboxsmooth < in.rsf > out.rsf repeat=1 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfboxsmooth']=sfboxsmooth

sfcanny = rsf.doc.rsfprog('sfcanny','system/generic/Mcanny.c','''Canny-like edge detector. ''')
sfcanny.par('min',rsf.doc.rsfpar('float','5.0','','''minimum threshold '''))
sfcanny.par('max',rsf.doc.rsfpar('float','95.0','','''maximum threshold '''))
sfcanny.version('1.7')
sfcanny.synopsis('''sfcanny < in.rsf > out.rsf min=5.0 max=95.0''','''''')
rsf.doc.progs['sfcanny']=sfcanny

sfcausint = rsf.doc.rsfprog('sfcausint','system/generic/Mcausint.c','''Causal integration on the first axis. ''')
sfcausint.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint integration '''))
sfcausint.version('1.7')
sfcausint.synopsis('''sfcausint < in.rsf > out.rsf adj=n''','''
December 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/370-Program-of-the-month-sfcausint.html
''')
rsf.doc.progs['sfcausint']=sfcausint

sfclip = rsf.doc.rsfprog('sfclip','system/generic/Mclip.c','''Clip the data.''')
sfclip.par('clip',rsf.doc.rsfpar('float','','','''clip value '''))
sfclip.par('value',rsf.doc.rsfpar('float','clip','','''replacement value '''))
sfclip.version('1.7')
sfclip.synopsis('''sfclip < in.rsf > out.rsf clip= value=clip''','''
The output is 
 clip if input > clip
-clip if input < -clip
input if |input| < clip 

See also sfclip2.

September 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/269-Program-of-the-month-sfclip.html
''')
rsf.doc.progs['sfclip']=sfclip

sfclip2 = rsf.doc.rsfprog('sfclip2','system/generic/Mclip2.c','''One- or two-sided data clipping.''')
sfclip2.par('upper',rsf.doc.rsfpar('float','+FLT_MAX','','''upper clip value '''))
sfclip2.par('lower',rsf.doc.rsfpar('float','-FLT_MAX','','''lower clip value '''))
sfclip2.version('1.7')
sfclip2.synopsis('''sfclip2 < in.rsf > out.rsf upper=+FLT_MAX lower=-FLT_MAX''','''
sfclip2 is a generalization of sfclip.

Clip values above xu:         sfclip2 < in.rsf > out.rsf upper=xu
Clip values below xl:         sfclip2 < in.rsf > out.rsf lower=xl
Clip values outside [xu,xl]:  sfclip2 < in.rsf > out.rsf upper=xu lower=xl

sfclip2 < in.rsf > out.rsf upper=x lower=-x

is equivalent to

sfclip < in.rsf > out.rsf clip=x
''')
rsf.doc.progs['sfclip2']=sfclip2

sfcmatmult = rsf.doc.rsfprog('sfcmatmult','system/generic/Mcmatmult.c','''Simple matrix multiplication for complex matrices ''')
sfcmatmult.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcmatmult.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfcmatmult.version('1.7')
sfcmatmult.synopsis('''sfcmatmult < in.rsf > out.rsf mat=mat.rsf adj=n''','''''')
rsf.doc.progs['sfcmatmult']=sfcmatmult

sfcmatmult2 = rsf.doc.rsfprog('sfcmatmult2','system/generic/Mcmatmult2.c','''Multiplication of two complex matrices ''')
sfcmatmult2.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcmatmult2.version('1.7')
sfcmatmult2.synopsis('''sfcmatmult2 < in.rsf > out.rsf mat=mat.rsf''','''''')
rsf.doc.progs['sfcmatmult2']=sfcmatmult2

sfcosft = rsf.doc.rsfprog('sfcosft','system/generic/Mcosft.c','''Multi-dimensional cosine transform.''')
sfcosft.par('sign#',rsf.doc.rsfpar('int','0','','''transform along #-th dimension 
	  [+1 forward or -1 backward] '''))
sfcosft.version('1.7')
sfcosft.synopsis('''sfcosft < in.rsf > out.rsf sign#=0''','''
The input and output are real and have the same dimensions. 
Pad the data if you need to suppress wrap-around effects.
''')
rsf.doc.progs['sfcosft']=sfcosft

sfcostaper = rsf.doc.rsfprog('sfcostaper','system/generic/Mcostaper.c','''Cosine taper around the borders (N-D). ''')
sfcostaper.par('nw#',rsf.doc.rsfpar('int','0','','''tapering on #-th axis '''))
sfcostaper.version('1.7')
sfcostaper.synopsis('''sfcostaper < in.rsf > out.rsf nw#=0''','''
April 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/381-Program-of-the-month-sfcostaper.html 
''')
rsf.doc.progs['sfcostaper']=sfcostaper

sfderiv = rsf.doc.rsfprog('sfderiv','system/generic/Mderiv.c','''First derivative with a maximally linear FIR differentiator. ''')
sfderiv.par('order',rsf.doc.rsfpar('int','6','','''filter order '''))
sfderiv.par('scale',rsf.doc.rsfpar('bool','n','','''if scale by 1/dx '''))
sfderiv.version('1.7')
sfderiv.synopsis('''sfderiv < in.rsf > out.rsf order=6 scale=n''','''
May 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/290-Program-of-the-month-sfderiv.html
''')
rsf.doc.progs['sfderiv']=sfderiv

sfdipfilter = rsf.doc.rsfprog('sfdipfilter','system/generic/Mdipfilter.c','''Filter data based on dip in 2-D or 3-D.''')
sfdipfilter.par('dim',rsf.doc.rsfpar('int','2','[2,3]','''Dimensionality: filter 2-D planes or 3-D cubes '''))
sfdipfilter.par('angle',rsf.doc.rsfpar('bool','n','','''Filter based on angle (or velocity) '''))
sfdipfilter.par('v',rsf.doc.rsfpar('float','-1.','','''constant velocity (if angle-y)
	   The default is d(frequency)/d(wavenumber) '''))
sfdipfilter.par('ang1',rsf.doc.rsfpar('float','-50.','',''''''))
sfdipfilter.par('ang2',rsf.doc.rsfpar('float','-45.','',''''''))
sfdipfilter.par('ang3',rsf.doc.rsfpar('float','45.','',''''''))
sfdipfilter.par('ang4',rsf.doc.rsfpar('float','50.','','''Angle gate (in degrees) '''))
sfdipfilter.par('v1',rsf.doc.rsfpar('float','0.','',''''''))
sfdipfilter.par('v2',rsf.doc.rsfpar('float','0.1','',''''''))
sfdipfilter.par('v3',rsf.doc.rsfpar('float','99999.','',''''''))
sfdipfilter.par('v4',rsf.doc.rsfpar('float','999999.','','''Velocity gate '''))
sfdipfilter.par('pass',rsf.doc.rsfpar('bool','y','','''Pass or reject band '''))
sfdipfilter.version('1.7 Mdipfilter.c 11735 2014-02-07 15:39:24Z sfomel')
sfdipfilter.synopsis('''sfdipfilter < in.rsf > out.rsf dim=2 angle=n v=-1. ang1=-50. ang2=-45. ang3=45. ang4=50. v1=0. v2=0.1 v3=99999. v4=999999. pass=y''','''
February 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/374-Program-of-the-month-sfdipfilter.html
''')
rsf.doc.progs['sfdipfilter']=sfdipfilter

sfdwt = rsf.doc.rsfprog('sfdwt','system/generic/Mdwt.c','''1-D digital wavelet transform ''')
sfdwt.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfdwt.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfdwt.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfdwt.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfdwt.version('1.7')
sfdwt.synopsis('''sfdwt < in.rsf > out.rsf inv=n adj=n unit=n type=''','''''')
rsf.doc.progs['sfdwt']=sfdwt

sfenoint2 = rsf.doc.rsfprog('sfenoint2','system/generic/Menoint2.c','''ENO interpolation in 2-D slices. ''')
sfenoint2.par('head',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfenoint2.par('xkey',rsf.doc.rsfpar('int','','','''x key number '''))
sfenoint2.par('ykey',rsf.doc.rsfpar('int','','','''y key number '''))
sfenoint2.par('interp',rsf.doc.rsfpar('int','2','','''interpolation order '''))
sfenoint2.version('1.7 Mbin.c 847 2004-10-27 20:33:16Z fomels')
sfenoint2.synopsis('''sfenoint2 < in.rsf > out.rsf head=head.rsf xkey= ykey= interp=2''','''''')
rsf.doc.progs['sfenoint2']=sfenoint2

sfextract = rsf.doc.rsfprog('sfextract','system/generic/Mextract.c','''Forward interpolation in 2-D slices. ''')
sfextract.par('head',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfextract.par('xkey',rsf.doc.rsfpar('int','0','','''x key number '''))
sfextract.par('ykey',rsf.doc.rsfpar('int','1','','''y key number '''))
sfextract.par('interp',rsf.doc.rsfpar('int','2','[1,2]','''interpolation method, 1: nearest neighbor, 2: bi-linear '''))
sfextract.version('1.7 Mextract.c 7107 2011-04-10 02:04:14Z ivlad')
sfextract.synopsis('''sfextract < in.rsf > out.rsf head=head.rsf xkey=0 ykey=1 interp=2''','''''')
rsf.doc.progs['sfextract']=sfextract

sffern = rsf.doc.rsfprog('sffern','system/generic/Mfern.c','''Generate fractal fern. ''')
sffern.par('n',rsf.doc.rsfpar('int','1000','','''number of points '''))
sffern.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sffern.par('angle',rsf.doc.rsfpar('bool','y','','''if y, use more angular fern '''))
sffern.version('1.7')
sffern.synopsis('''sffern > out.rsf n=1000 seed=time(NULL) angle=y''','''''')
rsf.doc.progs['sffern']=sffern

sffft1 = rsf.doc.rsfprog('sffft1','system/generic/Mfft1.c','''Fast Fourier Transform along the first axis. ''')
sffft1.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sffft1.par('inv',rsf.doc.rsfpar('bool','n','','''y, perform inverse transform '''))
sffft1.par('sym',rsf.doc.rsfpar('bool','n','','''y, symmetric scaling for Hermitian FFT '''))
sffft1.par('opt',rsf.doc.rsfpar('bool','y','','''y, determine optimal size for efficiency '''))
sffft1.par('memsize',rsf.doc.rsfpar('float','1000.0','',''''''))
sffft1.version('1.7')
sffft1.synopsis('''sffft1 < Fin.rsf > Fou.rsf verb=n inv=n sym=n opt=y memsize=1000.0''','''''')
rsf.doc.progs['sffft1']=sffft1

sffft3 = rsf.doc.rsfprog('sffft3','system/generic/Mfft3.c','''FFT transform on extra axis.''')
sffft3.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse transform '''))
sffft3.par('sym',rsf.doc.rsfpar('bool','n','','''if y, apply symmetric scaling to make the FFT operator Hermitian '''))
sffft3.par('sign',rsf.doc.rsfpar('int','inv? 1: 0','','''transform sign (0 or 1) '''))
sffft3.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sffft3.par('axis',rsf.doc.rsfpar('int','2','','''Axis to transform '''))
sffft3.par('pad',rsf.doc.rsfpar('int','2','','''padding factor '''))
sffft3.version('1.7')
sffft3.synopsis('''sffft3 < in.rsf > out.rsf inv=n sym=n sign=inv? 1: 0 opt=y axis=2 pad=2''','''
Input and output are complex data. The input is padded by factor pad.

July 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/298-Program-of-the-month-sffft3.html
''')
rsf.doc.progs['sffft3']=sffft3

sfgrad2 = rsf.doc.rsfprog('sfgrad2','system/generic/Mgrad2.c','''2-D smooth gradient. ''')
sfgrad2.version('1.7')
sfgrad2.synopsis('''sfgrad2 < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfgrad2']=sfgrad2

sfheat = rsf.doc.rsfprog('sfheat','system/generic/Mheat.c','''Finite-difference solution of 2-D heat-flow equation ''')
sfheat.par('impl',rsf.doc.rsfpar('bool','n','','''if y, use implicit scheme '''))
sfheat.par('alpha',rsf.doc.rsfpar('float','1.','',''''''))
sfheat.version('1.7')
sfheat.synopsis('''sfheat > out.rsf impl=n alpha=1.''','''''')
rsf.doc.progs['sfheat']=sfheat

sfhistogram = rsf.doc.rsfprog('sfhistogram','system/generic/Mhistogram.c','''Compute a histogram of integer- or float-valued input data.''')
sfhistogram.par('n1',rsf.doc.rsfpar('int','','','''number of histogram samples '''))
sfhistogram.par('o1',rsf.doc.rsfpar('float','','','''histogram origin '''))
sfhistogram.par('d1',rsf.doc.rsfpar('float','','','''histogram sampling '''))
sfhistogram.version('1.7')
sfhistogram.synopsis('''sfhistogram < in.rsf > out.rsf n1= o1= d1=''','''
The output grid is not centered on the bins; it marks their "left edge".
I.e., the first sample holds the number of values between o1 and o1+d1. 

February 2015 program of the month:
http://ahay.org/rsflog/index.php?/archives/427-Program-of-the-month-sfhistogram.html
''')
rsf.doc.progs['sfhistogram']=sfhistogram

sfigrad = rsf.doc.rsfprog('sfigrad','system/generic/Migrad.c','''Gradient on the first axis. ''')
sfigrad.par('square',rsf.doc.rsfpar('bool','n','','''if y, use gradient squared '''))
sfigrad.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfigrad.version('1.7')
sfigrad.synopsis('''sfigrad < in.rsf > out.rsf square=n adj=n''','''''')
rsf.doc.progs['sfigrad']=sfigrad

sfimpl2 = rsf.doc.rsfprog('sfimpl2','system/generic/Mimpl2.c','''2-D anisotropic diffusion. ''')
sfimpl2.par('rect1',rsf.doc.rsfpar('float','','','''vertical smoothing '''))
sfimpl2.par('rect2',rsf.doc.rsfpar('float','','','''horizontal smoothing '''))
sfimpl2.par('tau',rsf.doc.rsfpar('float','0.1','','''smoothing time '''))
sfimpl2.par('pclip',rsf.doc.rsfpar('float','50.','','''percentage clip for the gradient '''))
sfimpl2.par('up',rsf.doc.rsfpar('bool','n','','''smoothing style '''))
sfimpl2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfimpl2.par('nsnap',rsf.doc.rsfpar('int','1','','''number of snapshots '''))
sfimpl2.par('lin',rsf.doc.rsfpar('bool','n','','''if linear operator '''))
sfimpl2.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfimpl2.par('dist',rsf.doc.rsfpar('string ',desc='''inverse distance file (input) '''))
sfimpl2.par('snap',rsf.doc.rsfpar('string ',desc='''snapshot file (output) '''))
sfimpl2.version('1.7')
sfimpl2.synopsis('''sfimpl2 < in.rsf > out.rsf rect1= rect2= tau=0.1 pclip=50. up=n verb=n nsnap=1 lin=n adj=n dist= snap=''','''''')
rsf.doc.progs['sfimpl2']=sfimpl2

sfintshow = rsf.doc.rsfprog('sfintshow','system/generic/Mintshow.c','''Output interpolation filter. ''')
sfintshow.par('nw',rsf.doc.rsfpar('int','','','''interpolator size '''))
sfintshow.par('x',rsf.doc.rsfpar('float','','','''interpolation shift '''))
sfintshow.par('kai',rsf.doc.rsfpar('float','4.0','','''Kaiser window parameter '''))
sfintshow.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline,mom) '''))
sfintshow.version('1.7')
sfintshow.synopsis('''sfintshow > filt.rsf nw= x= kai=4.0 interp=''','''
See also: inttest1.
''')
rsf.doc.progs['sfintshow']=sfintshow

sfinttest1 = rsf.doc.rsfprog('sfinttest1','system/generic/Minttest1.c','''Interpolation from a regular grid in 1-D. ''')
sfinttest1.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinttest1.par('nw',rsf.doc.rsfpar('int','','','''interpolator size '''))
sfinttest1.par('same',rsf.doc.rsfpar('bool','y','','''same or different coordinates for each trace '''))
sfinttest1.par('kai',rsf.doc.rsfpar('float','4.0','','''Kaiser window parameter '''))
sfinttest1.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline,mom) '''))
sfinttest1.version('1.7')
sfinttest1.synopsis('''sfinttest1 < in.rsf > out.rsf coord=crd.rsf nw= same=y kai=4.0 interp=''','''
January 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/373-Program-of-the-month-sfinttest1.html
''')
rsf.doc.progs['sfinttest1']=sfinttest1

sfinttest2 = rsf.doc.rsfprog('sfinttest2','system/generic/Minttest2.c','''Interpolation from a regular grid in 2-D. ''')
sfinttest2.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinttest2.par('nw',rsf.doc.rsfpar('int','','','''interpolator size '''))
sfinttest2.par('kai',rsf.doc.rsfpar('float','4.0','','''Kaiser window parameter '''))
sfinttest2.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation (lagrange,cubic,kaiser,lanczos,cosine,welch,spline) '''))
sfinttest2.version('1.7')
sfinttest2.synopsis('''sfinttest2 < in.rsf > out.rsf coord=crd.rsf nw= kai=4.0 interp=''','''''')
rsf.doc.progs['sfinttest2']=sfinttest2

sfjacobi = rsf.doc.rsfprog('sfjacobi','system/generic/Mjacobi.c','''Find eigenvalues of a symmetric matrix by Jacobi's iteration. ''')
sfjacobi.par('eig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfjacobi.par('niter',rsf.doc.rsfpar('int','10','',''''''))
sfjacobi.par('eig',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfjacobi.version('1.7')
sfjacobi.synopsis('''sfjacobi < mat.rsf > val.rsf eig=eig.rsf niter=10''','''''')
rsf.doc.progs['sfjacobi']=sfjacobi

sflapfill = rsf.doc.rsfprog('sflapfill','system/generic/Mlapfill.c','''Missing data interpolation in 2-D by Laplacian regularization. ''')
sflapfill.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflapfill.par('niter',rsf.doc.rsfpar('int','200','','''number of iterations '''))
sflapfill.par('grad',rsf.doc.rsfpar('bool','n','','''if y, use gradient instead of laplacian '''))
sflapfill.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflapfill.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file with zeroes for missing data locations (auxiliary input file name)'''))
sflapfill.version('1.7')
sflapfill.synopsis('''sflapfill < in.rsf > out.rsf mask=mask.rsf niter=200 grad=n verb=n''','''''')
rsf.doc.progs['sflapfill']=sflapfill

sflaplac = rsf.doc.rsfprog('sflaplac','system/generic/Mlaplac.c','''2-D finite-difference Laplacian operation. ''')
sflaplac.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sflaplac.version('1.7')
sflaplac.synopsis('''sflaplac < in.rsf > out.rsf adj=n''','''''')
rsf.doc.progs['sflaplac']=sflaplac

sflinear = rsf.doc.rsfprog('sflinear','system/generic/Mlinear.c','''1-D linear interpolation.''')
sflinear.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflinear.par('sort',rsf.doc.rsfpar('bool','n','','''if y, the coordinates need sorting '''))
sflinear.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sflinear.par('rect',rsf.doc.rsfpar('int','1','','''smoothing regularization '''))
sflinear.par('nw',rsf.doc.rsfpar('int','2','','''interpolator size '''))
sflinear.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflinear.version('1.7')
sflinear.synopsis('''sflinear < in.rsf > out.rsf pattern=pattern.rsf sort=n niter=0 rect=1 nw=2''','''
The input should have n2=2 (coordinates,values)

For output, specify either n1= o1= d1= or pattern=
''')
rsf.doc.progs['sflinear']=sflinear

sflinefit = rsf.doc.rsfprog('sflinefit','system/generic/Mlinefit.c','''Fit a line to a set of points in 2-D.''')
sflinefit.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflinefit.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflinefit.version('1.7')
sflinefit.synopsis('''sflinefit < in.rsf > out.rsf pattern=pattern.rsf''','''''')
rsf.doc.progs['sflinefit']=sflinefit

sflorenz = rsf.doc.rsfprog('sflorenz','system/generic/Mlorenz.c','''Generate Lorenz attractor. ''')
sflorenz.par('niter',rsf.doc.rsfpar('int','1000','','''number of iterations '''))
sflorenz.par('n',rsf.doc.rsfpar('int','niter','','''set maximum '''))
sflorenz.par('rho',rsf.doc.rsfpar('double','28.00','','''Rayleigh number '''))
sflorenz.par('sigma',rsf.doc.rsfpar('double','10.00','','''Prandtl number '''))
sflorenz.par('beta',rsf.doc.rsfpar('double','8.00/3.00','','''Beta reference '''))
sflorenz.par('x0',rsf.doc.rsfpar('double','3.051522','','''intial x coordinate '''))
sflorenz.par('y0',rsf.doc.rsfpar('double','1.582542','','''intial y coordinate '''))
sflorenz.par('z0',rsf.doc.rsfpar('double','15.62388','','''intial z coordinate '''))
sflorenz.par('dt',rsf.doc.rsfpar('double','0.0001','','''time step '''))
sflorenz.version('1.7 Mlorenz.c 9567 2012-10-29 20:38:18Z sfomel')
sflorenz.synopsis('''sflorenz > out.rsf niter=1000 n=niter rho=28.00 sigma=10.00 beta=8.00/3.00 x0=3.051522 y0=1.582542 z0=15.62388 dt=0.0001''','''''')
rsf.doc.progs['sflorenz']=sflorenz

sflpad = rsf.doc.rsfprog('sflpad','system/generic/Mlpad.c','''Pad and interleave traces.''')
sflpad.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpad.par('jump',rsf.doc.rsfpar('int','2','','''aliasing '''))
sflpad.version('1.7')
sflpad.synopsis('''sflpad < in.rsf > out.rsf mask=mask.rsf jump=2''','''
Each initial trace is followed by "jump" zero traces, the same for planes.

March 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/377-Program-of-the-math-sflpad.html
''')
rsf.doc.progs['sflpad']=sflpad

sfmandelbrot = rsf.doc.rsfprog('sfmandelbrot','system/generic/Mmandelbrot.c','''Generate Mandelbrot set. ''')
sfmandelbrot.par('n1',rsf.doc.rsfpar('int','512','',''''''))
sfmandelbrot.par('n2',rsf.doc.rsfpar('int','512','','''dimensions '''))
sfmandelbrot.par('x0',rsf.doc.rsfpar('float','-2.','',''''''))
sfmandelbrot.par('y0',rsf.doc.rsfpar('float','-1.','','''set origin '''))
sfmandelbrot.par('xmax',rsf.doc.rsfpar('float','0.5','',''''''))
sfmandelbrot.par('ymax',rsf.doc.rsfpar('float','1.','','''set maximum '''))
sfmandelbrot.par('niter',rsf.doc.rsfpar('int','1000','','''number of iterations '''))
sfmandelbrot.par('dx',rsf.doc.rsfpar('float','(xmax-x0)/(n1-1)','',''''''))
sfmandelbrot.par('dy',rsf.doc.rsfpar('float','(ymax-y0)/(n2-1)','',''''''))
sfmandelbrot.version('1.7')
sfmandelbrot.synopsis('''sfmandelbrot > out.rsf n1=512 n2=512 x0=-2. y0=-1. xmax=0.5 ymax=1. niter=1000 dx=(xmax-x0)/(n1-1) dy=(ymax-y0)/(n2-1)''','''''')
rsf.doc.progs['sfmandelbrot']=sfmandelbrot

sfmatmult = rsf.doc.rsfprog('sfmatmult','system/generic/Mmatmult.c','''Simple matrix multiplication ''')
sfmatmult.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmatmult.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfmatmult.version('1.7')
sfmatmult.synopsis('''sfmatmult < in.rsf > out.rsf mat=mat.rsf adj=n''','''''')
rsf.doc.progs['sfmatmult']=sfmatmult

sfmax1 = rsf.doc.rsfprog('sfmax1','system/generic/Mmax1.c','''Picking local maxima on the first axis. ''')
sfmax1.par('min',rsf.doc.rsfpar('float','o1','','''minimum value of time '''))
sfmax1.par('max',rsf.doc.rsfpar('float','o1+(n1-1)*d1','','''maximum value of time '''))
sfmax1.par('np',rsf.doc.rsfpar('int','n1','','''maximum number of picks '''))
sfmax1.par('sorted',rsf.doc.rsfpar('bool','y','','''if y, sort by amplitude '''))
sfmax1.version('1.7')
sfmax1.synopsis('''sfmax1 < in.rsf > out.rsf min=o1 max=o1+(n1-1)*d1 np=n1 sorted=y''','''
Outputs complex numbers (time,amplitude) 

September 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/403-Program-of-the-month-sfmax1.html
''')
rsf.doc.progs['sfmax1']=sfmax1

sfmonof = rsf.doc.rsfprog('sfmonof','system/generic/Mmonof.c','''Mono-frequency wavelet estimation.''')
sfmonof.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmonof.par('a0',rsf.doc.rsfpar('float','1.','','''starting sharpness '''))
sfmonof.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmonof.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmonof.version('1.7')
sfmonof.synopsis('''sfmonof < in.rsf > out.rsf ma=ma.rsf a0=1. niter=100 verb=n''','''''')
rsf.doc.progs['sfmonof']=sfmonof

sfmutter = rsf.doc.rsfprog('sfmutter','system/generic/Mmutter.c','''Muting.''')
sfmutter.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmutter.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfmutter.par('nan',rsf.doc.rsfpar('bool','n','','''if y, put  nans instead of zeros '''))
sfmutter.par('tp',rsf.doc.rsfpar('float','0.150','','''end time '''))
sfmutter.par('t0',rsf.doc.rsfpar('float','0.','','''starting time '''))
sfmutter.par('v0',rsf.doc.rsfpar('float','1.45','','''velocity '''))
sfmutter.par('slope0',rsf.doc.rsfpar('float','1./v0','','''slope '''))
sfmutter.par('slopep',rsf.doc.rsfpar('float','slope0','','''end slope '''))
sfmutter.par('x0',rsf.doc.rsfpar('float','0.','','''starting space '''))
sfmutter.par('abs',rsf.doc.rsfpar('bool','y','','''if y, use absolute value |x-x0| '''))
sfmutter.par('inner',rsf.doc.rsfpar('bool','n','','''if y, do inner muter '''))
sfmutter.par('hyper',rsf.doc.rsfpar('bool','n','','''if y, do hyperbolic mute '''))
sfmutter.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmutter.version('1.7 Mmutter.c 7107 2011-04-10 02:04:14Z ivlad')
sfmutter.synopsis('''sfmutter < in.rsf > out.rsf offset=offset.rsf half=y nan=n tp=0.150 t0=0. v0=1.45 slope0=1./v0 slopep=slope0 x0=0. abs=y inner=n hyper=n''','''   
Data is smoothly weighted inside the mute zone.
The weight is zero for t <       (x-x0) * slope0
The weight is one  for t >  tp + (x-x0) * slopep

The signs are reversed for inner=y.
''')
rsf.doc.progs['sfmutter']=sfmutter

sfnoise = rsf.doc.rsfprog('sfnoise','system/generic/Mnoise.c','''Add random noise to the data.''')
sfnoise.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfnoise.par('type',rsf.doc.rsfpar('bool','y','','''noise distribution, y: normal, n: uniform '''))
sfnoise.par('var',rsf.doc.rsfpar('float','','','''noise variance '''))
sfnoise.par('range',rsf.doc.rsfpar('float','','','''noise range (default=1) '''))
sfnoise.par('mean',rsf.doc.rsfpar('float','0','','''noise mean '''))
sfnoise.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfnoise.version('1.7 Mnoise.c 13817 2015-02-03 00:18:33Z wangh0a')
sfnoise.synopsis('''sfnoise < in.rsf > out.rsf seed=time(NULL) type=y var= range= mean=0 rep=n''','''
July 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/262-Program-of-the-month-sfnoise.html
''')
rsf.doc.progs['sfnoise']=sfnoise

sfpostfilter2 = rsf.doc.rsfprog('sfpostfilter2','system/generic/Mpostfilter2.c','''Convert B-spline coefficients to data in 2-D. ''')
sfpostfilter2.par('nw',rsf.doc.rsfpar('int','','','''filter size '''))
sfpostfilter2.par('vert',rsf.doc.rsfpar('bool','y','','''include filter on the first axis '''))
sfpostfilter2.par('horz',rsf.doc.rsfpar('bool','y','','''include filter on the second axis '''))
sfpostfilter2.version('1.7')
sfpostfilter2.synopsis('''sfpostfilter2 < in.rsf > out.rsf nw= vert=y horz=y''','''''')
rsf.doc.progs['sfpostfilter2']=sfpostfilter2

sfpow = rsf.doc.rsfprog('sfpow','system/generic/Mpow.c','''Apply power gain. ''')
sfpow.par('tpow',rsf.doc.rsfpar('float','0.','','''power on the first axis '''))
sfpow.par('pow#',rsf.doc.rsfpar('float','(0,0,...)','','''power on #-th axis '''))
sfpow.version('1.7')
sfpow.synopsis('''sfpow < in.rsf > out.rsf tpow=0. pow#=(0,0,...)''','''
March 2013 program of the month:
http://www.ahay.org/rsflog/index.php?/archives/327-Program-of-the-month-sfpow.html
''')
rsf.doc.progs['sfpow']=sfpow

sfreg2tri = rsf.doc.rsfprog('sfreg2tri','system/generic/Mreg2tri.c','''Decimate a regular grid to triplets for triangulation. ''')
sfreg2tri.par('edgeout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreg2tri.par('nt',rsf.doc.rsfpar('int','','','''number of triplets '''))
sfreg2tri.par('zero',rsf.doc.rsfpar('float','0.','','''level surface '''))
sfreg2tri.par('edgeout',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfreg2tri.version('1.7')
sfreg2tri.synopsis('''sfreg2tri < in.rsf > out.rsf edgeout=edge.rsf nt= zero=0.''','''''')
rsf.doc.progs['sfreg2tri']=sfreg2tri

sfremap1 = rsf.doc.rsfprog('sfremap1','system/generic/Mremap1.c','''1-D ENO interpolation. ''')
sfremap1.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfremap1.par('n1',rsf.doc.rsfpar('int','n1','','''Number of output samples '''))
sfremap1.par('d1',rsf.doc.rsfpar('float','d1','','''Output sampling '''))
sfremap1.par('o1',rsf.doc.rsfpar('float','o1','','''Output origin '''))
sfremap1.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order '''))
sfremap1.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfremap1.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfremap1')
sfremap1.version('1.7 Mremap1.c 11244 2013-11-03 14:33:46Z sfomel')
sfremap1.synopsis('''sfremap1 < in.rsf > out.rsf pattern=pattern.rsf n1=n1 d1=d1 o1=o1 order=3''','''
November 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/364-Program-of-the-month-sfremap1.html
''')
rsf.doc.progs['sfremap1']=sfremap1

sfroots = rsf.doc.rsfprog('sfroots','system/generic/Mroots.c','''Find roots of a complex polynomial. ''')
sfroots.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfroots.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''tolerance for convergence '''))
sfroots.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfroots.par('sort',rsf.doc.rsfpar('string ',desc='''attribute for sorting (phase,amplitude,real,imaginary) '''))
sfroots.version('1.7')
sfroots.synopsis('''sfroots < poly.rsf > root.rsf niter=10 tol=1.0e-6 verb=y sort=''','''''')
rsf.doc.progs['sfroots']=sfroots

sfshapebin1 = rsf.doc.rsfprog('sfshapebin1','system/generic/Mshapebin1.c','''1-D inverse interpolation with shaping regularization. ''')
sfshapebin1.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfshapebin1.par('nx',rsf.doc.rsfpar('int','','','''number of bins '''))
sfshapebin1.par('xmin',rsf.doc.rsfpar('float','','','''grid size '''))
sfshapebin1.par('xmax',rsf.doc.rsfpar('float','','',''''''))
sfshapebin1.par('x0',rsf.doc.rsfpar('float','xmin','','''grid origin '''))
sfshapebin1.par('dx',rsf.doc.rsfpar('float','','','''grid sampling '''))
sfshapebin1.par('interp',rsf.doc.rsfpar('int','2','[1,2]','''forward interpolation method, 1: nearest neighbor, 2: linear '''))
sfshapebin1.par('filter',rsf.doc.rsfpar('float','3.','','''smoothing length '''))
sfshapebin1.par('niter',rsf.doc.rsfpar('int','nx','','''number of conjugate-gradient iterations '''))
sfshapebin1.par('eps',rsf.doc.rsfpar('float','1./nd','','''regularization parameter '''))
sfshapebin1.par('pef',rsf.doc.rsfpar('bool','n','','''if y, use monofrequency regularization '''))
sfshapebin1.par('gauss',rsf.doc.rsfpar('bool','n','','''if y, use Gaussian shaping '''))
sfshapebin1.par('pad',rsf.doc.rsfpar('int','0','','''padding for Gaussian shaping '''))
sfshapebin1.par('head',rsf.doc.rsfpar('string ',desc=''''''))
sfshapebin1.version('1.7 Mshapebin1.c 13985 2015-03-26 13:56:59Z sfomel')
sfshapebin1.synopsis('''sfshapebin1 < in.rsf > out.rsf verb=y nx= xmin= xmax= x0=xmin dx= interp=2 filter=3. niter=nx eps=1./nd pef=n gauss=n pad=0 head=''','''''')
rsf.doc.progs['sfshapebin1']=sfshapebin1

sfsharpen = rsf.doc.rsfprog('sfsharpen','system/generic/Msharpen.c','''Sharpening operator ''')
sfsharpen.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsharpen.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfsharpen.par('other',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsharpen.par('other',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsharpen.version('1.7')
sfsharpen.synopsis('''sfsharpen < in.rsf > out.rsf other=other.rsf perc=50.0''','''''')
rsf.doc.progs['sfsharpen']=sfsharpen

sfslice = rsf.doc.rsfprog('sfslice','system/generic/Mslice.c','''Extract a slice using picked surface (usually from a stack or a semblance).''')
sfslice.par('pick',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfslice.version('1.7')
sfslice.synopsis('''sfslice < in.rsf pick=pick.rsf > out.rsf''','''
See also: sfpick.
''')
rsf.doc.progs['sfslice']=sfslice

sfsmooth = rsf.doc.rsfprog('sfsmooth','system/generic/Msmooth.c','''Multi-dimensional triangle smoothing. ''')
sfsmooth.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfsmooth.par('adj',rsf.doc.rsfpar('bool','n','','''run in the adjoint mode '''))
sfsmooth.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmooth.par('diff#',rsf.doc.rsfpar('bool','(n,n,...)','','''differentiation on #-th axis '''))
sfsmooth.version('1.7 Msmooth.c 9744 2013-01-19 17:12:34Z sfomel')
sfsmooth.synopsis('''sfsmooth < in.rsf > out.rsf repeat=1 adj=n rect#=(1,1,...) diff#=(n,n,...)''','''
January 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/280-Program-of-the-month-sfsmooth.html
''')
rsf.doc.progs['sfsmooth']=sfsmooth

sfsmoothder = rsf.doc.rsfprog('sfsmoothder','system/generic/Msmoothder.c','''Smooth first derivative on the first axis.''')
sfsmoothder.par('eps',rsf.doc.rsfpar('float','0.2','','''smoothness parameter '''))
sfsmoothder.version('1.7')
sfsmoothder.synopsis('''sfsmoothder < in.rsf > der.rsf eps=0.2''','''
Applies D/(I + eps*D'D)
''')
rsf.doc.progs['sfsmoothder']=sfsmoothder

sfsmoothreg2 = rsf.doc.rsfprog('sfsmoothreg2','system/generic/Msmoothreg2.c','''Smoothing in 2-D by simple regularization.''')
sfsmoothreg2.par('eps',rsf.doc.rsfpar('float','1.','','''smoothness parameter '''))
sfsmoothreg2.par('repeat',rsf.doc.rsfpar('int','1','','''repeat smoothing '''))
sfsmoothreg2.version('1.7')
sfsmoothreg2.synopsis('''sfsmoothreg2 < in.rsf > smooth.rsf eps=1. repeat=1''','''''')
rsf.doc.progs['sfsmoothreg2']=sfsmoothreg2

sfspectra = rsf.doc.rsfprog('sfspectra','system/generic/Mspectra.c','''Frequency spectra. ''')
sfspectra.par('all',rsf.doc.rsfpar('bool','n','','''if y, compute average spectrum for all traces '''))
sfspectra.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfspectra.version('1.7')
sfspectra.synopsis('''sfspectra < in.rsf > out.rsf all=n opt=y''','''
March 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/285-Program-of-the-month-sfspectra.html
''')
rsf.doc.progs['sfspectra']=sfspectra

sfspectra2 = rsf.doc.rsfprog('sfspectra2','system/generic/Mspectra2.c','''Frequency spectra in 2-D. ''')
sfspectra2.par('all',rsf.doc.rsfpar('bool','n','','''if y, compute average spectrum for all traces '''))
sfspectra2.version('1.7')
sfspectra2.synopsis('''sfspectra2 < in.rsf > out.rsf all=n''','''''')
rsf.doc.progs['sfspectra2']=sfspectra2

sfspline = rsf.doc.rsfprog('sfspline','system/generic/Mspline.c','''1-D cubic spline interpolation.''')
sfspline.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfspline.par('fp',rsf.doc.rsfpar('floats','','','''end-point derivatives  [2]'''))
sfspline.par('sort',rsf.doc.rsfpar('bool','n','','''if y, the coordinates need sorting '''))
sfspline.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfspline.version('1.7')
sfspline.synopsis('''sfspline < in.rsf > out.rsf pattern=pattern.rsf fp= sort=n''','''
Specify either n1= o1= d1= or pattern=
''')
rsf.doc.progs['sfspline']=sfspline

sfsplinefilter = rsf.doc.rsfprog('sfsplinefilter','system/generic/Msplinefilter.c','''Convert data to B-spline coefficients. ''')
sfsplinefilter.par('nw',rsf.doc.rsfpar('int','','','''filter size '''))
sfsplinefilter.version('1.7')
sfsplinefilter.synopsis('''sfsplinefilter < in.rsf > out.rsf nw=''','''''')
rsf.doc.progs['sfsplinefilter']=sfsplinefilter

sfthreshold = rsf.doc.rsfprog('sfthreshold','system/generic/Mthreshold.c','''Soft thresholding. ''')
sfthreshold.par('pclip',rsf.doc.rsfpar('float','','','''percentage to clip '''))
sfthreshold.version('1.7')
sfthreshold.synopsis('''sfthreshold < in.rsf > out.rsf pclip=''','''
November 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/409-Program-of-the-month-sfthreshold.html
''')
rsf.doc.progs['sfthreshold']=sfthreshold

sftrapez = rsf.doc.rsfprog('sftrapez','system/generic/Mtrapez.c','''Convolution with a trapezoidal filter. ''')
sftrapez.par('frequency',rsf.doc.rsfpar('floats','','','''frequencies (in Hz), default: (0.1,0.15,0.45,0.5)*Nyquist  [4]'''))
sftrapez.version('1.7')
sftrapez.synopsis('''sftrapez < in.rsf > out.rsf frequency=''','''''')
rsf.doc.progs['sftrapez']=sftrapez

sftri2reg = rsf.doc.rsfprog('sftri2reg','system/generic/Mtri2reg.c','''Interpolate triangulated triplets to a regular grid. ''')
sftri2reg.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftri2reg.par('edgein',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftri2reg.par('nodeout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftri2reg.par('edgeout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftri2reg.par('n1',rsf.doc.rsfpar('int','','',''''''))
sftri2reg.par('n2',rsf.doc.rsfpar('int','','',''''''))
sftri2reg.par('d1',rsf.doc.rsfpar('float','1.','',''''''))
sftri2reg.par('d2',rsf.doc.rsfpar('float','1.','',''''''))
sftri2reg.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sftri2reg.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sftri2reg.par('zero',rsf.doc.rsfpar('float','0.','','''level surface '''))
sftri2reg.par('nr',rsf.doc.rsfpar('int','0','','''number of refinements '''))
sftri2reg.par('pattern',rsf.doc.rsfpar('string ',desc='''pattern file for output dimensions (auxiliary input file name)'''))
sftri2reg.par('edgein',rsf.doc.rsfpar('string ',desc='''input edge file (auxiliary input file name)'''))
sftri2reg.par('nodeout',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftri2reg.par('edgeout',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftri2reg.version('1.7')
sftri2reg.synopsis('''sftri2reg < in.rsf > out.rsf pattern=pattern.rsf edgein=edge.rsf nodeout=out2.rsf edgeout=edge2.rsf n1= n2= d1=1. d2=1. o1=0. o2=0. zero=0. nr=0''','''''')
rsf.doc.progs['sftri2reg']=sftri2reg

sftrirand = rsf.doc.rsfprog('sftrirand','system/generic/Mtrirand.c','''Edit points for triangulation by removing similar and randomizing. ''')
sftrirand.version('1.7')
sftrirand.synopsis('''sftrirand < in.rsf > out.rsf''','''''')
rsf.doc.progs['sftrirand']=sftrirand

sftrishape = rsf.doc.rsfprog('sftrishape','system/generic/Mtrishape.c','''2-D irregular data interpolation using triangulation and shaping regularization. ''')
sftrishape.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftrishape.par('n1',rsf.doc.rsfpar('int','','',''''''))
sftrishape.par('n2',rsf.doc.rsfpar('int','','',''''''))
sftrishape.par('d1',rsf.doc.rsfpar('float','1.','',''''''))
sftrishape.par('d2',rsf.doc.rsfpar('float','1.','',''''''))
sftrishape.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sftrishape.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sftrishape.par('zero',rsf.doc.rsfpar('float','0.','','''level surface '''))
sftrishape.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sftrishape.par('rect1',rsf.doc.rsfpar('int','1','',''''''))
sftrishape.par('rect2',rsf.doc.rsfpar('int','1','','''smoothing regularization '''))
sftrishape.par('nw',rsf.doc.rsfpar('int','2','','''interpolator size '''))
sftrishape.par('fast',rsf.doc.rsfpar('bool','n','','''if y, use GMRES inversion '''))
sftrishape.par('sym',rsf.doc.rsfpar('bool','n','','''if y, use symmetric shaping '''))
sftrishape.par('tol',rsf.doc.rsfpar('float','1e-3','','''tolerance for stopping iteration '''))
sftrishape.par('pattern',rsf.doc.rsfpar('string ',desc='''pattern file for output dimensions (auxiliary input file name)'''))
sftrishape.version('1.7')
sftrishape.synopsis('''sftrishape < in.rsf > out.rsf pattern=pattern.rsf n1= n2= d1=1. d2=1. o1=0. o2=0. zero=0. niter=0 rect1=1 rect2=1 nw=2 fast=n sym=n tol=1e-3''','''''')
rsf.doc.progs['sftrishape']=sftrishape

sfunif2 = rsf.doc.rsfprog('sfunif2','system/generic/Munif2.c','''Generate 2-D layered velocity model from specified interfaces. ''')
sfunif2.par('x0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('z0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('v00',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('dvdx',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('dvdz',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('n1',rsf.doc.rsfpar('int','','','''Number of samples on the depth axis '''))
sfunif2.par('d1',rsf.doc.rsfpar('float','','','''Sampling of the depth axis '''))
sfunif2.par('o1',rsf.doc.rsfpar('float','0.','','''Origin of the depth axis '''))
sfunif2.par('label1',rsf.doc.rsfpar('string ',desc='''depth axis label '''))
sfunif2.par('unit1',rsf.doc.rsfpar('string ',desc=''''''))
sfunif2.version('1.7')
sfunif2.synopsis('''sfunif2 < surface.rsf > model.rsf x0= z0= v00= dvdx= dvdz= n1= d1= o1=0. label1= unit1=''','''
In each layer, velocity is a linear function of position.

Inspired by SU's unif2.

October 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/359-Program-of-the-month-sfunif2.html
''')
rsf.doc.progs['sfunif2']=sfunif2

sfunif3 = rsf.doc.rsfprog('sfunif3','system/generic/Munif3.c','''Generate 3-D layered velocity model from specified interfaces. ''')
sfunif3.par('x0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('y0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('z0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('v00',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('dvdx',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('dvdy',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('dvdz',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('n1',rsf.doc.rsfpar('int','','','''Number of samples on the depth axis '''))
sfunif3.par('d1',rsf.doc.rsfpar('float','','','''Sampling of the depth axis '''))
sfunif3.par('o1',rsf.doc.rsfpar('float','0.','','''Origin of the depth axis '''))
sfunif3.par('layers',rsf.doc.rsfpar('string ',desc='''file with layer properties '''))
sfunif3.version('1.7 Munif3.c 4796 2009-09-29 19:39:07Z ivlad')
sfunif3.synopsis('''sfunif3 < surface.rsf > model.rsf x0= y0= z0= v00= dvdx= dvdy= dvdz= n1= d1= o1=0. layers=''','''
Unless layers= is specified, velocity is a linear function of position inside
each layer.

Inspired by SU's unif2.
''')
rsf.doc.progs['sfunif3']=sfunif3

rsf.doc.progs['sftpow']=sfpow
