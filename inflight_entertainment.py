

def can_two_movies_fill_flight(movie_lengths, flight_length):
    hash_set = set(movie_lengths)

    for length in movie_lengths:
        if length == flight_length / 2:
            return movie_lengths.count(length) >= 2

        if (flight_length - length) in hash_set:
            return True

    return False



if __name__ == "__main__":
    can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)