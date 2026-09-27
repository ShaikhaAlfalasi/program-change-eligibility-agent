import os

from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig
from google.genai import errors


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


# Models are ordered from preferred to fallback.
GEMINI_MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
]


def generate_with_fallback(prompt, use_url_context=False):
    """
    Generate a Gemini response using a fallback model strategy.

    Temporary availability errors such as 503 cause the next
    model to be tried.

    Other errors are raised immediately because switching
    models is unlikely to solve them.
    """

    errors_encountered = []

    for model in GEMINI_MODELS:

        try:
            print(f"Trying Gemini model: {model}")

            config = None

            if use_url_context:
                config = GenerateContentConfig(
                    tools=[
                        {"url_context": {}}
                    ]
                )

            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=config
            )

            print(f"Success with model: {model}")

            return response

        except errors.ServerError as error:

            print(f"Temporary server error with {model}:")
            print(error)

            errors_encountered.append({
                "model": model,
                "error": str(error)
            })

            # Try the next model.

        except errors.ClientError as error:

            # 429 = rate limit / temporary quota issue.
            if getattr(error, "code", None) == 429:

                print(f"Rate limit with {model}:")
                print(error)

                errors_encountered.append({
                    "model": model,
                    "error": str(error)
                })

                # Try the next model.

            else:
                # Examples: 400, 401, 403
                # These are not model-availability problems.
                raise

        except Exception:
            # Unexpected errors should not be silently
            # hidden by switching models.
            raise

    raise RuntimeError(
        "All configured Gemini models failed.\n"
        + "\n".join(
            f'{error["model"]}: {error["error"]}'
            for error in errors_encountered
        )
    )