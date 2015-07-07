sfwiki2static = rsf.doc.rsfprog('sfwiki2static','user/ivlad/Mwiki2static.py','''Downloads the Madagascar wiki as static html''')
sfwiki2static.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag'''))
sfwiki2static.par('outdir',rsf.doc.rsfpar('string','.','',''''''))
sfwiki2static.version('1.7')
sfwiki2static.synopsis('''sfwiki2static verb=n outdir=.''','''Wiki pages are downloaded every time. Main_Page is moved to index.html
Html files in local dir are deleted if not present on the wiki, in order
to avoid accumulation of dead wiki pages. To save bandwidth cost and
download time, images and linked documents are downloaded only if a
local copy is not present.''')
rsf.doc.progs['sfwiki2static']=sfwiki2static

