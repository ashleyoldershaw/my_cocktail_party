#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import os

# this program simply listens for a ros message
# then triggers the recovery procedure when appropriate

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    os.system("./runplan.sh diago_0 recover")

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('interrupt_listener', anonymous=True)

    rospy.Subscriber("interrupt_listener", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
