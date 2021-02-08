def picmaker():
    file = open("image.ppm", "w")
    file.write("P3 500 500 255\n")
    for y in range(500):
        for x in range(500):
            if not (x - 250) ** 2 + (y - 50) ** 2 > 50 ** 2:  # the sun
                r = 252
                g = 212
                b = 64
            elif y <= 250:  # blue sky
                r = 55
                g = 134 + y // 3
                b = 235
            elif y <= 375:  # ocean
                new_y = y - 250
                r = 0
                g = 54 + new_y // 2
                b = 190
            else:  # sand
                new_y = y - 375
                r = 225 - new_y // 4
                g = 178
                b = 128
            file.write(str(r) + " " + str(g) + " " + str(b) + " ")
        file.write("\n")
    file.close


picmaker()
