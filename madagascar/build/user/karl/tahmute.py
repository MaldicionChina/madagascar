sftahmute = rsf.doc.rsfprog('sftahmute','user/karl/Mtahmute.c','''Read Trace And Header (tah) from standard input, MUTE ''')
sftahmute.par('xmute',rsf.doc.rsfpar('floats','','',''' [numxmute]'''))
sftahmute.par('tmute',rsf.doc.rsfpar('floats','','',''' [numtmute]'''))
sftahmute.par('verbose',rsf.doc.rsfpar('int','1','','''\n
       flag to control amount of print
       0 terse, 1 informative, 2 chatty, 3 debug
    '''))
sftahmute.par('ntaper',rsf.doc.rsfpar('int','12','','''\n
       length of the taper on the stack mute
    '''))
sftahmute.version('1.7')
sftahmute.synopsis('''sftahmute < in.rsf > out.rsf xmute= tmute= verbose=1 ntaper=12''','''''')
rsf.doc.progs['sftahmute']=sftahmute

