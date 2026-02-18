import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from decimal import Decimal, getcontext

# ══════════════════════════════════════════════════════════════════════════════
#  SPRACHEN & ÜBERSETZUNGEN
# ══════════════════════════════════════════════════════════════════════════════
LANGUAGES = {
    "🇩🇪  Deutsch":           "de",
    "🇬🇧  English":           "en",
    "🇫🇷  Français":          "fr",
    "🇪🇸  Español":           "es",
    "🇮🇹  Italiano":          "it",
    "🇵🇹  Português":         "pt",
    "🇳🇱  Nederlands":        "nl",
    "🇵🇱  Polski":            "pl",
    "🇷🇺  Русский":           "ru",
    "🇺🇦  Українська":        "uk",
    "🇨🇳  中文 (简体)":        "zh",
    "🇯🇵  日本語":             "ja",
    "🇰🇷  한국어":             "ko",
    "🇸🇦  العربية":           "ar",
    "🇹🇷  Türkçe":            "tr",
    "🇸🇪  Svenska":           "sv",
    "🇳🇴  Norsk":             "no",
    "🇩🇰  Dansk":             "da",
    "🇫🇮  Suomi":             "fi",
    "🇨🇿  Čeština":           "cs",
    "🇷🇴  Română":            "ro",
    "🇭🇺  Magyar":            "hu",
    "🇬🇷  Ελληνικά":          "el",
    "🇮🇳  हिन्दी":             "hi",
    "🇮🇩  Bahasa Indonesia":  "id",
}

