sfdespike2 = rsf.doc.rsfprog('sfdespike2','user/gee/Mdespike2.c','''Remove spikes in by sliding 2-D medians. ''')
sfdespike2.par('wide1',rsf.doc.rsfpar('int','5','',''''''))
sfdespike2.par('wide2',rsf.doc.rsfpar('int','5','','''sliding window width '''))
sfdespike2.version('1.7')
sfdespike2.synopsis('''sfdespike2 < in.rsf > out.rsf wide1=5 wide2=5''','''''')
rsf.doc.progs['sfdespike2']=sfdespike2

