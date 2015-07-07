sfspectra2 = rsf.doc.rsfprog('sfspectra2','system/generic/Mspectra2.c','''Frequency spectra in 2-D. ''')
sfspectra2.par('all',rsf.doc.rsfpar('bool','n','','''if y, compute average spectrum for all traces '''))
sfspectra2.version('1.7')
sfspectra2.synopsis('''sfspectra2 < in.rsf > out.rsf all=n''','''''')
rsf.doc.progs['sfspectra2']=sfspectra2

