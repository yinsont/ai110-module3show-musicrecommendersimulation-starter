# Music Recommendation Data Flow

## Process Overview

```mermaid
flowchart TD
    Start([Start]) --> Input["📥 INPUT: User Profile<br/>favorite_genre<br/>favorite_mood<br/>target_energy<br/>likes_acoustic"]
    
    Input --> LoadCSV["📂 Load CSV<br/>↓<br/>songs_list = 18 songs"]
    
    LoadCSV --> InitScores["Initialize<br/>scored_songs = []"]
    
    InitScores --> Loop{"More songs<br/>in CSV?"}
    
    Loop -->|Yes| FetchSong["🎵 Fetch next song<br/>from CSV"]
    
    FetchSong --> Score["⚙️ PROCESS: Calculate Score<br/>──────────<br/>genre_match: +2.0?<br/>mood_match: +1.0?<br/>energy_sim: ×1.5<br/>valence_sim: ×0.75<br/>danceability: ×0.5<br/>tempo_prox: +0.25?<br/>acoustic_bonus: +0.25?"]
    
    Score --> Store["📋 Store in Memory<br/>scored_songs.append<br/>(song, total_score)"]
    
    Store --> Loop
    
    Loop -->|No| Sort["🔄 Sort by Score<br/>scored_songs.sort<br/>descending"]
    
    Sort --> Rank["🏆 Rank Top K<br/>top_k_songs = ranked[0:k]"]
    
    Rank --> Output["📤 OUTPUT: Ranked List<br/>Position 1: Song + Score<br/>Position 2: Song + Score<br/>...<br/>Position K: Song + Score"]
    
    Output --> End([End])
    
    style Input fill:#e1f5ff
    style Score fill:#fff3e0
    style Output fill:#e8f5e9
    style Start fill:#f3e5f5
    style End fill:#f3e5f5
```

## Scoring Recipe

| Component | Points |
|-----------|--------|
| Genre match | +2.0 |
| Mood match | +1.0 |
| Energy similarity | ×1.5 |
| Valence similarity | ×0.75 |
| Danceability | ×0.5 |
| Tempo proximity | +0.25 |
| Acoustic bonus | +0.25 |
| **Max Score** | **~6.25** |

## Flow Summary

1. **INPUT**: Load user preferences and CSV songs
2. **PROCESS**: Loop through each song, calculate score using weighting formula
3. **OUTPUT**: Sort all scored songs and return top K recommendations
