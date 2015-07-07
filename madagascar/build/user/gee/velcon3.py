sfvelcon3 = rsf.doc.rsfprog('sfvelcon3','user/gee/Mvelcon3.c','''3-D finite-difference velocity continuation on a helix ''')
sfvelcon3.par('adj',rsf.doc.rsfpar('bool','y','','''forward or backward continuation '''))
sfvelcon3.par('inv',rsf.doc.rsfpar('int','1','','''inversion type '''))
sfvelcon3.par('nv',rsf.doc.rsfpar('int','nt','','''velocity steps '''))
sfvelcon3.par('vel',rsf.doc.rsfpar('float','1.','','''initial velocity '''))
sfvelcon3.version('1.7')
sfvelcon3.synopsis('''sfvelcon3 < inp.rsf > out.rsf adj=y inv=1 nv=nt vel=1.''','''''')
rsf.doc.progs['sfvelcon3']=sfvelcon3

