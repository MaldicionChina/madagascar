/* Rice HPCSS seismic modeling and migration. */

/*************************************************************************

Copyright Rice University, 2009.
All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, provided that the above copyright notice(s) and this
permission notice appear in all copies of the Software and that both the
above copyright notice(s) and this permission notice appear in supporting
documentation.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF THIRD PARTY
RIGHTS. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR HOLDERS INCLUDED IN THIS
NOTICE BE LIABLE FOR ANY CLAIM, OR ANY SPECIAL INDIRECT OR CONSEQUENTIAL
DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.

Except as contained in this notice, the name of a copyright holder shall
not be used in advertising or otherwise to promote the sale, use or other
dealings in this Software without prior written authorization of the
copyright holder.

**************************************************************************/

/* Modified for distribution with Madagascar */

#include <rsf.h>

#include "wavefun.h"

#ifndef _wavefun_h

typedef struct {
    int nz;          /* number of gridpoints in z */
    int nx;          /* number of gridpoints in x */
    int nt;          /* number of time steps */
    int nm;          /* number of time steps to skip between movie frames
			(<=0 for no movie) */
    float dz;        /* step in z */
    float dx;        /* step in x */
    float dt;        /* step in t */
    float freq;      /* center frequency of Ricker wavelet */
    int isz;         /* source depth, in units of dz */
    int isxbeg;      /* far left source x coord in units of dx */
    int isxend;      /* far right source x coord in units of dx */
    int iskip;       /* interval between sources in units of dx */
    int igz;         /* recvr depth, in units of dz */
    int igxbeg;      /* far left receiver x coord in units of dx */
    int igxend;      /* far right receiver x coord in units of dx */
    int imbeg;       /* midpoint begin */
    int imend;       /* midpoint end */
    int imskip;      /* midpoint skip */
    int ihmax;       /* offset radius, units of dx */
    sf_file vfile;    /* velocity file - defines space grid */
    sf_file tfile;    /* trace output file */
    sf_file mfile;    /* movie file */
    sf_file rmfile;   /* receiver movie file */
    sf_file imfile;   /* image file */
} WINFO;
/*^*/

#endif

void getinputs(bool mod,  /* modeling or migration */ 
	       WINFO * wi /* parameters */) 
