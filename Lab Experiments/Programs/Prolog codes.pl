
/*Sum of Integers*/
sum(0, 0).
sum(N, S) :-
    N > 0,
    N1 is N - 1,
    sum(N1, S1),
    S is S1 + N.

:- initialization(main).

main :-
    sum(5, S),
    write('The sum is :'),
    write(S),
    nl.
   

/*DB fro Name and DOB*/
 % --- Database: name(Name, DOB) ---
 % DOB format: dd-mm-yyyy

 name("Priyanka", "21-03-2003").
 name("Arjun",     "10-11-1999").
 name("Neha",      "05-07-2001").
 name("Rahul",     "18-01-1998").

 % --- Query 1: Find DOB by Name ---
 dob_by_name(Name, DOB) :-
     name(Name, DOB).

     % --- Query 2: Find Name by DOB ---
     name_by_dob(DOB, Name) :-
         name(Name, DOB).

         % --- Query 3: List all records ---
         all_records :-
             forall(name(Name, DOB),
                        (write('Name: '), write(Name),
                                    write(', DOB: '), write(DOB), nl)).   

                                    
                                       
