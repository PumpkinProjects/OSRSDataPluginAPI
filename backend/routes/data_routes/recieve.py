from fastapi import APIRouter

router = APIRouter(
    tags=["Database Routes"]
)

@router.post("/data/recieve")
async def recieve(data):

    print(data)

    return "Successfully Recieved!"