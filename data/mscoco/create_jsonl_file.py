import os
from pycocotools_src.coco import COCO
import json
import glob

dataDir = '/srv/data/aics/datasets/mscoco/annotations/'
dataType = 'val2017'
annInstancesFile = '{}/instances_{}.json'.format(dataDir,dataType)
coco_instances = COCO(annInstancesFile)
annCaptionsFile = '{}/captions_{}.json'.format(dataDir,dataType)
coco_caps=COCO(annCaptionsFile)


faster_r_cnn_output = "/home/guscoleja@GU.GU.SE/volta/data/mscoco/images/coco_images/test2015/"
img_ids = list()

ann_count = 0
with open("output.jsonl", 'w') as f:
    for file in glob.glob(faster_r_cnn_output + '*.npy'):
        img_id = int(file.split('/')[-1].split('.npy')[0])
        ann_ids = coco_caps.getAnnIds(imgIds=img_id)
        annotations = coco_caps.loadAnns(ann_ids)
        sentences = list()
        for annotation in annotations:
            sentences.append(annotation['caption'])
            ann_count +=1
        if len(sentences) > 5:
            sentences = sentences[:5]
        elif len(sentences) < 5:
            while len(sentences)<5:
                sentences.append(sentences[-1])
        append_item = dict()
        append_item['sentences'] = sentences
        append_item['id'] = img_id
        f.write(json.dumps(append_item) + "\n")