TRANSLATIONS = {
    "title": {
        "de":"GigaPi Benchmark","en":"GigaPi Benchmark","fr":"GigaPi Benchmark",
        "es":"GigaPi Benchmark","it":"GigaPi Benchmark","pt":"GigaPi Benchmark",
        "nl":"GigaPi Benchmark","pl":"GigaPi Benchmark","ru":"GigaPi Бенчмарк",
        "uk":"GigaPi Бенчмарк","zh":"GigaPi 基准测试","ja":"GigaPi ベンチマーク",
        "ko":"GigaPi 벤치마크","ar":"GigaPi معيار","tr":"GigaPi Kıyaslama",
        "sv":"GigaPi Benchmark","no":"GigaPi Benchmark","da":"GigaPi Benchmark",
        "fi":"GigaPi Suorituskoe","cs":"GigaPi Benchmark","ro":"GigaPi Benchmark",
        "hu":"GigaPi Teljesítménymérés","el":"GigaPi Αναφορά","hi":"GigaPi बेंचमार्क",
        "id":"GigaPi Tolok Ukur",
    },
    "subtitle": {
        "de":"Pi-Berechnungs-Benchmark  •  Chudnovsky-Algorithmus",
        "en":"Pi Calculation Benchmark  •  Chudnovsky Algorithm",
        "fr":"Benchmark de calcul de Pi  •  Algorithme Chudnovsky",
        "es":"Benchmark de cálculo de Pi  •  Algoritmo Chudnovsky",
        "it":"Benchmark di calcolo di Pi  •  Algoritmo Chudnovsky",
        "pt":"Benchmark de cálculo de Pi  •  Algoritmo Chudnovsky",
        "nl":"Pi-berekeningsbenchmark  •  Chudnovsky-algoritme",
        "pl":"Benchmark obliczania Pi  •  Algorytm Chudnovsky'ego",
        "ru":"Тест вычисления числа Пи  •  Алгоритм Чудновского",
        "uk":"Тест обчислення числа Пі  •  Алгоритм Чудновського",
        "zh":"圆周率计算基准  •  楚德诺夫斯基算法",
        "ja":"円周率計算ベンチマーク  •  チュドノフスキーアルゴリズム",
        "ko":"원주율 계산 벤치마크  •  추드노프스키 알고리즘",
        "ar":"معيار حساب باي  •  خوارزمية تشودنوفسكي",
        "tr":"Pi Hesaplama Kıyası  •  Chudnovsky Algoritması",
        "sv":"Pi-beräkningsbenchmark  •  Chudnovsky-algoritmen",
        "no":"Pi-beregningsbenchmark  •  Chudnovsky-algoritmen",
        "da":"Pi-beregningsbenchmark  •  Chudnovsky-algoritmen",
        "fi":"Pi-laskennan suorituskoe  •  Chudnovsky-algoritmi",
        "cs":"Benchmark výpočtu Pi  •  Chudnovského algoritmus",
        "ro":"Benchmark calcul Pi  •  Algoritmul Chudnovsky",
        "hu":"Pi-számítási teljesítménymérés  •  Chudnovsky-algoritmus",
        "el":"Δοκιμή υπολογισμού Pi  •  Αλγόριθμος Chudnovsky",
        "hi":"पाई गणना बेंचमार्क  •  चुदनोवस्की एल्गोरिदम",
        "id":"Tolok ukur perhitungan Pi  •  Algoritma Chudnovsky",
    },
    "decimal_places": {
        "de":"Nachkommastellen von π:","en":"Decimal places of π:","fr":"Décimales de π:",
        "es":"Decimales de π:","it":"Cifre decimali di π:","pt":"Casas decimais de π:",
        "nl":"Decimalen van π:","pl":"Miejsca po przecinku π:","ru":"Знаков после запятой π:",
        "uk":"Знаків після коми π:","zh":"π 的小数位数:","ja":"πの小数点以下の桁数:",
        "ko":"π의 소수점 이하 자릿수:","ar":"الخانات العشرية لـ π:","tr":"π'nin ondalık basamakları:",
        "sv":"Decimaler av π:","no":"Desimaler av π:","da":"Decimaler af π:","fi":"π:n desimaalit:",
        "cs":"Desetinná místa π:","ro":"Zecimale ale lui π:","hu":"π tizedesjegyei:",
        "el":"Δεκαδικά ψηφία του π:","hi":"π के दशमलव स्थान:","id":"Tempat desimal π:",
    },
    "start": {
        "de":"▶  Start Benchmark","en":"▶  Start Benchmark","fr":"▶  Démarrer le test",
        "es":"▶  Iniciar prueba","it":"▶  Avvia benchmark","pt":"▶  Iniciar benchmark",
        "nl":"▶  Start benchmark","pl":"▶  Rozpocznij test","ru":"▶  Запустить тест",
        "uk":"▶  Запустити тест","zh":"▶  开始基准测试","ja":"▶  ベンチマーク開始",
        "ko":"▶  벤치마크 시작","ar":"▶  بدء الاختبار","tr":"▶  Kıyaslamayı Başlat",
        "sv":"▶  Starta benchmark","no":"▶  Start benchmark","da":"▶  Start benchmark",
        "fi":"▶  Käynnistä suorituskoe","cs":"▶  Spustit benchmark","ro":"▶  Pornește benchmark",
        "hu":"▶  Teljesítménymérés indítása","el":"▶  Έναρξη αναφοράς","hi":"▶  बेंचमार्क शुरू करें",
        "id":"▶  Mulai Benchmark",
    },
    "stop": {
        "de":"■  Stopp","en":"■  Stop","fr":"■  Arrêter","es":"■  Detener","it":"■  Ferma",
        "pt":"■  Parar","nl":"■  Stoppen","pl":"■  Zatrzymaj","ru":"■  Стоп","uk":"■  Стоп",
        "zh":"■  停止","ja":"■  停止","ko":"■  중지","ar":"■  إيقاف","tr":"■  Durdur",
        "sv":"■  Stoppa","no":"■  Stopp","da":"■  Stop","fi":"■  Pysäytä","cs":"■  Zastavit",
        "ro":"■  Oprește","hu":"■  Megállít","el":"■  Διακοπή","hi":"■  रोकें","id":"■  Hentikan",
    },
    "ready": {
        "de":"Bereit.","en":"Ready.","fr":"Prêt.","es":"Listo.","it":"Pronto.","pt":"Pronto.",
        "nl":"Klaar.","pl":"Gotowy.","ru":"Готово.","uk":"Готово.","zh":"就绪。","ja":"準備完了。",
        "ko":"준비 완료.","ar":"جاهز.","tr":"Hazır.","sv":"Redo.","no":"Klar.","da":"Klar.",
        "fi":"Valmis.","cs":"Připraven.","ro":"Gata.","hu":"Kész.","el":"Έτοιμο.","hi":"तैयार।",
        "id":"Siap.",
    },
    "calculating": {
        "de":"Berechne π auf {n} Stellen …","en":"Calculating π to {n} digits …",
        "fr":"Calcul de π à {n} décimales …","es":"Calculando π a {n} dígitos …",
        "it":"Calcolo di π a {n} cifre …","pt":"Calculando π com {n} dígitos …",
        "nl":"π berekenen tot {n} cijfers …","pl":"Obliczanie π do {n} cyfr …",
        "ru":"Вычисление π до {n} знаков …","uk":"Обчислення π до {n} знаків …",
        "zh":"正在计算 π 到 {n} 位 …","ja":"π を {n} 桁まで計算中 …",
        "ko":"π를 {n}자리까지 계산 중 …","ar":"حساب π حتى {n} خانة …",
        "tr":"π {n} basamağa hesaplanıyor …","sv":"Beräknar π till {n} siffror …",
        "no":"Beregner π til {n} sifre …","da":"Beregner π til {n} cifre …",
        "fi":"Lasketaan π {n} numeroon …","cs":"Výpočet π na {n} číslic …",
        "ro":"Calculez π la {n} cifre …","hu":"π kiszámítása {n} jegyre …",
        "el":"Υπολογισμός π σε {n} ψηφία …","hi":"π को {n} अंकों तक गणना …",
        "id":"Menghitung π hingga {n} digit …",
    },
    "done": {
        "de":"✔  Fertig!  {n} Stellen in {t}","en":"✔  Done!  {n} digits in {t}",
        "fr":"✔  Terminé !  {n} décimales en {t}","es":"✔  ¡Listo!  {n} dígitos en {t}",
        "it":"✔  Fatto!  {n} cifre in {t}","pt":"✔  Feito!  {n} dígitos em {t}",
        "nl":"✔  Klaar!  {n} cijfers in {t}","pl":"✔  Gotowe!  {n} cyfr w {t}",
        "ru":"✔  Готово!  {n} знаков за {t}","uk":"✔  Готово!  {n} знаків за {t}",
        "zh":"✔  完成！{n} 位，用时 {t}","ja":"✔  完了！{n} 桁、所要時間 {t}",
        "ko":"✔  완료!  {n}자리, {t} 소요","ar":"✔  تم!  {n} خانة في {t}",
        "tr":"✔  Tamamlandı!  {n} basamak, {t}","sv":"✔  Klart!  {n} siffror på {t}",
        "no":"✔  Ferdig!  {n} sifre på {t}","da":"✔  Færdig!  {n} cifre på {t}",
        "fi":"✔  Valmis!  {n} numeroa ajassa {t}","cs":"✔  Hotovo!  {n} číslic za {t}",
        "ro":"✔  Gata!  {n} cifre în {t}","hu":"✔  Kész!  {n} jegy {t} alatt",
        "el":"✔  Ολοκληρώθηκε!  {n} ψηφία σε {t}","hi":"✔  हो गया!  {n} अंक {t} में",
        "id":"✔  Selesai!  {n} digit dalam {t}",
    },
    "aborted": {
        "de":"Abgebrochen.","en":"Aborted.","fr":"Annulé.","es":"Cancelado.","it":"Annullato.",
        "pt":"Cancelado.","nl":"Afgebroken.","pl":"Przerwano.","ru":"Прервано.","uk":"Перервано.",
        "zh":"已中止。","ja":"中断しました。","ko":"중단됨.","ar":"تم الإلغاء.","tr":"İptal edildi.",
        "sv":"Avbruten.","no":"Avbrutt.","da":"Afbrudt.","fi":"Keskeytetty.","cs":"Přerušeno.",
        "ro":"Anulat.","hu":"Megszakítva.","el":"Ακυρώθηκε.","hi":"रद्द किया।","id":"Dibatalkan.",
    },
    "result": {
        "de":"Ergebnis:","en":"Result:","fr":"Résultat :","es":"Resultado:","it":"Risultato:",
        "pt":"Resultado:","nl":"Resultaat:","pl":"Wynik:","ru":"Результат:","uk":"Результат:",
        "zh":"结果:","ja":"結果:","ko":"결과:","ar":"النتيجة:","tr":"Sonuç:","sv":"Resultat:",
        "no":"Resultat:","da":"Resultat:","fi":"Tulos:","cs":"Výsledek:","ro":"Rezultat:",
        "hu":"Eredmény:","el":"Αποτέλεσμα:","hi":"परिणाम:","id":"Hasil:",
    },
    "last_runs": {
        "de":"Letzte Läufe:","en":"Last runs:","fr":"Dernières exécutions :",
        "es":"Últimas ejecuciones:","it":"Ultime esecuzioni:","pt":"Últimas execuções:",
        "nl":"Laatste runs:","pl":"Ostatnie uruchomienia:","ru":"Последние запуски:",
        "uk":"Останні запуски:","zh":"最近运行:","ja":"最近の実行:","ko":"최근 실행:",
        "ar":"آخر التشغيلات:","tr":"Son çalıştırmalar:","sv":"Senaste körningar:",
        "no":"Siste kjøringer:","da":"Seneste kørsler:","fi":"Viimeisimmät ajot:",
        "cs":"Poslední běhy:","ro":"Ultimele rulări:","hu":"Utolsó futások:",
        "el":"Τελευταίες εκτελέσεις:","hi":"अंतिम रन:","id":"Eksekusi terakhir:",
    },
    "error_range": {
        "de":"Bitte eine ganze Zahl >= 10 eingeben.",
        "en":"Please enter a whole number >= 10.",
        "fr":"Veuillez entrer un nombre entier >= 10.",
        "es":"Ingresa un número entero >= 10.",
        "it":"Inserisci un numero intero >= 10.",
        "pt":"Insira um número inteiro >= 10.",
        "nl":"Voer een geheel getal >= 10 in.",
        "pl":"Wprowadź liczbę całkowitą >= 10.",
        "ru":"Введите целое число >= 10.",
        "uk":"Введіть ціле число >= 10.",
        "zh":"请输入 >= 10 的整数。",
        "ja":"10以上の整数を入力してください。",
        "ko":"10 이상의 정수를 입력하세요.",
        "ar":"الرجاء إدخال رقم صحيح >= 10.",
        "tr":"Lütfen >= 10 tam sayı girin.",
        "sv":"Ange ett heltal >= 10.",
        "no":"Skriv inn et heltall >= 10.",
        "da":"Indtast et heltal >= 10.",
        "fi":"Anna kokonaisluku >= 10.",
        "cs":"Zadejte celé číslo >= 10.",
        "ro":"Introduceți un număr întreg >= 10.",
        "hu":"Adjon meg egy egész számot >= 10.",
        "el":"Εισαγάγετε έναν ακέραιο >= 10.",
        "hi":"कृपया >= 10 की पूर्ण संख्या दर्ज करें।",
        "id":"Masukkan bilangan bulat >= 10.",
    },
    "splash_btn": {
        "de":"Weiter  →","en":"Continue  →","fr":"Continuer  →","es":"Continuar  →",
        "it":"Continua  →","pt":"Continuar  →","nl":"Doorgaan  →","pl":"Kontynuuj  →",
        "ru":"Продолжить  →","uk":"Продовжити  →","zh":"继续  →","ja":"続行  →",
        "ko":"계속  →","ar":"متابعة  →","tr":"Devam  →","sv":"Fortsätt  →",
        "no":"Fortsett  →","da":"Fortsæt  →","fi":"Jatka  →","cs":"Pokračovat  →",
        "ro":"Continuați  →","hu":"Tovább  →","el":"Συνέχεια  →","hi":"जारी रखें  →",
        "id":"Lanjutkan  →",
    },
}


