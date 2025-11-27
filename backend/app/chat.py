import logging
from datetime import datetime
from os import environ
from venv import logger
import httpx

def get_time_difference(start_time: datetime, end_time: datetime) -> float:
    return (end_time - start_time).total_seconds()

# TODO: remove hard-coded operation
GQL_OPERATIONS = {
    "VideoCommentsByOffsetOrCursor": {
        "hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a",
    },
}

class ChatDownloader:
    def __init__(self):
        self.chat_log: list = []
        self._chat_message_ids: set = set()
        self.logger = logging.getLogger()

        self._headers = {"Client-Id": environ["CLIENT_ID"]}

    def get_segment(self, vod_id, offset: int = 0, cursor: str = ""):
        operation_info = GQL_OPERATIONS["VideoCommentsByOffsetOrCursor"]
        query_hash = operation_info["hash"]

        variables = {"videoID": vod_id}
        if offset != 0:
            variables["contentOffsetSeconds"] = offset
        elif cursor:
            variables["cursor"] = cursor

        q = [
                {
                    "extensions": {
                        "persistedQuery": {"sha256Hash": query_hash, "version": 1}
                    },
                    "operationName": "VideoCommentsByOffsetOrCursor",
                    "variables": variables,
                }
            ]

        r = httpx.post("https://gql.twitch.tv/gql",
            json=q,
            headers=self._headers
        ).json()

        comments = r[0]["data"]["video"]["comments"]

        if comments:
            if comments["pageInfo"]["hasNextPage"]:
                return [c["node"] for c in comments["edges"]], comments["edges"][-1]["cursor"]
            return [c["node"] for c in comments["edges"]], None
        return [], None

    def download(self, vod_id, offset: int = 0) -> list:
        cursor = ""
        chat_log = []
        while True:
            segment, cursor = self.get_segment(vod_id, offset=offset, cursor=cursor)
            chat_log += segment

            if not cursor:
                break

        return chat_log
