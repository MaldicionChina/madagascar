sfexpand = rsf.doc.rsfprog('sfexpand','user/fangg/Mexpand.c','''Expand 2D data  ''')
sfexpand.par('left',rsf.doc.rsfpar('int','0.5*nx','',''''''))
sfexpand.par('right',rsf.doc.rsfpar('int','0.5*nx','',''''''))
sfexpand.par('top',rsf.doc.rsfpar('int','0','',''''''))
sfexpand.par('bottom',rsf.doc.rsfpar('int','0','',''''''))
sfexpand.version('1.7')
sfexpand.synopsis('''sfexpand > out.rsf < in.rsf left=0.5*nx right=0.5*nx top=0 bottom=0''','''''')
rsf.doc.progs['sfexpand']=sfexpand

