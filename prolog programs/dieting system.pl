disease(fever).
disease(diabetes).
disease(high_bp).
disease(cold).

diet(fever, 'Drink plenty of water').
diet(diabetes, 'Eat high fibre foods').
diet(high_bp, 'Eat low salt foods').
diet(cold, 'Drink warm fluids').

suggest_diet(D, Advice) :-
    disease(D),
    diet(D, Advice).