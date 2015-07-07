sfdottest = rsf.doc.rsfprog('sfdottest','system/main/dottest.c','''Generic dot-product test for linear operators with adjoints ''')
sfdottest.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdottest.par('dat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdottest.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfdottest')
sfdottest.version('1.7')
sfdottest.synopsis('''sfdottest mod=mod.rsf dat=dat.rsf > pip.rsf''','''''')
rsf.doc.progs['sfdottest']=sfdottest

