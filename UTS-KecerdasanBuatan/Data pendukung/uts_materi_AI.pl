diagnosis(kekurangan_nutrisi) :-
    daun_menguning(yes),
    bercak_hitam(no),
    tanaman_layu(no).

diagnosis(busuk_akar) :-
    daun_menguning(no),
    tanaman_layu(yes),
    bercak_hitam(yes).

diagnosis(serangan_ulat) :-
    daun_berlubang(yes),
    daun_menguning(no).

diagnosis(bintik_daun) :-
    bercak_hitam(yes),
    daun_menguning(yes),
    daun_berlubang(no).

diagnosis(thrips) :-
    daun_menguning(yes),
    daun_berlubang(yes),
    tanaman_layu(no).

diagnosis(sehat) :-
    daun_menguning(no),
    tanaman_layu(no),
    daun_berlubang(no),
    bercak_hitam(no).

diagnosis(unknown) :-
    \+ diagnosis(kekurangan_nutrisi),
    \+ diagnosis(busuk_akar),
    \+ diagnosis(serangan_ulat),
    \+ diagnosis(bintik_daun),
    \+ diagnosis(thrips),
    \+ diagnosis(sehat).

