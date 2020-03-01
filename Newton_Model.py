import math

#declare system properties
g = 9.81 #m/s^2

moment_arm = .13 #m
hit_height = .19 #m
cup_height = .09 #m

theta_deg = 45 #launch angle in degrees
theta = math.radians(45) #launch angle in radians

deltaY = cup_height - hit_height

#define functions
def calc_ang_speed(vel):
    ang_speed = math.degrees(vel/(moment_arm))
    print("angspeed "+str(ang_speed))
    return ang_speed

def calc_launch_vel(deltaX):
    t = math.sqrt(2*(deltaX*math.tan(theta)-deltaY)/g)
    launch_vel = deltaX/(t*math.cos(theta))
    print("launchvel "+str(launch_vel))
    return launch_vel

def newton_hit_the_ball(hitter,deltaX):
    #calculate speed
    launch_vel = calc_launch_vel(deltaX)
    ang_speed = calc_ang_speed(launch_vel)

    #run
    hitter.run_angle(int(ang_speed),360*2)
