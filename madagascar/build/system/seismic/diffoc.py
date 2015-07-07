sfdiffoc = rsf.doc.rsfprog('sfdiffoc','system/seismic/Mdiffoc.c','''Diffraction focusing test. ''')
sfdiffoc.par('v0',rsf.doc.rsfpar('float','SF_EPS','','''initial velocity '''))
sfdiffoc.par('v',rsf.doc.rsfpar('float','','','''final velocity '''))
sfdiffoc.par('pad',rsf.doc.rsfpar('int','nt','','''padding for stretch '''))
sfdiffoc.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sfdiffoc.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfdiffoc.version('1.7')
sfdiffoc.synopsis('''sfdiffoc < inp.rsf > out.rsf v0=SF_EPS v= pad=nt pad2=2*kiss_fft_next_fast_size((n2+1)/2) extend=4''','''''')
rsf.doc.progs['sfdiffoc']=sfdiffoc

