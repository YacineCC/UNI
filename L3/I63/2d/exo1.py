#import tkinter as tk, point as poi, rectangle as rec, bresenham as bre, bezier as bez, affichage as aff
import affichage as aff, point as poi
#import numpy as np









if __name__ == "__main__":

    
    #aff.init_window_viewport(poi.Point(0, 0), poi.Point(1000, 1000), poi.Point(100, 100), poi.Point(700, 700))
    test = aff.Environement(poi.Point(0, 0), poi.Point(1000, 1000), poi.Point(100, 100), poi.Point(700, 700))
    print(test.H_ecran)
    

    
    


    """
    p1 = Point(10, 40)
    p2 = Point(100, 150)
    pro_p1 = projection(window, viewport, p1)
    pro_p2 = projection(window, viewport, p2)
    LISTE_POINTS += [p1, p2]
    print(pente(p1, p2))

    bresenham(pro_p1, pro_p2, root_canvas, root.winfo_height())

    test = Point(100, 100)
    print(test)

    pro = projection(window, viewport, test)
    allume_pixel(root_canvas, pro, root.winfo_height())
    print(pro)

    #allume_pixel(root_canvas, test, root.winfo_height())
    LISTE_POINTS += [test]
    

    p0 = Point(0, 0)
    p1 = Point(0, 1000)
    p2 = Point(1000, 1000)
    p3 = Point(1000, 0)

    bezier_algo(p0, p1, p2, p3, root_canvas, root.winfo_height(), window, viewport)


    root.mainloop()
    """
