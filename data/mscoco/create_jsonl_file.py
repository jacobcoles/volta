import os
faster_r_cnn_output = "./images/coco_images/test2015"
img_ids = list()


with open("output.jsonl", 'w') as f:
    for file in os.listdir(faster_r_cnn_output):
        img_id = int(file.strip('.npy'))
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
