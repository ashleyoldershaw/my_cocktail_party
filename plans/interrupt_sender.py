#!/usr/bin/env python
# license removed for brevity

# this file exists to send messages to trigger the learning procedure
# it can be attached to a button or something to have a better interface
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('interrupt_listener', String, queue_size=10)
    rospy.init_node('interrupt_sender', anonymous=True)

    hello_str = "hello world %s" % rospy.get_time()
    rospy.loginfo(hello_str)
    pub.publish(hello_str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
