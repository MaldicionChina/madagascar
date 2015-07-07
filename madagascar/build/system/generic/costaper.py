sfcostaper = rsf.doc.rsfprog('sfcostaper','system/generic/Mcostaper.c','''Cosine taper around the borders (N-D). ''')
sfcostaper.par('nw#',rsf.doc.rsfpar('int','0','','''tapering on #-th axis '''))
sfcostaper.version('1.7')
sfcostaper.synopsis('''sfcostaper < in.rsf > out.rsf nw#=0''','''
April 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/381-Program-of-the-month-sfcostaper.html 
''')
rsf.doc.progs['sfcostaper']=sfcostaper

