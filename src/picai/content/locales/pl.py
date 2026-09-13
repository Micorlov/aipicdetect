"""Polish translation table.

Falls back to English (see :func:`picai.content.locales.t`) for any key not defined here, but
every key from :mod:`picai.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "picai — otwarty detektor obrazów AI i narzędzie do czyszczenia metadanych",
    "page.home.description": (
        "Sprawdź, czy zdjęcie zostało wygenerowane przez AI, korzystając z picai — darmowego "
        "detektora typu open source. Użyj go w przeglądarce albo uruchom na własnym komputerze za "
        "pomocą Dockera lub Pythona."
    ),
    "page.home.h1": "Czy to zdjęcie jest prawdziwe? Poznaj wynik i dowód.",
    "page.faq.title": "FAQ o detektorze obrazów AI: dokładność, prywatność, formaty, modele",
    "page.faq.description": (
        "Odpowiedzi na najczęstsze pytania o picai: jak dokładne jest wykrywanie obrazów AI, gdzie "
        "przetwarzane jest Twoje zdjęcie, jakie formaty są obsługiwane, jak zmienić model i jakie "
        "obowiązują limity zapytań."
    ),
    "page.faq.h1": "Najczęściej zadawane pytania o picai",
    "page.faq.intro_suffix": (
        "To pytania, które ludzie zadają najczęściej: jak to działa, jak dokładne jest wykrywanie i "
        "co dzieje się z przesyłanymi zdjęciami."
    ),
    "page.faq.still_unsure_html": (
        'Nadal nie masz pewności? Zgłoś problem na <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHubie</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "picai to darmowe narzędzie open source, które ocenia prawdopodobieństwo, że obraz został "
        "wygenerowany przez AI, i usuwa ukryte metadane — w wersji hostowanej lub self-hosted, "
        "wybór należy do Ciebie."
    ),
    "home.lead": (
        "picai uruchamia otwarty model wykrywania AI i odczytuje każde pole EXIF, C2PA i IPTC, jakie "
        "niesie ze sobą zdjęcie — a następnie oddaje Ci czystą kopię, z której wszystko to zostało "
        "usunięte. Bez rejestracji, bez czarnej skrzynki."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · do 50 MB · przetwarzane w pamięci, nigdy nie zapisywane na dysku"
    ),
    "home.summary": (
        "picai to darmowe narzędzie open source, które ocenia prawdopodobieństwo, że obraz został "
        "wygenerowany przez AI, i usuwa ukryte metadane — w wersji hostowanej lub self-hosted, wybór "
        "należy do Ciebie. Ocenia prawdopodobieństwo, że zdjęcie zostało wytworzone przez generator "
        "AI, korzystając z otwartego klasyfikatora Hugging Face, i potrafi ponownie wyrenderować "
        "obraz, aby usunąć metadane EXIF, XMP, IPTC, ICC i C2PA. Skorzystaj z instancji hostowanej "
        "albo uruchom picai samodzielnie za pomocą Dockera lub Pythona."
    ),
    "home.stat.0": "otwarty model,<br>bez API stron trzecich",
    "home.stat.1": "rejestracji<br>wymaganych",
    "home.stat.2": "MB<br>limit przesyłania",
    # Detect steps
    "steps.detect.upload.name": "Prześlij.",
    "steps.detect.upload.text": (
        "Przeciągnij, wklej lub wybierz zdjęcie. Zostaje ono wysłane do serwera picai, z którego "
        "korzystasz (czyli na Twój własny komputer w wersji self-hosted), przechowywane w pamięci i "
        "nigdy nie zapisywane na dysku."
    ),
    "steps.detect.detect.name": "Wykryj.",
    "steps.detect.detect.text": (
        "Klasyfikator obrazów typu open source ocenia prawdopodobieństwo, że piksele zostały "
        "wytworzone przez generator."
    ),
    "steps.detect.decide.name": "Zdecyduj.",
    "steps.detect.decide.text": (
        "Otrzymujesz prawdopodobieństwo wygenerowania przez AI, przedział pewności oraz bloki "
        "metadanych, jakie niesie plik — jako prawdopodobieństwo, a nie werdykt."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Sprawdź.",
    "steps.scrub.inspect.text": (
        "Uruchom <code>picai inspect photo.jpg</code>, aby wyświetlić listę bloków EXIF, XMP, IPTC, "
        "C2PA i ICC, jakie niesie plik."
    ),
    "steps.scrub.scrub.name": "Wyczyść.",
    "steps.scrub.scrub.text": (
        "Uruchom <code>picai scrub photo.jpg</code> (lub <code>POST /scrub</code>). picai dekoduje "
        "piksele, stosuje orientację EXIF i buduje zupełnie nowy obraz z surowego bufora pikseli."
    ),
    "steps.scrub.verify.name": "Zweryfikuj.",
    "steps.scrub.verify.text": (
        "Uruchom <code>picai inspect photo.clean.jpg</code>; powinno wypisać „no metadata signatures "
        "found”."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Jak dokładny jest ten detektor?",
    "faq.accuracy.answer_html": (
        "Podaje prawdopodobieństwo, a nie werdykt. Wyniki bliskie 50% są oznaczane jako "
        "<em>Niepewne</em>; traktuj każdy pojedynczy wynik jako sygnał i łącz go z innymi dowodami. "
        'Więcej informacji znajdziesz na stronie <a href="/how-accurate">o dokładności detektorów '
        "obrazów AI</a>."
    ),
    "faq.leaves_computer.question": "Czy moje zdjęcie opuszcza mój komputer?",
    "faq.leaves_computer.answer_html": (
        "W tej publicznej instancji — tak: zdjęcie jest przesyłane na serwer picai (kontener Google "
        "Cloud Run prowadzony przez autora), oceniane w pamięci i nigdy nie zapisywane na dysku. "
        "Wyczyszczona kopia jest przechowywana w pamięci tylko do czasu, aż zastąpi ją 100 nowszych "
        "wyników albo kontener zostanie zrestartowany, i nic nie jest wysyłane do żadnego "
        'zewnętrznego API. Jeśli chcesz, żeby nic nie opuszczało Twojego komputera, '
        '<a href="/self-host">uruchom picai samodzielnie</a> za pomocą jednej komendy Dockera. '
        'Szczegóły znajdziesz na <a href="/privacy">stronie o prywatności</a>.'
    ),
    "faq.open_source.question": "Czy to projekt open source?",
    "faq.open_source.answer_html": (
        "Tak. Kod, obraz Dockera, CLI oraz GitHub Action znajdują się w "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">repozytorium picai</a> na '
        "licencji MIT. Detektor to otwarty model Hugging Face, który możesz sprawdzić lub zastąpić."
    ),
    "faq.remove_metadata.question": "Czy mogę usunąć C2PA i inne metadane?",
    "faq.remove_metadata.answer_html": (
        "Tak. Po sprawdzeniu zdjęcia użyj opcji <em>Pobierz czystą kopię</em>. picai odbudowuje "
        "obraz z jego pikseli, dzięki czemu EXIF, XMP, IPTC, C2PA i profil ICC zostają w całości "
        'pominięte. <a href="/remove-image-metadata">Jak działa czyszczenie</a>.'
    ),
    "faq.formats.question": "Jakie formaty są obsługiwane?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF oraz większość formatów, które potrafi zdekodować Pillow, o "
        "rozmiarze do 50 MB."
    ),
    "faq.why_metadata.question": "Dlaczego wyświetlane są metadane?",
    "faq.why_metadata.answer_html": (
        "Poświadczenia treści C2PA i znaczniki oprogramowania edycyjnego to wskazówki dotyczące "
        "pochodzenia pliku. Panel pokazuje, które bloki (EXIF, XMP, IPTC, C2PA, ICC) niesie plik, "
        'dzięki czemu możesz uwzględnić je obok wyniku. Zobacz <a href="/c2pa">poświadczenia treści '
        'C2PA</a> oraz <a href="/remove-image-metadata">jak usunąć metadane obrazu</a>.'
    ),
    "faq.different_model.question": "Czy mogę użyć innego modelu?",
    "faq.different_model.answer_html": (
        "Tak. Ustaw <code>PICAI_DETECTOR_MODEL</code> na dowolny model klasyfikacji obrazów z "
        "Hugging Face, którego etykiety rozróżniają treść AI/fałszywą od ludzkiej/prawdziwej."
    ),
    # FAQ (more slugs)
    "faq.free.question": "Czy picai jest darmowe?",
    "faq.free.answer_html": (
        "Tak. picai jest projektem open source na licencji MIT. Instancja hostowana jest darmowa w "
        "użyciu, z limitem 10 analiz na adres IP co 24 godziny; kopia self-hosted nie ma żadnego "
        "limitu."
    ),
    "faq.screenshots.question": "Czy działa na zrzutach ekranu lub mocno skompresowanych obrazach?",
    "faq.screenshots.answer_html": (
        "Działa, ale ponowne kodowanie, zmiana rozmiaru i zrzuty ekranu usuwają część śladów na "
        "poziomie pikseli, na których opiera się klasyfikator, więc spodziewaj się niższej pewności "
        "i większej liczby wyników <em>Niepewne</em>."
    ),
    "faq.which_generator.question": (
        "Czy potrafi rozpoznać, który generator stworzył obraz (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Nie. picai ocenia ogólne statystyki pikseli w podziale na wygenerowane i rzeczywiste; nie "
        "identyfikuje konkretnego generatora i nie ma wiedzy o generatorach wydanych po zebraniu "
        "danych treningowych jego modelu."
    ),
    "faq.false_positive.question": "Dlaczego prawdziwe zdjęcie zostało ocenione jako AI?",
    "faq.false_positive.answer_html": (
        "Mocne filtry, przetwarzanie HDR, powiększanie rozdzielczości (upscaling), ilustracje i "
        "renderingi 3D mają cechy statystyczne wspólne z obrazami wygenerowanymi. Wynik to "
        "prawdopodobieństwo, a nie dowód; fałszywe alarmy się zdarzają."
    ),
    "faq.offline.question": "Czy mogę uruchomić to offline?",
    "faq.offline.answer_html": (
        "Tak. Po tym, jak pierwsze uruchomienie pobierze model do pamięci podręcznej Hugging Face, "
        "self-hosted picai nie potrzebuje już dostępu do sieci."
    ),
    "faq.rate_limit.question": "Czy instancja hostowana ma limit zapytań?",
    "faq.rate_limit.answer_html": (
        "Tak: 10 analiz na IP klienta w dowolnym kroczącym 24-godzinnym oknie czasowym. Odpowiedzi "
        "zawierają nagłówek <code>X-RateLimit-Remaining</code>, a zapytanie przekraczające limit "
        "zwraca kod 429 z nagłówkiem <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Detektor",
    "nav.how_it_works": "Jak to działa",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Poradnik",
    "nav.api": "API",
    "nav.self-host": "Self-hosting",
    # Footer
    "footer.remove-image-metadata": "Usuwanie metadanych",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Prywatność",
    "footer.self-host": "Self-hosting",
    "footer.about": "O projekcie",
    # UI strings
    "ui.nav_aria_label": "Główna nawigacja",
    "ui.loading_status": "Ładowanie detektora…",
    "ui.hero_overline": "— Kryminalistyka obrazów AI typu open source",
    "ui.hero_heading_line1": "Czy to zdjęcie jest prawdziwe?",
    "ui.hero_heading_line2": "Poznaj wynik i dowód.",
    "ui.tool_aria_label": "Detektor obrazów AI",
    "ui.dropzone_aria_label": "Prześlij obraz do analizy",
    "ui.dropzone_title_fine": "Przeciągnij i upuść zdjęcie",
    "ui.dropzone_title_coarse": "Sprawdź zdjęcie",
    "ui.dropzone_sub_fine": "lub wklej ze schowka, albo",
    "ui.dropzone_sub_coarse": "z galerii lub aparatu",
    "ui.btn_check_image_fine": "Sprawdź ten obraz",
    "ui.btn_choose_photo_coarse": "Wybierz zdjęcie",
    "ui.btn_take_photo": "Zrób zdjęcie",
    "ui.dismiss_aria_label": "Zamknij",
    "ui.analyzing_prefix": "Analiza",
    "ui.analyzing_suffix": "· piksele · bloki metadanych",
    "ui.verdict_overline": "— Wynik",
    "ui.meter_real": "Prawdziwe",
    "ui.meter_uncertain": "Niepewne",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Wyniki to prawdopodobieństwa podawane przez klasyfikator, a nie werdykty. "
        '<a href="/how-accurate">Jak czytać wynik.</a>'
    ),
    "ui.btn_check_another": "Sprawdź inny obraz",
    "ui.preview_overline": "— Podgląd",
    "ui.preview_alt": "Podgląd przesłanego obrazu",
    "ui.metadata_overline": "— Metadane",
    "ui.metadata_heading": "Znalezione w pliku.",
    "ui.jpeg_segments_label": "Segmenty JPEG",
    "ui.btn_download_clean": "Pobierz czystą kopię",
    "ui.metadata_scrub_note_html": (
        "Odtworzone na nowo z pikseli, więc każdy z powyższych bloków zniknął. "
        '<a href="/remove-image-metadata">Jak to działa</a>'
    ),
    "ui.how_it_works_overline": "— Jak to działa",
    "ui.how_it_works_heading": "Trzy kroki. Nic nie jest zapisywane.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Przeczytaj poradnik o rozpoznawaniu '
        'obrazów AI</a> albo <a href="/self-host">uruchom go na własnym komputerze</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Zanim zapytasz.",
    "ui.faq_more_link": "Więcej pytań i odpowiedzi →",
    "ui.footer_tagline": "picai. · open source",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Ścieżka nawigacji",
    "ui.last_updated_prefix": "Ostatnia aktualizacja",
    "ui.source_on_github": "kod źródłowy na GitHubie",
    "ui.btn_try_detector": "Wypróbuj detektor",
    "ui.status_ready": "Detektor gotowy",
    "ui.status_unreachable": "Serwer niedostępny",
    "ui.loading_model_note": "Ładowanie modelu detektora (pierwsze uruchomienie pobiera ok. 750 MB)…",
    "ui.error_empty_file": "Ten plik jest pusty.",
    "ui.error_file_too_large": "{name} ma rozmiar {size} — limit wynosi 50 MB.",
    "ui.error_server_unreachable": "Nie udało się połączyć z serwerem: {message}",
    "ui.verdict_ai": "Prawdopodobnie wygenerowane przez AI",
    "ui.verdict_real": "Prawdopodobnie prawdziwe zdjęcie",
    "ui.verdict_uncertain": "Niepewne",
    "ui.confidence_suffix": "pewności",
    "ui.format_unknown": "nieznany",
    "ui.metadata_present": "Obecne",
    "ui.metadata_not_present": "Nieobecne",
    "ui.no_jpeg_segments": "Brak segmentów JPEG APP",
    "ui.quota_remaining": "Pozostało {remaining} z {limit} analiz na dziś",
}
