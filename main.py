import os
from audio_transcriber import AudioTranscriber
from youtube_mp3 import download_youtube_audio_as_mp3
import subprocess
import librosa

if __name__ == "__main__":
    # YouTubeのリンクを入力
    youtube_link = input("YouTubeのリンクを入力してください: ")
    output_directory = "/Users/sakatuyo07/Desktop/yossy_AI/static/image/mp3"
    output_file_name = input("出力するMP3ファイル名を入力してください (例: output.mp3): ")

# 出力ファイル名に拡張子.mp3が含まれているか確認し、追加
    if not output_file_name.endswith(".mp3"):
        output_file_name += ".mp3"

    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # フルパスの作成
    output_file_path = os.path.join(output_directory, output_file_name)

    # YouTubeからMP3ファイルをダウンロード
    download_youtube_audio_as_mp3(youtube_link, output_file_path)

    # ファイルが存在するか確認
    if not os.path.exists(output_file_path):
        print(f"エラー: ファイルが見つかりません: {output_file_path}")
    else:
        # AudioTranscriberインスタンスを作成
        transcriber = AudioTranscriber()

        # 文字起こしを開始（ダウンロードしたMP3ファイルを使用）
        try:
            # librosaを使って音声データを読み込む
            audio_data, _ = librosa.load(output_file_path, sr=None)
            transcriber.start_transcription(audio_data)
        except Exception as e:
            print(f"文字起こし中にエラーが発生しました: {str(e)}")



