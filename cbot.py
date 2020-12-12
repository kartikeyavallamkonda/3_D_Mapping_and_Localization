#!/usr/bin/env python

import rospy
from rospy.exceptions import ROSInterruptException
from geometry_msgs.msg import Twist


PI = 3.141592653589793238

def circle_bot():
    linear_velocity = float(input("Speed "))
    radius = float(input("Radius "))
    angular_velocity = linear_velocity / radius
    frequency = 10
    rospy.init_node("node_circle_publisher")
    publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
    message = Twist()
    message.linear.x = linear_velocity
    message.angular.z = angular_velocity
    rate = rospy.Rate(frequency)
    distance_travelled = 0
    target_distance = 2 * PI * radius
    while not rospy.is_shutdown() and distance_travelled < target_distance:
        publisher.publish(message)
        distance_travelled = distance_travelled + linear_velocity / frequency
        rate.sleep()
    message.linear.x = 0
    message.angular.z = 0
    publisher.publish(message)

if __name__ == "__main__":
    try: circle_bot()
    except ROSInterruptException: pass
