from fastapi import APIRouter, Request

router = APIRouter(
    tags=["Database Routes"]
)

@router.post("/data/recieve")
async def recieve(request: Request):

    data = await request.json()

    print(data)

    return "Successfully Recieved!"