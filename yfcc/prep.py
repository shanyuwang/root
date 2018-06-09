"""
    # 'path':"s3://multimedia-commons/data/images/{}/{}/{}.jpg".format(entries[2][:3],entries[2][3:6],entries[2]),
"""
import gzip, json, random

if __name__ == '__main__':
    frames = []
    for i, line in enumerate(gzip.GzipFile('nyc.txt.gz')):
        entries = line.split('\t')
        frames.append({
            'path':"https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/{}/{}/{}.jpg".format(
                entries[2][:3],entries[2][3:6],entries[2]),
            'regions':[
                {
                    "object_name":"name",
                    "full_frame":True,
                    "text":entries[8].replace('+',' '),
                },
                {
                    "object_name":"user_tags",
                    "full_frame":True,
                    "text":' '.join(entries[10].replace('+',' ').split(',')),
                }
            ]
        })
    for i, line in enumerate(gzip.GzipFile('paris.txt.gz')):
        entries = line.split('\t')
        frames.append({
            'path':"https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/{}/{}/{}.jpg".format(
                entries[2][:3],entries[2][3:6],entries[2]),
            'regions':[
                {
                    "object_name":"name",
                    "full_frame":True,
                    "text":entries[8].replace('+',' '),
                },
                {
                    "object_name":"user_tags",
                    "full_frame":True,
                    "text":' '.join(entries[10].replace('+',' ').split(',')),
                }
            ]
        })
    random.shuffle(frames)
    with gzip.open('framelist.gz','w') as out:
        json.dump({'frames':frames[:5000]},out)