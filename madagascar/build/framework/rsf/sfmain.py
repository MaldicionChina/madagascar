import rsf.doc

sfadd = rsf.doc.rsfprog('sfadd','system/main/add.c','''Add, multiply, or divide  RSF datasets.''')
sfadd.par('scale',rsf.doc.rsfpar('floats','','','''Scalar values to multiply each dataset with  [nin]'''))
sfadd.par('add',rsf.doc.rsfpar('floats','','','''Scalar values to add to each dataset  [nin]'''))
sfadd.par('sqrt',rsf.doc.rsfpar('bools','','','''If true take square root  [nin]'''))
sfadd.par('abs',rsf.doc.rsfpar('bools','','','''If true take absolute value  [nin]'''))
sfadd.par('log',rsf.doc.rsfpar('bools','','','''If true take logarithm  [nin]'''))
sfadd.par('exp',rsf.doc.rsfpar('bools','','','''If true compute exponential  [nin]'''))
sfadd.par('mode',rsf.doc.rsfpar('string ',desc=''''a' means add (default), 
	  'p' or 'm' means multiply, 
	  'd' means divide 
       '''))
sfadd.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfadd')
sfadd.version('1.7')
sfadd.synopsis('''sfadd > out.rsf scale= add= sqrt= abs= log= exp= mode= [< file0.rsf] file1.rsf file2.rsf ...''','''The various operations, if selected, occur in the following order:

(1) Take absolute value, abs=
(2) Add a scalar, add=
(3) Take the natural logarithm, log=
(4) Take the square root, sqrt=
(5) Multiply by a scalar, scale=
(6) Compute the base-e exponential, exp=
(7) Add, multiply, or divide the data sets, mode=

sfadd operates on integer, float, or complex data, but all the input
and output files must be of the same data type.

An alternative to sfadd is sfmath, which is more versatile, but may be
less efficient.
''')
rsf.doc.progs['sfadd']=sfadd

sfattr = rsf.doc.rsfprog('sfattr','system/main/attr.c','''Display dataset attributes.''')
sfattr.par('lval',rsf.doc.rsfpar('int','2','','''norm option, lval is a non-negative integer, computes the vector lval-norm '''))
sfattr.par('want',rsf.doc.rsfpar('string ',desc=''''all'(default), 'rms', 'mean', 'norm', 'var', 
       'std', 'max', 'min', 'nonzero', 'samples', 'short' 
        want=   'rms' displays the root mean square
        want=   'norm' displays the square norm, otherwise specified by lval.
        want=   'var' displays the variance
        want=   'std' displays the standard deviation
        want=   'nonzero' displays number of nonzero samples
        want=   'samples' displays total number of samples
        want=   'short' displays a short one-line version
     '''))
sfattr.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfattr')
sfattr.version('1.7')
sfattr.synopsis('''sfattr < in.rsf lval=2 want=''','''
Sample output from "sfspike n1=100 | sfbandpass fhi=60 | sfattr"
*******************************************
     rms =      0.992354
    mean =      0.987576
  2-norm =       9.92354
variance =    0.00955481
 std dev =     0.0977487
     max =       1.12735 at 97
     min =      0.151392 at 100
nonzero samples = 100
  total samples = 100
*******************************************

rms                = sqrt[ sum(data^2) / n ]
mean               = sum(data) / n
norm               = sum(abs(data)^lval)^(1/lval)
variance           = [ sum(data^2) - n*mean^2 ] / [ n-1 ]
standard deviation = sqrt [ variance ]
''')
rsf.doc.progs['sfattr']=sfattr

sfcat = rsf.doc.rsfprog('sfcat','system/main/cat.c','''Concatenate datasets. ''')
sfcat.par('order',rsf.doc.rsfpar('ints','','','''concatenation order  [nin]'''))
sfcat.par('space',rsf.doc.rsfpar('bool','','','''Insert additional space.
	   y is default for sfmerge, n is default for sfcat '''))
