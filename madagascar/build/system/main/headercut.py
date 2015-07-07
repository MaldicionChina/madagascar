sfheadercut = rsf.doc.rsfprog('sfheadercut','system/main/headercut.c','''Zero a portion of a dataset based on a header mask.''')
sfheadercut.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfheadercut.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheadercut')
sfheadercut.version('1.7 headerwindow.c 1303 2005-08-17 02:08:33Z fomels')
sfheadercut.synopsis('''sfheadercut mask=head.rsf < in.rsf > out.rsf''','''
The input data is a collection of traces n1xn2,
mask is an integer array of size n2.
''')
rsf.doc.progs['sfheadercut']=sfheadercut

