sfbyte2tif = rsf.doc.rsfprog('sfbyte2tif','user/fomels/_byte2tif.c','''Convert byte RSF to a TIFF image. ''')
sfbyte2tif.par('color',rsf.doc.rsfpar('bool','(bool)(3==n1)','',''''''))
sfbyte2tif.version('1.7')
sfbyte2tif.synopsis('''sfbyte2tif < in.rsf color=(bool)(3==n1)''','''''')
rsf.doc.progs['sfbyte2tif']=sfbyte2tif

