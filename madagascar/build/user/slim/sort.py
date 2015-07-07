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

