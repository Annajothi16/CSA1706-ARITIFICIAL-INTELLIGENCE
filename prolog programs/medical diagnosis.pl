symptom(fever, flu).
symptom(cough, flu).
symptom(body_pain, flu).

symptom(sneezing, cold).
symptom(runny_nose, cold).

symptom(thirst, diabetes).
symptom(frequent_urination, diabetes).

has_symptom(ravi, fever).
has_symptom(ravi, cough).
has_symptom(ravi, body_pain).

has_symptom(anu, sneezing).
has_symptom(anu, runny_nose).

diagnosis(X, flu) :-
    has_symptom(X, fever),
    has_symptom(X, cough),
    has_symptom(X, body_pain).

diagnosis(X, cold) :-
    has_symptom(X, sneezing),
    has_symptom(X, runny_nose).

diagnosis(X, diabetes) :-
    has_symptom(X, thirst),
    has_symptom(X, frequent_urination).