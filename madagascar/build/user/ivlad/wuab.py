sfwuab = rsf.doc.rsfprog('sfwuab','user/ivlad/Mwuab.py','''Wrapper for Utilities Acting on Binaries''')
sfwuab.par('prog',rsf.doc.rsfpar('string','','','''Non-madagascar utility'''))
sfwuab.par('inp',rsf.doc.rsfpar('string','','','''Input file'''))
sfwuab.par('tpar',rsf.doc.rsfpar('string','','','''Translated params, i.e.: "ni1=n1 ni2=n2"'''))
sfwuab.par('ipar',rsf.doc.rsfpar('string','','','''Independent params, i.e. "perc=100 cmap=rgb"'''))
sfwuab.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfwuab.version('1.7')
sfwuab.synopsis('''sfwuab prog= inp= tpar= ipar= verb=n''','''''')
rsf.doc.progs['sfwuab']=sfwuab

