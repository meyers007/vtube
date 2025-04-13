import sys, os, logging, datetime
from mangorest.mango import webapi
from io import BytesIO
#from django.conf import settings

logger = logging.getLogger( "vtube" )

#-------------------------------------------------------------------------------------------    
@webapi("/vtube/getDetails/")
def getDetails(request=None, user="me", dest_dir="/tmp/vtube/", src="", **kwargs):
    print(f" Requesting {src}")
    transcripts,summary, qa = "", "", ""
    if ( src):
        nbase = ""
        if src.startswith("/static/vtube/"):
            nbase = "vtube/" + src
        if os.path.exists(nbase+".transcript"):
            with(open(nbase+".transcript")) as f:
                transcripts = f.read();
        if os.path.exists(nbase+".qa"):
            with(open(nbase+".qa")) as f:
                qa = f.read();
        if os.path.exists(nbase+".summary"):
            with(open(nbase+".summary")) as f:
                summary = f.read();

    ret = dict( src= src, transcripts=transcripts, summary = summary, qa=qa)
    return ret

@webapi("/vtube/addQA/")
def addQA(request=None, user="me", comments="", src="", **kwargs):
    print(f" Adding QA to {src}")

    qa = ""
    if (not comments.strip() or not src):
        return qa

    nbase = "vtube/static/vtube/videos/media/"
    if ("https://" in src or "http://" in src):
        if (src.endswith("/")):
            src = src[:-1]
        nbase += src.split("/")[-1]
    elif src.startswith("/static/vtube/"):
        nbase = "vtube/" + src


    qaFILEName = nbase+".qa"
    if os.path.exists(qaFILEName):
        with(open(qaFILEName)) as f:
            qa = f.read();
    qa += f"<div class=vtubeComments> {user} {datetime.datetime.now()}: {comments}</div>"
    with(open(qaFILEName , "wt")) as f:
        f.write(qa);
    print(f" Adding QA to {src}: {qa}")

    return qa


@webapi("/vtube/update/")
def updateMeta(request=None, user="me", what="trans|summary", content="", src="", **kwargs):
    print(f" Adding {content} => {what} to {src}")
    if (not content.strip() or not src ):
        return "Nothing updated!!"

    nbase = "vtube/static/vtube/videos/media/"
    if ("https://" in src or "http://" in src):
        if (src.endswith("/")):
            src = src[:-1]
        nbase += src.split("/")[-1]
    elif src.startswith("/static/vtube/"):
        nbase = "vtube/" + src

    trFILEName = nbase+".transcript"
    smFILEName = nbase+".summary"

    if (what.startswith("tr")):
        file = trFILEName
    else:
        file = smFILEName

    qa = f"Updated by, {user} {datetime.datetime.now()}:<br/> {content}"
    print("===> " , qa , file)
    with(open(file , "wt")) as f:
        f.write(qa);

    return qa
