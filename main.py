from flask import Flask,send_file,request
from pytube import YouTube
app = Flask(__name__)

@app.route('/',methods=['GET'])
def Main_Page():
    idk = '47JKU1sYFzw'
    link = request.args.get('link')
    youtubeLink = "https://www.youtube.com/watch?v=" + link
    yt = YouTube(youtubeLink)
    ys = yt.streams.get_audio_only()
    ys.download()
    fileLocation= ys.get_file_path()



    return send_file(fileLocation, as_attachment=True)















if __name__=='__main__':
    app.run(debug=True)
