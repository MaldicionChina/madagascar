sfmf = rsf.doc.rsfprog('sfmf','user/yliu/Mmf.c','''1D median filtering. ''')
sfmf.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmf.version('1.7 Mmf.c 13867 2015-03-03 00:18:28Z sfomel')
sfmf.synopsis('''sfmf < in.rsf > out.rsf nfw= boundary=n''','''
January 2015 program of the month:
http://ahay.org/rsflog/index.php?/archives/425-Program-of-the-month-sfmf.html
''')
rsf.doc.progs['sfmf']=sfmf

