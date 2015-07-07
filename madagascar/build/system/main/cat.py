sfcat = rsf.doc.rsfprog('sfcat','system/main/cat.c','''Concatenate datasets. ''')
sfcat.par('order',rsf.doc.rsfpar('ints','','','''concatenation order  [nin]'''))
sfcat.par('space',rsf.doc.rsfpar('bool','','','''Insert additional space.
	   y is default for sfmerge, n is default for sfcat '''))
sfcat.par('axis',rsf.doc.rsfpar('int','3','','''Axis being merged '''))
sfcat.par('nspace',rsf.doc.rsfpar('int','(int) (ni/(20*nin) + 1)','','''if space=y, number of traces to insert '''))
sfcat.par('o',rsf.doc.rsfpar('float','','','''axis origin '''))
sfcat.par('d',rsf.doc.rsfpar('float','','','''axis sampling '''))
sfcat.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcat')
sfcat.version('1.7 cat.c 13759 2015-01-09 03:51:11Z sfomel')
sfcat.synopsis('''sfcat > out.rsf order= space= axis=3 nspace=(int) (ni/(20*nin) + 1) o= d= [<file0.rsf] file1.rsf file2.rsf ... ''','''sfmerge inserts additional space between merged data.
''')
rsf.doc.progs['sfcat']=sfcat

