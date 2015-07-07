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

