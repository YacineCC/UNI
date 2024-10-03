#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
# from Image import open
from PIL import Image

###############################################################
# variables globales
year, day = 0, 0  # Terre
luna, periode = 0, 0  # Lune
quadric = None
SOLEIL, TERRE, ATERRE, LUNE = 1, 2, 3, 4  # ID astre, planete, satellite
texture_planete = [None for i in range(5)]
# variables globales importantes en programmation evenementiel car c'est l'utilisateur
# qui a le controle, en temps normal on évite les variables globales pour éviter les
# effets de bord.
year, day = 0, 0
axe_x, axe_y, axe_z = 0, 0, 0
quadric = None
# Couleurs RVBA
red = (1.0, 0.0, 1.0, 0.0)
yellow = (1.0, 1.0, 0.0, 0.0)
blue = (0.0, 0.0, 1.0, 0.0)
white = (1.0, 1.0, 1.0, 0.0)

X,Y,Z,angv,angh = 0,0,0,0,0

###############################################################
# chargement des textures

def LoadTexture(filename, ident):
    global texture_planete
    image = Image.open(filename)  # retourne une PIL.image
    
    ix = image.size[0]
    iy = image.size[1]
    # image = image.tostring("raw", "RGBX", 0, -1)
    image = image.tobytes("raw", "RGBX", 0, -1)
    
    # 2d texture (x and y size)
    # BUG (?)
    #glBindTexture(GL_TEXTURE_2D, glGenTextures(1, texture_planete[ident]))
    texture_planete[ident] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, int(texture_planete[ident]))

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    # commente car alpha blinding (cf. atmosphere)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

###############################################################
# creation des composants du systeme

def CreerPlanete(rayon):
    # Tuples RVG pour les différents types de lumière 
    ambient = (0.1, 0.1, 0.1, 1.0)
    diffuse = (0.8, 0.8, 0.8, 1.0)
    Black = (0.0, 0.0, 0.0, 1.0)
    sph1 = gluNewQuadric()

    
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Black)
    glMaterialfv(GL_FRONT, GL_EMISSION, ambient)
    glMaterialf(GL_FRONT, GL_SHININESS, 0.0)

    gluQuadricDrawStyle(sph1, GLU_FILL)
    gluQuadricNormals(sph1, GLU_SMOOTH)
    gluQuadricTexture(sph1, GL_TRUE)
    gluSphere(sph1, rayon, 100, 80)



def CreerSoleil(rayon):

    sph1 = gluNewQuadric()


    glMaterialfv(GL_FRONT, GL_EMISSION, yellow)
    glMaterialf(GL_FRONT, GL_SHININESS, 0.0)

    gluQuadricDrawStyle(sph1, GLU_FILL)
    gluQuadricNormals(sph1, GLU_SMOOTH)
    gluQuadricTexture(sph1, GL_TRUE)
    gluSphere(sph1, rayon, 100, 80)

###############################################################
# affichage

def display_sun():
    
    glBindTexture(GL_TEXTURE_2D, SOLEIL)
    CreerSoleil(0.7)
    

def display_earth():
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(2.0, 0.0, 0.0)
    glRotatef(day, 0.0, 1.0, 0.0)

    glBindTexture(GL_TEXTURE_2D, TERRE)
    CreerPlanete(0.2)

    

def display_atmosphere():
    glMaterialf(GL_FRONT, GL_SHININESS, 0.0)
    glRotatef(year, 0.0, 1.0, 0.0)
    glRotatef(day, 0.0, 1.0, 0.0)
    glBindTexture(GL_TEXTURE_2D, ATERRE)
    glEnable(GL_BLEND)
    glBlendFunc (GL_SRC_ALPHA,GL_ONE)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    


    CreerPlanete(0.25)
    glDisable(GL_BLEND)


def display_moon():
    
    glRotatef(luna, 0.0, 1.0, 0.0)
    glTranslatef(0.5, 0.0, 0.0)
    glRotatef(periode, 0.0, 1.0, 0.0)

    glBindTexture(GL_TEXTURE_2D, LUNE)
    CreerPlanete(0.1)
    

###############################################################
# 

def init_texture():
    # Parcourir les deux en parrallele et load texture de chaque couples (fichier,id)
    planets = [SOLEIL, TERRE, ATERRE, LUNE]
    textures = ["sun.bmp", "earth.bmp", "earthcld.bmp","moon.bmp"]
    for p,t in zip(planets, textures):
        LoadTexture(t, p)
    


