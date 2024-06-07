from httpx import AsyncClient
from main._config import config


async def post_process(client: AsyncClient):
    response = await client.post(
        f"{config.NODE_SERVER}/smarthome/actions/postprocess",
        json={}
    )
    return response.status_code 


async def create_video():
    import subprocess

    subprocess.run(
        ["./bash.sh"]
    )
    return {"message": "Video has been created."}
