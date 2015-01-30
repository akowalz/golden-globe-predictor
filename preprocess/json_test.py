import sys
import json

def write_tweets(source_path, out_path, attr):
    written = 0
    with open(source_path, 'r') as json_file:
        outfile = open(out_path, 'w')
        for line in json_file:
            content = json.loads(line)[attr]
            outfile.write(content.encode('utf-8') + "\n".encode('utf-8'))
            written += 1
            if written % 1000 == 0:
                print "Wrote %d tweets" % written

write_tweets("../goldenglobes2015.json", sys.argv[1], "text")
