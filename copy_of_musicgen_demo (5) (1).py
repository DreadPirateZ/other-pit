# -*- coding: utf-8 -*-
"""Copy of MusicGen Demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13mV5X31_gikp2vbNYuN5LWgUBS3H4Sek
"""

!python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft
# !python3 -m pip install -U audiocraft

from audiocraft.models import musicgen
from audiocraft.utils.notebook import display_audio
import torch

model = musicgen.MusicGen.get_pretrained('medium', device='cuda')
model.set_generation_params(duration=30)

res = model.generate([
    'crazy EDM, heavy bang',
    'classic reggae track with an electronic guitar solo',
    'lofi slow bpm electro chill with organic samples',
    'rock with saturated guitars, a heavy bass line and crazy drum break and fills.',
    'earthy tones, environmentally conscious, ukulele-infused, harmonic, breezy, easygoing, organic instrumentation, gentle grooves',
],
    progress=True)
display_audio(res, 32000)

"""See our repo https://github.com/facebookresearch/audiocraft for more details on how to use this model!

See also [MusicGen Gradio Demo](https://colab.research.google.com/drive/1-Xe9NCdIs2sCUbiSmwHXozK6AAhMm7_i?usp=sharing) for a Colab using the Gradio app instead!

"""



