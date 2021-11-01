from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List

import srt

from utils import to_time_str

@dataclass
class Description:
    id: str
    start: str
    end: str
    content: str


@dataclass
class Youtube:
    file_id: str
    title: str
    descriptions: List[Description] = field(default_factory=list)

    @classmethod
    def from_file(cls, path: Path) -> Youtube:
        file_id = path.name.split()[0]
        title = path.stem[6:-3]  # extract title from path
        youtube = cls(file_id=file_id, title=title)
        with open(path) as f:
            for raw_desc in srt.parse(f.read()):
                youtube.descriptions.append(Description(
                    id=f"{file_id}-{raw_desc.index:04}",
                    start=to_time_str(int(raw_desc.start.total_seconds()+0.5)),
                    end=to_time_str(int(raw_desc.end.total_seconds()+0.5)),
                    content=raw_desc.content.strip(),
                ))
        return youtube


def main():
    description_dir = Path("lolcs/description")
    if not description_dir.exists():
        raise ValueError(f"Description Directory is not exists: {description_dir.resolve()}")
    description_files = sorted(description_dir.glob("*.srt"))
    if not description_files:
        raise ValueError("There are not .srt files.")

    youtube_videos = []
    with open(Path("lolcs/youtube_descriptions.jsonl"), "w") as jsonfile:
        for path in description_files:
            youtube_video = Youtube.from_file(path)
            youtube_videos.append(youtube_video)
            jsonfile.write(json.dumps(asdict(youtube_video)))
            jsonfile.write("\n")


if __name__ == '__main__':
    main()
