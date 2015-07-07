/* vplot filter for OpenGL. */
/*
  Copyright (C) 2009 The University of Texas at Austin
  
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
*/

#ifdef __APPLE__
#include <OpenGL/glu.h>
#include <GLUT/glut.h>
#else
#include <GL/glu.h>
#include <GL/glut.h>
#ifdef FREEGLUT
#include <GL/freeglut_ext.h>
#endif
#endif

#include <limits.h>

#include "../include/attrcom.h"
#include "../include/extern.h"
#include "../include/params.h"
#include "../include/err.h"
#include "../include/erasecom.h"
#include "../include/closestat.h"
#include "../include/enum.h"

#include "../genlib/genpen.h"
#include "../utilities/util.h"

#include "dovplot.h"
#include "init_vplot.h"

#include "oglpen.h"

char            name[] = "oglpen";
#include "ogldoc.h"

#include "_device.h"

#define PPI 100.0  /* pixels per inch */
#define NCOLOR 256 /* number of colors */
#define MAXVERT 1000
#define TEX_SIZE 256 /* Texture size  - should be a power of two */
#define LIST_CHUNK 1000 /* Define how many display lists generate at once */
#define MAX_CHUNKS 100000 /* How many chunks of display lists to have */
#define WIN_HEIGHT 760 /* Default window height */
#define DEV_SCALE 10 /* Scale factor between OpenGL and window coordinate systems */
#define MIN_DELAY 50.0 /* Maximum animation delay */
#define MAX_DELAY 10000.0 /* Minimum animation delay */

static float *color_table = NULL;
static bool light = false;
static bool stretchy = false;
static bool aalias = false;
static int aawidth = 1;
static int oglcolor, nx, ny;
static unsigned int *ogllists = NULL; /* Bases of every LIST_CHUNK display lists */
static unsigned char *tex_buf = NULL; /* Temporary buffer for loading textures */
static unsigned int frames_num = 0;
static unsigned int curr_frame = 0;
static float delay = 50; /* milliseconds */
static int direction = 0; /* Animation direction */
static int dirway = 0; /* Animation direction for both ways */
static bool animate = false; /* Animatio flag */
static int menu_tag = 0; /* GLUT menu tag */
static bool has_menu = false;
static int window_id; /* GLUT window identificator */

#define MAX_TITLE_STR 64
static const char *pen_title = "OpenGL pen";
static char title_strbuf[MAX_TITLE_STR];
static int curr_title_frame = -1;

enum {
    MENU_NEXT,
    MENU_PREV,
    MENU_RESTART,
    MENU_RUN,
    MENU_STOP,
    MENU_DIRECTION,
    MENU_STRETCHY,
    MENU_FULLSCREEN,
    MENU_QUIT
};


static void oglquit (int status) {
    glutDestroyWindow (window_id);
    exit (status);
}

void opendev (int argc, char* argv[])
/*< open >*/
{
    const char *color;
    int dwidth, dheight, mwidth; /*, mheight; */
    int win_width, win_height;

    sf_parenv("SFPENOPTS");

    dev.txfont = DEFAULT_HARDCOPY_FONT;
    dev.txprec = DEFAULT_HARDCOPY_PREC;
    dev.brake = BREAK_IGNORE;

    /* control routines */
    dev.reset = oglreset;
    dev.erase = oglerase;
    dev.close = oglclose;

    dev.area = oglarea;
    dev.raster = oglraster;
    dev.attributes = oglattr;
    dev.plot = oglplot;
    dev.startpoly = oglstartpoly;
    dev.midpoly = oglmidpoly;
    dev.endpoly = oglendpoly;
    dev.point = oglpoint;

    dev.need_end_erase = true;
    dev.smart_clip = true;
    dev.smart_raster = true;
    dev.num_col = NCOLOR;

    color_table = (float*)malloc (3*NCOLOR*sizeof (float));
    tex_buf = (unsigned char*)malloc (TEX_SIZE*TEX_SIZE*sizeof (unsigned char));
    ogllists = (unsigned int*)malloc (MAX_CHUNKS*sizeof (unsigned int));

    glutInit (&argc, argv);

    dwidth = glutGet (GLUT_SCREEN_WIDTH);
    dheight = glutGet (GLUT_SCREEN_HEIGHT);
    mwidth = glutGet (GLUT_SCREEN_WIDTH_MM);
/*    mheight = glutGet (GLUT_SCREEN_HEIGHT_MM); */

    win_height = WIN_HEIGHT;
    if (win_height > 0.85*dheight)
        win_height = 0.85*dheight;
    win_width = win_height / VP_SCREEN_RATIO;

    ny = win_height*DEV_SCALE;
    nx = ny / VP_SCREEN_RATIO;

    dev.pixels_per_inch = (float)nx / 
                          ((float)win_width / (float)dwidth*mwidth / 25.4);
    dev.aspect_ratio = 1.0;
    sf_getfloat ("aspect", &dev.aspect_ratio);
    /* aspect ratio */
    sf_getfloat ("ppi", &dev.pixels_per_inch);
    /* pixels per inch */

    dev.xmin = 0;
    dev.ymin = 0;
    dev.xmax = nx;
    dev.ymax = ny;

    invras = false;

    glutInitWindowSize (win_width, win_height);

    glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE | GLUT_STENCIL);
    if (!glutGet (GLUT_DISPLAY_MODE_POSSIBLE)) {
        fprintf (stderr, "OpenGL device does not support stencil buffer: using genpatarea ()\n");
        dev.area = genpatarea;
        glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE);
        if (!glutGet (GLUT_DISPLAY_MODE_POSSIBLE)) {
            fprintf (stderr, "OpenGL device does not support double buffer: trying single buffer\n");
            glutInitDisplayMode (GLUT_RGBA | GLUT_SINGLE);
            if (!glutGet (GLUT_DISPLAY_MODE_POSSIBLE)) {
                fprintf (stderr, "OpenGL device device initialization failed\n");
                exit (-1);
            }
        }
    }

    window_id = glutCreateWindow (pen_title);
    glutDisplayFunc (oglredraw);
    glutKeyboardFunc (oglkeyboard);
    glutIdleFunc (NULL);
    glutReshapeFunc (oglreshape);

    if (NULL == (color = sf_getstring ("bgcolor"))) color = "black";
    /* background color (black,white,light,dark) */

    switch (color[0]) {
        case 'b': /* black */
        case 'd': /* dark */
        default:
            light = false;
            break;
        case 'w': /* white */
        case 'l': /* light */
            light = true;
            break;
    }

    if (!sf_getbool ("stretchy", &stretchy)) stretchy = false;
    /* y - stretch plot to all borders of the drawing area */

    if (!sf_getbool ("aalias", &aalias)) aalias = false;
    /* y - draw lines, points, polygons with antialialing */
    if (!sf_getint ("aawidth", &aawidth)) aawidth = 1;
    /* width of transition areas when aalias=y */
}

