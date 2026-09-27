from llm_client import generate_with_fallback


prompt = """
Reply with exactly:

LLM FALLBACK TEST SUCCESS
"""


response = generate_with_fallback(prompt)

print("\n" + "=" * 80)
print("RESPONSE")
print("=" * 80)

print(response.text)

print("\n" + "=" * 80)
print("LLM FALLBACK TEST COMPLETE")
print("=" * 80)