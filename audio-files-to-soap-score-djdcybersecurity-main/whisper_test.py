import whisper

def main():
    model = whisper.load_model("base")  # You can also try "small" if performance is okay

    audio_path = "audio/017af3f5-d145-41a2-95a4-5acfa0f1bd06.wav"  # Or another valid file
    print(f"Transcribing {audio_path}...")
    result = model.transcribe(audio_path)

    transcript_text = result.get("text", "").strip()
    print("\n--- TRANSCRIPT ---\n")
    print(transcript_text)

if __name__ == "__main__":
    main()
