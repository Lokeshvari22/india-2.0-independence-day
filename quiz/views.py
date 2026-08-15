from django.shortcuts import render, redirect

from .models import Question


def quiz(request):

    questions = Question.objects.all()

    if request.method == "POST":

        score = 0
        answers = {}

        for question in questions:

            answer = request.POST.get(
                f"question_{question.id}"
            )

            answers[str(question.id)] = answer

            if answer == question.correct_answer:
                score += 1

        request.session["quiz_score"] = score

        request.session["quiz_total"] = questions.count()

        request.session["quiz_answers"] = answers

        return redirect("quiz:result")

    return render(
        request,
        "quiz/quiz.html",
        {
            "questions": questions
        }
    )


def result(request):

    score = request.session.get(
        "quiz_score",
        0
    )

    total = request.session.get(
        "quiz_total",
        0
    )

    answers = request.session.get(
        "quiz_answers",
        {}
    )

    questions = Question.objects.all()

    results = []

    for question in questions:

        user_answer = answers.get(
            str(question.id)
        )

        results.append({
            "question": question,
            "user_answer": user_answer,
            "correct": (
                user_answer
                == question.correct_answer
            ),
        })

    percentage = 0

    if total > 0:
        percentage = round(
            (score / total) * 100
        )

    return render(
        request,
        "quiz/result.html",
        {
            "score": score,
            "total": total,
            "percentage": percentage,
            "results": results,
        }
    )


def restart(request):

    request.session.pop(
        "quiz_score",
        None
    )

    request.session.pop(
        "quiz_total",
        None
    )

    request.session.pop(
        "quiz_answers",
        None
    )

    return redirect("quiz:quiz")