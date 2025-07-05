from sys import argv

def main():
    words_amount = int(argv[1])
    
    words_counts : dict = {}
    file = open('./text.txt', 'r')
    for line in file:
        current_line_words = line.strip().split()
        for word in current_line_words:
            if word in words_counts:
                words_counts[word] += 1
            else:
                words_counts[word] = 1
                
    sorted_words_with_counts = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)
    # sorted_words = [word_and_count[0] for word_and_count in sorted_words_with_counts]
    sorted_words = [word for word, count in sorted_words_with_counts]
    print(sorted_words[:words_amount])


if __name__ == "__main__":
    main()