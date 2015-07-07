sffiglist = rsf.doc.rsfprog('sffiglist','user/jennings/Mfiglist.py','''Compare Vplot files in Fig and Lock directories''')
sffiglist.par('figdir',rsf.doc.rsfpar('string','','','''fig directory, default = ./Fig'''))
sffiglist.par('lockdir',rsf.doc.rsfpar('string','','','''lock directory, default = lock counterpart of figdir'''))
sffiglist.par('list',rsf.doc.rsfpar('string','','','''how much to list [none,diff,miss,all], default = all'''))
sffiglist.par('show',rsf.doc.rsfpar('string','','','''how much to show [none,diff,miss,all], default = none'''))
sffiglist.par('rsftest',rsf.doc.rsfpar('bool','n','','''write .rsftest file?'''))
sffiglist.par('copy',rsf.doc.rsfpar('bool','n','','''copy different figs from figdir to lockdir?'''))
sffiglist.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sffiglist')
sffiglist.version('1.7')
sffiglist.synopsis('''sffiglist figdir= lockdir= list= show= rsftest=n copy=n''','''Parameter figdir is path to Fig directory, default is ./Fig.
Parameter lockdir is path to Lock directory:
    If figdir is in $RSFSRC/book/[book]/[chapter]/[section],
        then default lockdir is $RSFFIGS/[book]/[chapter]/[section].
    If figdir is not in $RSFSRC/book/[book]/[chapter]/[section],
        then default lockdir is $RSFALTFIGS/[book]/[chapter]/[section].

Parameter list controls files to list, default is all.
Parameter show controls files to flip with sfpen, default is none.

list|show = none    No files, print only summary.
list|show = diff    Files that are different, determined by sfvplotdiff.
list|show = miss    Files missing from figdir or lockdir, and different files.
list|show = all     All files.

File list codes:

space   indicates files that are the same.
  -     indicates file in lockdir that is missing from figdir.
  +     indicates extra file in figdir that is missing from lockdir.
number  is return code from sfvplotdiff indicating different files.''')
rsf.doc.progs['sffiglist']=sffiglist

