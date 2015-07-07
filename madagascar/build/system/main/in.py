sfin = rsf.doc.rsfprog('sfin','system/main/in.c','''Display basic information about RSF files.''')
sfin.par('info',rsf.doc.rsfpar('bool','y','','''If n, only display the name of the data file. '''))
sfin.par('check',rsf.doc.rsfpar('float','2.','','''Portion of the data (in Mb) to check for zero values. '''))
sfin.par('trail',rsf.doc.rsfpar('bool','y','','''If n, skip trailing dimensions of  one '''))
sfin.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfin')
sfin.version('1.7')
sfin.synopsis('''sfin info=y check=2. trail=y [<file0.rsf] file1.rsf file2.rsf ...''','''n1,n2,... are data dimensions
o1,o2,... are axis origins
d1,d2,... are axis sampling intervals
label1,label2,... are axis labels
unit1,unit2,... are axis units
''')
rsf.doc.progs['sfin']=sfin

