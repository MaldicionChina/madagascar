sfdifference = rsf.doc.rsfprog('sfdifference','user/yliu/Mdifference.c','''Difference profile of two data ''')
sfdifference.par('subtracter',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdifference.version('1.7 Mdifference.c 4796 2009-09-29 19:39:07Z ivlad')
sfdifference.synopsis('''sfdifference < in.rsf > out.rsf subtracter=sub.rsf''','''''')
rsf.doc.progs['sfdifference']=sfdifference

