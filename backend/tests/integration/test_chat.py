from app import ChatDownloader

def test_download():
    chat_downloader = ChatDownloader()
    # TODO: hardcoded value
    chat_log = chat_downloader.download("2626748422")
    assert len(chat_log) > 0
