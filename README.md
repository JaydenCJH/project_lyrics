
![Alyrics Logo](https://github.com/JaydenCJH/project_lyrics/assets/35475313/22d34c93-4626-4035-b8a3-2688a8deb788) 
Alyrics: AI를 활용한 작사 및 작곡 모델 개발 프로젝트. 

Alyrics is a project to compose and write lyrics using RNN and LSTM.

## 팀 (Team)
**허은영** (Team Leader): 팀 리더 + 개발. To oversee the overall progress of the project + develop.

**최재형** (Project Manager): 음악파트 및 프로젝트 같이 관리 + 개발. In charge of composition part, manage project together + develop.

**한재현** (Data Manager): 프로젝트 전반적인 데이터 수집 + 개발. Data collection + develop

**최정민** (Data Manager): 프로젝트 전반적인 데이터 수집 + 개발. Data collection + develop.



## 프로젝트 소개 (Project description)
Almusic는 AI를 활용하여 작사 및 반주를 생성하는 프로젝트입니다. 
이 프로젝트는 사전학습 모델 없이 여러 장르에 맞는 작사 및 작곡을 하기위해 진행했습니다.

Almusic is project aimed to create lyrics and compose music using deep learning.
We aimed to compose and create lyrics without using any pre-trained models.

## 폴더 설명
**Extraction**: 작사 및 작곡 데이터 추출 코드와 데이터. 

**Extraction**: To crawl for lyrics data from melon and crawl MIDI data.

**MIDI_music.ipynb**: 작곡 관련 데이터 및 작곡 LSTM 모델. 
사용하려면 Linux system 에서 지원하는 lib을 사용하기때문에 윈도우스로 하면 실행이 안됩니다.

**MIDI_music.ipynb**: Composing related LSTM model.
To use this, it's using a library supported only for Linux.
sudo apt install -y fluidsynth
Inspired by Generate music RNN 


**RNN**: 작사 RNN 모델. RNN model to generate lyrics.

**lyrics_data**: 작사 관련 데이터. Data for lyrics generation

**wc**: 작사 데이터 워드 클라우드. Wordcloud created from lyrics generation

**lstm**: 작사 LSTM 모델. LSTM model to generate lyrics
