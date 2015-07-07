sfmoveout = rsf.doc.rsfprog('sfmoveout','system/seismic/Mmoveout.c','''Put spikes at an arbitrary moveout ''')
sfmoveout.par('n1',rsf.doc.rsfpar('int','','','''time samples '''))
sfmoveout.par('d1',rsf.doc.rsfpar('float','1.','','''time sampling '''))
sfmoveout.par('o1',rsf.doc.rsfpar('float','0.','','''time origin '''))
sfmoveout.par('eps',rsf.doc.rsfpar('float','0.1','','''stretch regularization '''))
sfmoveout.par('nw',rsf.doc.rsfpar('int','10','','''wavelet length '''))
sfmoveout.version('1.7')
sfmoveout.synopsis('''sfmoveout < warp.rsf > out.rsf n1= d1=1. o1=0. eps=0.1 nw=10''','''''')
rsf.doc.progs['sfmoveout']=sfmoveout

