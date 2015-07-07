sfreverse = rsf.doc.rsfprog('sfreverse','system/main/reverse.c','''Reverse one or more axes in the data hypercube. ''')
sfreverse.par('which',rsf.doc.rsfpar('int','-1','','''Which axis to reverse.
       To reverse a given axis, start with 0,
       add 1 to number to reverse n1 dimension,
       add 2 to number to reverse n2 dimension,
       add 4 to number to reverse n3 dimension, etc.
       Thus, which=7 would reverse the first three dimensions,
       which=5 just n1 and n3, etc.
       which=0 will just pass the input on through unchanged. '''))
sfreverse.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfreverse.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfreverse.par('opt',rsf.doc.rsfpar('string ',desc='''If y, change o and d parameters on the reversed axis;
       if i, don't change o and d '''))
sfreverse.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfreverse')
sfreverse.version('1.7')
sfreverse.synopsis('''sfreverse < in.rsf > out.rsf which=-1 verb=n memsize=sf_memsize() opt=''','''''')
rsf.doc.progs['sfreverse']=sfreverse

