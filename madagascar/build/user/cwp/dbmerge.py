sfdbmerge = rsf.doc.rsfprog('sfdbmerge','user/cwp/Mdbmerge.py','''''')
sfdbmerge.version('1.7')
sfdbmerge.synopsis('''sfdbmerge''','''A program that can be used to merge separate SCons databases together.  Typically used when an SConstruct is split
into multiple pieces (e.g. on a cluster).

args:
    outdb - path of the output database

    strings - names of the databases to merge together
''')
rsf.doc.progs['sfdbmerge']=sfdbmerge

