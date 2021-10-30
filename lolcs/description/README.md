# about how to get CS-lol's description in srt format from Youtube

## requirement
- Windows
- python >= 3.7

# procedures
- Step 1: install [ffmpeg](https://www.ffmpeg.org/)
- Step 2: get youtube-dl.exe from https://github.com/ytdl-org/youtube-dl/releases/tag/2021.06.06
- Step 3: put youtube-dl.exe on your directory
- Step 4: open windows terminal from step 3's directory
    - input the following command separately to get the raw vtt YouTube's subtitle files:
    
            .\youtube-dl.exe -f 'bestvideo[height<=144]+bestaudio/best[height<=144]' -o "lolcs/description/0%(playlist_index)s - %(title)s.%(ext)s" --skip-download --write-auto-sub --playlist-items 1-5,10,12,30,34,41,71,99 --merge-output-format mp4 https://www.youtube.com/watch?v=X7AvGgnlceM"&"list=PLcvpEVobSi9e3nCd8U55sxgnoz85ZZYfj
            .\youtube-dl.exe -f 'bestvideo[height<=144]+bestaudio/best[height<=144]' -o "lolcs/description/%(playlist_index)s - %(title)s.%(ext)s" --skip-download --write-auto-sub --playlist-items 262,273,275,276,279,284 --merge-output-format mp4 https://www.youtube.com/watch?v=X7AvGgnlceM"&"list=PLcvpEVobSi9e3nCd8U55sxgnoz85ZZYfj
            .\youtube-dl.exe -f 'bestvideo[height<=144]+bestaudio/best[height<=144]' -o "lolcs/description/998 - %(title)s.%(ext)s" --skip-download --write-auto-sub https://www.youtube.com/watch?v=NhebWJhVQe4"&"t
            .\youtube-dl.exe -f 'bestvideo[height<=144]+bestaudio/best[height<=144]' -o "lolcs/description/999 - %(title)s.%(ext)s" --skip-download --write-auto-sub https://www.youtube.com/watch?v=w8Am7vnPyQw"&"t

- 5: ensure 20 *.vtt are in .\\lolcs\\description\\, then open windows terminal from step 3's directory, run

            python .\YouTube-vtt-to-srt.py
            
- 6: go next step for preprocessing