void oglbuildmenu (void)
/*< menu builder >*/
{
    if (has_menu)
        glutDestroyMenu (menu_tag);
    else
        has_menu = true;

    menu_tag = glutCreateMenu (oglmenu);
    if (frames_num > 1 || animate) {
        if (!animate) {
            glutAddMenuEntry ("Next", MENU_NEXT);
            glutAddMenuEntry ("Prev", MENU_PREV);
            glutAddMenuEntry ("Restart", MENU_RESTART);
            glutAddMenuEntry ("Run", MENU_RUN);
        } else
            glutAddMenuEntry ("Stop", MENU_STOP);
        glutAddMenuEntry (direction == 2 ? "Forwards" :
                          direction == 1 ? "Both ways" : "Backwards", MENU_DIRECTION);
    }
    glutAddMenuEntry (stretchy ? "Rigid" : "Stretchy", MENU_STRETCHY);
    glutAddMenuEntry ("Full Screen", MENU_FULLSCREEN);
    glutAddMenuEntry ("Quit", MENU_QUIT);
#ifdef __APPLE__
    glutAttachMenu (GLUT_LEFT_BUTTON); /* for single-button Macs */
#else
    glutAttachMenu (GLUT_RIGHT_BUTTON);
#endif
}

void oglreset (void)
/*< reset >*/
{
    int value, r, g, b;

    /* reset color table */
    color_table[0] = 1.0*light;
    color_table[NCOLOR] = 1.0*light;
    color_table[NCOLOR*2] = 1.0*light;

    for (value = 1; value < 8; value++) {
        r = MAX_GUN*((value & 2) / 2);
        g = MAX_GUN*((value & 4) / 4);
        b = MAX_GUN*((value & 1) / 1);

        if (light) {
            color_table[value] = (MAX_GUN - r) / (float)MAX_GUN;
            color_table[NCOLOR + value] = (MAX_GUN - g) / (float)MAX_GUN;
            color_table[NCOLOR*2 + value] = (MAX_GUN - b) / (float)MAX_GUN;
        } else {
            color_table[value] = r / (float)MAX_GUN;
            color_table[NCOLOR + value] = g / (float)MAX_GUN;
            color_table[NCOLOR*2 + value] = b / (float)MAX_GUN;
        }
    }
 
    for (value = 8; value < NCOLOR; value++) {
        color_table[value] = 1.0*light;
        color_table[NCOLOR + value] = 1.0*light;
        color_table[NCOLOR*2 + value] = 1.0*light;
    }

    glDisable (GL_DEPTH_TEST);
    glDepthFunc (GL_ALWAYS);
    glShadeModel (GL_FLAT);
    glPolygonMode (GL_FRONT_AND_BACK, GL_FILL);
    glDisable (GL_CULL_FACE);
    glDisable (GL_LIGHTING);
    glDisable (GL_SCISSOR_TEST);
    glDisable (GL_STENCIL_TEST);
    glPixelStorei (GL_PACK_ALIGNMENT, 1);
    glPixelStorei (GL_UNPACK_ALIGNMENT, 1);
    glClearStencil (0);
    if (aalias) {
        glEnable (GL_LINE_SMOOTH);
        glEnable (GL_POINT_SMOOTH);
        glEnable (GL_POLYGON_SMOOTH);
        glLineWidth (aawidth);
        glPointSize (aawidth);
    }
    glDisable (GL_CLIP_PLANE0);
    glDisable (GL_CLIP_PLANE1);
    glDisable (GL_CLIP_PLANE2);
    glDisable (GL_CLIP_PLANE3);
}

/* Process queued events from the event loop */
static void oglprocessevents (void) {
#if defined(__APPLE__) && (GLUT_MACOSX_IMPLEMENTATION >= 2)
    if (!animate && frames_num == 1) {
        oglstartanimation ();
        oglbuildmenu ();
    }
    glutCheckLoop ();
#elif defined(FREEGLUT)
    if (!animate && frames_num == 1) {
        oglstartanimation ();
        oglbuildmenu ();
    }
    glutMainLoopEvent ();
#endif
}

void oglerase (int command)
/*< erase >*/
{
    switch (command) {
        case ERASE_START:
            ogllists[0] = glGenLists (LIST_CHUNK*2);
            glNewList (ogllists[0], GL_COMPILE_AND_EXECUTE);
            glClear (GL_COLOR_BUFFER_BIT);
            frames_num++;
            break;
        case ERASE_MIDDLE:
            glFlush ();
            glEndList ();
            /* Generate another display list - for color background */
            glNewList (ogllists[frames_num / LIST_CHUNK] +
                       (frames_num % LIST_CHUNK)*2 - 1,
                       GL_COMPILE_AND_EXECUTE);
            glClearColor (color_table[0],
                          color_table[NCOLOR],
                          color_table[NCOLOR*2], 0.0f);
            glEndList ();
            if (1 == frames_num)
                fprintf (stderr, "Preparing animation\n");
            else if (frames_num % 50 == 0)
                fprintf (stderr, "Finished %d frames\n", frames_num);
            oglprocessevents ();
            if (!(frames_num % LIST_CHUNK))
                ogllists[frames_num / LIST_CHUNK] = glGenLists (LIST_CHUNK*2);
            /* Main display list - all plotting */
            glNewList (ogllists[frames_num / LIST_CHUNK] +
                       (frames_num % LIST_CHUNK)*2,
                       GL_COMPILE_AND_EXECUTE);
            glClear (GL_COLOR_BUFFER_BIT);
            frames_num++;
            break;
        case ERASE_END:
            glFlush ();
            glEndList ();
            /* Generate another display list - for color background */
            glNewList (ogllists[frames_num / LIST_CHUNK] +
                       (frames_num % LIST_CHUNK)*2 - 1,
                       GL_COMPILE_AND_EXECUTE);
            glClearColor (color_table[0],
                          color_table[NCOLOR],
                          color_table[NCOLOR*2], 0.0f);
            glEndList ();
            if (frames_num > 1)
                fprintf (stderr, "Finished all frames\n");
            break;
        default:
            break;
    }
    /* Reset clipping */
    glDisable (GL_CLIP_PLANE0);
    glDisable (GL_CLIP_PLANE1);
    glDisable (GL_CLIP_PLANE2);
    glDisable (GL_CLIP_PLANE3);
}

void oglstartanimation ()
{
/*< start animation >*/
    animate = true;
    glutTimerFunc (delay, oglanimate, 0);
}

