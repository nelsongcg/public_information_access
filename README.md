# Access to public information

This project provides two results, 

1) An alternative taxonomy to the one officially provided by government agencies. Not only that, but a novel approach that can respond to the changes over time and is bottom up.

2) An API that can be deployed on a website and help users to evaluate immediately the odds of their requests being granted or denied.

## Tech stack

This project was deployed in the cloud using AWS infrascture, namely Sagemaker, S3 and lambda. Most of the code is based on Python 3.6. The specific libraries used can be found in the requirements.txt file. Notable mentions are Bertopic (for creating the taxonomy) and sagemaker (to make the deployment)

## Set up

To replicate the results shown in this project simply follow the notebooks 'Topic discovery' and 'setup'.