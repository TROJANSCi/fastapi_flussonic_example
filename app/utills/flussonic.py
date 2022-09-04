import time
import uuid
import hashlib
from typing import Union

from app.core.configure import get_setting

flussonic_host: str = get_setting('flussonic_host')
secretkey: str = get_setting('secretkey')
life_time: int = get_setting('life_time')
stream_path: str = get_setting('stream_path')
ipaddr: Union[bool, str] = get_setting('ipaddr')
desync: int = get_setting('desync')


async def generate_uri(video: str, ip: str = None, types: str = "embed") -> str:
    start_time = int(time.time())
    end_time = int(start_time + life_time)
    salt = uuid.uuid4().hex
    ipaddress = ip if type(ipaddr) == bool else ipaddr

    hash_str = f"{stream_path}{video}{ipaddr}{start_time}{end_time}{secretkey}{salt}"
    hash = hashlib.sha1(hash_str.encode('utf-8')).hexdigest()
    token = f"{hash}-{salt}-{end_time}-{start_time}"

    link = f"{flussonic_host}/{stream_path}{video}/embed.html?token={token}&remote={ipaddress}"
    embed = f'<iframe allowfullscreen style="width:640px; height:480px;" src="{link}"></iframe>'

    return embed if types == 'embed' else link