void oglanimate (int value)
/*< animation >*/
{
    if (!animate)
        return;

    switch (direction) {
        case 0: /* Forwards */
            if (curr_frame == (frames_num - 1))
                curr_frame = 0;
            else
                curr_frame++;
            break;
        case 1: /* Backwards */
            if (curr_frame == 0)
                curr_frame = frames_num - 1;
            else
                curr_frame--;
            break;
        case 2: /* Both ways */
            if (dirway == 0 && curr_frame == (frames_num - 1)) {
                dirway = 1;
                curr_frame = frames_num - 1;
            } if (dirway == 1 && curr_frame == 0) {
                dirway = 0;
                curr_frame = 1;
            } else {
                curr_frame += dirway ? -1 : 1;
            }
            break;
    }

    glutPostRedisplay ();
    glutTimerFunc (delay, oglanimate, 0);
}

void oglclose (int status)
/*< close >*/
{
    switch (status) {
        case CLOSE_PAUSE:
            break;
        case CLOSE_ERROR:
        case CLOSE_INTERRUPT:
        case CLOSE_NORMAL:
            if (frames_num > 1 && !animate)
                oglstartanimation ();
            oglbuildmenu ();
#if defined(__APPLE__) && (GLUT_MACOSX_IMPLEMENTATION >= 2)
            for (;;)
                glutCheckLoop ();
#else
            glutMainLoop ();
#endif
            break;
        case CLOSE_FLUSH:
            glFlush ();
        default:
            break;
    }
}

void oglattr (int command, int value, int v1, int v2, int v3)
/*< attr >*/
{
    GLdouble eq[4];

    switch (command) {
        case SET_COLOR:
            oglcolor = value;
            glColor3f (color_table[oglcolor],
                       color_table[NCOLOR + oglcolor],
                       color_table[NCOLOR*2 + oglcolor]);
            break;
        case SET_COLOR_TABLE:
            color_table[value] = v1 / (float)MAX_GUN;
            color_table[NCOLOR + value] = v2 / (float)MAX_GUN;
            color_table[NCOLOR*2 + value] = v3 / (float)MAX_GUN;
            if (value == oglcolor)
                glColor3f (color_table[oglcolor],
                           color_table[NCOLOR + oglcolor],
                           color_table[NCOLOR*2 + oglcolor]);
            break;
        case SET_WINDOW:
            /* Right */
            glEnable (GL_CLIP_PLANE0);
            eq[0] = -1; eq[1] = 0; eq[2] = 0; eq[3] = v2 + 0.5;
            glClipPlane (GL_CLIP_PLANE0, eq);
            /* Left */
            glEnable (GL_CLIP_PLANE1);
            eq[0] = 1; eq[1] = 0; eq[2] = 0; eq[3] = -value + 0.5;
            glClipPlane (GL_CLIP_PLANE1, eq);
            /* Up */
            glEnable (GL_CLIP_PLANE2);
            eq[0] = 0; eq[1] = -1; eq[2] = 0; eq[3] = v3 + 0.5;
            glClipPlane (GL_CLIP_PLANE2, eq);
            /* Down */
            glEnable (GL_CLIP_PLANE3);
            eq[0] = 0; eq[1] = 1; eq[2] = 0; eq[3] = -v1 + 0.5;
            glClipPlane (GL_CLIP_PLANE3, eq);
            break;
        default:
            break;
    }
}

void oglplot(int x, int y, int draw)
/*< plot >*/
{
    static int oldx = 0, oldy = 0;

    if (draw) {
        glBegin (GL_LINES);
        glVertex2i (oldx, oldy);
        glVertex2i (x, y);
        glEnd ();
    } else {
        dev.lost = 0;
    }

    oldx = x;
    oldy = y;
}

void oglstartpoly (int npts)
/*< startploy >*/
{
    glBegin (GL_LINE_STRIP);
}

void oglmidpoly (int x, int y)
/*< midploy >*/
{
    glVertex2i (x, y);
}

void oglendpoly (int last)
/*< midploy >*/
{
    glEnd ();
}

void oglpoint(int x, int y)
/*< point >*/
{
    glBegin (GL_POINTS);
    glVertex2i (x, y);
    glEnd ();
}

void oglarea (int npts, struct vertex *head)
/*< area >*/
{
    int i, x, y;
    int xvmin = INT_MAX, xvmax = INT_MIN,
        yvmin = INT_MAX, yvmax = INT_MIN;

    /* Use stencil buffer to implement the even-odd rule */
    glColorMask (GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE);
    glEnable (GL_STENCIL_TEST);
    glClear (GL_STENCIL_BUFFER_BIT);
    glStencilMask (0x01);
    glStencilFunc (GL_ALWAYS, 0, 0);
    /* First - calculate self-intersections in the stencil buffer */
    glStencilOp (GL_KEEP, GL_KEEP, GL_INVERT);
    glBegin (GL_TRIANGLE_FAN);
    for (i = 0; i < npts && i < MAXVERT; i++) {
        x = head->x;
        y = head->y;
        glVertex2i (x, y);
        head = head->next;
        if (x < xvmin)
            xvmin = x;
        if (x > xvmax)
            xvmax = x;
        if (y < yvmin)
            yvmin = y;
        if (y > yvmax)
            yvmax = y;
    }
    glEnd ();
    glStencilOp (GL_KEEP, GL_KEEP, GL_KEEP);
    /* Second - draw polygons only where stencil is 1 - odd number of intersection */
    glStencilFunc (GL_EQUAL, 1, 1);
    glColorMask (GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE);
    glBegin (GL_QUADS);
    glVertex2i (xvmin, yvmin);
    glVertex2i (xvmax, yvmin);
    glVertex2i (xvmax, yvmax);
    glVertex2i (xvmin, yvmax);
    glEnd ();
    glClear (GL_STENCIL_BUFFER_BIT);
    glDisable (GL_STENCIL_TEST);
}

