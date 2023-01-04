from fastapi import APIRouter
from utility.init.api_key import token_creator

router = APIRouter(
    tags=["Plugin Init Route"]
)

@router.get("/init")
async def init():

    """
        Init Endpoint for FastAPI

        returns token
    """

    token = await token_creator()

    return token