import sys, os

import rsf.doc

import rsf.sfplot
import rsf.sflibplot
import rsf.sfplplot
import rsf.sfpens
import rsf.sfsumain
import rsf.sfsuplot
import rsf.sfgeneric
import rsf.sfmain
import rsf.sfseismic
import rsf.sfkarl
import rsf.sfaklokov
import rsf.sfbash
import rsf.sfbrowaeys
import rsf.sfchen
import rsf.sfchengjb
import rsf.sfchenyk
import rsf.sfcram
import rsf.sfcuda
import rsf.sfcwp
import rsf.sfediazp
import rsf.sffangg
import rsf.sffomels
import rsf.sfgchliu
import rsf.sfgee
import rsf.sfgodwinj
import rsf.sfhpcss
import rsf.sfivlad
import rsf.sfjeff
import rsf.sfjennings
import rsf.sfjingwei
import rsf.sfjmonsegny
import rsf.sfjsun
import rsf.sfjun
import rsf.sfjyan
import rsf.sfkourkina
import rsf.sflcasasan
import rsf.sflexing
import rsf.sfllisiw
import rsf.sfparvaneh
import rsf.sfpetsc
import rsf.sfpoulsonj
import rsf.sfpsava
import rsf.sfpwd
import rsf.sfpyang
import rsf.sfrickettj
import rsf.sfridder
import rsf.sfrweiss
import rsf.sfsaragiotis
import rsf.sfseisinv
import rsf.sfseplib_compat
import rsf.sfslim
import rsf.sfsongxl
import rsf.sftariq
import rsf.sftsai
import rsf.sfurdaneta
import rsf.sfxuxin
import rsf.sfyliu
import rsf.sfzone
import rsf.sfbase
import rsf.sftrace
import rsf.sfgrid
import rsf.sfacd
import rsf.sfasg
import rsf.sfseq

import rsf.vpplot


try:
    import rsf.use
except:
    pass

RSFROOT="/mnt/Archivos/Universidad_de_Antioquia/Proyectos/C3_LINUX/debian_packaging/paquetes/En_Proceso/madagascar/Paquete/madagascar-1.7/debian/madagascar/usr"
    
def selfdoc():
    'Display man page'
    prognm = os.path.basename(sys.argv[0])
    if prognm[0] == 'M' and prognm[-3:] == '.py':
        # User testing code in his local directory
        prognm = 'sf' + prognm[1:-3]
        msg = 'Self-doc may be out of synch, do "scons install" in RSFSRC'
        sys.stderr.write(msg+'\n')

    prog = rsf.doc.progs.get(prognm)
    if prog != None:
        prog.document(25,RSFROOT)
    else:
        sys.stderr.write('No installed man page for ' + prognm+'\n')
