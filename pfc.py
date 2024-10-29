import random

pfc_condition_win = {
    "pierre": {"pierre": 0, "feuille": -1, "ciseaux": 1},
    "feuille": {"pierre": 1, "feuille": 0, "ciseaux": -1},
    "ciseaux": {"pierre": -1, "feuille": 1, "ciseaux": 0},
}


def pfc():
    input("Appuyez sur une touche pour commencer")
    print("Pierre, Feuille, Ciseaux")
    print("1. Pierre")
    print("2. Feuille")
    print("3. Ciseaux")

    player = int(input("Votre choix: ")) - 1

    ia_choice = random.randint(0, 2)

    if (
        pfc_condition_win[list(pfc_condition_win.keys())[player]][
            list(pfc_condition_win.keys())[ia_choice]
        ]
        == 1
    ):
        print("Vous avez gagné")
        print("L'ordinateur a choisi", list(pfc_condition_win.keys())[ia_choice])
        return

    if (
        pfc_condition_win[list(pfc_condition_win.keys())[player]][
            list(pfc_condition_win.keys())[ia_choice]
        ]
        == -1
    ):
        print("Vous avez perdu")
        print("L'ordinateur a choisi", list(pfc_condition_win.keys())[ia_choice])
        return

    print("Égalité")
    print("L'ordinateur a choisi", list(pfc_condition_win.keys())[ia_choice])
    return


if __name__ == "__main__":
    pfc()
