sfhwtex = rsf.doc.rsfprog('sfhwtex','system/seismic/Mhwtex.c','''Huygens wavefront tracing traveltimes ''')
sfhwtex.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhwtex.par('verb',rsf.doc.rsfpar('bool','n','','''velocity file '''))
sfhwtex.par('nt',rsf.doc.rsfpar('int','100','',''''''))
sfhwtex.par('ot',rsf.doc.rsfpar('float','0','',''''''))
sfhwtex.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfhwtex.version('1.7')
sfhwtex.synopsis('''sfhwtex < Fv.rsf sou=Fs.rsf > Fw.rsf verb=n nt=100 ot=0 dt=0.001''','''''')
rsf.doc.progs['sfhwtex']=sfhwtex

