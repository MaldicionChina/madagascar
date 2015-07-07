sffinstack = rsf.doc.rsfprog('sffinstack','system/seismic/Mfinstack.c','''DMO and stack by finite-difference offset continuation. ''')
sffinstack.version('1.7')
sffinstack.synopsis('''sffinstack < cmp.rsf > stk.rsf''','''''')
rsf.doc.progs['sffinstack']=sffinstack

