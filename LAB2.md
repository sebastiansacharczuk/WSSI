<details><summary>Zadanie 1</summary>
    <ul>
        <details>
            <summary>Treść</summary>
            <img src="https://github.com/sebastiansacharczuk/WSSI/assets/88279205/53b7d687-dd3e-4acf-9ea9-f924b6e94ac8" alt="Image">
        </details>
        <details><summary>Odpowiedź</summary> 
        <details><summary>1.1</summary>
          <ul>
            <p>A. Osoby X i Y sa rodzenstwem</p>
            <p>B. Osoby X i Y sa kuzynami</p>
            <p>C. Osoby X i Y sa dziadkami tego samego wnuczka/wnuczke</p>
            <p>D. Osoba Y jest przybranym rodzicem (np. ojczymem) dla osoby X</p>
            <p>E. Osoby X i Y sa dla siebie rodzenstwem przyrodnim</p>
            <p>F. Osoba X ma dziecko z rodzenstwem osoby Y</p>
            <p>G.Osoba X jest jednoczenstwie rodzenstwem i wujkiem/ciocia dla osoby Y</p>
          </ul>
        </details>
        <details><summary>1.2</summary>
          <p>1.2odp</p>
        </details>  
        </details>
    </ul>
</details>


<details><summary>Zadanie 2</summary>
    <ul>
        <details><summary>Treść</summary>
          <img src="https://github.com/sebastiansacharczuk/WSSI/assets/88279205/2e955530-ee1d-4249-aafe-431a58640a40" alt="Image">
        </details>
        <details><summary>Odpowiedź</summary> 
          <ul>
            <p>1. kobieta(X) :- \+ mezczyzna(X).</p>
            <p>2. ojciec(X,Y) :- rodzic(X, Y), mezczyzna(X).</p>
            <p>3. matka(X,Y) :- rodzic(X, Y), kobieta(X).</p>
            <p>4. corka(X,Y) :- rodzic(Y, X), kobieta(X).</p>
            <p>
                5. brat_rodzony(X,Y) :-<br />
                mezczyzna(X),<br />
                rodzic(Z, X), rodzic(Z, Y),<br />
                rodzic(W, X), rodzic(W, Y),<br />
                X \= Y, W \= Z.
            </p>
            <p>
                6. brat_przyrodni(X,Y) :-<br />
    mezczyzna(X),<br />
    rodzic(Z, X), rodzic(Z, Y),<br />
    rodzic(W, X), rodzic(V, Y),<br />
    X \= Y, W \= V, W \= Z, V \= Z.
            </p>
            <p>
                7. kuzyn(X, Y) :-<br />
                rodzic(Z, X),<br />
                rodzic(W, Y),<br />
                rodzic(L, Z), rodzic(L, W),<br />
                rodzic(M, Z), rodzic(M, W),<br />
                Z \= W, L \= M.
            </p>
            <p>
                8. dziadek_od_strony_ojca(X, Y) :-<br />
                rodzic(X, Z), rodzic(Z, Y),<br />
                mezczyzna(X), mezczyzna(Z).
            </p>
            <p>
                9. dziadek_od_strony_matki(X, Y) :-<br />
                rodzic(X, Z), rodzic(Z, Y),<br />
                mezczyzna(X), kobieta(Z).
            </p>
            <p>
                10. dziadek(X, Y) :-<br />
                mezczyzna(X),<br />
                rodzic(X, Z),<br />
                rodzic(Z, Y).
            </p>
            <p>
                11. babcia(X, Y) :-<br />
                kobieta(X),<br />
                rodzic(X, Z),<br />
                rodzic(Z, Y).
            </p>
            <p>
                12. wnuczka(X, Y) :-<br />
                (babcia(Y, X);dziadek(Y, X)),<br />
                kobieta(X).
            </p>
            <p>
                13. przodek_do2pokolenia_wstecz(X,Y) :-<br />
                rodzic(X, Y);<br />
                (rodzic(X, Z), rodzic(Z, Y)).</p>
            <p>
                14. przodek_do3pokolenia_wstecz(X,Y) :-<br />
                rodzic(X, Y);<br />
                (rodzic(X, Z), rodzic(Z, Y));<br />
                (rodzic(X, Z), rodzic(Z, W), rodzic(W, Y)).
            </p>  
          </ul>
        </details>
    </ul>
</details>
