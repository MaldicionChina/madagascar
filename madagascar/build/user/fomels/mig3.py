sfmig3 = rsf.doc.rsfprog('sfmig3','user/fomels/Mmig3.c','''3-D Kirchhoff time migration with antialiasing. ''')
sfmig3.par('hdr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig3.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('d2',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('o2',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('n3',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('d3',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('o3',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('vel',rsf.doc.rsfpar('float','','','''migration velocity '''))
sfmig3.par('antialias',rsf.doc.rsfpar('string ',desc='''antialiasing type [triangle,flat,steep,none] '''))
sfmig3.version('1.7')
sfmig3.synopsis('''sfmig3 < in.rsf hdr=head.rsf > mig.rsf n2= d2= o2= n3= d3= o3= n1= vel= antialias=''','''''')
rsf.doc.progs['sfmig3']=sfmig3

