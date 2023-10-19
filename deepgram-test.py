from deepgram import Deepgram
from dotenv import load_dotenv
import os
import json

load_dotenv()

if "DEEPGRAM_API_KEY" not in os.environ:
    raise Exception("Missing DEEPGRAM_API_KEY env var")


# The API key we created in step 3
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Hosted sample file
AUDIO_URL = "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"


def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    source = {"url": AUDIO_URL}
    options = {"smart_format": True, "model": "nova", "language": "en-US"}

    print("Requesting transcript...")
    print("Your file may take up to a couple minutes to process.")
    print(
        "While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s."
    )
    print(
        "To learn more about customizing your transcripts check out developers.deepgram.com"
    )

    response = dg_client.transcription.sync_prerecorded(source, options)
    print(json.dumps(response, indent=4))


main()
