import sys
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import wave
import json
import os

# 🧠 Import the mapping function
from mapping import best_match

# Step 1: Normalize audio
def normalize_audio(input_path, output_path):
    try:
        print(f"🎧 Loading input audio: {input_path}")
        audio = AudioSegment.from_file(input_path)
        normalized = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2).normalize()
        normalized.export(output_path, format="wav")
        print(f"✅ Normalized audio saved as {output_path}")
    except Exception as e:
        print(f"⚠️ Error during normalization: {e}")
        sys.exit(1)

# Step 2: Transcribe audio
def transcribe_audio(wav_path, model_path):
    try:
        wf = wave.open(wav_path, "rb")
    except Exception as e:
        print(f"⚠️ Failed to open WAV file: {e}")
        return

    # 🧪 Format check
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        print("⚠️ WAV file must be mono, 16-bit, 16kHz. Please normalize correctly.")
        return

    print(f"📁 Attempting to load model from: {model_path}")
    try:
        model = Model(model_path)
    except Exception as e:
        print(f"🚨 Model load failed: {e}")
        return

    try:
        rec = KaldiRecognizer(model, wf.getframerate())
    except Exception as e:
        print(f"⚠️ Failed to initialize recognizer: {e}")
        return

    print(f"\n🎙️ Transcribing: {wav_path}")
    final_text = ""
    try:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                print("✅", result.get("text"))
            else:
                partial = json.loads(rec.PartialResult())
                print("…", partial.get("partial"))
        final = json.loads(rec.FinalResult())
        final_text = final.get("text", "").strip()
        print("🎯 Final:", final_text if final_text else "[No final text captured]")
    except Exception as e:
        print(f"⚠️ Error during transcription: {e}")
        return

    # 🧩 Step 3 — hook STT → Mapping
    if final_text:
        print("\n🔗 Passing to NLP Mapper...")
        try:
            matched_file = best_match(final_text)
            if matched_file:
                print(f"🎬 Animation file triggered: {matched_file}")
            else:
                print("⚠️ No matching animation found.")
                with open("unmatched_phrases.txt", "a", encoding="utf-8") as f:
                    f.write(final_text + "\n")
        except Exception as e:
            print(f"⚠️ Error in mapping logic: {e}")

    # 📝 Optional: log final transcription
    try:
        with open("sample_log.txt", "w", encoding="utf-8") as f:
            f.write(final_text + "\n")
    except Exception as e:
        print(f"⚠️ Failed to write transcription log: {e}")

# Step 4: Run everything
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide an input audio file (.wav or .m4a).")
    else:
        input_file = sys.argv[1]
        normalized_file = "normalized.wav"

        # ✅ Make sure this matches your language
        model_path = r"D:\audio_to_stt_app\vosk_model"

        normalize_audio(input_file, normalized_file)
        transcribe_audio(normalized_file, model_path)