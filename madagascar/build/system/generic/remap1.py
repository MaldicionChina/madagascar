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

