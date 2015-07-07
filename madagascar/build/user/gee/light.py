sflight = rsf.doc.rsfprog('sflight','user/gee/Mlight.c','''Apply 2-D directional high-pass to highlight data.''')
sflight.par('ax',rsf.doc.rsfpar('float','1.','','''x direction '''))
sflight.par('ay',rsf.doc.rsfpar('float','1.','','''y direction '''))
sflight.par('eps',rsf.doc.rsfpar('float','0.','','''highpass filter parameter; if eps=0, apply derivative '''))
sflight.version('1.7 Mlight.c 7107 2011-04-10 02:04:14Z ivlad')
sflight.synopsis('''sflight < in.rsf > out.rsf ax=1. ay=1. eps=0.''','''''')
rsf.doc.progs['sflight']=sflight

