# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:51:25 2021

@author: Thanasis
"""

from google_speech import Speech
# say "Hello World"
text = 'абзац административный'
lang = 'ru'
speech = Speech(text, lang)
speech.play()

# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
#sox_effects = ("speed", "1.5")
#speech.play(sox_effects)

# save the speech to an MP3 file (no effect is applied)
speech.save('russian1.mp3')

from yandex_speech import TTS
tts = TTS("zahar", "mp3", "60589d42-0e42-b742-8942-thekeyisalie")
tts.generate("абзац")
tts.save()
speech.play()