void oglraster (int xpix, int ypix, int xmin, int ymin, int xmax, int ymax, 
                unsigned char **raster_block, int orient, int dither_it)
{
/*< raster >*/
    int i, j, k, l, hnum, wnum, kmax, lmax, width, height;
    GLuint *tex_id;
    float stepy, stepx;
    float xtex, ytex;
    float x_min, x_max, y_min, y_max;

    /* Colormap table */
    if (!dither_it) {
        glPixelTransferi (GL_MAP_COLOR, GL_TRUE);
        glPixelMapfv (GL_PIXEL_MAP_I_TO_R, NCOLOR, color_table);
        glPixelMapfv (GL_PIXEL_MAP_I_TO_G, NCOLOR, &color_table[NCOLOR]);
        glPixelMapfv (GL_PIXEL_MAP_I_TO_B, NCOLOR, &color_table[NCOLOR * 2]);
    }

    height = orient % 2 ? xpix : ypix;
    width = orient % 2 ? ypix : xpix;

    wnum = width / TEX_SIZE + ((width % TEX_SIZE) != 0);
    hnum = height / TEX_SIZE + ((height % TEX_SIZE) != 0);
    stepy = (ymax - ymin + 1) / (height / (float)TEX_SIZE);
    stepx = (xmax - xmin + 1) / (width / (float)TEX_SIZE);

    tex_id = (GLuint*)malloc (hnum*wnum*sizeof (GLuint));
    glGenTextures (hnum*wnum, tex_id);

    /* Loop over tiles and make textures */
    for (i = 0; i < wnum; i++) {
        kmax = i != (wnum - 1) ? TEX_SIZE : width - i * TEX_SIZE;
        for (j = 0; j < hnum; j++) {
            lmax = j != (hnum - 1) ? TEX_SIZE : height - j * TEX_SIZE;
            /* Copy samples to the local buffer */
            switch (orient) {
                case 0:
                    for (l = 0; l < lmax; l++) {
                        for (k = 0; k < kmax; k++) {
                            tex_buf[k*TEX_SIZE + l] =
                            raster_block[height - j*TEX_SIZE - l - 1][i*TEX_SIZE + k];
                        }
                    }
                    break;
                case 1:
                    for (k = 0; k < kmax; k++) {
                        for (l = 0; l < lmax; l++) {
                            tex_buf[k*TEX_SIZE + l] =
                            raster_block[width - i*TEX_SIZE - k - 1][height - j*TEX_SIZE - l - 1];
                        }
                    }
                    break;
                case 2:
                    for (l = 0; l < lmax; l++) {
                        for (k = 0; k < kmax; k++) {
                            tex_buf[k*TEX_SIZE + l] =
                            raster_block[j*TEX_SIZE + l][width - i*TEX_SIZE - k - 1];
                        }
                    }
                    break;
                case 3:
                    for (k = 0; k < kmax; k++) {
                        for (l = 0; l < lmax; l++) {
                            tex_buf[k*TEX_SIZE + l] =
                            raster_block[i*TEX_SIZE + k][j*TEX_SIZE + l];
                        }
                    }
                    break;
            }

            glBindTexture (GL_TEXTURE_2D, tex_id[i*hnum + j]);
            glTexEnvi (GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);
            glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
            glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP);
            glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
            glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
            /* Send texture samples to OpenGL */
            glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB, TEX_SIZE, TEX_SIZE, 0,
                                         dither_it ? GL_LUMINANCE : 
                                                     GL_COLOR_INDEX,
                                         GL_UNSIGNED_BYTE, tex_buf);
            glBindTexture (GL_TEXTURE_2D, 0);
        }
    }
    /* Loop over tiles and render textures */
    for (i = 0; i < wnum; i++) {
        x_min = xmin + i*stepx;
        x_max = i != (wnum - 1) ? xmin + (i + 1)*stepx : xmax;
        xtex = i != (wnum - 1) ? 1.0 : 1.0*(width - i*TEX_SIZE) / (float)TEX_SIZE;
        for (j = 0; j < hnum; j++) {
            y_min = ymin + j*stepy;
            y_max = j != (hnum - 1) ? ymin + (j + 1)*stepy : ymax;
            ytex = j != (hnum - 1) ? 1.0 : 1.0*(height - j*TEX_SIZE) / (float)TEX_SIZE;
            glEnable (GL_TEXTURE_2D);
            glBindTexture (GL_TEXTURE_2D, tex_id[i*hnum + j]);
            glBegin (GL_QUADS);
            glTexCoord2f (0, 0);
            glVertex2i (x_min, y_min);
            glTexCoord2f (0, xtex);
            glVertex2i (x_max, y_min);
            glTexCoord2f (ytex, xtex);
            glVertex2i (x_max, y_max);
            glTexCoord2f (ytex, 0);
            glVertex2i (x_min, y_max);
            glEnd ();
            glBindTexture (GL_TEXTURE_2D, 0);
            glDisable (GL_TEXTURE_2D);
        }
    }

    if (!dither_it)
        glPixelTransferi (GL_MAP_COLOR, GL_FALSE);

    free (tex_id);
}

void oglredraw (void)
/*< OpenGL redraw >*/
{
    /* Set background color */
    glCallList (ogllists[curr_frame / LIST_CHUNK] +
                (curr_frame % LIST_CHUNK)*2 + 1);
    /* Plotting */
    glCallList (ogllists[curr_frame / LIST_CHUNK] +
                (curr_frame % LIST_CHUNK)*2);
    glutSwapBuffers ();

    if (frames_num > 1 && curr_title_frame != (int) curr_frame) {
        curr_title_frame = curr_frame;
        snprintf (title_strbuf, MAX_TITLE_STR - 1, "%s: frame %d of %d",
                  pen_title, curr_title_frame + 1, frames_num);
        glutSetWindowTitle (title_strbuf);
    }
}

void oglreshape (int width, int height)
/*< OpenGL reshape >*/
{
    GLdouble wh = 1.0;

    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    if (!stretchy) {
        if (VP_ABSOLUTE == size) {
            ny = height*DEV_SCALE;
            nx = ny*width/height;
            glOrtho (-1, nx,
                     -1, ny, -1, 1);
        } else {
            if (width*VP_SCREEN_RATIO <= height) {
                wh = (GLfloat)height / (GLfloat)width / VP_SCREEN_RATIO;
                glOrtho (-1, nx,
                         -1, ny*wh, -1, 1);
            } else {
                wh = ((GLfloat)width / (GLfloat)height)*VP_SCREEN_RATIO;
                glOrtho (-1, nx*wh,
                         -1, ny, -1, 1);
            }
        }
    } else
        glOrtho (-1, nx,
                 -1, ny, -1, 1);
    glMatrixMode (GL_MODELVIEW);
    glLoadIdentity ();

    glViewport (0, 0, width, height);

    glutPostRedisplay ();
}

void oglmenu (int value)
/*< OpenGL menu >*/
{
    switch (value) {
        case MENU_NEXT:
            if (!animate) {
                if (curr_frame == (frames_num - 1))
                    curr_frame = 0;
                else
                    curr_frame++;
                break;
            }
            break;
        case MENU_PREV:
            if (!animate) {
                if (curr_frame == 0)
                    curr_frame = frames_num - 1;
                else
                    curr_frame--;
            }
            break;
        case MENU_RESTART:
            if (!animate) {
                if (direction == 1)
                    curr_frame = frames_num - 1;
                else
                    curr_frame = 0;
            }
            break;
        case MENU_RUN:
            oglstartanimation ();
            oglbuildmenu ();
            break;
        case MENU_STOP:
            animate = false;
            oglbuildmenu ();
            break;
        case MENU_DIRECTION:
            direction++;
            if (direction > 2)
                direction = 0;
            oglbuildmenu ();
            break;
        case MENU_STRETCHY:
            stretchy = (bool) !stretchy;
            oglreshape (glutGet (GLUT_WINDOW_WIDTH), glutGet (GLUT_WINDOW_HEIGHT));
            oglbuildmenu ();
            break;
        case MENU_FULLSCREEN:
            glutFullScreen ();
            break;
        case MENU_QUIT:
            oglquit (0);
            break;
        default:
            break;    
    }
    glutPostRedisplay ();
}

