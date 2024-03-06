def rate_performance(score):
    if score > 80:
        return "Distinction"
    elif score >= 60 and score <= 80:
        return "Credit"
    elif score >= 40 and score < 60:
        return "Fair"
    else:
        return "Fail"

def main():
    try:
        score = float(input("Enter student's score: "))
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
        else:
            rating = rate_performance(score)
            print(f"Student's performance: {rating}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the score.")

if __name__ == "__main__":
    main()
