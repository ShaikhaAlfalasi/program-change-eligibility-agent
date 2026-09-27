import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_request_type(request_id):
    response = (
        supabase
        .table("Request")
        .select("Request_Type")
        .eq("Request_ID", request_id)
        .limit(1)
        .execute()
    )

    if response is None or not response.data:
        return None

    return response.data[0]["Request_Type"]


def get_program_change_request(request_id):
    response = (
        supabase
        .rpc(
            "get_program_change_request",
            {"p_request_id": request_id}
        )
        .execute()
    )

    return response.data