sfheaderwindow = rsf.doc.rsfprog('sfheaderwindow','system/main/headerwindow.c','''Window a dataset based on a header mask.''')
sfheaderwindow.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfheaderwindow.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfheaderwindow.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheaderwindow')
sfheaderwindow.version('1.7 headerwindow.c 13686 2014-12-15 00:23:45Z sfomel')
sfheaderwindow.synopsis('''sfheaderwindow mask=head.rsf < in.rsf > out.rsf inv=n''','''
The input data is a collection of traces n1xn2,
mask is an integer array os size n2, windowed is n1xm2,
where m2 is the number of nonzero elements in mask.
''')
rsf.doc.progs['sfheaderwindow']=sfheaderwindow

