sfintbin = rsf.doc.rsfprog('sfintbin','system/seismic/Mintbin.c','''Data binning by trace sorting. ''')
sfintbin.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfintbin.par('xkey',rsf.doc.rsfpar('int','','','''x key number (if no xk), default is fldr '''))
sfintbin.par('ykey',rsf.doc.rsfpar('int','','','''y key number (if no yk), default is tracf '''))
sfintbin.par('xmin',rsf.doc.rsfpar('int','','','''x minimum '''))
sfintbin.par('xmax',rsf.doc.rsfpar('int','','','''x maximum '''))
sfintbin.par('ymin',rsf.doc.rsfpar('int','','','''y minimum '''))
sfintbin.par('ymax',rsf.doc.rsfpar('int','','','''y maximum '''))
sfintbin.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfintbin.par('xk',rsf.doc.rsfpar('string ',desc='''x key name '''))
sfintbin.par('yk',rsf.doc.rsfpar('string ',desc='''y key name '''))
sfintbin.par('map',rsf.doc.rsfpar('string ',desc='''output map file '''))
sfintbin.par('mask',rsf.doc.rsfpar('string ',desc='''output mask file '''))
sfintbin.version('1.7 Mintbin.c 13909 2015-03-12 22:47:41Z sfomel')
sfintbin.synopsis('''sfintbin < in.rsf > out.rsf inv=n xkey= ykey= xmin= xmax= ymin= ymax= head= xk= yk= map= mask=''','''
If inv=n, the input is 2-D (n1 x ntr). The output is 3-D (n1 x n2 x n3), n2 and
n3 correspond to two selected keys from the header file. 

If inv=y, the input is 3-D, and the output is 2-D.

if xkey < 0, the first axis indexes traces in a gather like cdpt.
''')
rsf.doc.progs['sfintbin']=sfintbin

