from __future__ import unicode_literals
import youtube_dl


def downloadAndConvertToMp3VideosFromYoutube(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(str('done!').upper())

    except Exception as error:
        print('Algo deu errado :(')
        print(f'Erro: {error}')