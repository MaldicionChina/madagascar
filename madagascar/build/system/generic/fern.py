sffern = rsf.doc.rsfprog('sffern','system/generic/Mfern.c','''Generate fractal fern. ''')
sffern.par('n',rsf.doc.rsfpar('int','1000','','''number of points '''))
sffern.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sffern.par('angle',rsf.doc.rsfpar('bool','y','','''if y, use more angular fern '''))
sffern.version('1.7')
sffern.synopsis('''sffern > out.rsf n=1000 seed=time(NULL) angle=y''','''''')
rsf.doc.progs['sffern']=sffern

