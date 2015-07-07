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

