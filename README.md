# pyRHVoice
Python wrapper for RHVoice TTS

## Prerequisites
1. RHVoice. Instructions [here](https://cordelianew.university.innopolis.ru/wiki/doku.php?id=rhvoice)

## Install
`python setup.py install`

## Usage
    from pyrhvoice import RHVoice
    rhvoice = RHVoice()
    audio_path = rhvoice.get_audio_path('hello world')
    audio = rhvoice.get_audio('привет, мир!')
    rhvoice.play('hello world!')