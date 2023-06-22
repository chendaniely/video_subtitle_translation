# using this example
# https://stackoverflow.com/questions/62728985/how-do-i-translate-using-huggingface-from-chinese-to-english
#


import srt
from tqdm import tqdm

import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


with open("020-clean/A_Lifelong_Journey_-_S01E01_-_Episode_1.srt") as f:
    subtitles = list(srt.parse(f.read()))


tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

subtitles_translated = []

for sub in tqdm(subtitles):
    text = sub.content
    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
    translation = model.generate(**tokenized_text)
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=False)[0]

    sub.content = translated_text
    subtitles_translated.append(sub)

subtitles_translated[10]

with open("030-output/A_Lifelong_Journey_-_S01E01_-_Episode_1_en.srt", "w") as f:
    f.write(srt.compose(subtitles_translated))
