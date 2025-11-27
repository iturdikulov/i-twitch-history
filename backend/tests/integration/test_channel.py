from app import Channel

def test_vods_list():
    channel = Channel()
    # TODO: hardcoded value
    vods = channel.vods("bobross")
    assert len(vods) > 0
