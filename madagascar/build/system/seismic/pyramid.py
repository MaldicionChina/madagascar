sfpyramid = rsf.doc.rsfprog('sfpyramid','system/seismic/Mpyramid.c','''Pyramid transform ''')
sfpyramid.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfpyramid.par('nu',rsf.doc.rsfpar('int','','',''''''))
sfpyramid.par('du',rsf.doc.rsfpar('float','dx','',''''''))
sfpyramid.par('u0',rsf.doc.rsfpar('float','x0','',''''''))
sfpyramid.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfpyramid.version('1.7')
sfpyramid.synopsis('''sfpyramid < in.rsf > out.rsf inv=n nu= du=dx u0=x0 eps=0.01''','''''')
rsf.doc.progs['sfpyramid']=sfpyramid

