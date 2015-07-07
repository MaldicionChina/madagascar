sfrtoc = rsf.doc.rsfprog('sfrtoc','system/main/rtoc.c','''Convert real data to complex (by adding zero imaginary part).''')
sfrtoc.par('pair',rsf.doc.rsfpar('bool','n','','''y - use odd elements for real part and even ones for imaginary part '''))
sfrtoc.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfrtoc')
sfrtoc.version('1.7 rtoc.c 9248 2012-10-04 22:44:29Z vovizmus')
sfrtoc.synopsis('''sfrtoc < real.rsf > cmplx.rsf pair=n''','''
See also: sfcmplx
''')
rsf.doc.progs['sfrtoc']=sfrtoc

