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

