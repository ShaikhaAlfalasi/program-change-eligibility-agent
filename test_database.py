from database import get_program_change_request

request_id = "STUD_CPSR_CHP3_000048"

result = get_program_change_request(request_id)

print(result)