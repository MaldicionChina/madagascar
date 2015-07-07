sfsimidenoise = rsf.doc.rsfprog('sfsimidenoise','user/chenyk/Msimidenoise.c','''Random noise attenuation using local similarity ''')
sfsimidenoise.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimidenoise.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfsimidenoise.version('1.7')
sfsimidenoise.synopsis('''sfsimidenoise < in.rsf > out.rsf similarity=simi.rsf thr=''','''''')
rsf.doc.progs['sfsimidenoise']=sfsimidenoise

