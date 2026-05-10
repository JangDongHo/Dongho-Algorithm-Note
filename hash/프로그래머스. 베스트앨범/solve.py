def solution(genres, plays):
    data = {}
    genre_play_cnt = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_cnt[genre] = genre_play_cnt.get(genre, 0) + play
        data.setdefault(genre, []).append((play, i))

    result = []

    for genre, _ in sorted(genre_play_cnt.items(), key=lambda x: x[1], reverse=True):
        musics = sorted(data[genre], key=lambda x: (-x[0], x[1]))
        result.extend([idx for _, idx in musics[:2]])

    return result