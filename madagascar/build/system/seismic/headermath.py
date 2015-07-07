sfheadermath = rsf.doc.rsfprog('sfheadermath','system/seismic/Mheadermath.c','''Mathematical operations, possibly on header keys. ''')
sfheadermath.par('segy',rsf.doc.rsfpar('bool','y','','''if SEGY headers '''))
sfheadermath.par('nkey',rsf.doc.rsfpar('int','-1','','''number of key to replace '''))
sfheadermath.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfheadermath.par('key',rsf.doc.rsfpar('string ',desc='''key to replace '''))
sfheadermath.par('output',rsf.doc.rsfpar('string ',desc='''Describes the output in a mathematical notation. '''))
sfheadermath.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheadermath')
sfheadermath.version('1.7')
sfheadermath.synopsis('''sfheadermath < in.rsf > out.rsf segy=y nkey=-1 memsize=sf_memsize() key= output=''','''
Known functions for float data: 
cos,  sin,  tan,  acos,  asin,  atan, 
cosh, sinh, tanh, acosh, asinh, atanh,
exp,  log,  sqrt, abs, erf, erfc, sign

Known functions for int data: sign, abs

See also sfmath.

An addition operation can be performed by sfadd.
''')
rsf.doc.progs['sfheadermath']=sfheadermath

