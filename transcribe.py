#!/usr/bin/env python
import colabexts
from colabexts import jcommon
import whisper,  os, datetime, argparse, io, soundfile, sys, hashlib, torch
import numpy as np

#-----------------------------models-----------------------------------------------------------------
import platform
device = "cpu"
if (torch.cuda.is_available() ):
    device = "cuda"
#elif torch.backends.mps.is_available() and platform.processor() =='arm':
#    device = "mps"
#-----------------------------------------------------------------------------------
def transcribe(file ="/Users/snarayan/Desktop/data/audio/index.mp4", **kwargs):
    tr = whisper.load_model("base", device=device)
    result = tr.transcribe(file)
    return result

def para(txt):
    sents = txt.split(". ")
    ret = ""
    for i in range(0,len(sents),5):
        ret +=  " ".join(sents[i:i+5]) + "\n"
    return ret 
#-----------------------------------------------------------------------------------
sysargs=None
def addargs():
    global sysargs
    p = argparse.ArgumentParser(f"{os.path.basename(sys.argv[0])}:")
    p.add_argument('-u', '--url', type=str, required=1, help="File, URL, Youtube URL")
    try:
        sysargs, unknown=p.parse_known_args(sys.argv[1:])
    except argparse.ArgumentError as exc:
        print(exc.message )
        
    if (unknown):
        print("Unknown options: ", unknown)
    return sysargs
#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    if (not colabexts.jcommon.inJupyter()):
        t1 = datetime.datetime.now()
        sysargs = addargs()
        ret = transcribe(sysargs.url)
        par = para(ret['text'])

        with open(sysargs.url + ".transcript", "w") as f:
            f.write(par)
        t2 = datetime.datetime.now()
        print(f"#All Done in {str(t2-t1)} ***")
    else:
        pass
