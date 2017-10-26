import bisect 
from random import randint
from math import sin, pi

class Interpolate(object):
    def __init__(self, x_list, y_list):
        if any([y - x <= 0 for x, y in zip(x_list, x_list[1:])]):
            raise ValueError("x_list must be in strictly ascending order!")
        x_list = self.x_list = map(float, x_list)
        y_list = self.y_list = map(float, y_list)
        intervals = zip(x_list, x_list[1:], y_list, y_list[1:])
        self.slopes = [(y2 - y1)/(x2 - x1) for x1, x2, y1, y2 in intervals]
        
    def __getitem__(self, x):
        i = bisect.bisect_left(self.x_list, x) - 1
        return self.y_list[i] + self.slopes[i] * (x - self.x_list[i])

    def diff(self,x):
        n = self[i + 1]
        return int(n) - int(self[i])

def human_like_hover(dest):

    MOVE_MOUSE_DELAY = 0.7
    FPS = 30.0
    FRAME_COUNT = int(FPS * MOVE_MOUSE_DELAY)
    MAX_RAND_OFFSET = 5
    
    
    Settings.MoveMouseDelay = 0
    start = Env.getMouseLocation()
    x_interpolator = Interpolate([0, FRAME_COUNT], [start.x,dest.x])
    y_interpolator = Interpolate([0, FRAME_COUNT], [start.y,dest.y])
    
    curr = start
    curr_linear = start
    
    for i in range(0,FRAME_COUNT):
        random_multiplyer = sin(i/float(FRAME_COUNT) * pi)
        x_random_modifyer = int(float(randint(- MAX_RAND_OFFSET,MAX_RAND_OFFSET)) * random_multiplyer)
        y_random_modifyer = int(float(randint(- MAX_RAND_OFFSET,MAX_RAND_OFFSET)) * random_multiplyer)
        #print x_random_modifyer
        print i/float(FRAME_COUNT) * pi
    
        lin_offsets = (x_interpolator.diff(i),y_interpolator.diff(i))
        
        rand_offsets = ( lin_offsets[0] + x_random_modifyer, lin_offsets[1] + y_random_modifyer )
    
        
        offsets = (
                rand_offsets[0] - (curr.x - curr_linear.x),
                rand_offsets[1] - (curr.y - curr_linear.y)
                )
        
        curr.x += offsets[0]
        curr.y += offsets[1]
    
        curr_linear.x += lin_offsets[0]
        curr_linear.y += lin_offsets[1]
        
    
        mouseMove(
                offsets[0],
                offsets[1]
                )
        sleep(1/FPS)
    
    Settings.MoveMouseDelay = MOVE_MOUSE_DELAY * 0.3
    hover(dest)
    
    Settings.MoveMouseDelay = MOVE_MOUSE_DELAY

#test
#human_like_hover(Location(500,500))
