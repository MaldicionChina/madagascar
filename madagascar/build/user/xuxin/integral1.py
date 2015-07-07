sfintegral1 = rsf.doc.rsfprog('sfintegral1','user/xuxin/Mintegral1.c','''integration ''')
sfintegral1.par('rule',rsf.doc.rsfpar('string ',desc='''t, s : quadrature rules '''))
sfintegral1.version('1.7')
sfintegral1.synopsis('''sfintegral1 < Fin.rsf > Fout.rsf rule=''','''''')
rsf.doc.progs['sfintegral1']=sfintegral1

