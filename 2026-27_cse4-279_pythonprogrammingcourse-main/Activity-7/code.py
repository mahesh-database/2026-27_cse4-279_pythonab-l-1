
positive = ["good", "excellent", "helpful",
            "amazing", "wonderful"]

negative = ["bad", "poor", "difficult",
            "boring", "worst"]

n = int(input("Enter number of feedback sentences: "))

for i in range(n):

    feedback = input("\nEnter feedback: ")

    words = feedback.lower().split()

    pos_count = 0
    neg_count = 0

    for word in words:

        word = word.strip(".,!?")

        if word in positive:
            pos_count += 1

        elif word in negative:
            neg_count += 1

    score = pos_count - neg_count

    if score > 0:
        result = "Positive"

    elif score < 0:
        result = "Negative"

    else:
        result = "Neutral"

    print("\n----- FEEDBACK RESULT -----")
    print("Feedback:", feedback)
    print("Positive Keywords:", pos_count)
    print("Negative Keywords:", neg_count)
    print("Sentiment Score:", score)
    print("Classification:", result)

