sfbyte2jpg = rsf.doc.rsfprog('sfbyte2jpg','user/fomels/_byte2jpg.c','''Convert byte RSF to a JPEG image. ''')
sfbyte2jpg.par('color',rsf.doc.rsfpar('bool','(bool)(3==n1)','',''''''))
sfbyte2jpg.version('1.7')
sfbyte2jpg.synopsis('''sfbyte2jpg < in.rsf color=(bool)(3==n1)''','''''')
rsf.doc.progs['sfbyte2jpg']=sfbyte2jpg

