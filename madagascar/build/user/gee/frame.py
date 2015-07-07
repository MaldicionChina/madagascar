sfframe = rsf.doc.rsfprog('sfframe','user/gee/Mframe.c','''Create a frame for binning.''')
sfframe.par('xyz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfframe.par('base',rsf.doc.rsfpar('float','0.','','''base to be subtracted from z '''))
sfframe.version('1.7 Mframe.c 7107 2011-04-10 02:04:14Z ivlad')
sfframe.synopsis('''sfframe < in.rsf > out.rsf xyz=xyzs.rsf base=0.''','''''')
rsf.doc.progs['sfframe']=sfframe

