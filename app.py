import string

from flask import Flask,send_file,request
from pytube import YouTube
import os

path = './Songs'
translation_table = str.maketrans('', '', string.punctuation)

app = Flask(__name__)



@app.route('/',methods=['GET'])
def Main_Page():

    link = request.args.get('link')
    youtubeLinkTemplate = "https://www.youtube.com/watch?v="

    youtubeLink = youtubeLinkTemplate + link
    print(youtubeLink)
    yt = YouTube(youtubeLink)
    ys = yt.streams.get_audio_only()

    safeString = yt.title
    safeString = safeString.translate(translation_table)
    filename = safeString.replace(" ","") + ".aac"

    print("hi")
    ys.download(filename=filename,output_path=path,skip_existing=True,timeout=20,max_retries=2)
    print(ys.get_file_path())


    fileLocation = f"{path}/{filename}"
    print(fileLocation)
    print(filename)
    fileToBeSend = (send_file(fileLocation, as_attachment=True))
    return fileToBeSend




if __name__=='__main__':

    if not (os.path.exists(path)):
        print("Created Songs directory")
        os.mkdir(path)

    app.run(debug=True,host="0.0.0.0")