void oglkeyboard (unsigned char key, int x, int y)
/*< OpenGL keyboard callback >*/
{
    switch (key) {
        case 'F': /* Fast */
        case 'f':
            if (frames_num > 1) {
                delay *= 0.5;
                if (delay < MIN_DELAY)
                    delay = MIN_DELAY;
                fprintf (stderr, "Animation delay [ms]: %f\n", delay);
            }
            break;
        case 'S': /* Slow */
        case 's':
            if (frames_num > 1) {
                delay *= 2.0;
                if (delay > MAX_DELAY)
                    delay = MAX_DELAY;
                fprintf (stderr, "Animation delay [ms]: %f\n", delay);
            }
            break;
        case 'N': /* Next */
        case 'n':
	    if (frames_num > 1) {
		if (animate) {
		    animate = false;
		    oglbuildmenu ();
		}
		if (curr_frame == (frames_num - 1))
                    curr_frame = 0;
                else
                    curr_frame++;
                break;
            }
            break;
        case 'm': /* Prev */
        case 'M':
            if (frames_num > 1) {
		if (animate) {
		    animate = false;
		    oglbuildmenu ();
		}
                if (curr_frame == 0)
                    curr_frame = frames_num - 1;
                else
                    curr_frame--;
            }
            break;
        case 'R': /* Run */
        case 'r':
            if (!animate && frames_num > 1) {
                oglstartanimation ();
                oglbuildmenu ();
            }
            break;
        case '.': /* Stop */
            if (animate && frames_num > 1) {
                animate = false;
                oglbuildmenu ();
            }
            break;
        case 'D': /* Direction */
        case 'd':
            if (frames_num > 1) {
                direction++;
                if (direction > 2)
                    direction = 0;
                fprintf (stderr, "Animation direction: %s\n",
                         direction == 2 ? "Both ways" :
                         direction == 1 ? "Backwards" : "Forwards");
                oglbuildmenu ();
            }
            break;
        case 'T': /* Stretchy */
        case 't':
            stretchy = (bool) !stretchy;
            oglreshape (glutGet (GLUT_WINDOW_WIDTH), 
			glutGet (GLUT_WINDOW_HEIGHT));
            oglbuildmenu ();
            break;
        case 'Q': /* Quit */
        case 'q':
            oglquit (0);
            break;
        default:
            break;    
    }
    glutPostRedisplay ();
}

/*
  Copyright (C) 1987 The Board of Trustees of Stanford University
  
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
*/

/*
 *
 *  source file:   ./filters/init_vplot.c
 *
 * Joe Dellinger (SEP), Feb 18 1988
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Joe Dellinger, Feb 20 1988
 *	#define GETPAR to be fetch if SEPlib version.
 * Joe Dellinger Feb 24 1988
 * 	Moved gen_do_dovplot to genlib, where it belongs.
 *	txfont, txprec, txovly, overlay defaults remembered.
 * Joe Dellinger Feb 28 1988
 *	Changed fatness to scale with size of screen and scale,
 *	like any regular geometric attribute.
 * Joe Dellinger Mar 4 1988
 *	Fixed slight bug with fatness scaling and style=old.
 * Joe Dellinger Mar 17 1988
 *	Added "colormask" option.
 * Joe Dellinger April 15 1988
 *	Check for illegal colormask values.
 * Joe Dellinger Oct 28 1988
 *	Put in "no_stretch_text" flag.
 * Steve Cole Feb 2 1989
 *      Added default x and y scale parameters for use by vppen.
 * Joe Dellinger May 7 1989
 *	Added break=ignore option.
 *	Made txsquare=yes the default.
 * Joe Dellinger May 20 1989
 *	"/dev/tty" may NOT be openable. Behave gracefully in this case.
 * Joe Dellinger August 2 1989
 *	Put in redpow, greenpow, bluepow, redmap, greenmap, bluemap
 * W. Bauske IBM 03-26-91 
 *	Apply the SysV fixes to the code for the RS/6000
 *	Removed re-declare of system alloc routines for RS/6000
 * Dave Nichols 9-17-92
 *      Include stdlib.h if it is available instead of defining malloc.  
 * Stew Levin  2/27/95 
 *	Solaris mods.
 * Bob Clapp 1/24/96
 *      Changed a whole bunch of fetches to getches
 * Bob Clapp 10/98 
 *      Changed signals from bsd to posix1 for linux
 */

#include	<stdio.h>
#include	<math.h>

extern FILE * fdopen (int fd, const char *mode);

#include	<sys/ioctl.h>
#include	<sys/types.h>
#include	<sys/stat.h>
#include <fcntl.h>

#include <unistd.h>

#include	<ctype.h>
#include	<string.h>

#include <rsfplot.h>
/*^*/

#include	"../include/params.h"	/* for machine dependencies */
#include	"../include/enum.h"
#include	"../include/err.h"
#include	"../include/attrcom.h"
#include	"../include/intcom.h"
#include	"../include/mesgcom.h"
#include	"../include/erasecom.h"
#include	"../include/closestat.h"
#include	"../include/pat.h"
#include	"../include/vertex.h"
#include	"../include/round.h"
#include	"../include/extern.h"

#include "../utilities/util.h"
#include "../genlib/genpen.h"

#include "init_vplot.h"

#define		OPEN_ERROR	-1

/*
 * Other things that may need to be reset in dev.open
 * (Can't reset them some of them in dev.reset, because the user may
 * override from the command line.)
 */
/* should pipes be allowed for input? */
int             allow_pipe = YES;

/*
 * These may be reset to device-dependent defaults.
 */
float           fatmult = 1.;
float           patternmult = 1.;

/*
 * Look in extern.h for a better-organized list of the preceding.
 * Here I have left things which are also filter options with the
 * other filter options, even though they also belong in the above
 * categories.
 */

/*
 * flags and variables
 */
char            callname[25];
int             xcenterflag, ycenterflag;
int             ever_called = NO;
int             first_time = YES;
int             device_open = NO;	/* used by ERR */
int             out_isatty = YES;	/* If NO, output is a file or pipe */
int             nplots = 0;	/* number of plots made */
bool             no_stretch_text = true;	/* Don't allow stretched text? */

/*
 * coordinate variables
 */
int             xwmax, xwmin, ywmax, ywmin;	/* window */
int             xnew, ynew;	/* new pen location */
int             xold, yold;	/* old pen location */
char           *txbuffer;
int             txbuflen, vxbuflen;
struct vertex  *vxbuffer;
int             xret, yret;
float           mxx, mxy, myx, myy;
/*
 * This is so the device can throw in a coordinate transformation
 * for its convenience ON TOP OF whatever transformation the user
 * wants.
 */
