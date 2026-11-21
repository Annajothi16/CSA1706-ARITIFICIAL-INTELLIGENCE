
% BACKWARD CHAINING - DENGUE FEVER

% Patient details (known facts)

ns1_test(patient1, negative).

fever(patient1).
headache(patient1).
rash(patient1).

platelets(patient1, 85000).

% Rule R1:
% If NS1 test is positive, patient has Dengue Fever

dengue_fever(Patient) :-
    ns1_test(Patient, positive).

% Rule R2:
% If fever, headache, rash and platelet count
% is less than 100000, patient has Dengue Fever

dengue_fever(Patient) :-
    fever(Patient),
    headache(Patient),
    rash(Patient),
    platelets(Patient, Count),
    Count < 100000.

% Backward chaining goal
check_dengue(Patient) :-
    dengue_fever(Patient),
    write('Patient has Dengue Fever.'), nl.

check_dengue(Patient) :-
    \+ dengue_fever(Patient),
    write('Dengue Fever is not proved.'), nl.
