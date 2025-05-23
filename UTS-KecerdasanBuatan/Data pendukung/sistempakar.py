# -*- coding: utf-8 -*-
"""UTS_Materi_AI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o5G3Qhn_sZ2G3722LGt9YmXgaGYEmTFY
"""

!pip install experta

!pip install --upgrade frozendict

from experta import *

class Diagnosis(KnowledgeEngine):
    @Rule(Fact(daun_menguning=True) & Fact(bercak_hitam=False) & Fact(tanaman_layu=False))
    def penyakit_kekurangan_nutrisi(self):
        print("Sepertinya tanaman anda mengalami kekurangan nutrisi.")

    @Rule(Fact(daun_menguning=False) & Fact(tanaman_layu=True) & Fact(bercak_hitam=True))
    def penyakit_busuk_akar(self):
        print("Sepertinya tanaman anda mengalami busuk akar.")

    @Rule(Fact(daun_berlubang=True) & Fact(daun_menguning=False))
    def hama_serangan_ulat(self):
        print("Tanaman anda mungkin diserang ulat pemakan daun.")

    @Rule(Fact(bercak_hitam=True) & Fact(daun_menguning=True) & Fact(daun_berlubang=False))
    def penyakit_bintik_daun(self):
        print("Tanaman anda mungkin terkena penyakit bintik daun.")

    @Rule(Fact(daun_menguning=True) & Fact(daun_berlubang=True) & Fact(tanaman_layu=False))
    def hama_thrips(self):
        print("Tanaman anda kemungkinan besar diserang thrips.")

    @Rule(Fact(daun_menguning=False) & Fact(tanaman_layu=False) & Fact(daun_berlubang=False) & Fact(bercak_hitam=False))
    def sehat(self):
        print("Tanaman anda sehat!")

    @Rule(AS.f << Fact(), salience=-10)
    def default_diagnosis(self):
        print("Gejala yang terdeteksi tidak cocok dengan data yang ada. Silakan periksa kembali atau konsultasikan lebih lanjut.")

def get_input():
    """Helper function to get user input as boolean (yes/no)."""
    def ask_question(question):
        return input(question + "(yes/no): ").strip().lower() == "yes"

    return {
        "bercak_hitam": ask_question("Apakah tanaman anda memiliki bercak hitam?"),
        "daun_menguning": ask_question("Apakah tanaman anda daunnya tampak menguning?"),
        "daun_berlubang": ask_question("Apakah tanaman anda memiliki daun berlubang?"),
        "tanaman_layu": ask_question("Apakah tanaman anda layu?")
    }

if __name__ == "__main__":
    symptoms = get_input()
    engine = Diagnosis()
    engine.reset()

    for symptom, present in symptoms.items():
        engine.declare(Fact(**{symptom: present}))

    engine.run()