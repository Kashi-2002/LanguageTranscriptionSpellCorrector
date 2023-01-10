from hindiwsd import hindi_wsd  
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
import shutil
import json
from contextlib import suppress

# print(hindi_wsd.wordsense("सीफ वल कप के फाइनल में "))   

# with open(".venv\destination.json",encoding='utf8') as json_file:
#         data = json.loads(json_file.read())
        
# transcript=data['transcription']
# print(transcript)

app=FastAPI()

@app.post("/")
def spellcollector(file: UploadFile = File(...)):
    # if(language=="hindi"):
    # model=modelload(language)
    with open(".venv\destination.json", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    with open(".venv\destination.json",encoding='utf8') as json_file:
        data = json.loads(json_file.read())
    transcript=data['transcription']
    # model.punctuate_text(transcript)
    # print(transcript)
    with suppress(UnicodeDecodeError):
        hindi_wsd.wordsense(transcript)
    # try:

    #     # continue
    # except UnicodeDecodeError:
    #     pass
    dict1 = {}
    with open("test.txt" ,"r",encoding="utf-8") as fh:
        for line in fh:
            description = line.strip()
        dict1["spellcorrected"] = description
        out_file = open("spellcorrect.json", "w")
        json.dump(dict1, out_file, indent = 4, sort_keys = False)
    return dict1