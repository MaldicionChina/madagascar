import rsf.doc

sfboolcmp = rsf.doc.rsfprog('sfboolcmp','user/slim/Mboolcmp.c','''Element-wise boolean comparison of values. For int/float/complex data-sets.''')
sfboolcmp.par('right_f',rsf.doc.rsfpar('float','','','''compare input (left) to a single float value (right) '''))
sfboolcmp.par('eps',rsf.doc.rsfpar('float','0','','''comparing within this range epsilon '''))
sfboolcmp.par('right',rsf.doc.rsfpar('string ',desc='''the rsf file you will be comparing to '''))
sfboolcmp.par('sign',rsf.doc.rsfpar('string ',desc=''''eq'(default),'gt','ge','lq','lt','ne'
        sign=   'eq' equal-to ( == )
        sign=   'gt' greater-than ( > )
        sign=   'ge' greater-than or equal-to ( >= )
        sign=   'lq' less-than or equal-to ( <= )
        sign=   'lt' less-than ( < )
        sign=   'ne' not-equal ( != )
	sign=   'and' the values are both non-zero ( && )
	sign=   'or' one value is non-zero ( !! )
    '''))
sfboolcmp.version('1.7')
sfboolcmp.synopsis('''sfboolcmp < in.rsf > out.rsf right_f= eps=0 right= sign=''','''This program will solve the solution to this problem:
    - [input] [sign] [right]
    - sfboolcmp <left.rsf sign=ge right=right.rsf 
    - left.rsf >= right.rsf
This will return a vector of same length as left and return 0's or 1's depending on the result of the inequality.  Optionally you can supply a right_f parameter to compare the input data to a single value.

Written by: C. Brown, UBC
Created: Nov 2007
''')
rsf.doc.progs['sfboolcmp']=sfboolcmp

sfthr = rsf.doc.rsfprog('sfthr','user/slim/Mthr.c','''Threshold float/complex inputs given a constant/varying threshold level.''')
sfthr.par('fthr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthr.par('thr',rsf.doc.rsfpar('float','','','''threshold level (positive number) '''))
sfthr.par('fthr',rsf.doc.rsfpar('string ',desc='''varying threshold level (positive number) (auxiliary input file name)'''))
sfthr.par('mode',rsf.doc.rsfpar('string ',desc=''''soft', 'hard', 'nng' (default: soft)'''))
sfthr.version('1.7')
sfthr.synopsis('''sfthr < in.rsf > out.rsf fthr=fthr.rsf thr= mode=''','''
Methods available:
- soft
- hard
- non-negative Garrote (nng)

Written by: Gilles Hennenfent & Colin Russell, UBC
Created: February 2006
''')
rsf.doc.progs['sfthr']=sfthr

sfsort = rsf.doc.rsfprog('sfsort','user/slim/Msort.c','''Sort a float/complex vector by absolute values.''')
sfsort.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfsort.par('ascmode',rsf.doc.rsfpar('bool','n','','''y=ascending; n=descending '''))
sfsort.par('dim',rsf.doc.rsfpar('int','dim','','''maximum dimension '''))
sfsort.version('1.7')
sfsort.synopsis('''sfsort < in.rsf > out.rsf memsize=sf_memsize() ascmode=n dim=dim''','''
Written by: Gilles Hennenfent & Henryk Modzelewski, UBC
Created: February 2006
''')
rsf.doc.progs['sfsort']=sfsort

sfset2zero = rsf.doc.rsfprog('sfset2zero','user/slim/Mset2zero.c','''replaces content of RSF file with zeros''')
sfset2zero.version('1.7')
sfset2zero.synopsis('''sfset2zero file1.rsf [file2.rsf ...]''','''Used to create initial guess for SLIMpy.
''')
rsf.doc.progs['sfset2zero']=sfset2zero

sffileheader = rsf.doc.rsfprog('sffileheader','user/slim/Mfileheader.c','''dumps header information to the standard output.''')
sffileheader.par('large',rsf.doc.rsfpar('bool','n','','''if y, file with large dimensions. '''))
sffileheader.par('parform',rsf.doc.rsfpar('bool','y','','''If y, print out parameter=value. If n, print out value. '''))
sffileheader.par('all',rsf.doc.rsfpar('bool','n','','''If y, print all values, icluding singleton dimensions.
       If n, drop trailing singleteon dimensions.'''))
sffileheader.version('1.7')
sffileheader.synopsis('''sffileheader < in.rsf large=n parform=y all=n''','''   Extended sffiledims.''')
rsf.doc.progs['sffileheader']=sffileheader

sffdct = rsf.doc.rsfprog('sffdct','user/slim/Mfdct.py','''''')
sffdct.par('nbs',rsf.doc.rsfpar('int','4','','''number of scale for the decomposition'''))
sffdct.par('nba',rsf.doc.rsfpar('int','8','','''number of angle at the 2nd coarsest scale'''))
sffdct.par('ac',rsf.doc.rsfpar('bool','1','','''curvelets at finest scale'''))
sffdct.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint transform'''))
sffdct.version('1.7')
sffdct.synopsis('''sffdct nbs=4 nba=8 ac=1 adj=n''','''Madagascar wrapper to the Fast Discrete Curvelet Transform (FDCT)

Requirements:
- Python API enable in Madagascar
- PyCurveLab (https://wave.eos.ubc.ca/Software/Licenced/)
- CurveLab (http://www.curvelet.org/)
''')
rsf.doc.progs['sffdct']=sffdct

sfkilltraces = rsf.doc.rsfprog('sfkilltraces','user/slim/Mkilltraces.py','''''')
sfkilltraces.par('perc',rsf.doc.rsfpar('float','.75','','''percentage of traces to remove'''))
sfkilltraces.par('maxfactor',rsf.doc.rsfpar('float','1.','','''maximum gap factor'''))
sfkilltraces.par('seed',rsf.doc.rsfpar('int','np.random.randn(','',''''''))
sfkilltraces.version('1.7')
sfkilltraces.synopsis('''sfkilltraces perc=.75 maxfactor=1. seed=np.random.randn(''','''Return mask to remove random traces in 2D and 3D using a maximum gap
size constraint
''')
rsf.doc.progs['sfkilltraces']=sfkilltraces

sfjitter = rsf.doc.rsfprog('sfjitter','user/slim/Mjitter.py','''''')
sfjitter.par('perc',rsf.doc.rsfpar('float','.75','','''percentage of traces to remove'''))
sfjitter.par('jit',rsf.doc.rsfpar('float','1/(1-perc','',''''''))
sfjitter.par('seed',rsf.doc.rsfpar('int','np.random.randn(','',''''''))
sfjitter.version('1.7')
sfjitter.synopsis('''sfjitter perc=.75 jit=1/(1-perc seed=np.random.randn(''','''Return mask to remove random traces in 2D using jittered sampling
''')
rsf.doc.progs['sfjitter']=sfjitter

