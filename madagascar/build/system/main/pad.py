sfpad = rsf.doc.rsfprog('sfpad','system/main/pad.c','''Pad a dataset with zeros.''')
sfpad.par('beg#',rsf.doc.rsfpar('int','0','','''the number of zeros to add before the beginning of #-th axis '''))
sfpad.par('end#',rsf.doc.rsfpar('int','0','','''the number of zeros to add after the end of #-th axis '''))
sfpad.par('n#',rsf.doc.rsfpar('int','','','''the output length of #-th axis - padding at the end '''))
sfpad.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfpad')
sfpad.version('1.7 pad.c 11208 2013-10-28 23:36:36Z sfomel')
sfpad.synopsis('''sfpad < in.rsf > out.rsf beg#=0 end#=0 n#=''','''
   n#out is equivalent to n#, both of them overwrite end#.

   Other parameters from the command line are passed to the output (similar to sfput).
''')
rsf.doc.progs['sfpad']=sfpad

