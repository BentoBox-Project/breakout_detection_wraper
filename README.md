# breakout_detection_wraper
Twitter's R breakout detection package wraper for python on a docker.  
For more information on the Breakout detection package you can check [this article explaining it.](https://blog.twitter.com/engineering/en_us/a/2014/breakout-detection-in-the-wild.html)

Make sure to have installed docker on your environment, if you need more information go to [DOCKER DOCUMENTATION](https://docs.docker.com/get-started/).  
This script also uses Pipenv for it's python virtual environment and dependencies, for more information on how to use this go to [the pipenv documentation](https://pipenv-fork.readthedocs.io/en/latest/).

To run this script you need clone this repo and then build and run the docker container as following:

Based on the Docker build and run [Documentation](https://docs.docker.com/get-started/part2/):

Build the app
Make sure you are in the repository top. Here’s what `ls` should show:

```
$ ls  
Dockerfile                README.md  
Pipfile                   breakout_detection_wraper  
Pipfile.lock              install_packages.R  
```

Now run the build command. This creates a Docker image, which we’re going to name using the --tag option. Use -t if you want to use the shorter option.

`$ docker build --tag=boutdetect . `

(NOTICE THAT THERE IS A DOT AT THE END OF THIS COMMAND)

Where is your built image? 
It’s in your machine’s local Docker image registry
To show it run the following command:

`$ docker image ls`

|   REPOSITORY  |     TAG     |   IMAGE ID    |      CREATED      | 
|---------------|-------------|---------------|--------------------
|  boutdetect   |   lastest   |  326387cea398 |   23 seconds ago  |

Now to run the image you need to run the command:
` $ docker run boutdetect `

That's it!
Now you should get a result like the following:

```
$loc  
[1]  31  88 750  
  
$time  
[1] 1.406  
  
$pval  
[1] NA  
```
