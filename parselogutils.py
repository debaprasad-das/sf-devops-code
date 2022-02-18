import traceback
import validations
import constants
from collections import defaultdict


class ParseLogUtils:
    def __init__(self):
        pass

    def collect_requests_per_day(self, logfile):
        """Method to collect requests per day from a webserver log file
        :param logfile : Type String : log file to be parsed
        :return: None
        """

        try:
            occurrences = defaultdict(lambda: defaultdict(int))
            requests = constants.REQUESTS

            with open(logfile, 'r') as f:
                for line in f:
                    date = line.split()[3].strip("[").split(":")[0]
                    # validating date as some junk date entry is there
                    if validations.validate_date(date):
                        for request in requests:
                            if request in line:
                                occurrences[date][request] += 1

            # deep copy to remove defaultdict type from dictionary
            occurrences = {k: dict(v) for k, v in occurrences.items()}

            for date in occurrences:
                print(date + " - has these requests counts", occurrences[date])

        except Exception:
            print(traceback.format_exc())

    def collect_useragent_per_day(self, logfile):
        """Method to collect 3 most frequent User Agents by day from a webserver log file
        :param logfile : Type String : log file to be parsed
        :return: None
        """
        try:
            occurrences = defaultdict(lambda: defaultdict(int))
            with open(logfile, 'r') as f:
                for line in f:
                    user_agent = line.strip().split('"')[-2].split()[0].strip(";")
                    date = line.split()[3].strip("[").split(":")[0]
                    # validating date as some junk date entry is there
                    if validations.validate_date(date):
                        if user_agent in occurrences[date]:
                            occurrences[date][user_agent] += 1
                        else:
                            occurrences[date][user_agent] = 0

            # deep copy to remove defaultdict type from dictionary
            occurrences = {k: dict(v) for k, v in occurrences.items()}

            for date in occurrences:
                res = dict(sorted(occurrences[date].items(), key=lambda item: item[1], reverse=True))
                if len(res) > 3:
                    print(date + " - has most requests from following user agents (top 3) - ", list(res.items())[:3])

        except Exception:
            print(traceback.format_exc())

    def collect_get_vs_post_per_os_per_day(self, logfile):
        """Method to collect the ratio of GET's to POST's by OS by day from a webserver log
        :param logfile : Type String : log file to be parsed
        :return: None
        """
        try:
            occurrences = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
            oss = constants.OPERATING_SYSTEMS
            requests = constants.REQUESTS_V2
            with open(logfile, 'r') as f:
                for line in f:
                    date = line.split()[3].strip("[").split(":")[0]
                    # validating date as some junk date entry is there
                    if validations.validate_date(date):
                        for os in oss:
                            if os in line:
                                for req in requests:
                                    if req in line:
                                        occurrences[date][os][req] += 1

            # deep copy to remove defaultdict type from dictionary
            occurrences = {k: dict(v) for k, v in occurrences.items()}

            for date in occurrences:
                for os in occurrences[date]:
                    res = []
                    for req in occurrences[date][os]:
                        res.append((req, occurrences[date][os][req]))
                    print(date + " - has GET vs POST requests by operating system type" + " " + os, res)

        except Exception:
            print(traceback.format_exc())
