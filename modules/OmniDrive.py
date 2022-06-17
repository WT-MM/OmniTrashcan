class OmniDrive:
    
    def __init__(self):
        pass
    
    def setMotors(self, motors):
        self.motor1, self.motor2, self.motor3 = motors
        return self
    
    def setWheelSize(self, size):
        self.wheelSize = size
        return self
    
    def setWheelDist(self, dist):
        self.dist = dist
        return self
    
    """
    Normalized to -1 to 1
    Rotation in degrees
    """
    def drive(self, translation, rotation):
        rotMatrix = [[-0.33, 0.58, 0.33], [-0.33, -0.58, 0.33], [0.67, 0, 0.33]]
        combined = translation.copy().append(rotation/360)
        wheelSpeeds = rotMatrix * combined
        self.motor1.set(wheelSpeeds[0])
        self.motor2.set(wheelSpeeds[1])
        self.motor3.set(wheelSpeeds[2])
        
    
    '''
    [x,y,w] = [cos(a1 + pi/2) cos(a2 + pi/2) cos(a3 + pi/2)
                sin(a1 + pi/2 sin(a1+pi/2) + sin(a1+pi/2))]
                * [s1,s2,s3]

    https://pdfs.semanticscholar.org/ed22/2105a1e4c42d64c207bcc55dec5aacd70275.pdf
    
    
    
    '''