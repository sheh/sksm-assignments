import json
from typing import List
from pathlib import Path
from abc import abstractmethod

import boto3


class FileFetcher:
    @abstractmethod        
    def fetch(self):
        pass


class S3FileFetcher(FileFetcher):
    def __init__(self, bucket: str, credentials_file: str):
        self.bucket = bucket
        with open(credentials_file, 'r') as f:
            credentials = json.load(f)

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key'],
        )
        
    def fetch(self, path: str):
        return self.s3.get_object(Bucket=self.bucket, Key=path)["Body"].read()


class LocalFileFetcher(FileFetcher):
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        
    def fetch(self, path: str):
        with open(self.root_path / path, "rb") as f:
            return f.read()


class AudioFetcher:
    
    def __init__(self, fetcher: FileFetcher):
        self.fetcher = fetcher
        
    def fetch(self, urls: List[str]):
        for url in urls:
            yield self.fetcher.fetch(url)


def save_audio(audio: bytes, path: str):
    with open(path, "wb") as f:
        f.write(audio)


if __name__ == "__main__":
    fetcher = LocalFileFetcher("data")
    audio_fetcher = AudioFetcher(fetcher)
    for audio in audio_fetcher.fetch(["data/audio.mp3"]):
       save_audio(audio, "data_local/audio.mp3")
    
    fetcher = S3FileFetcher("my-bucket", "credentials.json")
    audio_fetcher = AudioFetcher(fetcher)
    for audio in audio_fetcher.fetch(["data/audio.mp3"]):
        save_audio(audio, "data_s3/audio.mp3")