def init():
    global quadric
    glClearColor (0.0, 0.0, 0.0, 0.0) # Couleur du fond, noir ici
    glShadeModel (GL_SMOOTH)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    glEnable(GL_DEPTH_TEST) # Active la profondeur
    glEnable(GL_LIGHTING) # Active l'eclairage, ne pas oublier le LIGHTi après 
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_DITHER)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    light()
    init_texture()

def light():
    red, blue, white, yellow
    diffuse = (0.7, 0.7, 0.7, 1.0)
    specular = (0.001, 0.001, 0.001, 1.0)
    pos = (0, 0, 0.5, 1)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, yellow)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 9.0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    #glLightfv(GL_LIGHT1, GL_POSITION, (0, 0, -10, 1))

    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    creer_camera()


def display():
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Ne pas oublier le depth buffer
    #glColor4f (1.0, 1.0, 0.0, 1.0) # Que pour la 2D

    light_position = (0.0, 0.0, 2.2, 1.0)

    
    creer_camera()
    #glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glPushMatrix()
    #glTranslate(0, 0, zoom)
    
    gluLookAt(axe_x, axe_y, axe_z, 0, 0, 0, 0, 1, 0)

    display_sun()
    glPushMatrix()
    

    display_earth()
    display_atmosphere()
    glPushMatrix()
    
    display_moon()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

    

    


    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    #glMatrixMode(gluPerspective)

    glLoadIdentity()
    #gluPerspective(20, (width/height), 0.1, 50)
    # if width <= height:
    #     #glOrtho(-2.5, 2.5, -2.5*height/width, 2.5*height/width, -10.0, 10.0)
        
    # else:
    #     #glOrtho(-2.5*width/height, 2.5*width/height, -2.5, 2.5, -10.0, 10.0)
    #     gluPerspective(20, 16/9, 50)
    #glMatrixMode(GL_MODELVIEW)
    #glLoadIdentity()
    #gluLookAt(0, 0, -15, 0, 0, 0, 0, 1, 0)

# def keyboard(key, x, y):
#     global day, year, axe_x, axe_y, axe_z
#     key = key.decode('utf-8')

#     if key == 'j':
#         day = (day + 10) % 360
#     elif key == 'J':
#         day = (day - 10) % 360
#     elif key == 'a':
#         year = (year + 5) % 360
#     elif key == 'A':
#         year = (year - 5) % 360
#     elif key == '\033':
#         # sys.exit( )  # Exception ignored
#         glutLeaveMainLoop()
#     elif key == 'z':
#         axe_z -= 0.1
#     elif key == 's':
#         axe_z += 0.1
#     elif key == 'q':
#         axe_x += 0.1
#     elif key == 'd':
#         axe_x -= 0.1
    

def creer_camera():
    glRotatef(angv,0,1.0,0)
    glRotatef(angh,1.0,0,0)
    glTranslatef(X,0,Z)
    glTranslatef(0,0,-5)

def keyboard(key, x, y):
    """fonction pour pouvoir déplacer mes objets"""
    global day, year, sat , X, Z, angv, angh
    key = key.decode('utf-8')
    if key == 'e':
        day = (day + 10) % 360
        year = (year + 5) % 360
        sat = (sat + 28 ) % 360
    elif key == 'a':
        day = (day + 10) % 360
        sat = (sat + 28 ) % 360
    elif key == 'z':
        Z = Z+0.5
    elif key == 'q':
        X = X + 0.5
    elif key == 's':
        Z = Z - 0.5
    elif key == 'd':
        X = X - 0.5
    elif key == 'o':
        angh = (angh - 10) % 360
    elif key == 'k':
        angv = (angv - 10) % 360
    elif key == 'l':
        angh = (angh + 10 ) % 360
    elif key == 'm':
        angv = (angv + 10 ) % 360
    elif key == '\033':
        # sys.exit( )  # Exception ignored
        glutLeaveMainLoop()
    glutPostRedisplay()  # indispensable en Python

    
    glutPostRedisplay()  # indispensable en Python


def idle():
    """ Fonction qui sera appelée quand il n'y a pas d'action d'utilisateur"""
    global day, year, luna, periode
    day = (day + 1) % 360
    year = (year + 1) % 360
    luna = (luna + 1) % 360
    periode = (periode + 1) % 360
    glutPostRedisplay()
###############################################################
# MAIN


glutInit(sys.argv)

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

glutCreateWindow('planet')
glutReshapeWindow(512,512)

# Fonctions d'opengl qui prennent des callbacks
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutIdleFunc(idle)
init()

glutMainLoop()


