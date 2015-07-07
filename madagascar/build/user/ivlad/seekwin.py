sfseekwin = rsf.doc.rsfprog('sfseekwin','user/ivlad/Mseekwin.f90','''Cannot take input from a pipe because stdin cannot be seeked through''')
sfseekwin.par('whence',rsf.doc.rsfpar('','sf_seek_set','',''''''))
sfseekwin.par('nseek',rsf.doc.rsfpar('','10         ','',''''''))
sfseekwin.par('nread',rsf.doc.rsfpar('','10         ','',''''''))
sfseekwin.version('1.7')
sfseekwin.synopsis('''sfseekwin < in.rsf > out.rsf whence=sf_seek_set nseek=10          nread=10         ''','''''')
rsf.doc.progs['sfseekwin']=sfseekwin

