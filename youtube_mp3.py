import yt_dlp

# YouTubeから音声をダウンロードしてMP3に変換する関数
def download_youtube_audio_as_mp3(url, output_path="output.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',  # 最高品質の音声フォーマットを選択
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # ビットレートを設定（192kbps）
        }],
        'outtmpl': output_path,  # 出力ファイル名のテンプレート
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"MP3ファイルが保存されました: {output_path}")
    except yt_dlp.utils.DownloadError as e:
        print(f"エラーが発生しました: {str(e)}")
        print("FFmpegのインストールを確認してください。")