int             default_rotate = 0, default_hshift = 0, default_vshift = 0;
float           default_scale = 1., default_xscale = 1., default_yscale = 1.;

/*
 * attribute variables
 */
int             linestyle;
int             cur_color = DEFAULT_COLOR;
int             pat_color = DEFAULT_COLOR + 1;
int             next_color;

int             default_txfont, default_txprec, default_txovly;
int             fat = 0;
int             afat = 0;
int             ipat = 0;	/* currently loaded pattern */
struct pat      pat[NPAT + 1];
float           dashsum = 0.;
int             dashon = NO;	/* Dashed lines? */
float           dashes[MAXDASH * 2];
float           dashpos = 0.;	/* Position in current dashing pattern */
int             color_set[MAX_COL + 1][_NUM_PRIM];
int             num_col_8;


/*
 * filter options - flags
 */

/*
 * Invras determines the polarity of dithered raster.
 * invras=n means raster works the same way as vectors; what is normally
 * WHITE on most devices is BLACK on a hardcopy black and white device.
 * invras=y is the proper default to make dithered images not come out as negatives
 */
bool             invras = true;
bool             window = true;
bool             shade = true;
bool             framewindows = false;
bool             endpause = false;
bool             honor_background = true;

bool             wantras = true;
bool             colormask[5];

/*
 * filter options - enumerated
 */
vp_plotstyle    style = VP_NO_STYLE_YET;
vp_plotstyle    default_style = VP_STANDARD;
int             rotate;
int             size = RELATIVE;
int             erase = FORCE_INITIAL | DO_LITERALS;

/*
 * filter options - valued
 */
int             xcenter, ycenter;	/* Vplot of point to force as center */
int             fatbase = 0;
int             epause = 0;	/* time to pause before erasing screen */
bool            overlay = false;	/* 1=overlay 0=replace */
int             default_overlay;
bool		serifs_OK = true;  /* If false, substitute serif fonts */

/*
 * 0 = none
 * 1 = random
 * 2 = Ordered
 * 3 = Floyd-Steinberg
 * 4 = Halftone
 */
int             dither = 1;	/* Dithering type */

int             xWmax, xWmin, yWmax, yWmin;
float           hshift, vshift;	/* Allow global translation of plot */
float           scale;	/* global scale */
float           xscale;	/* global x-scale */
float           yscale;	/* global y-scale */
float           hdevscale;	/* Vplot units to device units for x */
float           vdevscale;	/* Vplot units to device units for y */
float           txscale;/* global text scale */
float           mkscale;/* global marker scale */
float           dashscale;	/* global dashed line scale */
char            *interact=NULL;	/* Where to store coordinate
						 * file */
float           greyc = 1.;	/* Nonlinear correction */
float           pixc = 1.;	/* Pixel overlap correction */
float           redpow = 1., redmap[4] = {1., 0., 0., 0.};
float           greenpow = 1., greenmap[4] = {0., 1., 0., 0.};
float           bluepow = 1., bluemap[4] = {0., 0., 1., 0.};

/* filter options - resettable between plots */
int             user_rotate;
float           user_txscale;
float           user_mkscale;
float           user_dashscale;
float           user_scale;
float           user_xscale;
float           user_yscale;
int             user_size;
float           user_hshift;
float           user_vshift;
bool             user_xwmax_flag;
float           user_xwmax;
bool             user_ywmax_flag;
float           user_ywmax;
bool             user_xwmin_flag;
float           user_xwmin;
bool            user_ywmin_flag;
float           user_ywmin;

int             ifat = 0;
float           fatmult_orig;

bool mono;

/*
 * file and terminal control variables
 */
int             pltoutfd, stderrfd, controlfd;
FILE *pltout;

void  (*message) (int command, const char* string) = genmessage;
struct stat     stderrstat;
struct stat     pltoutstat;
FILE           *pltin;

FILE           *controltty;
char            outbuf[BUFSIZ];

#include <stdlib.h>

char            group_name[MAXFLEN + 1];
int             group_number = 0;
FILE           *pltinarray[MAXIN];
char            pltinname[MAXIN][MAXFLEN + 1];
char            pltname[MAXFLEN + 1] = "";

extern void reset_windows (void);

