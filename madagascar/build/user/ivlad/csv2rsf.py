sfcsv2rsf = rsf.doc.rsfprog('sfcsv2rsf','user/ivlad/Mcsv2rsf.py','''Convert a delimited-text ASCII file to RSF binary floating point or int.''')
sfcsv2rsf.par('delimiter',rsf.doc.rsfpar('string',',','','''Separator between values in input file'''))
sfcsv2rsf.par('dtype',rsf.doc.rsfpar('string','float','','''Input type'''))
sfcsv2rsf.par('verb',rsf.doc.rsfpar('bool','n','','''Whether to echo n1, n2, infill/truncation'''))
sfcsv2rsf.par('debug',rsf.doc.rsfpar('bool','n','','''Extra verbosity for debugging'''))
sfcsv2rsf.par('trunc',rsf.doc.rsfpar('bool','n','','''Truncate or add zeros if nr elems in rows differs'''))
sfcsv2rsf.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfcsv2rsf.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sfcsv2rsf.par('d1',rsf.doc.rsfpar('float','1.','',''''''))
sfcsv2rsf.par('d2',rsf.doc.rsfpar('float','1.','',''''''))
sfcsv2rsf.par('unit1',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.par('unit2',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.par('label1',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.par('label2',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcsv2rsf')
sfcsv2rsf.version('1.7')
sfcsv2rsf.synopsis('''sfcsv2rsf delimiter=, dtype=float verb=n debug=n trunc=n o1=0. o2=0. d1=1. d2=1. unit1=unknown unit2=unknown label1=unknown label2=unknown''','''Zeros will be added if number of elements is not the same in each row.
n1 and n2 are computed automatically. For consistency with sfdisfil and 
sfmatmult, output is C-style order (row-first), i.e. rows in input file 
become dimension-1 columns in output. Output encoding is native. If n2=1 in
output, the second dimension will not be written to the header.''')
rsf.doc.progs['sfcsv2rsf']=sfcsv2rsf

