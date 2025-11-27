from app import Channel, ChatDownloader

def test_download_vods_chat():
    vods = Channel().vods("bobross", limit=1)

    chat_downloader = ChatDownloader()
    for vod in vods:
        chat_log = chat_downloader.download(vod.id)
        assert len(chat_log) > 0
