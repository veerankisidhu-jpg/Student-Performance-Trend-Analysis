        return "Average"
    else:
        return "Needs Improvement"


def get_subject_scores(student_scores, subject_index):
    """Collect one subject's scores across all examinations."""
    scores = []
    for exam_scores in student_scores:
        scores.append(exam_scores[subject_index])
    return scores


def analyze_student(student):
    name = student[0]
    exam_scores = student[1]

    print("\n" + "=" * 60)
    print("Student:", name)
    print("-" * 60)

    exam_averages = []
    for index in range(len(exam_scores)):
        exam_average = average(exam_scores[index])
        exam_averages.append(exam_average)
        print(f"{EXAM_NAMES[index]} average: {exam_average:.2f}%")

    improvement = exam_averages[-1] - exam_averages[0]
    if improvement > 0:
        print(f"Overall trend: Improved by {improvement:.2f} percentage points")
    elif improvement < 0:
        print(f"Overall trend: Declined by {abs(improvement):.2f} percentage points")
    else:
        print("Overall trend: No change")

    overall_average = average(exam_averages)
    print(f"Overall average: {overall_average:.2f}%")
    print("Classification:", classify_student(overall_average))

    print("\nSubject trends:")
    weak_subjects = []

    for subject_index in range(len(SUBJECTS)):
        scores = get_subject_scores(exam_scores, subject_index)
        subject_average = average(scores)
        change = scores[-1] - scores[0]

        if change > 0:
            trend = f"Improved by {change} marks"
        elif change < 0:
            trend = f"Declined by {abs(change)} marks"
        else:
            trend = "No change"

        print(f"  {SUBJECTS[subject_index]}: {scores} | Average: "
              f"{subject_average:.2f} | {trend}")

        # A subject is consistently weak if the score is below 50
        # in at least 2 examinations.
        low_score_count = 0
        for score in scores:
            if score < WEAK_SUBJECT_LIMIT:
                low_score_count += 1

        if low_score_count >= WEAK_EXAM_COUNT:
            weak_subjects.append(SUBJECTS[subject_index])

    if weak_subjects:
        print("Consistently weak subjects:", ", ".join(weak_subjects))
    else:
        print("Consistently weak subjects: None")


def show_class_summary():
    print("\n" + "=" * 60)
    print("CLASS PERFORMANCE SUMMARY")
    print("=" * 60)
    print(f"{'Student':<12}{'Overall Average':<20}{'Classification'}")

    for student in students:
        exam_averages = []
        for exam_scores in student[1]:
            exam_averages.append(average(exam_scores))

        overall_average = average(exam_averages)
        classification = classify_student(overall_average)

        print(f"{student[0]:<12}{overall_average:<20.2f}{classification}")


def main():
    print("STUDENT PERFORMANCE TREND ANALYSIS")
    print("Examinations:", ", ".join(EXAM_NAMES))
    print("Subjects:", ", ".join(SUBJECTS))

    for student in students:
        analyze_student(student)

    show_class_summary()


if __name__ == "__main__":
    main()
