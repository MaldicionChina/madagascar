sfmflt = rsf.doc.rsfprog('sfmflt','user/chen/Mmflt.c','''3D Recursive median filter ''')
sfmflt.par('rect1',rsf.doc.rsfpar('int','1','','''filter length on 1st axis '''))
sfmflt.par('rect2',rsf.doc.rsfpar('int','0','','''filter length on 2nd axis '''))
sfmflt.par('rect3',rsf.doc.rsfpar('int','0','','''filter length on 3nd axis '''))
sfmflt.version('1.7')
sfmflt.synopsis('''sfmflt < in.rsf > out.rsf rect1=1 rect2=0 rect3=0''','''''')
rsf.doc.progs['sfmflt']=sfmflt

