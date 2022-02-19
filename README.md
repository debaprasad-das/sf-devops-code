
# Log parsing tool


# parselog tool usage - help 
```commandline
python parselog.py --help
usage: parselog.py [-h] --logfile LOGFILE [--findbyrequests] [--findbyuseragent] [--findbyos]

Command line tool for log parsing

optional arguments:
  -h, --help         show this help message and exit
  --logfile LOGFILE  log file to be parsed
  --findbyrequests   number of requests served by day
  --findbyuseragent  3 most frequent User Agents by day
  --findbyos         ratio of GET's to POST's by OS by day
```

# Get requests count by day

```commandline
python parselog.py --logfile resources/sample.log --findbyrequests
01/Dec/2011 - has these requests counts {'GET': 2555, 'POST': 270, 'PUT': 14}
02/Dec/2011 - has these requests counts {'GET': 2288, 'POST': 282, 'PUT': 13}
03/Dec/2011 - has these requests counts {'GET': 536, 'POST': 66}

```

# Get most frequent User Agents by day (top 3)

```commandline
python parselog.py --logfile resources/sample.log  --findbyuseragent
01/Dec/2011 - has most requests from following user agents (top 3) -  [('Mozilla/5.0', 1603), ('Mozilla/4.0', 569), ('WordPress/3.2.1', 105)]
02/Dec/2011 - has most requests from following user agents (top 3) -  [('Mozilla/5.0', 1408), ('Mozilla/4.0', 540), ('WordPress/3.2.1', 101)]
03/Dec/2011 - has most requests from following user agents (top 3) -  [('Mozilla/5.0', 389), ('Mozilla/4.0', 100), ('WordPress/3.2.1', 22)]
```

# ratio of GET's to POST's by OS by day
```commandline
python parselog.py --logfile resources/sample.log  --findbyos
01/Dec/2011 - has GET vs POST requests by operating system Windows [('GET', 614), ('POST', 161)]
01/Dec/2011 - has GET vs POST requests by operating system Linux [('GET', 123), ('POST', 1)]
01/Dec/2011 - has GET vs POST requests by operating system X11 [('GET', 120), ('POST', 1)]
01/Dec/2011 - has GET vs POST requests by operating system Macintosh [('GET', 94)]
02/Dec/2011 - has GET vs POST requests by operating system Windows [('GET', 559), ('POST', 177)]
02/Dec/2011 - has GET vs POST requests by operating system Linux [('GET', 141), ('POST', 1)]
02/Dec/2011 - has GET vs POST requests by operating system X11 [('GET', 111), ('POST', 1)]
02/Dec/2011 - has GET vs POST requests by operating system Macintosh [('GET', 70)]
03/Dec/2011 - has GET vs POST requests by operating system Windows [('GET', 121), ('POST', 40)]
03/Dec/2011 - has GET vs POST requests by operating system Linux [('GET', 37), ('POST', 1)]
03/Dec/2011 - has GET vs POST requests by operating system X11 [('GET', 24), ('POST', 1)]
03/Dec/2011 - has GET vs POST requests by operating system Macintosh [('GET', 2)]
```


# Negative cases handling

```commandline
python parselog.py --logfile resources/sam --findbyrequests
Please provide a valid path for log file
```

```commandline
python parselog.py --logfile resources
Please provide a valid log file
```

```commandline
python parselog.py --logfile resources/sample.log 
Please provide at least one parsing option
```

```commandline
python parselog.py --logfile resources/sample.log  --findbyrequests --findbyuseragent 
Please provide one parsing option at a time 
```
