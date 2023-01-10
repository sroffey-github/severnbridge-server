
# Severn Bridge Status Script

This is a simple script that scrapes **nationalhighways** official website and gets the status of the severn bridge.

## Environment Variables

The script uses an IFTTT webhook to alert to send a notification to the users phone. You will need to setup your own applet and get the token for the webhook, then store it in a `.env` file.

```
TOKEN=<your token>
```

## Setup

I reccomend you set this script up as a cronjob, you will need python installed and you will also need to know the location of your python3 installation. To do so copy the output of the followinf command

```
which python3
```

Then create a file called `cronjob.sh` and add the following

```
cd <your path>/severnbridge-server
/usr/bin/python3 <your path>/severnbridge-server/app.py
```

*Make sure you make the file executable*

```
chmod +x cronjob.sh
```