def t(key: str, lang: str, **kw) -> str:
    text = TRANSLATIONS.get(key, {}).get(lang) or TRANSLATIONS.get(key, {}).get("en", key)
    return text.format(**kw) if kw else text


# ══════════════════════════════════════════════════════════════════════════════
#  FARBEN
# ══════════════════════════════════════════════════════════════════════════════
BG      = "#0d0d0d"
PANEL   = "#1a1a1a"
ACCENT  = "#00aaff"
ACCENT2 = "#0066cc"
TEXT    = "#e8e8e8"
TEXT_DIM= "#888888"
GREEN   = "#00ff88"
YELLOW  = "#ffcc00"
RED     = "#ff4444"


# ══════════════════════════════════════════════════════════════════════════════
#  PI-BERECHNUNG (Chudnovsky)
# ══════════════════════════════════════════════════════════════════════════════
def chudnovsky_pi(digits: int) -> str:
    getcontext().prec = digits + 20
    C = 426880 * Decimal(10005).sqrt()
    M, X, S = Decimal(1), Decimal(1), Decimal(13591409)
    for i in range(1, digits // 14 + 2):
        M = M * (6*i-5) * (2*i-1) * (6*i-1) // (i**3 * 24)
        X *= -262537412640768000
        S += Decimal(M * (13591409 + 545140134 * i)) / X
    return str(C / S)[:digits + 2]


# ══════════════════════════════════════════════════════════════════════════════
#  SPLASH – Sprachauswahl
# ══════════════════════════════════════════════════════════════════════════════
class SplashScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.chosen_lang = None
        self._current_lang = "de"
        self.title("GigaPi – Language / Sprache")
        self.geometry("430x580")
        self.resizable(False, False)
        self.configure(bg=BG)
        self._build()

    def _build(self):
        # Banner
        banner = tk.Frame(self, bg=ACCENT2, pady=18)
        banner.pack(fill="x")
        tk.Label(banner, text="π  GigaPi", font=("Consolas", 28, "bold"),
                 bg=ACCENT2, fg="white").pack()
        tk.Label(banner, text="Select your language / Sprache wählen",
                 font=("Consolas", 9), bg=ACCENT2, fg="#cce5ff").pack(pady=(2,0))

        # Suchfeld
        sf = tk.Frame(self, bg=BG, pady=10)
        sf.pack(fill="x", padx=20)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._filter)
        entry = tk.Entry(sf, textvariable=self.search_var,
                         font=("Consolas", 11), bg=PANEL, fg=TEXT,
                         insertbackground=ACCENT, relief="flat",
                         highlightthickness=1, highlightcolor=ACCENT,
                         highlightbackground="#333")
        entry.pack(fill="x", ipady=7)
        entry.insert(0, "🔍  ")
        entry.bind("<FocusIn>", lambda e: (entry.delete(0,"end")
                   if entry.get().startswith("🔍") else None))

        # Liste
        lf = tk.Frame(self, bg=BG)
        lf.pack(fill="both", expand=True, padx=20, pady=(0,10))
        sb = tk.Scrollbar(lf, bg=PANEL, troughcolor=BG, activebackground=ACCENT)
        sb.pack(side="right", fill="y")
        self.listbox = tk.Listbox(lf, font=("Segoe UI Emoji", 12),
                                   bg=PANEL, fg=TEXT,
                                   selectbackground=ACCENT2, selectforeground="white",
                                   relief="flat", activestyle="none", cursor="hand2",
                                   yscrollcommand=sb.set, highlightthickness=0)
        self.listbox.pack(fill="both", expand=True)
        sb.config(command=self.listbox.yview)

        self.lang_keys = list(LANGUAGES.keys())
        self._populate(self.lang_keys)
        self.listbox.selection_set(0)

        # Button
        self.btn = tk.Button(self, text="Weiter  →",
                              font=("Consolas", 13, "bold"),
                              bg=ACCENT, fg="white", activebackground=ACCENT2,
                              activeforeground="white", relief="flat",
                              padx=20, pady=11, cursor="hand2",
                              command=self._confirm)
        self.btn.pack(pady=(0,18), padx=20, fill="x")

        self.listbox.bind("<Double-Button-1>", lambda _: self._confirm())
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

    def _populate(self, keys):
        self.listbox.delete(0, "end")
        for k in keys:
            self.listbox.insert("end", f"  {k}")

    def _filter(self, *_):
        q = self.search_var.get().lower().replace("🔍  ","").strip()
        self.lang_keys = [k for k in LANGUAGES if q in k.lower()] if q else list(LANGUAGES.keys())
        self._populate(self.lang_keys)
        if self.lang_keys:
            self.listbox.selection_set(0)
            self._on_select()

    def _on_select(self, *_):
        sel = self.listbox.curselection()
        if sel:
            lk = self.lang_keys[sel[0]]
            self._current_lang = LANGUAGES[lk]
            self.btn.config(text=t("splash_btn", self._current_lang))

    def _confirm(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        self.chosen_lang = LANGUAGES[self.lang_keys[sel[0]]]
        self.destroy()


# ══════════════════════════════════════════════════════════════════════════════
#  HAUPT-APP
# ══════════════════════════════════════════════════════════════════════════════
class GigaPiApp(tk.Tk):
    def __init__(self, lang: str):
        super().__init__()
        self.lang = lang
        self._running    = False
        self._thread     = None
        self._start_time = 0.0
        self.history: list[str] = []

        self.title(t("title", lang))
        self.geometry("640x520")
        self.resizable(False, False)
        self.configure(bg=BG)
        self._build_ui()

    def _build_ui(self):
        L = self.lang

        # Banner
        banner = tk.Frame(self, bg=ACCENT2, pady=12)
        banner.pack(fill="x")
        tk.Label(banner, text=f"π  {t('title', L)}",
                 font=("Consolas", 22, "bold"), bg=ACCENT2, fg="white").pack()
        tk.Label(banner, text=t("subtitle", L),
                 font=("Consolas", 9), bg=ACCENT2, fg="#cce5ff").pack()

        # Einstellungen
        cfg = tk.Frame(self, bg=PANEL, padx=20, pady=16)
        cfg.pack(fill="x", padx=14, pady=(14, 0))
        tk.Label(cfg, text=t("decimal_places", L), font=("Consolas", 11),
                 bg=PANEL, fg=TEXT).grid(row=0, column=0, sticky="w")
        self.digits_var = tk.IntVar(value=1000)
        style = ttk.Style(); style.theme_use("default")
        style.configure("TCombobox", fieldbackground=BG, background=PANEL,
                         foreground=TEXT, selectbackground=ACCENT2)
        entry_digits = tk.Entry(cfg, textvariable=self.digits_var, width=12,
                     font=("Consolas", 11), bg=BG, fg=GREEN,
                     insertbackground=GREEN, relief="flat",
                     highlightthickness=1, highlightcolor=ACCENT,
                     highlightbackground="#333")
        entry_digits.grid(row=0, column=1, padx=(12,0), sticky="w", ipady=4)
        # Preset buttons
        presets_frame = tk.Frame(cfg, bg=PANEL)
        presets_frame.grid(row=1, column=0, columnspan=3, sticky="w", pady=(8,0))
        for n in [1_000, 10_000, 100_000, 1_000_000, 10_000_000]:
            lbl = f"{n:,}".replace(",",".")
            tk.Button(presets_frame, text=lbl,
                      font=("Consolas", 9), bg="#222", fg=ACCENT,
                      activebackground=ACCENT2, activeforeground="white",
                      relief="flat", padx=8, pady=3, cursor="hand2",
                      command=lambda v=n: self.digits_var.set(v)
                      ).pack(side="left", padx=(0,5))

        # Buttons
        bf = tk.Frame(self, bg=BG); bf.pack(pady=12)
        self.btn_start = tk.Button(bf, text=t("start", L),
                                    font=("Consolas",12,"bold"), bg=ACCENT, fg="white",
                                    activebackground=ACCENT2, activeforeground="white",
                                    relief="flat", padx=20, pady=8, cursor="hand2",
                                    command=self._start)
        self.btn_start.grid(row=0, column=0, padx=8)
        self.btn_stop = tk.Button(bf, text=t("stop", L),
                                   font=("Consolas",12,"bold"), bg="#333", fg=TEXT_DIM,
                                   activebackground=RED, activeforeground="white",
                                   relief="flat", padx=20, pady=8, cursor="hand2",
                                   state="disabled", command=self._stop)
        self.btn_stop.grid(row=0, column=1, padx=8)

        # Status & Timer
        info = tk.Frame(self, bg=BG); info.pack(fill="x", padx=18)
        self.status_var = tk.StringVar(value=t("ready", L))
        tk.Label(info, textvariable=self.status_var, font=("Consolas",10),
                 bg=BG, fg=TEXT_DIM, anchor="w").pack(side="left")
        self.timer_var = tk.StringVar(value="00:00.000")
        tk.Label(info, textvariable=self.timer_var, font=("Consolas",14,"bold"),
                 bg=BG, fg=ACCENT).pack(side="right")

        # Fortschritt
        style.configure("P.Horizontal.TProgressbar",
                          troughcolor=PANEL, background=ACCENT, thickness=10)
        self.progress = ttk.Progressbar(self, style="P.Horizontal.TProgressbar",
                                          mode="indeterminate", length=612)
        self.progress.pack(padx=14, pady=6)

        # Ergebnis
        rf = tk.Frame(self, bg=PANEL, padx=12, pady=10)
        rf.pack(fill="both", expand=True, padx=14, pady=(0,14))
        tk.Label(rf, text=t("result", L), font=("Consolas",10,"bold"),
                 bg=PANEL, fg=ACCENT).pack(anchor="w")
        self.result_text = tk.Text(rf, height=8, font=("Consolas",9),
                                    bg=BG, fg=GREEN, insertbackground=GREEN,
                                    relief="flat", wrap="char", state="disabled")
        self.result_text.pack(fill="both", expand=True, pady=(4,0))

        # Letzte Läufe
        hf = tk.Frame(self, bg=BG, padx=14); hf.pack(fill="x", pady=(0,10))
        tk.Label(hf, text=t("last_runs", L), font=("Consolas",9),
                 bg=BG, fg=TEXT_DIM).pack(anchor="w")
        self.hist_var = tk.StringVar(value="—")
        tk.Label(hf, textvariable=self.hist_var, font=("Consolas",9),
                 bg=BG, fg=YELLOW, anchor="w", justify="left").pack(anchor="w")

    # ── Logik ──────────────────────────────────────────────────────────────────
    def _start(self):
        try:
            digits = int(self.digits_var.get())
            if digits < 10: raise ValueError
        except (ValueError, tk.TclError):
            messagebox.showerror("Error", t("error_range", self.lang)); return

        self._running = True
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal", bg=RED, fg="white")
        self.status_var.set(t("calculating", self.lang, n=f"{digits:,}"))
        self._set_result("")
        self.progress.start(10)
        self._start_time = time.perf_counter()
        self._tick()
        self._thread = threading.Thread(target=self._run_benchmark,
                                         args=(digits,), daemon=True)
        self._thread.start()

    def _run_benchmark(self, digits):
        try:
            pi_str  = chudnovsky_pi(digits)
            elapsed = time.perf_counter() - self._start_time
            if self._running:
                self.after(0, self._finish, pi_str, elapsed, digits)
        except Exception as e:
            self.after(0, self._error, str(e))

    def _stop(self):
        self._running = False
        self.progress.stop()
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled", bg="#333", fg=TEXT_DIM)
        self.status_var.set(t("aborted", self.lang))

    def _tick(self):
        if not self._running: return
        elapsed = time.perf_counter() - self._start_time
        m, s = divmod(elapsed, 60)
        self.timer_var.set(f"{int(m):02d}:{s:06.3f}")
        self.after(50, self._tick)

    def _finish(self, pi_str, elapsed, digits):
        self._running = False
        self.progress.stop()
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled", bg="#333", fg=TEXT_DIM)
        m, s = divmod(elapsed, 60)
        ts = f"{int(m):02d}:{s:06.3f}"
        self.timer_var.set(ts)
        self.status_var.set(t("done", self.lang, n=f"{digits:,}", t=ts))
        self._set_result(pi_str)
        self.history.insert(0, f"  {digits:>7,}  →  {ts}")
        self.history = self.history[:5]
        self.hist_var.set("\n".join(self.history))

    def _error(self, msg):
        self._running = False
        self.progress.stop()
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled", bg="#333", fg=TEXT_DIM)
        self.status_var.set(f"Error: {msg}")

    def _set_result(self, text):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("end", text)
        self.result_text.config(state="disabled")


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    splash = SplashScreen()
    splash.mainloop()
    if splash.chosen_lang:
        GigaPiApp(splash.chosen_lang).mainloop()
