sfgpurayt = rsf.doc.rsfprog('sfgpurayt','user/jmonsegny/Mgpurayt.cu','''Parallel shortest path ray tracing''')
sfgpurayt.par('ray',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpurayt.par('ctime',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpurayt.par('sx',rsf.doc.rsfpar('','0','','''Horizontal node source coordinate (int)'''))
sfgpurayt.par('sz',rsf.doc.rsfpar('','0','','''Vertical node source coordinate (int)'''))
sfgpurayt.par('bs',rsf.doc.rsfpar('','16','','''Cuda block is a square with bs*bs threads. Must divide dimensions of in.rsf, bs >= 1 (int)'''))
sfgpurayt.par('ord',rsf.doc.rsfpar('','3','','''Forward star has (ord*ord-1) nodes, ord >= 1 (int)'''))
sfgpurayt.par('dx',rsf.doc.rsfpar('','1.0f','','''Horizontal and vertical separation between nodes, dx > 0.0 (float)'''))
sfgpurayt.par('ray',rsf.doc.rsfpar('','','','''Output file for a sfgraph compatible ray file. Empty for no ray output.'''))
sfgpurayt.par('ctime',rsf.doc.rsfpar('','','','''Output rsf file for computation time. Empty for no computation time output.'''))
sfgpurayt.version('1.7')
sfgpurayt.synopsis('''sfgpurayt < in.rsf > out.rsf ray=rayout.rsf ctime=ctimeout.rsf sx=0 sz=0 bs=16 ord=3 dx=1.0f ray= ctime=''','''''')
rsf.doc.progs['sfgpurayt']=sfgpurayt

