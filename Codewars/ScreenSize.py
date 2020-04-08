def find_screen_height(width, ratio): 
    screen_ratio = ratio.split(':')
    
    screen_height = width / (screen_ratio[0] / screen_ratio[-1])
    
    return "{}x{}".format(str(width), screen_height)

print(find_screen_height(1024, "4:3"))