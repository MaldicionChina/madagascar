sfpatch = rsf.doc.rsfprog('sfpatch','user/fomels/Mpatch.c','''Patching (N-dimensional). ''')
sfpatch.par('n0',rsf.doc.rsfpar('ints','','','''data dimensions (for inv=y)  [dim]'''))
sfpatch.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sfpatch.par('p',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sfpatch.par('inv',rsf.doc.rsfpar('bool','n','','''inverse or forward operation '''))
sfpatch.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpatch.par('weight',rsf.doc.rsfpar('bool','n','','''if y, apply weighting to each patch '''))
sfpatch.par('dim',rsf.doc.rsfpar('int','dim0','',''''''))
sfpatch.version('1.7')
sfpatch.synopsis('''sfpatch < in.rsf > out.rsf n0= w= p= inv=n verb=n weight=n dim=dim0''','''
w is window size (defaults to n1,n2,...)
p is number of patches in different dimensions (defaults to 1,1,...)

If inv=n, the number of output dimensions is twice the number of input dimensions.
If inv=y, the number of output dimensions is half the number of input dimensions.

September 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/357-Program-of-the-month-sfpatch.html
''')
rsf.doc.progs['sfpatch']=sfpatch

