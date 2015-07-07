sfdisfil = rsf.doc.rsfprog('sfdisfil','system/main/disfil.c','''Print out data values.''')
sfdisfil.par('number',rsf.doc.rsfpar('bool','y','','''If number the elements '''))
sfdisfil.par('col',rsf.doc.rsfpar('int','0','','''Number of columns.
       The default depends on the data type:
       10 for int and char,
       5 for float,
       3 for complex '''))
sfdisfil.par('format',rsf.doc.rsfpar('string ',desc='''Format for numbers (printf-style).
       The default depends on the data type:
       "%4d " for int and char,
       "%13.4g" for float,
       "%10.4g,%10.4gi" for complex '''))
sfdisfil.par('header',rsf.doc.rsfpar('string ',desc='''Optional header string to output before data '''))
sfdisfil.par('trailer',rsf.doc.rsfpar('string ',desc='''Optional trailer string to output after data '''))
sfdisfil.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfdisfil')
sfdisfil.version('1.7 disfil.c 7791 2011-10-29 13:22:26Z sfomel')
sfdisfil.synopsis('''sfdisfil < in.rsf number=y col=0 format= header= trailer=''','''
Alternatively, use sfdd and convert to ASCII form.
''')
rsf.doc.progs['sfdisfil']=sfdisfil

