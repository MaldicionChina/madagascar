import rsf.doc

sfminmax = rsf.doc.rsfprog('sfminmax','user/jennings/Mminmax.c','''Element by element minimum or maximum of two RSF files.''')
sfminmax.par('file1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfminmax.par('file2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfminmax.par('file1',rsf.doc.rsfpar('string ',desc='''RSF filename required, data type must be float (auxiliary input file name)'''))
sfminmax.par('file2',rsf.doc.rsfpar('string ',desc='''RSF filename required, data type must be float (auxiliary input file name)'''))
sfminmax.par('mode',rsf.doc.rsfpar('string ',desc=''''min' (default) or 'max' '''))
sfminmax.version('1.7 Mminmax.c 4796 2009-09-29 19:39:07Z ivlad')
sfminmax.synopsis('''sfminmax file1=file1.rsf file2=file2.rsf > out.rsf mode=''','''
file1 and file2 must have the same number of elements.

See also: sflistminmax, sfstack.
''')
rsf.doc.progs['sfminmax']=sfminmax

sflistminmax = rsf.doc.rsfprog('sflistminmax','user/jennings/Mlistminmax.c','''Construct incremental minimum or maximum lists from an RSF file.''')
sflistminmax.par('mode',rsf.doc.rsfpar('string ',desc=''''min' (default) or 'max' '''))
sflistminmax.version('1.7 Mlistminmax.c 4796 2009-09-29 19:39:07Z ivlad')
sflistminmax.synopsis('''sflistminmax < in.rsf > out.rsf mode=''','''
Constructs the following set of minimum or maximum lists for each
x2, x3, ... xn in the input RSF file:

out[0] = in[0]
out[i] = min or max of (in[i], out[i-1]) for i = 1, 2, 3, ... n1

The input file data type must be float.
The output file data type will be float.

sflistminmax mode=min, can be used to simulate "erosion" for a set of 
geological surfaces, producing a new set of surfaces that do not cross.

See also: sfminmax, sfstack.
''')
rsf.doc.progs['sflistminmax']=sflistminmax

sfsizes = rsf.doc.rsfprog('sfsizes','user/jennings/Msizes.c','''Display the size of RSF files.''')
sfsizes.par('files',rsf.doc.rsfpar('bool','y','','''If y, print size of each file.  If n, print only total. '''))
sfsizes.par('human',rsf.doc.rsfpar('bool','n','','''If y, print human-readable file size.  If n, print byte count. '''))
sfsizes.par('su',rsf.doc.rsfpar('bool','n','','''Same for Seismic Unix '''))
sfsizes.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfsizes')
sfsizes.version('1.7 Msizes.c 7537 2011-07-28 06:13:30Z sfomel')
sfsizes.synopsis('''sfsizes files=y human=n su=n file1.rsf file2.rsf ...''','''Prints the element size, number of elements, and number of bytes
for a list of RSF files.  Non-RSF files are ignored.
''')
rsf.doc.progs['sfsizes']=sfsizes

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

