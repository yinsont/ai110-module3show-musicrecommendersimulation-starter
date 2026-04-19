# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**VibeRider**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

It generates personalized song recommendations based on a user's preferred genre, mood, energy level, and acoustic preference. It assumes users have stable music tastes across these four dimensions and works best for discovery within a curated catalog rather than billions of songs. This is a classroom simulation designed to teach recommendation logic—not for real production use—but grounded in actual preference data.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

VibeRider scores each song by first checking if genre and mood match the user's preferences (+2.0 and +1.0 points respectively), then adds bonuses based on how close the song's energy, valence, danceability, tempo, and acousticness are to what the user wants. The key change from starter logic: genre gets double the weight of mood, and energy similarity (0–1.5 points) heavily influences the final score. All songs get ranked by total score and the top K are returned as recommendations.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 18 songs across 14 genres (pop, rock, lofi, ambient, jazz, soul, metal, classical, reggae, synthwave, electronic, hip-hop, indie pop, indie rock, dark ambient) and 14 moods (chill, happy, intense, focused, moody, relaxed, energetic, dreamy, playful, romantic, aggressive, inspirational, adventurous, introspective). No songs were added or removed from the original dataset. 
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

Works well for users with consistent genre and mood preferences. Captures the relationship between energy and song characteristics effectively. Recommendations align with intuition when multiple attributes match (e.g., chill lofi tracks cluster well). 
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

Doesn't consider artist preferences, release date, or listening history. Limited to 18 songs; doesn't generalize to larger catalogs. Acoustic preference is binary rather than nuanced. May overweight genre for users with flexible tastes. Smaller moods like "introspective" have fewer songs to recommend.  
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

Tested profiles like lofi lovers, energetic pop fans, and ambient relaxation seekers—verified that top results matched input preferences. Surprised by how energy similarity could override mood in some edge cases.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Could add artist affinity, collaborative filtering based on similar users, ranking by artist recency, confidence scores for recommendations, and diversity penalties to avoid recommending too many similar songs.  
---

## 9. Personal Reflection  

Learned that simple weighting schemes can be surprisingly effective with careful tuning. Was interesting to see how different user types need different attribute priorities. This made me appreciate how building a "good enough" recommender requires balancing accuracy with computational simplicity.  
