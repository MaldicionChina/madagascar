sfdd = rsf.doc.rsfprog('sfdd','system/main/dd.c','''Convert between different formats. ''')
sfdd.par('trunc',rsf.doc.rsfpar('bool','n','','''Truncate or round to nearest when converting from float to int/short '''))
sfdd.par('line',rsf.doc.rsfpar('int','8','','''Number of numbers per line (for conversion to ASCII) '''))
sfdd.par('ibm',rsf.doc.rsfpar('bool','n','','''Special case - assume integers actually represent IBM floats '''))
sfdd.par('form',rsf.doc.rsfpar('string ',desc='''ascii, native, xdr '''))
sfdd.par('type',rsf.doc.rsfpar('string ',desc='''int, float, complex, short '''))
sfdd.par('format',rsf.doc.rsfpar('string ',desc='''Element format (for conversion to ASCII) '''))
sfdd.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfdd')
sfdd.version('1.7')
sfdd.synopsis('''sfdd < in.rsf > out.rsf trunc=n line=8 ibm=n form= type= format=''','''''')
rsf.doc.progs['sfdd']=sfdd

