sfort3dhomodevK = rsf.doc.rsfprog('sfort3dhomodevK','user/chengjb/Mort3dhomodevK.c','''3D three-components projection deviation correction operators calculation in''')
sfort3dhomodevK.par('apvy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevK.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevK.par('taper',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevK.par('vp0',rsf.doc.rsfpar('float','3000.0','',''''''))
sfort3dhomodevK.par('vs0',rsf.doc.rsfpar('float','1500.0','',''''''))
sfort3dhomodevK.par('de1',rsf.doc.rsfpar('float','0.05','',''''''))
sfort3dhomodevK.par('de2',rsf.doc.rsfpar('float','-0.05','',''''''))
sfort3dhomodevK.par('de3',rsf.doc.rsfpar('float','0.15','',''''''))
sfort3dhomodevK.par('ep1',rsf.doc.rsfpar('float','0.2','',''''''))
sfort3dhomodevK.par('ep2',rsf.doc.rsfpar('float','0.05','',''''''))
sfort3dhomodevK.par('ga1',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dhomodevK.par('ga2',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dhomodevK.par('alpha',rsf.doc.rsfpar('float','0.','',''''''))
sfort3dhomodevK.par('the',rsf.doc.rsfpar('float','0.','',''''''))
sfort3dhomodevK.par('phi',rsf.doc.rsfpar('float','0.','',''''''))
sfort3dhomodevK.par('hnx',rsf.doc.rsfpar('int','250','',''''''))
sfort3dhomodevK.par('hny',rsf.doc.rsfpar('int','250','',''''''))
sfort3dhomodevK.par('hnz',rsf.doc.rsfpar('int','250','',''''''))
sfort3dhomodevK.par('dx',rsf.doc.rsfpar('float','10.','',''''''))
sfort3dhomodevK.par('dy',rsf.doc.rsfpar('float','10.','',''''''))
sfort3dhomodevK.par('dz',rsf.doc.rsfpar('float','10.','',''''''))
sfort3dhomodevK.par('itaper',rsf.doc.rsfpar('int','1','',''''''))
sfort3dhomodevK.version('1.7')
sfort3dhomodevK.synopsis('''sfort3dhomodevK > Fo1.rsf apvy=Fo2.rsf apvz=Fo3.rsf taper=Fo4.rsf vp0=3000.0 vs0=1500.0 de1=0.05 de2=-0.05 de3=0.15 ep1=0.2 ep2=0.05 ga1=0.1 ga2=0.1 alpha=0. the=0. phi=0. hnx=250 hny=250 hnz=250 dx=10. dy=10. dz=10. itaper=1''',''' * homogeneous orthorhombic media
   Copyright (C) 2012 Tongji University, Shanghai, China 

   Authors: Jiubing Cheng and Tengfei Wang 
     
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
rsf.doc.progs['sfort3dhomodevK']=sfort3dhomodevK

