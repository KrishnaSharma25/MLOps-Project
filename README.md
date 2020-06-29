# Tweak of mlops model of cnn by using transfer learning and integrate with the DevOps automation

- Knowlege of tools Required
- Dockerfile for creating cnn image
- Jenkins
- GitHub
Implementation -
1. Create container image that has Python3 and Keras or numpy installed using Dockerfile.

Build dockerfile - # docker build -t <name of image>:version <path of dockerfile>
  2. When we launch this image, it should automatically starts Train the model in the container.

Launch the container from the mlops image
Run the cnn.py file that is uploaded on the github
3. Create a job chain of Job1, Job2, Job3, & Job4 using build pipeline plugin in Jenkins .

## Job1 : Pull the GitHub repository automatically when some developers push repository to GitHub.

## Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the software required for the CNN processing).

## Job3 : Train your model and predict accuracy or metrics. if metrics accuracy is less than 90% , then Tweak the machine learning model architecture , Retrain the model and notify the developer that the best model is being created successfully.

## Job4 : If container where app is running, fails due to any reason then this job should automatically start the container again from where the last trained model left.
