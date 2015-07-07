sfcdottest = rsf.doc.rsfprog('sfcdottest','system/main/cdottest.c','''Generic dot-product test for complex linear operators with adjoints ''')
sfcdottest.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdottest.par('dat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdottest.version('1.7')
sfcdottest.synopsis('''sfcdottest mod=mod.rsf dat=dat.rsf > pip.rsf''','''''')
rsf.doc.progs['sfcdottest']=sfcdottest

