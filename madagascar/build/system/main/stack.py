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

