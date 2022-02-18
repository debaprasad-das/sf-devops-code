import subprocess


subprocess.call(["python", "parselog.py", "--logfile", "resources/sample.log", "--findbyrequests"])

subprocess.call(["python", "parselog.py", "--logfile", "resources/sample.log", "--findbyuseragent"])

subprocess.call(["python", "parselog.py", "--logfile", "resources/sample.log", "--findbyos"])