import os
import json
import pytz
from datetime import datetime
from dateutil import parser
from base64 import b64decode, b64encode
from Cryptodome.Cipher import ChaCha20_Poly1305
from dotenv import load_dotenv

load_dotenv(".env")

TOKEN_SECRET = b64decode(os.environ.get('API_TOKEN_SECRET').encode("utf-8"))

async def token_creator():

    """ 
    Creates a Token
    """

    payload = {
        "created_on": str(datetime.now().astimezone(pytz.utc))
    }

    payload_jsonify = json.dumps(payload)
    payload_bytes = payload_jsonify.encode("utf-8")

    cipher = ChaCha20_Poly1305.new(key=TOKEN_SECRET)
    nonce = cipher.nonce
    cipherpayload, tag = cipher.encrypt_and_digest(payload_bytes)
    token = nonce + cipherpayload + tag
    
    token = b64encode(token).decode("utf-8")

    return token



