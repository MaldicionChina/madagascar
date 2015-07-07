sfintbin3 = rsf.doc.rsfprog('sfintbin3','system/seismic/Mintbin3.c','''4-D data binning. ''')
sfintbin3.par('xkey',rsf.doc.rsfpar('int','','','''x key number (if no xk), default is fldr '''))
sfintbin3.par('ykey',rsf.doc.rsfpar('int','','','''y key number (if no yk), default is iline '''))
sfintbin3.par('zkey',rsf.doc.rsfpar('int','','','''z key number (if no zk), default is xline '''))
sfintbin3.par('xmin',rsf.doc.rsfpar('int','','','''x minimum '''))
sfintbin3.par('xmax',rsf.doc.rsfpar('int','','','''x maximum '''))
sfintbin3.par('ymin',rsf.doc.rsfpar('int','','','''y minimum '''))
sfintbin3.par('ymax',rsf.doc.rsfpar('int','','','''y maximum '''))
sfintbin3.par('zmin',rsf.doc.rsfpar('int','','','''z minimum '''))
sfintbin3.par('zmax',rsf.doc.rsfpar('int','','','''z maximum '''))
sfintbin3.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfintbin3.par('xk',rsf.doc.rsfpar('string ',desc='''x key name '''))
sfintbin3.par('yk',rsf.doc.rsfpar('string ',desc='''y key name '''))
sfintbin3.par('zk',rsf.doc.rsfpar('string ',desc='''z key name '''))
sfintbin3.par('mask',rsf.doc.rsfpar('string ',desc='''output mask file '''))
sfintbin3.version('1.7')
sfintbin3.synopsis('''sfintbin3 < in.rsf > out.rsf xkey= ykey= zkey= xmin= xmax= ymin= ymax= zmin= zmax= head= xk= yk= zk= mask=''','''
   if xkey < 0, the first axis indexes traces in a gather like cdpt.
''')
rsf.doc.progs['sfintbin3']=sfintbin3

