from os import environ

from twichist import ChatDownloader

def test_download():
    chat_downloader = ChatDownloader()
    chat = chat_downloader.download("2626748422")
    print(chat)
