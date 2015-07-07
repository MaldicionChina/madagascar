sfspike = rsf.doc.rsfprog('sfspike','system/main/spike.c','''Generate simple data: spikes, boxes, planes, constants. ''')
sfspike.par('mag',rsf.doc.rsfpar('floats','','','''spike magnitudes  [nsp]'''))
sfspike.par('nsp',rsf.doc.rsfpar('int','1','','''Number of spikes '''))
sfspike.par('k#',rsf.doc.rsfpar('ints','[0,...]','','''spike starting position  [nsp]'''))
sfspike.par('l#',rsf.doc.rsfpar('ints','[k1,k2,...]','','''spike ending position  [nsp]'''))
sfspike.par('p#',rsf.doc.rsfpar('floats','[0,...]','','''spike inclination (in samples)  [nsp]'''))
sfspike.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfspike.par('o#',rsf.doc.rsfpar('float','[0,0,...]','','''origin on #-th axis '''))
sfspike.par('d#',rsf.doc.rsfpar('float','[0.004,0.1,0.1,...]','','''sampling on #-th axis '''))
sfspike.par('label#',rsf.doc.rsfpar('string','[Time,Distance,Distance,...]','','''label on #-th axis '''))
sfspike.par('unit#',rsf.doc.rsfpar('string','[s,km,km,...]','','''unit on #-th axis '''))
sfspike.par('title',rsf.doc.rsfpar('string ',desc='''title for plots '''))
sfspike.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfspike')
sfspike.version('1.7 spike.c 8430 2012-05-01 15:29:37Z sfomel')
sfspike.synopsis('''sfspike < in.rsf > spike.rsf mag= nsp=1 k#=[0,...] l#=[k1,k2,...] p#=[0,...] n#= o#=[0,0,...] d#=[0.004,0.1,0.1,...] label#=[Time,Distance,Distance,...] unit#=[s,km,km,...] title=''','''
Spike positioning is given in samples and starts with 1.
''')
rsf.doc.progs['sfspike']=sfspike

