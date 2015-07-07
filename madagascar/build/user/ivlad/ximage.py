sfximage = rsf.doc.rsfprog('sfximage','user/ivlad/Mximage.py','''Displays a 2-D RSF file with Seismic Unix's ximage''')
sfximage.par('inp',rsf.doc.rsfpar('string','','','''Input file'''))
sfximage.par('par',rsf.doc.rsfpar('string','','','''ximage params that can't be found in RSF headr'''))
sfximage.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfximage.version('1.7')
sfximage.synopsis('''sfximage inp= par= verb=n''','''Test with:
sfspike n1=5 n2=3 nsp=3 k1=1,3,4 k2=1,2,3 > junk.rsf;
sfximage inp=junk.rsf par="perc=100 cmap=rgb1 legend=1";
You should see a picture with blue background and red blobs.
See also sfimage.''')
rsf.doc.progs['sfximage']=sfximage

