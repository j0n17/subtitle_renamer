# Subtitle renamer
Pseudo automatically rename subtitles with movies' name

# Usage : 

```sh
usage: rename_subtitles.py [-h] -d DIRECTORY -s SUBTITLE_EXT -e EPISODE_EXT --regex-episode REGEX_EPISODE --regex-subtitle REGEX_SUBTITLE

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
  -s SUBTITLE_EXT, --subtitle-ext SUBTITLE_EXT
  -e EPISODE_EXT, --episode-ext EPISODE_EXT
  --regex-episode REGEX_EPISODE
  --regex-subtitle REGEX_SUBTITLE
```

Given the following files :
```sh
/media/tv_shows/LegallyObtainedTVShow S03E07 wwwww.mkv
/media/tv_shows/LegallyObtainedTVShow S03E08 xxxxx.mkv
/media/tv_shows/LegallyObtainedTVShow S03E09 yyyyy.mkv
/media/tv_shows/LegallyObtainedTVShow S03E10 zzzzz.mkv

/media/tv_shows/ubuntu-20.04-live-server-amd64 - 3x07 - aaaaa.en.srt
/media/tv_shows/ubuntu-20.04-live-server-amd64 - 3x08 - bbbbb.en.srt
/media/tv_shows/ubuntu-20.04-live-server-amd64 - 3x09 - ccccc.en.srt
/media/tv_shows/ubuntu-20.04-live-server-amd64 - 3x10 - ccccc.en.srt
```

Run :
```sh
python3 rename_subtitles.py -d /media/tv_shows -s srt -e mkv --regex-episode "S(\d+)E(\d+) " --regex-subtitle "- (\d+)x(\d+) -"
```

To have :
```sh
/media/tv_shows/LegallyObtainedTVShow S03E07 wwwww.mkv
/media/tv_shows/LegallyObtainedTVShow S03E08 xxxxx.mkv
/media/tv_shows/LegallyObtainedTVShow S03E09 yyyyy.mkv
/media/tv_shows/LegallyObtainedTVShow S03E10 zzzzz.mkv

/media/tv_shows/LegallyObtainedTVShow S03E07 wwwww.srt
/media/tv_shows/LegallyObtainedTVShow S03E08 xxxxx.srt
/media/tv_shows/LegallyObtainedTVShow S03E09 yyyyy.srt
/media/tv_shows/LegallyObtainedTVShow S03E10 zzzzz.srt
```
