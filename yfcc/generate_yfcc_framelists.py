"""
    # 'path':"s3://multimedia-commons/data/images/{}/{}/{}.jpg".format(entries[2][:3],entries[2][3:6],entries[2]),
"""
import bz2, json, gzip, sys
from collections import defaultdict


class FramelistGenerator(object):

    def __init__(self,fname):
        self.fname = fname


    def process(self):
        if fname.endswith('.gz'):
            f = gzip.GzipFile(fname)
        elif fname.endswith('.bz2'):
            f = bz2.BZ2File(fname)
        else:
            f = open(self.fname)
        count = 0
        for i, line in enumerate(f):
            if i % 10 == 0:
                count += 1
                if count % 10 ** 5 == 0:
                    print "completed {}".format(count)
                entries = line.split('\t')
                fid = entries[2]

    # for i, line in enumerate(gzip.GzipFile('nyc.txt.gz')):
    #     entries = line.split('\t')
    #     frames.append({
    #         'path':"https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/{}/{}/{}.jpg".format(
    #             entries[2][:3],entries[2][3:6],entries[2]),
    #         'regions':[
    #             {
    #                 "object_name":"name",
    #                 "full_frame":True,
    #                 "text":entries[8].replace('+',' '),
    #             },
    #             {
    #                 "object_name":"user_tags",
    #                 "full_frame":True,
    #                 "text":' '.join(entries[10].replace('+',' ').split(',')),
    #             }
    #         ]
    #     })


if __name__ == '__main__':
    fname = sys.argv[-1]
    last_tag_index = 0
    last_fid_index = 0
    tag_to_index = {}
    fid_to_index = {}
    inverted_index = defaultdict(list)
    #         if fid not in fid_to_index:
    #             last_fid_index += 1
    #             fid_to_index[fid] = last_fid_index
    #         for t in entries[10].replace('+',' ').split(','):
    #             if t not in tag_to_index:
    #                 tag_to_index[t] = last_tag_index
    #                 last_tag_index += 1
    #             inverted_index[tag_to_index[t]].append(fid_to_index[fid])
    # with gzip.open('yfcc_index.json.gz','w') as out:
    #     json.dump((tag_to_index,fid_to_index,inverted_index),out)