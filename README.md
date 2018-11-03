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

# Data Model
##Sketches
| Field Name       | Type     |
|..................|..........|
| SketchID         | GUID     |
| TwitterID        | INT      |
| FavCount         | INT      |
| RetweetCount     | INT      |
| InstructionSetID | GUID     |
| FileName         | NVARCHAR |
| CreatedDate      | DateTime |

##InstructionSets
| Field Name       | Type     |
|..................|..........|
| InstructionSetID | GUID     |
| Lines            | INT      |
| Arcs             | INT      |

# References
## Pi Coding
- https://projects.raspberrypi.org/en/projects/tweeting-babbage/
- https://projects.raspberrypi.org/en/projects/documenting-your-code/
## Twitter Analytics
- https://blog.bufferapp.com/twitter-analytics
- https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
- https://github.com/bonzanini/Book-SocialMediaMiningPython
## Data Management
- https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/5
- http://raspberrywebserver.com/sql-databases/using-mysql-on-a-raspberry-pi.html