/*< get input parameters >*/
{
    vfile = sf_input("in");
    /* velocity file - defines space grid */

    if (!sf_histint(vfile,"n1",&nz) ||
	!sf_histint(vfile,"n2",&nx) ||
	!sf_histfloat(vfile,"d1",&dz)||
	!sf_histfloat(vfile,"d2",&dx))
	sf_error("Need to specify n1=, n2=, d1=, d2= in velocity");

    if (NULL != sf_getstring("source")) {
	/* source movie file */
	mfile = sf_output("source");
    } else {
	mfile = NULL;
    }

    if (mod) {
	tfile = sf_output("out");
	if (!sf_getint("nt",&nt)) sf_error("Need nt=");
	/* number of time steps */
	if (!sf_getfloat("dt",&dt)) sf_error("Need dt=");
	/* step in t */	
    } else { 
	tfile = sf_input("trace");
	if (!sf_histint(tfile,"n1",&nt)) 
	    sf_error("Need n1= in trace");
	if (!sf_histfloat(tfile,"d1",&dt)) 
	    sf_error("Need d1= in trace");
    }

    if (NULL != sf_getstring("receiver")) {
	/* receiver movie file */
	rmfile = sf_output("receiver");
    } else {
	rmfile = NULL;
    }

    if (mod) {
	imfile= NULL;
    } else {
	imfile= sf_output("out");
	/* image file */
    } 


    if (!sf_getint("nm",&nm)) nm=0;
    /* number of time steps to skip between movie frames
       (<=0 for no movie) */
    
    if (!sf_getint("isz",&isz)) isz=1;
    /* source depth, in units of dz */
    
    if (!sf_getint("isxbeg",&isxbeg)) isxbeg=(nx)/2;
    /* far left source x coord in units of dx */
    
    if (!sf_getint("isxend",&isxend)) isxend=(nx)/2;
    /* far right source x coord in units of dx */
    
    if (!sf_getint("iskip",&iskip)) iskip=1;
    /* interval between sources in units of dx */
    
    if (!sf_getint("igz",&igz)) igz=1;
    /* recvr depth, in units of dz */
    
    if (!sf_getint("igxbeg",&igxbeg)) igxbeg=1;
    /* far left receiver x coord in units of dx */
    
    if (!sf_getint("igxend",&igxend)) igxend=0;
    /* far right receiver x coord in units of dx */
    
    if (!sf_getfloat("fpeak",&freq)) freq=0.01;
    /* center frequency of Ricker wavelet */
    
    /* default is zero offset */
    
    if (!sf_getint("ihmax",&ihmax)) ihmax=0;
    /* offset radius, units of dx */
    
    if (!sf_getint("imbeg",&imbeg)) imbeg=ihmax;
    /* midpoint begin */
    
    if (!sf_getint("imend",&imend)) imend=nx-ihmax-1;
    /* midpoint end */
    
    if (!sf_getint("imskip",&imskip)) imskip=1;
    /* midpoint skip */
 
    /* sanity-check */
    if (iskip<1 || imskip<1) 
	sf_error("either source or midpoint skip is "
		 "nonpositive - ABORT");
    
    if (imbeg<ihmax) 
	sf_error("first midpoint located within "
		 "offset radius of domain boundary - ABORT");
    
    if (imend>nx-ihmax-1) 
	sf_error("first midpoint located within "
		 "offset radius of domain boundary - ABORT");
    
    if (nx<1||nz<1) 
	sf_error("number of spatial samples input is "
		 "nonpositive - ABORT");
    
    if (isxbeg<1 || isxend>nx-2 ||
	isz<1 || isz>nz-2) {
	sf_warning("source indices isz=%d, isxbeg=%d isxend=%d place source",
		   isz,isxbeg,isxend);
	sf_error("outside of wavefield update region [1,%d] x [1,%d]",
		 nz-1,nx-1);
    }
    
    if (igz<1 || igz>nz-2 ||
	igxbeg<1 || igxbeg > nx-2 ||
	igxend<1 || igxend > nx-2) {
	sf_warning("receiver depth index igz=%d or cable endpoint",igz);
	sf_warning("indices igxbeg=%d, igxend=%d place receivers outside of",
		   igxbeg,igxend);
	sf_error("wavefield update region [1,%d] x [1,%d]",
		 nz-1,nx-1);
    }

    if (mod) {
	sf_putint(tfile,"n1",nt);
	sf_putfloat(tfile,"d1",dt);
	sf_putfloat(tfile,"o1",0.);
	sf_putstring(tfile,"label1","Time");
	sf_putstring(tfile,"unit1","s");
	sf_putint(tfile,"n2",igxend-igxbeg+1);
	sf_putfloat(tfile,"d2",dx);
	sf_putfloat(tfile,"o2",igxbeg*dx);
	sf_putstring(tfile,"label2","Receiver");
	sf_putint(tfile,"n3",(isxend-isxbeg)/iskip+1);
	sf_putfloat(tfile,"d3",iskip*dx);
	sf_putfloat(tfile,"o3",isxbeg*dx);
	sf_putstring(tfile,"label3","Source");
    } 

    if (NULL != mfile && nm) {
	sf_putint(mfile,"n3",nt/nm);
	sf_putfloat(mfile,"o3",0.);
	sf_putfloat(mfile,"d3",nm*dt);
	sf_putstring(mfile,"label3","Time");
	sf_putstring(mfile,"unit3","s");
    }

    if (NULL != rmfile) {
	sf_putint(rmfile,"n3",nt);
	sf_putfloat(rmfile,"o3",0.);
	sf_putfloat(rmfile,"d3",dt);
	sf_putstring(rmfile,"label3","Time");
	sf_putstring(rmfile,"unit3","s");
    }
}

void fassign(float * a, float c, int n) 
/*< assign constant to array - presumes memory already allocated >*/
{
  int i;
  for (i=0;i<n;i++) a[i]=c;
}

void fzeros(float * a, int n) 
/*< assign zero to array - presumes memory already allocated >*/
{
  int i;
  for (i=0;i<n;i++) a[i]=0.0;
}

void fsquare(float * a, int n) 
/*< square array elements - presumes memory already allocated
  and initialized >*/
{
  int i;
  for (i=0;i<n;i++) a[i]=a[i]*a[i];
}

float fgetmax(float * a, int n) 
/*< get max val from array >*/
{
  int i;
  float m=-SF_HUGE;
  for (i=0;i<n;i++) m=fmaxf(m,a[i]);
  return m;
}

float fgetmin(float * a, int n) 
/*< get min val from array >*/
{
  int i;
  float m=SF_HUGE;
  for (i=0;i<n;i++) m=fminf(m,a[i]);
  return m;
}

float fgetrick(float t, float fpeak) 
/*< return value at t of causal Ricker wavelet with peak frequency f >*/    
{
    float st=SF_PI*fpeak*(t-(1.2/fpeak));
    st*=st;
    return (1-2*st)*exp(-st);
}
