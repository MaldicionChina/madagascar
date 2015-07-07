sfbooklist = rsf.doc.rsfprog('sfbooklist','user/jennings/Mbooklist.py','''List properties of Madagascar example book directories.''')
sfbooklist.par('levels',rsf.doc.rsfpar('int','3','','''directory search depth'''))
sfbooklist.par('list',rsf.doc.rsfpar('string','','','''how much to list [all,filter,none], default = all'''))
sfbooklist.par('timer',rsf.doc.rsfpar('string','','','''output execution time [log,file,none], default = none'''))
sfbooklist.par('rsfproj',rsf.doc.rsfpar('string','','','''rsfproj filter [yes,no,both], default = yes'''))
sfbooklist.par('size',rsf.doc.rsfpar('int','1024**2','','''max data size filter (MB)'''))
sfbooklist.par('uses',rsf.doc.rsfpar('string','','','''uses filter, default = any'''))
sfbooklist.par('nofetch',rsf.doc.rsfpar('bool','y','','''fetch-no-data filter'''))
sfbooklist.par('public',rsf.doc.rsfpar('bool','n','','''fetch-public-data filter'''))
sfbooklist.par('private',rsf.doc.rsfpar('bool','n','','''fetch-private-data filter'''))
sfbooklist.par('local',rsf.doc.rsfpar('bool','n','','''fetch-local-data filter'''))
sfbooklist.par('command',rsf.doc.rsfpar('string','','','''command to execute in each directory, default = none'''))
sfbooklist.par('skipfile',rsf.doc.rsfpar('string','','','''file with list of directories to skip'''))
sfbooklist.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfbooklist')
sfbooklist.version('1.7')
sfbooklist.synopsis('''sfbooklist levels=3 list= timer= rsfproj= size=1024**2 uses= nofetch=y public=n private=n local=n command= skipfile=''','''Scan a directory tree (or list of directory trees) to a given depth,
inventory the contents, and optionally execute a command in each leaf.

The inventory and optional command occurs only at the specified depth
(default 3), not the intervening depths.  Directories named .svn are
skipped.  Only directories containing an SConstruct file are listed or
executed.

Optional directory filters controlling inventory or command execution
may be specified based on existence of .rsfproj file, sf programs used,
type of external data required, and total rsf data-file size of the
completed example.  A an optional input text file may also be specified
containing a list of examples to skip.

The optional command is executed in /bin/sh.

Examples (from within $RSFSRC):

sfbooklist book                         # inventory of book
sfbooklist levels=2 book/geostats       # inventory of book/geostats
sfbooklist command=scons book           # build examples with default filters
sfbooklist size=5 command=scons book    # build examples smaller than 5MB
''')
rsf.doc.progs['sfbooklist']=sfbooklist