void init_vplot (int argc, char* argv[])
/*< Initialize and declare global variables. >*/
{
    char           *stringptr;
    int             ii;
    char            *string;
    float           ftemp;


    txbuffer = (char *) malloc (TXBUFLEN);
    txbuflen = TXBUFLEN;
/*
 * Sun III lint complains about "pointer alignment problem" here,
 * although the documentation makes it sound like that shouldn't
 * be possible.
 */
    vxbuffer = (struct vertex *) malloc (sizeof (struct vertex) * VXBUFLEN);
    vxbuflen = VXBUFLEN;

    /*
     * If the device can't do color, it can set mono to YES If device is
     * mono, this overrides the user's insistence that it isn't. So GETPAR
     * before we call dev.open. 
     */
    if (!sf_getbool ("mono",&mono)) mono=false;
    /* no color */

    /*
     * Initialize all patterns to be undefined. (device can create a
     * device-dependent default set if it wishes) 
     */
    for (ii = 0; ii <= NPAT; ii++)
    {
	pat[ii].patbits = NULL;
    }

/*
 * The device-independent code MAY NOT actually read from
 * the terminal itself. However, these variables are 
 * declared so that the device-dependent routines can use
 * them if they wish as a courtesy.
 */
    controlfd = open ("/dev/tty", 0);
    if (controlfd == OPEN_ERROR)
    {
	controltty = NULL;
    }
    else
    {
	controltty = fdopen (controlfd, "r");
    }

    pltout = stdout;

    /*
     * Call device open before doing anything else. this finalizes pltout 
     */
    dev.open (argc,argv);
    device_open = YES;

    /*
     * If graphics output going to control terminal, disable echoing and
     * arrange for use of device's message routine 
     */
    pltoutfd = fileno (pltout);
    stderrfd = fileno (stderr);
    out_isatty = isatty (pltoutfd);

    sf_getbool ("endpause", &endpause);
    sf_getbool ("cachepipe",&dev.cachepipe);
    sf_getbool ("shade", &shade);
    sf_getbool ("wantras", &wantras);
    sf_getbool ("window", &window);
    sf_getbool ("frame", &framewindows);
    sf_getbool ("overlay", &overlay);
    default_overlay = overlay;
    sf_getbool ("invras", &invras);
    sf_getbool ("txsquare", &no_stretch_text);
    sf_getbool ("serifs", &serifs_OK);
    sf_getbool ("background",&honor_background);

    if (!sf_getbools ("colormask",colormask,5)) 
	colormask[0] = colormask[1] = colormask[2] = 
	    colormask[3] = colormask[4] = true;
    if (!colormask[4] && colormask[3]) colormask[4] = true;

    if (!sf_getfloat ("redpow",  &redpow)) redpow=1.0;
    if (!sf_getfloat ("greenpow",  &greenpow)) greenpow=1.0;
    if (!sf_getfloat ("bluepow",  &bluepow)) bluepow=1.0;

    if (redpow <= 0. || greenpow <= 0. || bluepow <= 0.)
	ERR (FATAL, name, "Invalid color pow option.");
    
    sf_getfloats ("red",  redmap, 4);
    sf_getfloats ("green",  greenmap, 4);
    sf_getfloats ("blue",  bluemap, 4);

    sf_getint ("dither",  &dither); /* dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning */
    sf_getfloat ("greyc",  &greyc); /* "grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" */
    sf_getfloat ("pixc",  &pixc);   /* "pixel  correction" controls  alteration of the grey scale, see "man vplotraster". */

    sf_getint ("txfont",  &dev.txfont);
    sf_getint ("txprec",  &dev.txprec);
    sf_getint ("txovly",  &dev.txovly);

    if (! serifs_OK)
    {
        if (dev.txfont == DEFAULT_HARDCOPY_FONT) dev.txfont = DEFAULT_SANSSERIF_FONT;
        if (dev.txfont == GREEK_SERIF_FONT) dev.txfont = GREEK_SANSSERIF_FONT;
    }

    default_txfont = dev.txfont;
    default_txprec = dev.txprec;
    default_txovly = dev.txovly;

    if (NULL != (string = sf_getstring ("erase")))
    {
	if ((string[0] == 'n') || (string[0] == 'N'))
	    erase = NO;
	else
	if ((string[0] == 'o') || (string[0] == 'O'))
	    erase = FORCE_INITIAL;
	else
	if ((string[0] == 'l') || (string[0] == 'L'))
	    erase = DO_LITERALS;
	else
	    erase = FORCE_INITIAL | DO_LITERALS;
    }

    if (NULL != (string = sf_getstring ("break")))
    {
	if (string[0] == 'b')
	    dev.brake = BREAK_BREAK;
	else
	if (string[0] == 'e')
	    dev.brake = BREAK_ERASE;
	else
	    dev.brake = BREAK_IGNORE;
    }

    xcenter = 0;
    ycenter = 0;
    xcenterflag = NO;
    ycenterflag = NO;
    if (sf_getfloat ("xcenter",  &ftemp))
    {
	xcenterflag = YES;
	xcenter = ROUND (ftemp * RPERIN);
    }
    if (sf_getfloat ("ycenter",  &ftemp))
    {
	ycenterflag = YES;
	ycenter = ROUND (ftemp * RPERIN);
    }

    if ((stringptr = getenv ("PATTERNMULT")) != NULL)
    {
	sscanf (stringptr, "%f", &patternmult);
    }
    if (!sf_getfloat ("patternmult",  &patternmult)) patternmult = 1.;

    interact = sf_getstring ("interact");
    if (!sf_getint ("pause",  &epause)) epause=0;

    if (NULL != interact)
    {
	epause = 0;		/* interact makes it own sort of pausing */
	endpause = false;
    }

    /*
     * Find the default style 
     */
    stringptr = NULL;
    if (NULL != (string = sf_getstring ("style")))
	stringptr = string;
    else
	stringptr = getenv ("PLOTSTYLE");
    if (stringptr != NULL)
    {
	if ((stringptr[0] == 'r') || (stringptr[0] == 'R') ||
	    (stringptr[0] == 'm') || (stringptr[0] == 'M'))
	    default_style = VP_ROTATED;
	else
	if ((stringptr[0] == 'o') || (stringptr[0] == 'O'))
	    default_style = VP_OLD;
	else
	if ((stringptr[0] == 'a') || (stringptr[0] == 'A'))
	    default_style = VP_ABSOLUTE;
	else
	    default_style = VP_STANDARD;
    }

/*
 * Options changeable between calls to dovplot
 * (By calling reset_parameters or reset())
 * Dovplot calls reset every time it starts. It only calls
 * reset_parameters the first time.
 *
 * Things in this category:
 * user_*
 * fatmult_orig, fatbase
 */

    if (!sf_getfloat ("fatmult",  &fatmult)) {
	if ((stringptr = getenv ("FATMULT")) != NULL)
	{
	    sscanf (stringptr, "%f", &fatmult);
	}
    }

    fatmult_orig = fatmult;

    if (!sf_getint ("rotate",  &user_rotate)) user_rotate = 0;

    if (!sf_getfloat ("txscale",  &user_txscale)) user_txscale = 1.0;
    if (!sf_getfloat ("mkscale",  &user_mkscale)) user_mkscale = 1.0;
    if (!sf_getfloat ("dashscale",  &user_dashscale)) user_dashscale = 1.0;

    if (!sf_getfloat ("scale",  &user_scale)) user_scale = 1.0;
    if (!sf_getfloat ("xscale",  &user_xscale)) user_xscale = 1.0;
    if (!sf_getfloat ("yscale",  &user_yscale)) user_yscale = 1.0;

    user_size = size;
    if (NULL != (string = sf_getstring ("size")))
    {
	if ((string[0] == 'a') || (string[0] == 'A'))
	    user_size = VP_ABSOLUTE;
	else
	    user_size = RELATIVE;
    }

    if (!sf_getfloat ("hshift",  &user_hshift) &&
	!sf_getfloat ("xshift",  &user_hshift)) user_hshift = 0.;
    if (!sf_getfloat ("vshift",  &user_vshift) &&
	!sf_getfloat ("yshift",  &user_vshift)) user_vshift = 0.;

    user_xwmax_flag = sf_getfloat ("xwmax",  &user_xwmax);
    user_ywmax_flag = sf_getfloat ("ywmax",  &user_ywmax);
    user_xwmin_flag = sf_getfloat ("xwmin",  &user_xwmin);
    user_ywmin_flag = sf_getfloat ("ywmin",  &user_ywmin);

    if (!sf_getint ("fat",  &fatbase)) fatbase = 0;
    /* base line fatness */


/*
 *  These parameters can simply be changed at any time with no
 *  need for re-initialization of anything else:
 *
 *  shade, wantras
 *
 */

}

