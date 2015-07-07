/*        Generated by TAPENADE     (INRIA, Tropics team)
    Tapenade 3.7 (r4786) - 21 Feb 2013 15:53
*/
#include "cstd.h"

/*
  Differentiation of acd_2d_4 in forward (tangent) mode:
   variations   of useful results: **up
   with respect to varying inputs: **csq **uc **up
   RW status of diff variables: **csq:in **uc:in **up:in-out
   Plus diff mem management of: csq:in *csq:in uc:in *uc:in up:in
                *up:in
*/
void acd_2d_4_d(float **uc, float **ucd, float **up, float **upd, float **csq,
        float **csqd, int *s, int *e, float c0, float *c1, float *c2, int *lbc
        , int *rbc) {
    int i0, i1;
    int s0=s[0];
    int e0=e[0];

    float lap;
    for (i1 = s[1]; i1 <= e[1]; i1++)
#pragma ivdep
        for (i0 = s0; i0 <= e0; i0++) {
	  lap=(c0*uc[i1][i0]+
	       c1[0]*(uc[i1][i0+1]+uc[i1][i0-1])+
	       c1[1]*(uc[i1+1][i0]+uc[i1-1][i0])+
	       c2[0]*(uc[i1][i0+2]+uc[i1][i0-2])+
	       c2[1]*(uc[i1+2][i0]+uc[i1-2][i0]));
            upd[i1][i0] = 2.0*ucd[i1][i0] - upd[i1][i0] + 
	      csqd[i1][i0]*lap + 
	      csq[i1][i0]*(c0*ucd[i1][i0]+
			   c1[0]*(ucd[i1][i0+1]+ucd[i1][i0-1])+
			   c1[1]*(ucd[i1+1][i0]+ucd[i1-1][i0])+
			   c2[0]*(ucd[i1][i0+2]+ucd[i1][i0-2])+
			   c2[1]*(ucd[i1+2][i0]+ucd[i1-2][i0]));
            up[i1][i0] = 2.0*uc[i1][i0] - up[i1][i0] + 
	      csq[i1][i0]*lap;
        }
    /* boundary conditions - note that uc[-1][i]=0 etc. */
    if (lbc[1])
#pragma ivdep
        for (i0 = s0; i0 <= e0; i0++) {
            upd[s[1] - 2][i0] = -upd[s[1]][i0];
            up[s[1] - 2][i0] = -up[s[1]][i0];
        }
    if (rbc[1])
#pragma ivdep
        for (i0 = s0; i0 <= e0; i0++) {
            upd[e[1] + 2][i0] = -upd[e[1]][i0];
            up[e[1] + 2][i0] = -up[e[1]][i0];
        }
    if (lbc[0])
#pragma ivdep
        for (i1 = s[1]; i1 <= e[1]; ++i1) {
            upd[i1][s[0] - 2] = -upd[i1][s[0]];
            up[i1][s[0] - 2] = -up[i1][s[0]];
        }
    if (rbc[0])
#pragma ivdep
        for (i1 = s[1]; i1 <= e[1]; ++i1) {
            upd[i1][e[0] + 2] = -upd[i1][e[0]];
            up[i1][e[0] + 2] = -up[i1][e[0]];
        }
}
