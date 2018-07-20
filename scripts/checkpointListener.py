#!/usr/bin/env python
# adapted from the code provided by ROS tutorials
# this program listens for checkpoints given in a nominal petri net plan and publishes it to a parameter
import rospy
from std_msgs.msg import String

def callback(data):
    if (data.data[:17] == "LABEL_CHECKPOINT_"):
        checkpoint = data.data[17:-1]
        pub.publish(checkpoint)
        rospy.set_param('/diago_0/pnp/checkpoint', checkpoint)
        rospy.loginfo("New checkpoint: " + checkpoint)
    else:
        if (rospy.get_param('/diago_0/pnp/PNPCurrentPlan') not in ('interrupt', 'stop')) and (data.data != "abort"):
            if (len(data.data) > 5 and data.data[-6:] == ".exec;"): # if it ends like that it's an action, if not it's the last place
                rospy.set_param('/diago_0/pnp/currentTask', data.data[0:-6])
            else:
                rospy.set_param('/diago_0/pnp/currentPlace',data.data)
            

def listener():
    rospy.Subscriber("/diago_0/pnp/currentActivePlaces", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('checkpointListener', anonymous=True)
    rospy.set_param('/diago_0/pnp/checkpoint', "STARTER CHECKPOINT")
    rospy.set_param('/diago_0/pnp/currentTask', "STARTER ACTION")
    rospy.set_param('/diago_0/pnp/currentPlace', "STARTER PLACE")
    pub = rospy.Publisher('/diago_0/pnp/checkpointString', String, queue_size=10)
    print ("Listening to the PNP...")
    listener()
    
