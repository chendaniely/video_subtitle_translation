import re

import srt


_RE_COMBINE_WHITESPACE = re.compile(r"\s+")


def clean_whitespace(text):
    """Remove any extra spaces between words"""
    return _RE_COMBINE_WHITESPACE.sub(" ", text).strip()

def remove_non_chinese(text):
    """Remove any non chinese characters"""
    return re.sub(r"[^\u4e00-\u9fff]", "", text)


with open("010-input/A_Lifelong_Journey_-_S01E01_-_Episode_1.srt") as f:
    subtitles = list(srt.parse(f.read()))


subtitles_clean = []

subtitles[834]
for sub in subtitles:
    new_sub_content = clean_whitespace(sub.content)
    new_sub_content = remove_non_chinese(new_sub_content)
    sub.content = new_sub_content
    subtitles_clean.append(sub)

subtitles_clean[834]

with open("020-clean/A_Lifelong_Journey_-_S01E01_-_Episode_1.srt", "w") as f:
    f.write(srt.compose(subtitles_clean))

###

subtitles[0].content

for idx, con in enumerate(subtitles):
    print(f"{idx}: {con.content}")

sub_content = subtitles[377].content

sub_content.strip().replace("\n", " ")


subtitles[834].content.strip().replace("\n", " ")

my_str = _RE_COMBINE_WHITESPACE.sub(" ", subtitles[834].content.strip().replace("\n", " ")).strip()
my_str