sfwavmod = rsf.doc.rsfprog('sfwavmod','user/chen/Mwavmod.c','''1-2-3D finite difference modeling ''')
sfwavmod.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavmod.par('sgrid',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavmod.par('ggrid',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavmod.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwavmod.par('jt',rsf.doc.rsfpar('int','1','','''time interval in observation system '''))
sfwavmod.par('jtm',rsf.doc.rsfpar('int','100','','''time interval of wave movie '''))
sfwavmod.par('ot',rsf.doc.rsfpar('float','0.0','','''time delay '''))
sfwavmod.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfwavmod.par('wfl',rsf.doc.rsfpar('string ',desc='''wavefield movie file (auxiliary output file name)'''))
sfwavmod.version('1.7')
sfwavmod.synopsis('''sfwavmod < in.rsf vel=vel.rsf sgrid=sgrid.rsf ggrid=ggrid.rsf > dat.rsf wfl=wfl.rsf jt=1 jtm=100 ot=0.0 verb=n''','''''')
rsf.doc.progs['sfwavmod']=sfwavmod

