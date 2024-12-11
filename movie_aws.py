
import streamlit as st

# Title of the app
st.title("IMDb Movie Recommendation System")

# Input box for the movie name
movie_name = st.text_input("Enter a movie you have watched:", "")

if st.button("Recommend Similar Movies"):
    if movie_name.lower() == "noelle":
        # Description for the entered movie
        st.subheader("Description for the movie you entered:")
        entered_movie = {
            "title": "Noelle",
            "year": 2019,
            "average_rating": 3.00,
            "common_genres": "Children",
            "description": "Noelle (2019) is a delightful holiday comedy about Kris Kringle's spirited daughter, Noelle, who embarks on a whimsical adventure to save Christmas. Filled with humor, heart, and holiday magic, the film showcases themes of family, responsibility, and the joy of spreading festive cheer."
        }
        st.markdown(f"**{entered_movie['title']}**")
        st.write(f"Year: {entered_movie['year']}")
        st.write(f"Average Rating: {entered_movie['average_rating']}")
        st.write(f"Common Genres: {entered_movie['common_genres']}")
        st.write(f"Description: {entered_movie['description']}")
        st.write("---")
        
        # Display recommended movies
        st.subheader("4 Recommended Similar Movies:")
        recommended_movies = [
            {
                "title": "Up",
                "year": 2009,
                "average_rating": 3.96,
                "common_genres": 1,
                "description": "Up (2009) is a heartwarming Pixar animated film about Carl, a widowed balloon salesman, who fulfills his late wife's dream by flying their house to Paradise Falls. Accompanied by Russell, a spirited young scout, they embark on an adventure filled with friendship, danger, and discovery, learning the value of new beginnings."
            },
            {
                "title": "How to Train Your Dragon",
                "year": 2010,
                "average_rating": 3.91,
                "common_genres": 1,
                "description": "How to Train Your Dragon (2010) is a DreamWorks animated film about Hiccup, a young Viking who befriends a feared dragon, Toothless. Challenging his village's dragon-hunting traditions, Hiccup discovers the true nature of dragons. Together, they embark on a journey of friendship, courage, and understanding that transforms their world."
            },
            {
                "title": "Inside Out",
                "year": 2015,
                "average_rating": 3.93,
                "common_genres": 1,
                "description": "Inside Out (2015) is a Pixar animated film exploring the emotions inside 11-year-old Riley's mind—Joy, Sadness, Anger, Fear, and Disgust. As Riley faces a challenging move, Joy and Sadness embark on a journey to restore balance. The film highlights the importance of embracing all emotions for growth and understanding."
            },
            {
                "title": "Toy Story 3",
                "year": 2010,
                "average_rating": 3.86,
                "common_genres": 1,
                "description": "Toy Story 3 (2010) follows Woody, Buzz, and the gang as they face an uncertain future when their owner, Andy, leaves for college. Accidentally donated to a daycare, they encounter new challenges and form unexpected alliances. The heartwarming Pixar film explores themes of loyalty, change, and the power of friendship."
            }
        ]
        
        for movie in recommended_movies:
            st.markdown(f"**{movie['title']}**")
            st.write(f"Year: {movie['year']}")
            st.write(f"Average Rating: {movie['average_rating']}")
            st.write(f"Common Genres: {movie['common_genres']}")
            st.write(f"Description: {movie['description']}")
            st.write("---")
    else:
        st.write("No recommendations available for the entered movie.")