void init_colors (void)
/*< init colors >*/
{
int             ii;

    /*
     * Set up the default color table 
     */

/*
 * First 7 colors are assumed to map to the standard 7 pen colors
 * on ALL devices, even those with no settable colors!
 */
    for (ii = 0; ii < 8; ii++)
    {
/*     if(color_set[ii][STATUS]!=SET){*/
	    color_set[ii][STATUS] = SET;
	    color_set[ii][_RED] = MAX_GUN * ((ii & 2) / 2);
	    color_set[ii][_GREEN] = MAX_GUN * ((ii & 4) / 4);
	    color_set[ii][_BLUE] = MAX_GUN * ((ii & 1) / 1);
	    color_set[ii][_GREY] = greycorr ((int) ((MAX_GUN * ii) / 7));
/*   }*/
    }

    if (mono)
    {
	/* Monochrome devices are assumed to have no settable colors */
	dev.num_col = 0;
    }

    num_col_8 = (dev.num_col > 8) ? dev.num_col : 8;

    if (mono)
    {
	color_set[0][MAP] = 0;
	for (ii = 1; ii <= MAX_COL; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][MAP] = 7;
	}
	for (ii = num_col_8; ii < 256; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][_GREY] = color_set[((ii - 8) % 7) + 1][_GREY];
	}
	/* Put a grey scale in the upper half of the color table */
	for (ii = 256; ii <= MAX_COL; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][_GREY] = greycorr (ii - 256);
	}
    }
    else
    {
	/*
	 * Unmapped colors shouldn't be mapped; ie, they map to themselves 
	 */

	for (ii = 0; ii < num_col_8; ii++)
	{
	    color_set[ii][MAP] = ii;
	 }
	/*
	 * Colors outside the range of this terminal map cyclically back into
	 * colors 1 through 7 
	 */
	for (ii = num_col_8; ii <= MAX_COL; ii++)
	{
	    color_set[ii][MAP] = ((ii - 8) % 7) + 1;
	}
    }
}

void setstyle (vp_plotstyle new_style)
/*< set style >*/
{
    /*
     * Check to see if the style has changed 
     */
    if (new_style == style)
	return;

    style = new_style;
    reset_parameters ();
}

void reset_parameters (void)
/*< reset parameters >*/
{
    float           inches;	/* scaling base for y axis */
    float           screenheight, screenwidth;	/* true size of the screen */
    int             ix, iy;

    dev.xorigin = 0;
    dev.yorigin = 0;

    rotate = default_rotate;
    rotate += user_rotate;

    txscale = user_txscale;
    mkscale = user_mkscale;
    dashscale = user_dashscale;

    scale = default_scale * user_scale;
    xscale = default_xscale * user_xscale;
    yscale = default_yscale * user_yscale;

    fatmult = fatmult_orig;

    size = user_size;

    switch (style)
    {
/*
 * The old standard on the machine erebus.
 * Pretty much dead now. Still useful for some old programs nobody's
 * wanted to update.
 */
	case VP_OLD:
	    txscale /= 3.;
	    fatmult /= 3.;
	    scale *= 3.;
	    inches = VP_STANDARD_HEIGHT;
	    break;
/*
 * The old standard on the machine mazama. A useful coordinate system
 * for geological sorts of plots. 
 * The Y axis goes the long way, across the screen, which is the device's
 * horizontal axis.
 */
	case VP_ROTATED:
	    rotate += 90;
	    inches = VP_ROTATED_HEIGHT;
	    break;
	case VP_ABSOLUTE:
	    size = VP_ABSOLUTE;
	case VP_STANDARD:
	default:
	    inches = VP_STANDARD_HEIGHT;
	    break;
    }

    if (rotate >= 0)
	rotate = rotate % 360;
    else
	rotate = ((rotate % 360) + 360) % 360;

    mxx = cosf (SF_PI * rotate / 180.);
    myy = cosf (SF_PI * rotate / 180.);
    mxy = sinf (SF_PI * rotate / 180.);
    myx = -sinf (SF_PI * rotate / 180.);

    if (size == VP_ABSOLUTE)
    {
	vdevscale = dev.pixels_per_inch / (float) (RPERIN * dev.aspect_ratio);
	hdevscale = dev.pixels_per_inch / (float) RPERIN;
    }
    else
    {
	/*
	 * Fit the inches x inches unit square into a displayable box with
	 * aspect ratio SCREEN_RATIO 
	 */
	screenwidth = (dev.xmax - dev.xmin) * dev.pixels_per_inch;
	screenheight =
	 (dev.ymax - dev.ymin) * dev.pixels_per_inch * dev.aspect_ratio;
	if ((screenheight / screenwidth) > VP_SCREEN_RATIO)
	{
	    vdevscale = (VP_SCREEN_RATIO * ((dev.xmax - dev.xmin) / dev.aspect_ratio)) /
	     (inches * RPERIN);
	    hdevscale = vdevscale * dev.aspect_ratio;
	}
	else
	{
	    vdevscale = (dev.ymax - dev.ymin) / (inches * RPERIN);
	    hdevscale = vdevscale * dev.aspect_ratio;
	}
    }

    hshift = default_hshift;
    vshift = default_vshift;

    if (style == VP_ROTATED)
    {
	vshift += dev.ymax - dev.ymin;
    }

    yscale *= scale;
    xscale *= scale;
    mkscale *= scale;

/*
 * Set up fatness multiplication factor
 */
    fatmult *= scale * hdevscale * RPERIN / FATPERIN;

    /*
     * The point (xcenter,ycenter) in vplot coordinates is to be centered in
     * the screen. 
     */
    if (xcenterflag || ycenterflag)
    {
	vptodevxy (xcenter, ycenter, &ix, &iy);
	if (xcenterflag)
	{
	    hshift += (dev.xmax + dev.xmin) / 2 - ix;
	}
	if (ycenterflag)
	{
	    vshift += (dev.ymax + dev.ymin) / 2 - iy;
	}
    }

    hshift += user_hshift * dev.pixels_per_inch;
    vshift += user_vshift * dev.pixels_per_inch / dev.aspect_ratio;

/* plot window parameters defaulted */
/* to maximum size */

    devtovpw (dev.xmin, dev.ymin, dev.xmax, dev.ymax,
	      &xWmin, &yWmin, &xWmax, &yWmax);

    if (user_xwmax_flag)
	xWmax = ROUND (user_xwmax * RPERIN);
    if (user_ywmax_flag)
	yWmax = ROUND (user_ywmax * RPERIN);
    if (user_xwmin_flag)
	xWmin = ROUND (user_xwmin * RPERIN);
    if (user_ywmin_flag)
	yWmin = ROUND (user_ywmin * RPERIN);

    vptodevw (xWmin, yWmin, xWmax, yWmax, &xWmin, &yWmin, &xWmax, &yWmax);

    wlimit (dev.xmin, dev.xmax, &xWmin, &xWmax);
    wlimit (dev.ymin, dev.ymax, &yWmin, &yWmax);

    xwmax = xWmax;		/* plot window parameters defaulted */
    xwmin = xWmin;		/* to maximum size 		 */
    ywmax = yWmax;
    ywmin = yWmin;
    reset_windows ();
}

void wlimit (int min, int max, int *xmin, int *xmax)
/*< wlimit >*/
{
    if (*xmin < min)
	*xmin = min;

    if (*xmax > max)
	*xmax = max;
}
