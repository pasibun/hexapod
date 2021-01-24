class HexapodLeg(object):
    name = None
    coxa = None
    femur = None
    tibia = None
    max_front_position = []
    max_back_position = []
    max_left_position = []
    max_right_position = []
    rest_position = []

    def __init__(self, name, coxa, femur, tibia, front, back, left, right, rest):
        self.name = name
        self.coxa = coxa
        self.femur = femur
        self.tibia = tibia
        self.max_front_position = front
        self.max_back_position = back
        self.max_left_position = left
        self.max_right_position = right
        self.rest_position = rest
