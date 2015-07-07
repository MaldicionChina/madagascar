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

