main(Input, OutputA, OutputB) :-
    solve_a(Input, OutputA),
    solve_b(Input, OutputB).

solve_a(Input, Output) :-
    sum_of_rotated_matches(Input, 1, Output).

solve_b(Input, Output) :-
    string_chars(Input, Chars),
    length(Chars, Length),
    Rotation is Length / 2,
    sum_of_rotated_matches(Input, Rotation, Output).

sum_of_rotated_matches(Input, Rotation, Output) :-
    string_chars(Input, Chars),
    maplist(atom_number, Chars, Digits),
    rotate(Digits, Rotation, Rotated),
    sum_of_matches(Digits, Rotated, Output).

rotate(R, 0, R).
rotate([H|T], N, R) :-
    N > 0,
    append(T, [H], S),
    M is N - 1,
    rotate(S, M, R).

sum_of_matches([], [], 0).
sum_of_matches([X|Xs], [X|Ys], Output) :-
    sum_of_matches(Xs, Ys, RestOutput),
    Output is RestOutput + X.
sum_of_matches([X|Xs], [Y|Ys], Output) :-
    X \= Y,
    sum_of_matches(Xs, Ys, Output).