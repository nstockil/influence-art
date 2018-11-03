# Influence Art 

The code behind the journey of an artist.

## TODO
- Arm interactions (motors.py)
    - reset position of arm
    - basic shapes movements (circle, square, triangle, line, curve)
    - hitting clear button
    - pen lift/drop
- Twitter interactions (twitter.py)
    - tweet photo and return post unique id
    - retrieve data on tweet performance
- Photo interactions (photo.py)
    - taking a photo
    - applying appropriate filter for getting distinctive image
- Data interface
    - add popularity data to source
    - retrieve instructions for new art (algorithm based on current popularity data)

# Environment Set Up
Assumed running on Raspbian OS

## Configure Virtual Env Set Up
### Create Environment
virtualenv /home/pyenvs/influence

### Start Environment
source /home/pyenvs/influence/bin/activate

### Configure
Update pip in th env
    pip install --upgrade pip

Once Activated you can use pip install to set up the required modules/things
    gpiozero
    picamera
    tweepy

### Stopping the environment
Finish up: deactivate.bat


# References
https://projects.raspberrypi.org/en/projects/tweeting-babbage/