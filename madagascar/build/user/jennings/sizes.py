sfsizes = rsf.doc.rsfprog('sfsizes','user/jennings/Msizes.c','''Display the size of RSF files.''')
sfsizes.par('files',rsf.doc.rsfpar('bool','y','','''If y, print size of each file.  If n, print only total. '''))
sfsizes.par('human',rsf.doc.rsfpar('bool','n','','''If y, print human-readable file size.  If n, print byte count. '''))
sfsizes.par('su',rsf.doc.rsfpar('bool','n','','''Same for Seismic Unix '''))
sfsizes.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfsizes')
sfsizes.version('1.7 Msizes.c 7537 2011-07-28 06:13:30Z sfomel')
sfsizes.synopsis('''sfsizes files=y human=n su=n file1.rsf file2.rsf ...''','''Prints the element size, number of elements, and number of bytes
for a list of RSF files.  Non-RSF files are ignored.
''')
rsf.doc.progs['sfsizes']=sfsizes

