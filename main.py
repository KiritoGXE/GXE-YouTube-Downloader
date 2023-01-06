from pytube import YouTube


def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("Si è verificato un errore durante il download!!")
  print("Il download è stato completato!!")


link = input(
  "Bevenuto nel GXE YouTube Downloader metti il link del video qui per iniziare!! URL: "
)
Download(link)