sfreal = rsf.doc.rsfprog('sfreal','system/main/real.c','''Extract real (sfreal) or imaginary (sfimag) part of a complex dataset. ''')
sfreal.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfreal')
sfreal.version('1.7')
sfreal.synopsis('''sfreal < cmplx.rsf > real.rsf''','''''')
rsf.doc.progs['sfreal']=sfreal

