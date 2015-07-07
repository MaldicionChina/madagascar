import rsf.doc

vp7ab = rsf.doc.rsfprog('vp7ab','plot/test/7ab.c','''''')
vp7ab.par('c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
vp7ab.par('d',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
vp7ab.par('top',rsf.doc.rsfpar('float','5.','',''''''))
vp7ab.par('c1',rsf.doc.rsfpar('float','0.5','',''''''))
vp7ab.par('c2',rsf.doc.rsfpar('float','5.','',''''''))
vp7ab.par('c',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
vp7ab.par('d',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
vp7ab.version('1.7 7ab.c 7107 2011-04-10 02:04:14Z ivlad')
vp7ab.synopsis('''vp7ab c=c.rsf d=d.rsf > plot.vpl top=5. c1=0.5 c2=5.''','''''')
rsf.doc.progs['vp7ab']=vp7ab

vpcmp = rsf.doc.rsfprog('vpcmp','plot/test/cmp.c','''''')
vpcmp.version('1.7 cmp.c 9406 2012-10-25 05:09:05Z sfomel')
vpcmp.synopsis('''vpcmp > plot.vpl''','''''')
rsf.doc.progs['vpcmp']=vpcmp

vpcroshyp = rsf.doc.rsfprog('vpcroshyp','plot/test/croshyp.c','''''')
vpcroshyp.version('1.7 croshyp.c 7107 2011-04-10 02:04:14Z ivlad')
vpcroshyp.synopsis('''vpcroshyp > plot.vpl''','''''')
rsf.doc.progs['vpcroshyp']=vpcroshyp

vpcsp = rsf.doc.rsfprog('vpcsp','plot/test/csp.c','''''')
vpcsp.version('1.7 csp.c 7107 2011-04-10 02:04:14Z ivlad')
vpcsp.synopsis('''vpcsp > plot.vpl''','''''')
rsf.doc.progs['vpcsp']=vpcsp

vpdc = rsf.doc.rsfprog('vpdc','plot/test/dc.c','''''')
vpdc.version('1.7 dc.c 7107 2011-04-10 02:04:14Z ivlad')
vpdc.synopsis('''vpdc > plot.vpl''','''''')
rsf.doc.progs['vpdc']=vpdc

vpdcretard = rsf.doc.rsfprog('vpdcretard','plot/test/dcretard.c','''''')
vpdcretard.version('1.7 dcretard.c 7107 2011-04-10 02:04:14Z ivlad')
vpdcretard.synopsis('''vpdcretard > plot.vpl''','''''')
rsf.doc.progs['vpdcretard']=vpdcretard

vpellipse = rsf.doc.rsfprog('vpellipse','plot/test/ellipse.c','''''')
vpellipse.version('1.7 ellipse.c 9406 2012-10-25 05:09:05Z sfomel')
vpellipse.synopsis('''vpellipse > plot.vpl''','''''')
rsf.doc.progs['vpellipse']=vpellipse

vpfrancis = rsf.doc.rsfprog('vpfrancis','plot/test/francis.c','''''')
vpfrancis.version('1.7')
vpfrancis.synopsis('''vpfrancis > plot.vpl''','''''')
rsf.doc.progs['vpfrancis']=vpfrancis

vpheadray = rsf.doc.rsfprog('vpheadray','plot/test/headray.c','''''')
vpheadray.version('1.7 headray.c 7107 2011-04-10 02:04:14Z ivlad')
vpheadray.synopsis('''vpheadray > plot.vpl''','''''')
rsf.doc.progs['vpheadray']=vpheadray

vphyplay = rsf.doc.rsfprog('vphyplay','plot/test/hyplay.c','''''')
vphyplay.version('1.7')
vphyplay.synopsis('''vphyplay > plot.vpl''','''  Copyright (C) 2004 University of Texas at Austin
  
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['vphyplay']=vphyplay

vpnmotraj = rsf.doc.rsfprog('vpnmotraj','plot/test/nmotraj.c','''''')
vpnmotraj.version('1.7 nmotraj.c 7107 2011-04-10 02:04:14Z ivlad')
vpnmotraj.synopsis('''vpnmotraj > plot.vpl''','''''')
rsf.doc.progs['vpnmotraj']=vpnmotraj

vpreflector = rsf.doc.rsfprog('vpreflector','plot/test/reflector.c','''''')
vpreflector.version('1.7 reflector.c 9406 2012-10-25 05:09:05Z sfomel')
vpreflector.synopsis('''vpreflector > plot.vpl''','''''')
rsf.doc.progs['vpreflector']=vpreflector

vpsg = rsf.doc.rsfprog('vpsg','plot/test/sg.c','''''')
vpsg.version('1.7 sg.c 7107 2011-04-10 02:04:14Z ivlad')
vpsg.synopsis('''vpsg > plot.vpl''','''''')
rsf.doc.progs['vpsg']=vpsg

vpvrms = rsf.doc.rsfprog('vpvrms','plot/test/vrms.c','''''')
vpvrms.version('1.7 vrms.c 7107 2011-04-10 02:04:14Z ivlad')
vpvrms.synopsis('''vpvrms > plot.vpl''','''''')
rsf.doc.progs['vpvrms']=vpvrms

vpwhitepruf = rsf.doc.rsfprog('vpwhitepruf','plot/test/whitepruf.c','''''')
vpwhitepruf.version('1.7 whitepruf.c 7107 2011-04-10 02:04:14Z ivlad')
vpwhitepruf.synopsis('''vpwhitepruf > plot.vpl''','''''')
rsf.doc.progs['vpwhitepruf']=vpwhitepruf

rsf.doc.progs['vpreflexpt']=vpreflector
rsf.doc.progs['vpreflkine']=vpreflector