sfcat.par('axis',rsf.doc.rsfpar('int','3','','''Axis being merged '''))
sfcat.par('nspace',rsf.doc.rsfpar('int','(int) (ni/(20*nin) + 1)','','''if space=y, number of traces to insert '''))
sfcat.par('o',rsf.doc.rsfpar('float','','','''axis origin '''))
sfcat.par('d',rsf.doc.rsfpar('float','','','''axis sampling '''))
sfcat.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcat')
sfcat.version('1.7 cat.c 13759 2015-01-09 03:51:11Z sfomel')
sfcat.synopsis('''sfcat > out.rsf order= space= axis=3 nspace=(int) (ni/(20*nin) + 1) o= d= [<file0.rsf] file1.rsf file2.rsf ... ''','''sfmerge inserts additional space between merged data.
''')
rsf.doc.progs['sfcat']=sfcat

sfcconjgrad = rsf.doc.rsfprog('sfcconjgrad','system/main/cconjgrad.c','''Generic conjugate-gradient solver for linear inversion with complex data ''')
sfcconjgrad.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcconjgrad.par('niter',rsf.doc.rsfpar('int','1','','''number of iterations '''))
sfcconjgrad.version('1.7')
sfcconjgrad.synopsis('''sfcconjgrad < dat.rsf mod=mod.rsf > to.rsf < from.rsf > out.rsf niter=1''','''''')
rsf.doc.progs['sfcconjgrad']=sfcconjgrad

