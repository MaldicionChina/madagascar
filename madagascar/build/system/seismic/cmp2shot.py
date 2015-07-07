sfcmp2shot = rsf.doc.rsfprog('sfcmp2shot','system/seismic/Mcmp2shot.c','''Convert CMPs to shots for regular 2-D geometry. ''')
sfcmp2shot.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfcmp2shot.version('1.7 Mcmp2shot.c 7107 2011-04-10 02:04:14Z ivlad')
sfcmp2shot.synopsis('''sfcmp2shot < in.rsf > out.rsf positive=y''','''''')
rsf.doc.progs['sfcmp2shot']=sfcmp2shot

