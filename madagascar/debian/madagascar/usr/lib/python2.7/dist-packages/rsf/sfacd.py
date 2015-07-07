import rsf.doc

sfacd = rsf.doc.rsfprog('sfacd','trip/iwave/acd/main/acd.cc','''None''')
sfacd.version('1.7')
sfacd.synopsis('''sfacd''','''''')
rsf.doc.progs['sfacd']=sfacd

sfacdvpe = rsf.doc.rsfprog('sfacdvpe','trip/iwave/acd/main/acdvpe.cc','''None''')
sfacdvpe.version('1.7')
sfacdvpe.synopsis('''sfacdvpe''','''''')
rsf.doc.progs['sfacdvpe']=sfacdvpe

