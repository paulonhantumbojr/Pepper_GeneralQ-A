# Overview

This Choregraphe (v2.5) project makes use of HTML/Javascript to implement the workflow of a quiz on the Pepper robot, as part of the HRI experiment whereby compliance in humans is being [tested](https://supervisorconnect.med.monash.edu/projects/do-social-robots-have-social-influence-exploration-conformity-compliance-and-persuasion). 

During interaction, Pepper will introduce how the [quiz](https://docs.google.com/document/d/1CSvxYsGtnIFGXu-Lr4lSYEnaO_VANeMz/edit?usp=sharing&ouid=100288249884668367427&rtpof=true&sd=true) is structured and guide the user as they progress through each question. Question categories vary but are mainly based on Australian culture and topics. The responses from the user are recorded and saved to calculate a score at the end. Extra exit questions are asked after the user has completed the quiz to inquire about their experience while approaching the same.

To install this package on a Pepper robot, open the [Quiz_1.pml](Quiz_1.pml) file in Choregraphe. Then use the upload to robot feature to send the package to the robot. This will add a launcher entry on the tablet of the robot which when selected will start the behavior.

This project was developed based on the [Pepper Tablet Survey tool](https://github.com/tianleimin/RobotCakeBarWaiterPepper).
