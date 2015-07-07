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

