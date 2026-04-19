"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Hardstyle & Techno Enthusiast Profile
    user_prefs = {
        "favorite_genre": "pop", 
        "favorite_mood": "happy",        
        "target_energy": 0.88,             
        "likes_acoustic": False            
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*70)
    genre = user_prefs['favorite_genre'].upper()
    mood = user_prefs['favorite_mood'].upper()
    print(f"🎵 TOP RECOMMENDATIONS FOR {genre} LOVERS ({mood} MOOD)")
    print("="*70 + "\n")
    
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"#{i} {song['title']}")
        print(f"    Artist: {song['artist']}")
        print(f"    Score:  {score:.2f}/6.25")
        print(f"    Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
