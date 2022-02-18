import argparse
import sys
from parselogutils import ParseLogUtils
import validations

# Entry point to the tool
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Command line tool for log parsing')
    parser.add_argument('--logfile', action='store', dest='logfile',
                        help='log file to be parsed',
                        required=True)
    parser.add_argument('--findbyrequests', action='store_true', dest='findrequests',
                        help='number of requests served by day',
                        required=False)
    parser.add_argument('--findbyuseragent', action='store_true', dest='finduseragent',
                        help='3 most frequent User Agents by day',
                        required=False)
    parser.add_argument('--findbyos', action='store_true', dest='findos', help='ratio of GET\'s to POST\'s by OS by day',
                        required=False)

    args = parser.parse_args()

    if not validations.is_valid_path(args.logfile):
        print("Please provide a valid path for log file")
        sys.exit(-1)

    if not validations.is_valid_file(args.logfile):
        print("Please provide a valid log file")
        sys.exit(-1)

    if not args.findrequests and not args.finduseragent and not args.findos:
        print("Please provide at least one parsing option")
        sys.exit(-1)

    if (args.findrequests and args.finduseragent and args.findos) or (args.findrequests and args.finduseragent) \
            or (args.findrequests and args.findos) or (args.finduseragent and args.findos):
        print("Please provide one parsing option at a time ")
        sys.exit(-1)

    logfile = args.logfile
    find_requests = args.findrequests
    find_useragent = args.finduseragent
    find_os = args.findos

    plog = ParseLogUtils()

    if find_requests:
        plog.collect_requests_per_day(logfile)
        sys.exit(0)

    if find_useragent:
        plog.collect_useragent_per_day(logfile)
        sys.exit(0)

    if find_os:
        plog.collect_get_vs_post_per_os_per_day(logfile)
        sys.exit(0)
