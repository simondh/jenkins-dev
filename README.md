# PythonProj

A minimal Tornado web server for debeloping my Jenkins pipeline skills.

Uses Python 3.7 in a virtual env at ~/.virtualenvs/PythonProj/bin/  
Use with:
`source  ~/.virtualenvs/PythonProj/bin/activate`  
(shellscript go.sh does this)  

The Tornado webserver listens on localhost:8888, try:  
`curl localhost:8888`  
Should return something like:  
`{"hostname": "simons-MBP-2.connect", "uid": 501}`

## Tests
`pytest main_test.py`  
Only one simple test

## Git Hub
`https://github.com/simondh/jenkins-dev`

### SSH Key
~/.ssh/id_rsa (.pub)



