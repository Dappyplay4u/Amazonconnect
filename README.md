# Spring-connect

Assignment: Creating a Call Center Application using Amazon Connect with 2 key features
using CloudFormation.
Introduction:
In this hands-on exercise, your task is to develop a call center application by seamlessly 
integrating two features into an Amazon Connect instance using a single CloudFormation stack. 
1. Playback Position in Queue for voice callers.
2. Post-Contact Survey for the voice callers.
Please check the reference section for two AWS blog posts that can be used as a starting point.
Pre-Requisite:
• Ensure you can access the AWS account with the provided username and password.
• Ensure all resources you create/deploy is in the US EAST (us-east-1).
Requirements:
Your primary objective is to create a call center application using CloudFormation, seamlessly 
integrating the following features:
1. Amazon Connect Instance Creation:
Utilize CloudFormation to create an Amazon Connect instance, configured with essential 
settings for inbound calls.
2. Playback Position in Queue for Voice Callers:
Implement a dynamic contact flow in Amazon Connect that plays the position in the queue for 
callers.
*Consider using connect blocks such as Play Prompt. Caller will hear the position in queue 
and remain in queue until the call is answered by the next available agent.
3. Enable Post-Call Survey for Voice Callers:
Establish a mechanism for collecting customer satisfaction scores through post-contact surveys
that can be later used for analysis.
*Caller should be offered a post call survey using amazon disconnect flow, survey should
include minimum 3 questions. The caller input range should be between 1 – 5.
4. CloudFormation Template:
A comprehensive CloudFormation template written in YAML or JSON. Clearly documented 
parameters, thorough comments explaining the purpose of each resource and configuration.
Upload your assignment by packaging the CloudFormation template to GitHub and share the 
link (make sure its public and accessible).
