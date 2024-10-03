def bezier_algo(p_0 : Point, p_1 : Point, p_2 : Point, p_3 : Point, canv : tk.Canvas, H_ecran, window : Rectangle, viewport :Rectangle):
    """On trace une courbe de Bezier avec 4 points de contrôles avec le procédé algorithmique."""

    # On projete les points
    p0 = projection(window, viewport, p_0)
    p1 = projection(window, viewport, p_1)
    p2 = projection(window, viewport, p_2)
    p3 = projection(window, viewport, p_3)
    allume_pixel(canv, p0, H_ecran)
    allume_pixel(canv, p1, H_ecran)
    allume_pixel(canv, p2, H_ecran)
    allume_pixel(canv, p3, H_ecran)


    u = 0
    while u <= 1:

        # Calcul des trois premiers barycentres
        B1 = Point((1-u) * p0.x + u * p1.x, (1-u) * p0.y + u * p1.y)
        B2 = Point((1-u) * p1.x + u * p2.x, (1-u) * p1.y + u * p2.y)
        B3 = Point((1-u) * p2.x + u * p3.x, (1-u) * p2.y + u * p3.y)

        # Calcul des deux nouveaux barycentres avec les trois construits
        B4 = Point((1-u) * B1.x + u * B2.x, (1-u) * B1.y + u * B2.y)
        B5 = Point((1-u) * B2.x + u * B3.x, (1-u) * B2.y + u * B3.y)
        
        # Calcul du dernier barycentre qui sera le point affiché
        B6 = Point((1-u) * B4.x + u * B5.x, (1-u) * B4.y + u * B5.y)
        allume_pixel(canv, B6, H_ecran)

        u += 0.01



#def bezier_bern()
