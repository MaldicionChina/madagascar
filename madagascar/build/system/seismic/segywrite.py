sfsegywrite = rsf.doc.rsfprog('sfsegywrite','system/seismic/Msegywrite.c','''Convert an RSF dataset to SEGY or SU.''')
sfsegywrite.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsegywrite.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfsegywrite.par('endian',rsf.doc.rsfpar('bool','y','','''Whether to automatically estimate endianness or not '''))
sfsegywrite.par('su',rsf.doc.rsfpar('bool','','','''y if input is SU, n if input is SEGY '''))
sfsegywrite.par('suxdr',rsf.doc.rsfpar('bool','n','','''y, SU has XDR support '''))
sfsegywrite.par('suxdr',rsf.doc.rsfpar('bool','n','','''y, SU has XDR support '''))
sfsegywrite.par('tape',rsf.doc.rsfpar('string ',desc='''output data '''))
sfsegywrite.par('hfile',rsf.doc.rsfpar('string ',desc='''input text data header file '''))
sfsegywrite.par('bfile',rsf.doc.rsfpar('string ',desc='''input binary data header file '''))
sfsegywrite.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfsegywrite')
sfsegywrite.version('1.7')
sfsegywrite.synopsis('''sfsegywrite < in.rsf tfile=hdr.rsf verb=n endian=y su= suxdr=n suxdr=n tape= hfile= bfile=''','''
Merges trace headers with data.

"suwrite" is equivalent to "segywrite su=y"

If bfile= and/or hfile= are not provided, they will be created automatically
using information from the trace headers.

The file for tfile= can be generated with sfsegyheader.
''')
rsf.doc.progs['sfsegywrite']=sfsegywrite

