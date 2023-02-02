# Overview

This Choregraphe (v2.5) project makes use of HTML/Javascript to implement the workflow of a quiz on the Pepper robot as part of the HRI experiment wherein compliance in humans is being [tested](https://supervisorconnect.med.monash.edu/projects/do-social-robots-have-social-influence-exploration-conformity-compliance-and-persuasion). 

During the interaction, Pepper will introduce how the quiz is structured and guide the user as they progress through each question. Question categories vary but are mainly based on various topics. The responses from the user are recorded and saved to calculate a score at the end. Additional exit questions are asked after the user has completed the quiz to inquire about their experience.

To install this package on a Pepper robot, open the [Pepper_trialQuiz.pml](https://github.com/paulonhantumbojr/Pepper_GeneralQ-A/blob/main/Pepper_trialQuiz.pml) file in Choregraphe. Then use the upload to robot feature to send the package to the robot. This will add a launcher entry on the robot's tablet, which will start the behaviour when selected.

This project was developed based on the [Pepper Tablet Survey tool](https://github.com/tianleimin/RobotCakeBarWaiterPepper), and part of the workflow was forked from a [health_survey](https://bitbucket.org/pepper_qut/health_assessment/src/master/) and a [problem_solver_app](https://bitbucket.org/pepper_qut/problem_solver_app/src/master/) bitbucket repo.
