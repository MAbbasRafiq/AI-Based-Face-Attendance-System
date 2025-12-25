import numpy as np

def find_best_match(live_embedding, known_encodings, known_names, threshold=1.2):
    distances = np.linalg.norm(
        np.array(known_encodings) - np.array(live_embedding),
        axis=1
    )

    min_index = np.argmin(distances)
    min_distance = distances[min_index]

    if min_distance < threshold:
        return known_names[min_index], min_distance
    else:
        return "Unknown", min_distance
