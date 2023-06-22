# video_subtitle_translation


## Setup

```shell
# Setup a virtual environment
python3 -m virtualenv venv

# Activate your virtual environment
source venv/bin/activate

# venv\Scripts\activate # for windows

# Install all requirements
pip install -r requirements.txt
```

## Main python packages

- [translatesubs](https://github.com/Montvydas/translatesubs)
- [pysubs2](https://github.com/tkarabela/pysubs2)
- [srt](https://github.com/cdown/srt)
- [transformers](https://huggingface.co/docs/transformers/installation)
  - used `pip install 'transformers[tf-cpu]'`
  - `pip install 'transformers[torch]'`
  - `pip install transformers[sentencepiece]`
  - `pip install sacremoses`