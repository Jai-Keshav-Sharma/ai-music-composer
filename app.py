import streamlit as st
import torchaudio
from audiocraft.models import musicgen
import os
import tempfile

# Streamlit UI
st.title("🎵 AI Music Composer")
st.write("Generate music using Meta’s MusicGen!")

# User input section
genre = st.selectbox("Choose a genre", ["pop", "jazz", "classical", "rock", "lofi", "electronic"])
mood = st.selectbox("Choose a mood", ["happy", "sad", "chill", "epic", "romantic"])
tempo = st.selectbox("Choose a tempo", ["slow", "mid", "fast"])

prompt = f"A {tempo} tempo {genre} track that feels {mood}"
st.markdown(f"**Prompt:** {prompt}")

# Generate button
if st.button("Generate Music"):
    with st.spinner("Loading model..."):
        model = musicgen.MusicGen.get_pretrained('small')
        model.set_generation_params(duration=10)

    with st.spinner("Generating music, please wait..."):
        wav = model.generate([prompt], progress=True)

        # Save to temp file
        output_dir = "musicgen_outputs"
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f"{genre}_{mood}_{tempo}.wav")
        torchaudio.save(file_path, wav[0].cpu(), sample_rate=32000)

        st.success("Music generated successfully!")
        st.audio(file_path, format='audio/wav')
        st.download_button("Download Music", open(file_path, "rb"), file_name=os.path.basename(file_path))
