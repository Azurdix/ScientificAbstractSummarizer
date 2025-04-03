# -*- coding: utf-8 -*-
"""MG_StreszczaczAbstraktowNaukowych.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ebd0PlD1zslqfOqLpkm3nJ_JnWR45Xro
"""

# 1) Pobranie i instalacja niezbędnych zasobów do NLTK
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# --- ALGORYTM PODSUMOWUJĄCY ABSTRAKTY NAUKOWE BY MATEUSZ GLENSZCZYK ---

def summarize_text(text, num_sentences=3):
    """
    Funkcja, która podsumowuje tekst wybierając 'num_sentences' najważniejszych zdań.
    Można ustalać dowolnie, ja ustawiłem trzy. Przy zmianie PROSZĘ PAMIĘTAĆ, że
    trzeba też na dole przy Summary zmienić na taką samą liczbę.
    Abstrakt pochodzi z mojej osobistej publikacji naukowej, dla łatwiejszej werfyikacji.
    Metodą jest obliczenie częstotliwości występowania słów (pomijając tzw. stop words) i wybranie zdań z największym wynikiem.
    """
    # Podział tekstu na zdania
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text  # Jeśli tekst jest bardzo krótki, zwracamy cały tekst

    # Przygotowanie zbioru stop words i znaków interpunkcyjnych
    stop_words = set(stopwords.words("english"))
    punctuation = set(string.punctuation)

    # Obliczanie częstotliwości występowania słów w tekście
    word_frequencies = {}
    for word in word_tokenize(text.lower()):
        if word in stop_words or word in punctuation:
            continue
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

    # Obliczenie punktacji dla każdego zdania
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        words = word_tokenize(sentence.lower())
        score = 0
        for word in words:
            if word in word_frequencies:
                score += word_frequencies[word]
        sentence_scores[i] = score

    # Wybranie indeksów zdań o najwyższych punktacjach
    top_sentence_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    # Sortowanie indeksów aby zachować oryginalną kolejność
    top_sentence_indices.sort()

    # Składamy podsumowanie
    summary = " ".join([sentences[i] for i in top_sentence_indices])
    return summary

# Funkcja podsumowująca (To tutaj wklejamy Abstrakt):
abstract_text = (
    "Examining the role of color in mate choice without testing what colors the study animal is capable of seeing can lead to ill-posed hypotheses and erroneous conclusions. Here, we test the seemingly reasonable assumption that the sexually dimorphic red coloration of the male jumping spider Saitis barbipes is distinguishable, by females, from adjacent black color patches. Using microspectrophotometry, we find clear evidence for photoreceptor classes with maximal sensitivity in the UV (359 nm) and green (526 nm), inconclusive evidence for a photoreceptor maximally sensitive in the blue (451 nm), and no evidence for a red photoreceptor. No colored filters within the lens or retina could be found to shift green sensitivity to red. To quantify and visualize whether females may nevertheless be capable of discriminating red from black color patches, we take multispectral images of males and calculate photoreceptor excitations and color contrasts between color patches. Red patches would be, at best, barely discriminable from black, and not discriminable from a low-luminance green. Some color patches that appear achromatic to human eyes, such as beige and white, strongly absorb UV wavelengths and would appear as brighter “spider-greens” to S. barbipes than the red color patches. Unexpectedly, we discover an iridescent UV patch that contrasts strongly with the UV-absorbing surfaces dominating the rest of the spider. We propose that red and black coloration may serve identical purposes in sexual signaling, functioning to generate strong achromatic contrast with the visual background. The potential functional significance of red coloration outside of sexual signaling is discussed."
)
print("Original Abstract:\n", abstract_text)
print("\nSummary:\n", summarize_text(abstract_text, num_sentences=3))