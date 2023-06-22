from googletrans import Translator

tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Onajon men sizni judayam yaxshi ko'raman"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)


tarjima_ru = tarjimon.translate(matn_uz, dest="turkish")
print(tarjima_ru.text)
