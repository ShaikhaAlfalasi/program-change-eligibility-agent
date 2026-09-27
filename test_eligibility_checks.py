from eligibility_agent import run_program_change_agent


request_id = "STUD_CPSR_CHP3_000050"

result = run_program_change_agent(request_id)

print("\n" + "=" * 80)
print("PROGRAM CHANGE ELIGIBILITY AGENT")
print("=" * 80)

print("\n" + result["report"])

print("\n" + "=" * 80)
print("AGENT TEST COMPLETE")
print("=" * 80)