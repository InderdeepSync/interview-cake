
def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0 for _ in range(0, highest_possible_score + 1)]

    for score in unsorted_scores:
        score_counts[score] += 1


    # Sort the scores in O(n) time
    result = []
    for score, count in enumerate(score_counts):
        result[0:0] = [score] * count


    return result


if __name__ == "__main__":
    print(sort_scores([37, 89, 41, 65, 91, 53], 100))
