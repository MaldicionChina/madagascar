sfshotholes = rsf.doc.rsfprog('sfshotholes','system/seismic/Mshotholes.c','''Remove random shot gathers from a 2-D dataset. ''')
sfshotholes.par('perc',rsf.doc.rsfpar('float','0.75','','''how many shots to remove '''))
sfshotholes.version('1.7')
sfshotholes.synopsis('''sfshotholes < in.rsf > mask.rsf perc=0.75''','''''')
rsf.doc.progs['sfshotholes']=sfshotholes

