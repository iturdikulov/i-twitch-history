import httpx
import logging
from os import environ
from pydantic import BaseModel

class Vod(BaseModel):
    id: str
    title: str

class Channel():
    def __init__(self):
        self.chat_log: list = []
        self._chat_message_ids: set = set()
        self.logger = logging.getLogger()

        self._headers = {"Client-Id": environ["CLIENT_ID"]}

    def get_channel_videos(self, owner_login, limit=10):
        """
        Retrieves all available videos for the channel.
        """
        cursor = ""
        variables = {
            "broadcastType": "ARCHIVE",
            "channelOwnerLogin": f"{owner_login}",
            "limit": limit,
            "videoSort": "TIME",
            "cursor": cursor
        }

        q = [
            {
                "extensions": {
                    "persistedQuery": {"sha256Hash": "67004f7881e65c297936f32c75246470629557a393788fb5a69d6d9a25a8fd5f", "version": 1}
                },
                "operationName": "FilterableVideoTower_Videos",
                "variables": variables,
            }
        ]

        videos = []
        while True:
            r = httpx.post("https://gql.twitch.tv/gql",
                json=q,
                headers=self._headers
            ).json()

            edges = [edge["data"]["user"]["videos"]["edges"] for edge in r]

            videos += [edge["node"] for edge in edges[0]]

            # Set cursor with hasNextPage validation
            if (r and r[0]["data"]["user"]["videos"]["pageInfo"]["hasNextPage"] is not False
            ):
                variables["cursor"] = r[0]["data"]["user"]["videos"]["edges"][-1]["cursor"]
            else:
                break

            if len(videos) >= limit:
                break

        return videos[:limit]

    def vods(self, owner_login):
        videos = self.get_channel_videos(owner_login)
        return [Vod(id=video["id"], title=video["title"]) for video in videos]
