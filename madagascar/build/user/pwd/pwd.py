sfpwd = rsf.doc.rsfprog('sfpwd','user/pwd/Mpwd.c','''3-D plane wave destruction. ''')
sfpwd.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwd.par('both',rsf.doc.rsfpar('bool','n','','''if y, compute both left and right predictions '''))
sfpwd.par('n4',rsf.doc.rsfpar('int','2','','''what to compute in 3-D. 0: in-line, 1: cross-line, 2: both '''))
sfpwd.par('order',rsf.doc.rsfpar('int','1','','''accuracy '''))
sfpwd.par('nj1',rsf.doc.rsfpar('int','1','','''in-line aliasing '''))
sfpwd.par('nj2',rsf.doc.rsfpar('int','1','','''cross-line aliasing '''))
sfpwd.version('1.7 Mpwd.c 10160 2013-04-10 20:11:15Z sfomel')
sfpwd.synopsis('''sfpwd < in.rsf dip=dip.rsf > out.rsf both=n n4=2 order=1 nj1=1 nj2=1''','''
February 2013 program of the month:
http://www.ahay.org/rsflog/index.php?/archives/321-Program-of-the-month-sfpwd.html
''')
rsf.doc.progs['sfpwd']=sfpwd

