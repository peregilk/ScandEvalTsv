
import jsonlines, os

folder = "/home/perk/ScandEvalTsv/datasets/sequence"
subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
#print(subfolders)

for d in subfolders:
    for filename in ["test","train"]:
        test_json = d+"/"+filename+".jsonl"
        test_tsv = d+"/"+filename+".tsv"
        with open(test_tsv, 'w+') as output_file:
            with jsonlines.open(test_json) as reader:
                for obj in reader:
                    output_file.write(obj['text'].replace("\t"," ") + "\t" + obj['label'].replace("\t","")+"\n")
