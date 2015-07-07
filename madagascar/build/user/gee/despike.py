sfdespike = rsf.doc.rsfprog('sfdespike','user/gee/Mdespike.c','''Remove spikes in by sliding 1-D medians. ''')
sfdespike.par('wide',rsf.doc.rsfpar('int','7','','''sliding window width '''))
sfdespike.version('1.7 Mdespike.c 11860 2014-02-22 16:38:50Z sfomel')
sfdespike.synopsis('''sfdespike < in.rsf > out.rsf wide=7''','''''')
rsf.doc.progs['sfdespike']=sfdespike

