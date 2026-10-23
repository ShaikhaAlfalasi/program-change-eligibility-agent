
import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY must be set in your .env file."
    )

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_program_change_request(request_id):
    """
    Retrieve Program Change request data through the
    authorized Supabase RPC function.

    This function does not query the Request table directly.
    """
    response = (
        supabase
        .rpc(
            "get_program_change_request",
            {"p_request_id": request_id}
        )
        .execute()
    )

    return response.data
