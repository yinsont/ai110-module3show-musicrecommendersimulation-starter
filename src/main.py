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
        "favorite_genre": "hardstyle",    # Primary: hardstyle, secondary: techno, electronic
        "favorite_mood": "intense",        # High-octane, adrenaline-driven
        "target_energy": 0.88,             # Very high energy (hardstyle/techno range)
        "likes_acoustic": False            # Pure electronic—no acoustic instruments
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations for Hardstyle/Techno Enthusiast:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
