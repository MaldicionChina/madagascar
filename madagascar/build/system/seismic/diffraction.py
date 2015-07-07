sfdiffraction = rsf.doc.rsfprog('sfdiffraction','system/seismic/Mdiffraction.c','''Generate diffractions in zero-offset data. ''')
sfdiffraction.par('w2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffraction.par('w12',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffraction.par('spikes',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffraction.par('freq',rsf.doc.rsfpar('float','0.2/dt','','''peak frequency for Ricker wavelet '''))
sfdiffraction.version('1.7')
sfdiffraction.synopsis('''sfdiffraction < w1.rsf w2=w2.rsf w12=w12.rsf spikes=spikes.rsf > data.rsf freq=0.2/dt''','''''')
rsf.doc.progs['sfdiffraction']=sfdiffraction

