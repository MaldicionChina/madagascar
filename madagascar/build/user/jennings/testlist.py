sftestlist = rsf.doc.rsfprog('sftestlist','user/jennings/Mtestlist.py','''Inventory test results of Madagascar example book directories.''')
sftestlist.par('levels',rsf.doc.rsfpar('int','3','','''directory search depth'''))
sftestlist.par('outfile',rsf.doc.rsfpar('string','','','''file name for detailed inventory table, default none'''))
sftestlist.par('untested',rsf.doc.rsfpar('bool','n','','''list untested examples?'''))
sftestlist.version('1.7')
sftestlist.synopsis('''sftestlist levels=3 outfile= untested=n''','''Scan a directory tree (or list of directory trees) to a given depth,
and inventory the contents and test results.

The inventory occurs only at the specified depth (default 3), not the
intervening depths.  Directories named .svn are skipped.  Only
directories containing an SConstruct file are listed.

Examples (from within $RSFSRC):

sftestlist book                         # inventory of book
sftestlist levels=2 book/geostats       # inventory of book/geostats
''')
rsf.doc.progs['sftestlist']=sftestlist

