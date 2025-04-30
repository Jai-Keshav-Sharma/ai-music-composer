import streamlit as st
import torchaudio
from audiocraft.models import musicgen
import os
import tempfile
import torch

# Check CUDA availability
device = "cuda" if torch.cuda.is_available() else "cpu"
st.set_page_config(page_title="🎵 AI Music Composer", page_icon="🎵")

# Streamlit UI
st.title("🎵 AI Music Composer")
st.write("Generate music using Meta's MusicGen!")

# User input section
genre = st.selectbox("Choose a genre", ["pop", "jazz", "classical", "rock", "lofi", "electronic"])
mood = st.selectbox("Choose a mood", ["happy", "sad", "chill", "epic", "romantic"])
tempo = st.selectbox("Choose a tempo", ["slow", "mid", "fast"])

prompt = f"A {tempo} tempo {genre} track that feels {mood}"
st.markdown(f"**Prompt:** {prompt}")

# Generate button
if st.button("Generate Music"):
    try:
        with st.spinner("Loading model..."):
            model = musicgen.MusicGen.get_pretrained('small')
            model.set_generation_params(duration=10)
            model.to(device)

        with st.spinner("Generating music, please wait..."):
            wav = model.generate([prompt], progress=True)

            # Save to temp file
            output_dir = "musicgen_outputs"
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, f"{genre}_{mood}_{tempo}.wav")
            
            try:
                torchaudio.save(file_path, wav[0].cpu(), sample_rate=32000)
                st.success("Music generated successfully!")
                st.audio(file_path, format='audio/wav')
                
                with open(file_path, "rb") as f:
                    st.download_button(
                        "Download Music",
                        f,
                        file_name=os.path.basename(file_path),
                        mime="audio/wav"
                    )
            except Exception as e:
                st.error(f"Error saving audio file: {str(e)}")
                
    except Exception as e:
        st.error(f"An error occurred during music generation: {str(e)}")
        if "CUDA out of memory" in str(e):
            st.info("💡 Tip: The model requires significant GPU memory. Try using a machine with more GPU memory or use CPU mode.")