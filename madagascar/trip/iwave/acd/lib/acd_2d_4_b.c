/*        Generated by TAPENADE     (INRIA, Tropics team)
    Tapenade 3.7 (r4786) - 21 Feb 2013 15:53
*/
#include "cstd.h"

/* #define TAPENADE */

/*
  Differentiation of acd_2d_4 in reverse (adjoint) mode:
   gradient     of useful results: **uc **up
   with respect to varying inputs: **csq **uc **up
   RW status of diff variables: **csq:out **uc:incr **up:in-out
   Plus diff mem management of: csq:in *csq:in uc:in *uc:in up:in
                *up:in
*/
void acd_2d_4_b(float **uc, float **ucb, float **up, float **upb, float **csq,
        float **csqb, int *s, int *e, float c0, float *c1, float *c2, int *lbc
        , int *rbc) {
    int i0, i1;
    int s0=s[0];
    int e0=e[0];
    float lap;
    float tempb;
    /* boundary conditions - note that uc[-1][i]=0 etc. */
    if (rbc[0])
        for (i1 = e[1]; i1 > s[1]-1; --i1) {
            upb[i1][e[0]] = upb[i1][e[0]] - upb[i1][e[0] + 2];
            upb[i1][e[0] + 2] = 0.0;
        }
    if (lbc[0])
        for (i1 = e[1]; i1 > s[1]-1; --i1) {
            upb[i1][s[0]] = upb[i1][s[0]] - upb[i1][s[0] - 2];
            upb[i1][s[0] - 2] = 0.0;
        }
    if (rbc[1])
#pragma ivdep
        for (i0 = e0; i0 > s0-1; --i0) {
	  /*
            tmp0b = upb[e[1] + 2][i0];
	    upb[e[1] + 2][i0] = 0.0;
	    upb[e[1]][i0] = upb[e[1]][i0] - tmp0b;
	  */
	  upb[e[1]][i0] = upb[e[1]][i0] - upb[e[1] + 2][i0];
	  upb[e[1] + 2][i0] = 0.0;
        }
    if (lbc[1])
#pragma ivdep
        for (i0 = e0; i0 > s0-1; --i0) {
	  /*
            tmpb = upb[s[1] - 2][i0];
            upb[s[1] - 2][i0] = 0.0;
            upb[s[1]][i0] = upb[s[1]][i0] - tmpb;
	  */
	  upb[s[1]][i0] = upb[s[1]][i0] - upb[s[1] - 2][i0];
	  upb[s[1] - 2][i0] = 0.0;
        }

    for (i1 = e[1]; i1 > s[1]-1; --i1)
#ifdef TAPENADE
        for (i0 = e0; i0 > s0-1; --i0) {
            lap=(c0*uc[i1][i0]+
		 c1[0]*(uc[i1][i0+1]+uc[i1][i0-1])+
		 c1[1]*(uc[i1+1][i0]+uc[i1-1][i0])+
		 c2[0]*(uc[i1][i0+2]+uc[i1][i0-2])+
		 c2[1]*(uc[i1+2][i0]+uc[i1-2][i0]));
            
            tempb = csq[i1][i0]*upb[i1][i0];

            csqb[i1][i0] = csqb[i1][i0] + lap*upb[i1][i0];
            ucb[i1][i0 + 2] = ucb[i1][i0 + 2] + c2[0]*tempb;
            ucb[i1][i0 + 1] = ucb[i1][i0 + 1] + c1[0]*tempb;
            ucb[i1 + 2][i0] = ucb[i1 + 2][i0] + c2[1]*tempb;
            ucb[i1 + 1][i0] = ucb[i1 + 1][i0] + c1[1]*tempb;
            ucb[i1][i0] = ucb[i1][i0] + c0*tempb + 2.0*upb[i1][i0];
            ucb[i1 - 1][i0] = ucb[i1 - 1][i0] + c1[1]*tempb;
            ucb[i1 - 2][i0] = ucb[i1 - 2][i0] + c2[1]*tempb;
            ucb[i1][i0 - 1] = ucb[i1][i0 - 1] + c1[0]*tempb;
            ucb[i1][i0 - 2] = ucb[i1][i0 - 2] + c2[0]*tempb;
            upb[i1][i0] = -upb[i1][i0];
        }
#else
#pragma ivdep
        for (i0 = s0+2; i0 <=e0+2; i0++) {
            lap=(c0*uc[i1][i0-2]+
		 c1[0]*(uc[i1][i0-1]+uc[i1][i0-3])+
		 c1[1]*(uc[i1+1][i0-2]+uc[i1-1][i0-2])+
		 c2[0]*(uc[i1][i0]+uc[i1][i0-4])+
		 c2[1]*(uc[i1+2][i0-2]+uc[i1-2][i0-2]));
            
            tempb = csq[i1][i0-2]*upb[i1][i0-2];

            csqb[i1][i0-2] = csqb[i1][i0-2] + lap*upb[i1][i0-2];
            ucb[i1][i0  ] = ucb[i1][i0  ] + c2[0]*tempb;
            ucb[i1][i0-1] = ucb[i1][i0-1] + c1[0]*tempb;
            ucb[i1 + 2][i0-2] = ucb[i1 + 2][i0-2] + c2[1]*tempb;
            ucb[i1 + 1][i0-2] = ucb[i1 + 1][i0-2] + c1[1]*tempb;
            ucb[i1][i0-2] = ucb[i1][i0-2] + c0*tempb + 2.0*upb[i1][i0-2];
            ucb[i1 - 1][i0-2] = ucb[i1 - 1][i0-2] + c1[1]*tempb;
            ucb[i1 - 2][i0-2] = ucb[i1 - 2][i0-2] + c2[1]*tempb;
            ucb[i1][i0 - 3] = ucb[i1][i0 - 3] + c1[0]*tempb;
            ucb[i1][i0 - 4] = ucb[i1][i0 - 4] + c2[0]*tempb;
            upb[i1][i0-2] = -upb[i1][i0-2];
        }
#endif
}
