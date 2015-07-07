sfmulticheck = rsf.doc.rsfprog('sfmulticheck','user/ivlad/Mmulticheck.c','''Check whether all values in a dataset are a multiple of a factor or not ''')
sfmulticheck.par('i_fac',rsf.doc.rsfpar('int','','',''''''))
sfmulticheck.version('1.7')
sfmulticheck.synopsis('''sfmulticheck < in.rsf i_fac=''','''''')
rsf.doc.progs['sfmulticheck']=sfmulticheck

