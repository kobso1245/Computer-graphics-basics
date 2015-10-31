from glfw import init, poll_events, make_context_current,window_should_close, create_window, swap_buffers, terminate
from OpenGL.GL import *
from OpenGL.GLU import *
def draw_cube(centre_x, centre_y, centre_z, length, colors):
    #front wall
    glBegin(GL_POLYGON)
    glNormal(0,0,1)
    glColor(colors.get('front')[0],
            colors.get('front')[1],
            colors.get('front')[2])
    glVertex(centre_x - length,
             centre_y + length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y + length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y - length,
             centre_z + length)
    glVertex(centre_x - length,
             centre_y - length,
             centre_z + length)
    glEnd()

    #back wall
    glBegin(GL_POLYGON)
    glNormal(0,0,-1)
    glColor(colors.get('back')[0],
            colors.get('back')[1],
            colors.get('back')[2])
    glVertex(centre_x - length,
             centre_y + length,
             centre_z - length)
    glVertex(centre_x + length,
             centre_y + length,
             centre_z - length)
    glVertex(centre_x + length,
             centre_y - length,
             centre_z - length)
    glVertex(centre_x - length,
             centre_y - length,
             centre_z - length)
    glEnd()

    #upper wall
    glBegin(GL_POLYGON)
    glColor(colors.get('up')[0],
            colors.get('up')[1],
            colors.get('up')[2])
    glVertex(centre_x - length,
             centre_y + length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y + length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y + length,
             centre_z - length)
    glVertex(centre_x - length,
             centre_y + length,
             centre_z - length)
    glEnd()

    #lower wall
    glBegin(GL_POLYGON)
    glColor(colors.get('down')[0],
            colors.get('down')[1],
            colors.get('down')[2])
    glVertex(centre_x - length,
             centre_y - length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y - length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y - length,
             centre_z - length)
    glVertex(centre_x - length,
             centre_y - length,
             centre_z - length)
    glEnd()


    #left wall
    glBegin(GL_POLYGON)
    glNormal(-1,0,0)
    glColor(colors.get('left')[0],
            colors.get('left')[1],
            colors.get('left')[2])
    glVertex(centre_x - length,
             centre_y + length,
             centre_z + length)
    glVertex(centre_x - length,
             centre_y - length,
             centre_z + length)
    glVertex(centre_x - length,
             centre_y - length,
             centre_z - length)
    glVertex(centre_x - length,
             centre_y + length,
             centre_z - length)
    glEnd()

    #right wall
    glBegin(GL_POLYGON)
    glNormal(1,0,0)
    glColor(colors.get('right')[0],
            colors.get('right')[1],
            colors.get('right')[2])
    glVertex(centre_x + length,
             centre_y + length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y - length,
             centre_z + length)
    glVertex(centre_x + length,
             centre_y - length,
             centre_z - length)
    glVertex(centre_x + length,
             centre_y + length,
             centre_z - length)
    glEnd()

def initial_setup():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65,1,1,100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,50,
              0,0,0,
              0,1,0)

def set_lightning():
    glEnable(GL_NORMALIZE)
    glLight(GL_LIGHT0, GL_POSITION, [1,1,2,0])
    #glEnable(GL_LIGHTNING)
    glEnable(GL_LIGHT0)

def main():
    init()

    window = create_window(500,500,"Hi",None,None)
    make_context_current(window)
    initial_setup()
    colors= {
            'front':(1,0,0),
            'back': (0,1,0),
            'left': (1,1,0),
            'right': (1,0,1),
            'up': (0,0,1),
            'down': (0,1,1)
            }
    glClearColor(1,1,1,1)
    glEnable(GL_DEPTH_TEST)
    set_lightning()
    while not window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotate(1,0,1,0)
        draw_cube(0,0,0,5,colors)
        swap_buffers(window)
        poll_events()

    terminate()

main()