sfcdottest = rsf.doc.rsfprog('sfcdottest','system/main/cdottest.c','''Generic dot-product test for complex linear operators with adjoints ''')
sfcdottest.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdottest.par('dat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdottest.version('1.7')
sfcdottest.synopsis('''sfcdottest mod=mod.rsf dat=dat.rsf > pip.rsf''','''''')
rsf.doc.progs['sfcdottest']=sfcdottest

sfcmplx = rsf.doc.rsfprog('sfcmplx','system/main/cmplx.c','''Create a complex dataset from its real and imaginary parts.''')
sfcmplx.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcmplx')
sfcmplx.version('1.7')
sfcmplx.synopsis('''sfcmplx < real.rsf > cmplx.rsf real.rsf imag.rsf''','''There has to be only two input files specified and no additional parameters.
''')
rsf.doc.progs['sfcmplx']=sfcmplx

sfconjgrad = rsf.doc.rsfprog('sfconjgrad','system/main/conjgrad.c','''Generic conjugate-gradient solver for linear inversion ''')
sfconjgrad.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconjgrad.par('mwt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconjgrad.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconjgrad.par('niter',rsf.doc.rsfpar('int','1','','''number of iterations '''))
sfconjgrad.par('mwt',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfconjgrad.par('x0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfconjgrad.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfconjgrad')
sfconjgrad.version('1.7')
sfconjgrad.synopsis('''sfconjgrad < dat.rsf mod=mod.rsf mwt=mwt.rsf x0=x0.rsf > to.rsf < from.rsf > out.rsf niter=1''','''''')
rsf.doc.progs['sfconjgrad']=sfconjgrad

sfcp = rsf.doc.rsfprog('sfcp','system/main/cp.c','''Copy or move a dataset.''')
sfcp.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcp')
sfcp.version('1.7')
sfcp.synopsis('''sfcp < in.rsf > out.rsf in.rsf out.rsf''','''sfcp - copy, sfmv - move.
Mimics standard Unix commands.
''')
rsf.doc.progs['sfcp']=sfcp

sfcut = rsf.doc.rsfprog('sfcut','system/main/cut.c','''Zero a portion of the dataset.''')
sfcut.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfcut.par('j#',rsf.doc.rsfpar('int','(1,...)','','''jump in #-th dimension '''))
sfcut.par('d#',rsf.doc.rsfpar('float','(d1,d2,...)','','''sampling in #-th dimension '''))
sfcut.par('f#',rsf.doc.rsfpar('largeint','(0,...)','','''window start in #-th dimension '''))
sfcut.par('min#',rsf.doc.rsfpar('float','(o1,o2,,...)','','''minimum in #-th dimension '''))
sfcut.par('n#',rsf.doc.rsfpar('int','(0,...)','','''window size in #-th dimension '''))
sfcut.par('max#',rsf.doc.rsfpar('float','(o1+(n1-1)*d1,o2+(n1-1)*d2,,...)','','''maximum in #-th dimension '''))
sfcut.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcut')
sfcut.version('1.7')
sfcut.synopsis('''sfcut < in.rsf > out.rsf verb=n j#=(1,...) d#=(d1,d2,...) f#=(0,...) min#=(o1,o2,,...) n#=(0,...) max#=(o1+(n1-1)*d1,o2+(n1-1)*d2,,...)''','''
Reverse of window. ''')
rsf.doc.progs['sfcut']=sfcut

sfdd = rsf.doc.rsfprog('sfdd','system/main/dd.c','''Convert between different formats. ''')
sfdd.par('trunc',rsf.doc.rsfpar('bool','n','','''Truncate or round to nearest when converting from float to int/short '''))
sfdd.par('line',rsf.doc.rsfpar('int','8','','''Number of numbers per line (for conversion to ASCII) '''))
sfdd.par('ibm',rsf.doc.rsfpar('bool','n','','''Special case - assume integers actually represent IBM floats '''))
sfdd.par('form',rsf.doc.rsfpar('string ',desc='''ascii, native, xdr '''))
sfdd.par('type',rsf.doc.rsfpar('string ',desc='''int, float, complex, short '''))
sfdd.par('format',rsf.doc.rsfpar('string ',desc='''Element format (for conversion to ASCII) '''))
sfdd.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfdd')
sfdd.version('1.7')
sfdd.synopsis('''sfdd < in.rsf > out.rsf trunc=n line=8 ibm=n form= type= format=''','''''')
rsf.doc.progs['sfdd']=sfdd

sfdisfil = rsf.doc.rsfprog('sfdisfil','system/main/disfil.c','''Print out data values.''')
sfdisfil.par('number',rsf.doc.rsfpar('bool','y','','''If number the elements '''))
sfdisfil.par('col',rsf.doc.rsfpar('int','0','','''Number of columns.
       The default depends on the data type:
       10 for int and char,
       5 for float,
       3 for complex '''))
sfdisfil.par('format',rsf.doc.rsfpar('string ',desc='''Format for numbers (printf-style).
       The default depends on the data type:
       "%4d " for int and char,
       "%13.4g" for float,
       "%10.4g,%10.4gi" for complex '''))
sfdisfil.par('header',rsf.doc.rsfpar('string ',desc='''Optional header string to output before data '''))
sfdisfil.par('trailer',rsf.doc.rsfpar('string ',desc='''Optional trailer string to output after data '''))
sfdisfil.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfdisfil')
sfdisfil.version('1.7 disfil.c 7791 2011-10-29 13:22:26Z sfomel')
sfdisfil.synopsis('''sfdisfil < in.rsf number=y col=0 format= header= trailer=''','''
Alternatively, use sfdd and convert to ASCII form.
''')
rsf.doc.progs['sfdisfil']=sfdisfil

sfdottest = rsf.doc.rsfprog('sfdottest','system/main/dottest.c','''Generic dot-product test for linear operators with adjoints ''')
sfdottest.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdottest.par('dat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdottest.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfdottest')
sfdottest.version('1.7')
sfdottest.synopsis('''sfdottest mod=mod.rsf dat=dat.rsf > pip.rsf''','''''')
rsf.doc.progs['sfdottest']=sfdottest

sfget = rsf.doc.rsfprog('sfget','system/main/get.c','''Output parameters from the header.''')
sfget.par('parform',rsf.doc.rsfpar('bool','y','','''If y, print out parameter=value. If n, print out value. '''))
sfget.par('all',rsf.doc.rsfpar('bool','n','','''If output all values. '''))
sfget.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfget')
sfget.version('1.7')
sfget.synopsis('''sfget parform=y all=n par1 par2 ...''','''''')
rsf.doc.progs['sfget']=sfget

sfheadercut = rsf.doc.rsfprog('sfheadercut','system/main/headercut.c','''Zero a portion of a dataset based on a header mask.''')
sfheadercut.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfheadercut.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheadercut')
sfheadercut.version('1.7 headerwindow.c 1303 2005-08-17 02:08:33Z fomels')
sfheadercut.synopsis('''sfheadercut mask=head.rsf < in.rsf > out.rsf''','''
The input data is a collection of traces n1xn2,
mask is an integer array of size n2.
''')
rsf.doc.progs['sfheadercut']=sfheadercut

sfheadersort = rsf.doc.rsfprog('sfheadersort','system/main/headersort.c','''Sort a dataset according to a header key. ''')
sfheadersort.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfheadersort.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheadersort')
sfheadersort.version('1.7 headersort.c 13857 2015-02-22 19:18:06Z sfomel')
sfheadersort.synopsis('''sfheadersort < in.rsf > out.rsf head=''','''''')
rsf.doc.progs['sfheadersort']=sfheadersort

sfheaderwindow = rsf.doc.rsfprog('sfheaderwindow','system/main/headerwindow.c','''Window a dataset based on a header mask.''')
sfheaderwindow.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfheaderwindow.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfheaderwindow.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheaderwindow')
sfheaderwindow.version('1.7 headerwindow.c 13686 2014-12-15 00:23:45Z sfomel')
sfheaderwindow.synopsis('''sfheaderwindow mask=head.rsf < in.rsf > out.rsf inv=n''','''
The input data is a collection of traces n1xn2,
mask is an integer array os size n2, windowed is n1xm2,
where m2 is the number of nonzero elements in mask.
''')
rsf.doc.progs['sfheaderwindow']=sfheaderwindow

sfin = rsf.doc.rsfprog('sfin','system/main/in.c','''Display basic information about RSF files.''')
sfin.par('info',rsf.doc.rsfpar('bool','y','','''If n, only display the name of the data file. '''))
sfin.par('check',rsf.doc.rsfpar('float','2.','','''Portion of the data (in Mb) to check for zero values. '''))
sfin.par('trail',rsf.doc.rsfpar('bool','y','','''If n, skip trailing dimensions of  one '''))
sfin.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfin')
sfin.version('1.7')
sfin.synopsis('''sfin info=y check=2. trail=y [<file0.rsf] file1.rsf file2.rsf ...''','''n1,n2,... are data dimensions
o1,o2,... are axis origins
d1,d2,... are axis sampling intervals
label1,label2,... are axis labels
unit1,unit2,... are axis units
''')
rsf.doc.progs['sfin']=sfin

sfinterleave = rsf.doc.rsfprog('sfinterleave','system/main/interleave.c','''Combine several datasets by interleaving.''')
sfinterleave.par('axis',rsf.doc.rsfpar('int','3','','''Axis for interleaving '''))
sfinterleave.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfinterleave')
sfinterleave.version('1.7')
sfinterleave.synopsis('''sfinterleave > out.rsf axis=3 [< file0.rsf] file1.rsf file2.rsf ...''','''''')
rsf.doc.progs['sfinterleave']=sfinterleave

sfmask = rsf.doc.rsfprog('sfmask','system/main/mask.c','''Create a mask.''')
sfmask.par('min',rsf.doc.rsfpar('float','','','''minimum header value '''))
sfmask.par('max',rsf.doc.rsfpar('float','','','''maximum header value '''))
sfmask.par('min',rsf.doc.rsfpar('int','','','''minimum header value '''))
sfmask.par('max',rsf.doc.rsfpar('int','','','''maximum header value '''))
sfmask.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfmask')
sfmask.version('1.7 mask.c 7791 2011-10-29 13:22:26Z sfomel')
sfmask.synopsis('''sfmask < in.rsf > out.rsf min= max= min= max=''','''
Mask is an integer data with ones and zeros. 
Ones correspond to input values between min and max.

The output can be used with sfheaderwindow.
''')
rsf.doc.progs['sfmask']=sfmask

sfmath = rsf.doc.rsfprog('sfmath','system/main/math.c','''Mathematical operations on data files.''')
sfmath.par('nostdin',rsf.doc.rsfpar('bool','n','','''y - ignore stdin '''))
sfmath.par('n#',rsf.doc.rsfpar('largeint','','','''size of #-th axis '''))
sfmath.par('d#',rsf.doc.rsfpar('float','(1,1,...)','','''sampling on #-th axis '''))
sfmath.par('o#',rsf.doc.rsfpar('float','(0,0,...)','','''origin on #-th axis '''))
sfmath.par('label#',rsf.doc.rsfpar('string','','','''label on #-th axis '''))
sfmath.par('unit#',rsf.doc.rsfpar('string','','','''unit on #-th axis '''))
sfmath.par('type',rsf.doc.rsfpar('string ',desc='''output data type [float,complex] '''))
sfmath.par('label',rsf.doc.rsfpar('string ',desc='''data label '''))
sfmath.par('unit',rsf.doc.rsfpar('string ',desc='''data unit '''))
sfmath.par('output',rsf.doc.rsfpar('string ',desc='''Mathematical description of the output '''))
sfmath.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfmath')
sfmath.version('1.7 math.c 10506 2013-07-11 23:22:00Z sfomel')
sfmath.synopsis('''sfmath > out.rsf nostdin=n n#= d#=(1,1,...) o#=(0,0,...) label#= unit#= type= label= unit= output=''','''   
Known functions: 
cos,  sin,  tan,  acos,  asin,  atan, 
cosh, sinh, tanh, acosh, asinh, atanh,
exp,  log,  sqrt, abs,
erf,  erfc, sign (for float data),
arg,  conj, real, imag (for complex data).

sfmath will work on float or complex data, but all the input and output
files must be of the same data type.

An alternative to sfmath is sfadd, which may be more efficient, but is
less versatile.

Examples:

sfmath x=file1.rsf y=file2.rsf power=file3.rsf \
output='sin((x+2*y)^power)' > out.rsf
sfmath < file1.rsf tau=file2.rsf output='exp(tau*input)' > out.rsf
sfmath n1=100 type=complex output="exp(I*x1)" > out.rsf

Arguments which are not treated as variables in mathematical expressions:
datapath=, type=, out=

See also: sfheadermath.''')
rsf.doc.progs['sfmath']=sfmath

sfpad = rsf.doc.rsfprog('sfpad','system/main/pad.c','''Pad a dataset with zeros.''')
sfpad.par('beg#',rsf.doc.rsfpar('int','0','','''the number of zeros to add before the beginning of #-th axis '''))
sfpad.par('end#',rsf.doc.rsfpar('int','0','','''the number of zeros to add after the end of #-th axis '''))
sfpad.par('n#',rsf.doc.rsfpar('int','','','''the output length of #-th axis - padding at the end '''))
sfpad.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfpad')
sfpad.version('1.7 pad.c 11208 2013-10-28 23:36:36Z sfomel')
sfpad.synopsis('''sfpad < in.rsf > out.rsf beg#=0 end#=0 n#=''','''
   n#out is equivalent to n#, both of them overwrite end#.

   Other parameters from the command line are passed to the output (similar to sfput).
''')
rsf.doc.progs['sfpad']=sfpad

sfput = rsf.doc.rsfprog('sfput','system/main/put.c','''Input parameters into a header. ''')
sfput.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfput')
sfput.version('1.7')
sfput.synopsis('''sfput < in.rsf > out.rsf [parameter=value list]''','''''')
rsf.doc.progs['sfput']=sfput

sfreal = rsf.doc.rsfprog('sfreal','system/main/real.c','''Extract real (sfreal) or imaginary (sfimag) part of a complex dataset. ''')
sfreal.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfreal')
sfreal.version('1.7')
sfreal.synopsis('''sfreal < cmplx.rsf > real.rsf''','''''')
rsf.doc.progs['sfreal']=sfreal

sfreverse = rsf.doc.rsfprog('sfreverse','system/main/reverse.c','''Reverse one or more axes in the data hypercube. ''')
sfreverse.par('which',rsf.doc.rsfpar('int','-1','','''Which axis to reverse.
       To reverse a given axis, start with 0,
       add 1 to number to reverse n1 dimension,
       add 2 to number to reverse n2 dimension,
       add 4 to number to reverse n3 dimension, etc.
       Thus, which=7 would reverse the first three dimensions,
       which=5 just n1 and n3, etc.
       which=0 will just pass the input on through unchanged. '''))
sfreverse.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfreverse.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfreverse.par('opt',rsf.doc.rsfpar('string ',desc='''If y, change o and d parameters on the reversed axis;
       if i, don't change o and d '''))
sfreverse.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfreverse')
sfreverse.version('1.7')
sfreverse.synopsis('''sfreverse < in.rsf > out.rsf which=-1 verb=n memsize=sf_memsize() opt=''','''''')
rsf.doc.progs['sfreverse']=sfreverse

sfrm = rsf.doc.rsfprog('sfrm','system/main/rm.c','''Remove RSF files together with their data.''')
sfrm.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfrm')
sfrm.version('1.7')
sfrm.synopsis('''sfrm file1.rsf [file2.rsf ...] [-i] [-v] [-f] ''','''Mimics the standard Unix rm command.

See also: sfmv, sfcp.
''')
rsf.doc.progs['sfrm']=sfrm

sfrotate = rsf.doc.rsfprog('sfrotate','system/main/rotate.c','''Rotate a portion of one or more axes in the data hypercube. ''')
sfrotate.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfrotate.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfrotate.par('rot#',rsf.doc.rsfpar('int','(0,0,...)','','''length of #-th axis that is moved to the end '''))
sfrotate.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfrotate')
sfrotate.version('1.7 rotate.c 1729 2006-03-12 10:00:32Z fomels')
sfrotate.synopsis('''sfrotate < in.rsf > out.rsf verb=n memsize=sf_memsize() rot#=(0,0,...)''','''''')
rsf.doc.progs['sfrotate']=sfrotate

sfrtoc = rsf.doc.rsfprog('sfrtoc','system/main/rtoc.c','''Convert real data to complex (by adding zero imaginary part).''')
sfrtoc.par('pair',rsf.doc.rsfpar('bool','n','','''y - use odd elements for real part and even ones for imaginary part '''))
sfrtoc.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfrtoc')
sfrtoc.version('1.7 rtoc.c 9248 2012-10-04 22:44:29Z vovizmus')
sfrtoc.synopsis('''sfrtoc < real.rsf > cmplx.rsf pair=n''','''
See also: sfcmplx
''')
rsf.doc.progs['sfrtoc']=sfrtoc

sfscale = rsf.doc.rsfprog('sfscale','system/main/scale.c','''Scale data.''')
sfscale.par('axis',rsf.doc.rsfpar('int','0','','''Scale by maximum in the dimensions up to this axis. '''))
sfscale.par('rscale',rsf.doc.rsfpar('float','0.','','''Scale by this factor. '''))
sfscale.par('pclip',rsf.doc.rsfpar('float','100.','','''data clip percentile '''))
sfscale.par('dscale',rsf.doc.rsfpar('float','1.','','''Scale by this factor (works if rscale=0) '''))
sfscale.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfscale')
sfscale.version('1.7')
sfscale.synopsis('''sfscale < in.rsf > out.rsf axis=0 rscale=0. pclip=100. dscale=1.''','''
To scale by a constant factor, you can also use sfmath.
''')
rsf.doc.progs['sfscale']=sfscale

sfspike = rsf.doc.rsfprog('sfspike','system/main/spike.c','''Generate simple data: spikes, boxes, planes, constants. ''')
sfspike.par('mag',rsf.doc.rsfpar('floats','','','''spike magnitudes  [nsp]'''))
sfspike.par('nsp',rsf.doc.rsfpar('int','1','','''Number of spikes '''))
sfspike.par('k#',rsf.doc.rsfpar('ints','[0,...]','','''spike starting position  [nsp]'''))
sfspike.par('l#',rsf.doc.rsfpar('ints','[k1,k2,...]','','''spike ending position  [nsp]'''))
sfspike.par('p#',rsf.doc.rsfpar('floats','[0,...]','','''spike inclination (in samples)  [nsp]'''))
sfspike.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfspike.par('o#',rsf.doc.rsfpar('float','[0,0,...]','','''origin on #-th axis '''))
sfspike.par('d#',rsf.doc.rsfpar('float','[0.004,0.1,0.1,...]','','''sampling on #-th axis '''))
sfspike.par('label#',rsf.doc.rsfpar('string','[Time,Distance,Distance,...]','','''label on #-th axis '''))
sfspike.par('unit#',rsf.doc.rsfpar('string','[s,km,km,...]','','''unit on #-th axis '''))
sfspike.par('title',rsf.doc.rsfpar('string ',desc='''title for plots '''))
sfspike.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfspike')
sfspike.version('1.7 spike.c 8430 2012-05-01 15:29:37Z sfomel')
sfspike.synopsis('''sfspike < in.rsf > spike.rsf mag= nsp=1 k#=[0,...] l#=[k1,k2,...] p#=[0,...] n#= o#=[0,0,...] d#=[0.004,0.1,0.1,...] label#=[Time,Distance,Distance,...] unit#=[s,km,km,...] title=''','''
Spike positioning is given in samples and starts with 1.
''')
rsf.doc.progs['sfspike']=sfspike

sfspray = rsf.doc.rsfprog('sfspray','system/main/spray.c','''Extend a dataset by duplicating in the specified axis dimension.''')
sfspray.par('axis',rsf.doc.rsfpar('int','2','','''which axis to spray '''))
sfspray.par('n',rsf.doc.rsfpar('int','','','''Size of the newly created dimension '''))
sfspray.par('d',rsf.doc.rsfpar('float','','','''Sampling of the newly created dimension '''))
sfspray.par('o',rsf.doc.rsfpar('float','','','''Origin of the newly created dimension '''))
sfspray.par('label',rsf.doc.rsfpar('string ',desc='''Label of the newly created dimension '''))
sfspray.par('unit',rsf.doc.rsfpar('string ',desc='''Units of the newly created dimension '''))
sfspray.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfspray')
sfspray.version('1.7 spray.c 7107 2011-04-10 02:04:14Z ivlad')
sfspray.synopsis('''sfspray < in.rsf > out.rsf axis=2 n= d= o= label= unit=''','''   This operation is adjoint to sfstack.
''')
rsf.doc.progs['sfspray']=sfspray

sfstack = rsf.doc.rsfprog('sfstack','system/main/stack.c','''Stack a dataset over one of the dimensions.''')
sfstack.par('scale',rsf.doc.rsfpar('floats','','','''optionally scale before stacking  [n2]'''))
sfstack.par('axis',rsf.doc.rsfpar('int','2','','''which axis to stack. If axis=0, stack over all dimensions '''))
sfstack.par('rms',rsf.doc.rsfpar('bool','n','','''If y, compute the root-mean-square instead of stack. '''))
sfstack.par('norm',rsf.doc.rsfpar('bool','y','','''If y, normalize by fold. '''))
sfstack.par('min',rsf.doc.rsfpar('bool','n','','''If y, find minimum instead of stack.  Ignores rms and norm. '''))
sfstack.par('max',rsf.doc.rsfpar('bool','n','','''If y, find maximum instead of stack.  Ignores rms and norm. '''))
sfstack.par('prod',rsf.doc.rsfpar('bool','n','','''If y, find product instead of stack.  Ignores rms and norm. '''))
sfstack.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfstack')
sfstack.version('1.7 stack.c 13288 2014-09-26 15:14:47Z ediazp')
sfstack.synopsis('''sfstack < in.rsf > out.rsf scale= axis=2 rms=n norm=y min=n max=n prod=n''','''
This operation is adjoint to sfspray.
''')
rsf.doc.progs['sfstack']=sfstack

sftransp = rsf.doc.rsfprog('sftransp','system/main/transp.c','''Transpose two axes in a dataset. ''')
sftransp.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sftransp.par('plane',rsf.doc.rsfpar('int','','','''Two-digit number with axes to transpose. The default is 12 '''))
sftransp.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sftransp')
sftransp.version('1.7')
sftransp.synopsis('''sftransp < in.rsf > out.rsf memsize=sf_memsize() plane=''','''
If you get a "Cannot allocate memory" error, give the program a
memsize=1 command-line parameter to force out-of-core operation.
''')
rsf.doc.progs['sftransp']=sftransp

sfwindow = rsf.doc.rsfprog('sfwindow','system/main/window.c','''Window a portion of a dataset. ''')
sfwindow.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfwindow.par('squeeze',rsf.doc.rsfpar('bool','y','','''if y, squeeze dimensions equal to 1 to the end '''))
sfwindow.par('j#',rsf.doc.rsfpar('int','(1,...)','','''jump in #-th dimension '''))
sfwindow.par('d#',rsf.doc.rsfpar('float','(d1,d2,...)','','''sampling in #-th dimension '''))
sfwindow.par('f#',rsf.doc.rsfpar('largeint','(0,...)','','''window start in #-th dimension '''))
sfwindow.par('min#',rsf.doc.rsfpar('float','(o1,o2,,...)','','''minimum in #-th dimension '''))
sfwindow.par('n#',rsf.doc.rsfpar('largeint','(0,...)','','''window size in #-th dimension '''))
sfwindow.par('max#',rsf.doc.rsfpar('float','(o1+(n1-1)*d1,o2+(n1-1)*d2,,...)','','''maximum in #-th dimension '''))
sfwindow.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfwindow')
sfwindow.version('1.7')
sfwindow.synopsis('''sfwindow < in.rsf > out.rsf verb=n squeeze=y j#=(1,...) d#=(d1,d2,...) f#=(0,...) min#=(o1,o2,,...) n#=(0,...) max#=(o1+(n1-1)*d1,o2+(n1-1)*d2,,...)''','''
Other parameters from the command line are passed to the output (similar to sfput).
''')
rsf.doc.progs['sfwindow']=sfwindow

sfmpi = rsf.doc.rsfprog('sfmpi','system/main/mpi.c','''MPI wrapper for embarassingly parallel jobs. ''')
sfmpi.par('input',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpi.par('output',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpi.par('split',rsf.doc.rsfpar('int','ndim','','''axis to split '''))
sfmpi.par('join',rsf.doc.rsfpar('int','axis','','''axis to join (0 means add) '''))
sfmpi.par('input',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmpi.version('1.7')
sfmpi.synopsis('''sfmpi input=inp.rsf output=out.rsf split=ndim join=axis''','''''')
rsf.doc.progs['sfmpi']=sfmpi

sfomp = rsf.doc.rsfprog('sfomp','system/main/omp.c','''OpenMP wrapper for embarassingly parallel jobs. ''')
sfomp.par('split',rsf.doc.rsfpar('int','ndim','','''axis to split '''))
sfomp.par('join',rsf.doc.rsfpar('int','axis','','''axis to join (0 means add) '''))
sfomp.version('1.7')
sfomp.synopsis('''sfomp < inp.rsf > out.rsf split=ndim join=axis''','''''')
rsf.doc.progs['sfomp']=sfomp

rsf.doc.progs['sfmin']=sfstack
rsf.doc.progs['sfmerge']=sfcat
rsf.doc.progs['sfmul']=sfadd
rsf.doc.progs['sfmv']=sfcp
rsf.doc.progs['sfmax']=sfstack
rsf.doc.progs['sfprod']=sfstack
rsf.doc.progs['sfrcat']=sfcat
rsf.doc.progs['sfdiv']=sfadd
rsf.doc.progs['sfimag']=sfreal
