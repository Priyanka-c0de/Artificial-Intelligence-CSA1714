import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-item rating matrix
data = {
    "Movie A": [5, 4, 0, 2, 5],
    "Movie B": [4, 5, 0, 3, 4],
    "Movie C": [0, 2, 5, 4, 0],
    "Movie D": [2, 0, 4, 5, 2],
    "Movie E": [5, 4, 0, 3, 5]
}

users = ["User 1", "User 2", "User 3", "User 4", "User 5"]

ratings = pd.DataFrame(data, index=users)

print("Rating Matrix:")
print(ratings)

# Calculate similarity between users
similarity = cosine_similarity(ratings)

similarity_df = pd.DataFrame(
    similarity,
    index=users,
    columns=users
)

print("\nUser Similarity:")
print(similarity_df.round(2))

# Select target user
target_user = "User 1"

# Find most similar user
similar_users = similarity_df[target_user].sort_values(
    ascending=False
)

most_similar_user = similar_users.index[1]

print("\nTarget User:", target_user)
print("Most Similar User:", most_similar_user)

# Movies liked by similar user
target_ratings = ratings.loc[target_user]
similar_user_ratings = ratings.loc[most_similar_user]

recommendations = similar_user_ratings[
    (similar_user_ratings > 0) &
    (target_ratings == 0)
]

print("\nRecommended Movies:")
print(recommendations.index.tolist())