sfbackdire = rsf.doc.rsfprog('sfbackdire','user/parvaneh/Mbackdire.c','''Background directivity(Dip). ''')
sfbackdire.par('verb',rsf.doc.rsfpar('bool','0','',''''''))
sfbackdire.version('1.7')
sfbackdire.synopsis('''sfbackdire < Zz.rsf > Zo.rsf verb=0''','''''')
rsf.doc.progs['sfbackdire']=sfbackdire

