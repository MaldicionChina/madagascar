sfagc = rsf.doc.rsfprog('sfagc','system/generic/Magc.c','''Automatic gain control. ''')
sfagc.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfagc.par('rect#',rsf.doc.rsfpar('int','(125,1,1,...)','','''smoothing radius on #-th axis '''))
sfagc.version('1.7')
sfagc.synopsis('''sfagc < in.rsf > out.rsf repeat=1 rect#=(125,1,1,...)''','''
October 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/271-Program-of-the-month-sfagc.html
''')
rsf.doc.progs['sfagc']=sfagc

