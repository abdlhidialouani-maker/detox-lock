"""
Detox Lock - fullscreen lock with a slow, soft navy-blue Windows 11-style background
and a motivational quote.

How to use:
  1. Install Python from python.org (tick "Add python.exe to PATH").
  2. Double-click run_detox.bat (or detox_lock.py).
  3. Choose minutes, press Start. Soft blue light slowly drifts across the screen until time is up.
  4. A random quote shows every time, and it changes every 20 seconds.

MUSIC: put any songs (.mp3 .wav .wma .m4a) in the folder  Music/DetoxLock  (inside your
Music library) or in a folder called  music  next to this program. Click
"Open music folder" in the start window. They play in random order while locked.

While locked, the mouse is frozen and the keyboard only types the exit code:
    12345678910   (then press Enter)
Note: Windows never lets any program block Ctrl+Alt+Del, so that and restarting the
PC can still end it. Save your work before you start!

Includes 100 quotes. Add or edit lines in the QUOTES list below to make it yours.
"""

import colorsys
import math
import os
import random
import sys
import time
import tkinter as tk

GIVE_UP_PHRASE = "12345678910"

# (quote, author) - leave author as "" for no name
QUOTES = [
    # --- Classic wisdom ---
    ("The journey of a thousand miles begins with a single step.", "Lao Tzu"),
    ("Nature does not hurry, yet everything is accomplished.", "Lao Tzu"),
    ("He who knows he has enough is rich.", "Lao Tzu"),
    ("It is not that we have a short time to live, but that we waste much of it.", "Seneca"),
    ("We suffer more often in imagination than in reality.", "Seneca"),
    ("Luck is what happens when preparation meets opportunity.", "Seneca"),
    ("You have power over your mind, not outside events. Realize this, and you will find strength.", "Marcus Aurelius"),
    ("The happiness of your life depends upon the quality of your thoughts.", "Marcus Aurelius"),
    ("Waste no more time arguing about what a good man should be. Be one.", "Marcus Aurelius"),
    ("Very little is needed to make a happy life; it is all within yourself, in your way of thinking.", "Marcus Aurelius"),
    ("Well begun is half done.", "Aristotle"),
    ("No man is free who is not master of himself.", "Epictetus"),
    ("First say to yourself what you would be; and then do what you have to do.", "Epictetus"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("He who learns but does not think is lost.", "Confucius"),
    ("The unexamined life is not worth living.", "Socrates"),
    ("The beginning is the most important part of the work.", "Plato"),
    ("The first and greatest victory is to conquer yourself.", "Plato"),
    ("The mind is everything. What you think you become.", "Buddha"),
    ("Peace comes from within. Do not seek it without.", "Buddha"),
    ("It is not enough to be busy. The question is: what are we busy about?", "Henry David Thoreau"),
    ("Our life is frittered away by detail. Simplify, simplify.", "Henry David Thoreau"),
    ("Go confidently in the direction of your dreams.", "Henry David Thoreau"),
    ("Nothing great was ever achieved without enthusiasm.", "Ralph Waldo Emerson"),
    ("Adopt the pace of nature: her secret is patience.", "Ralph Waldo Emerson"),
    ("Lost time is never found again.", "Benjamin Franklin"),
    ("Well done is better than well said.", "Benjamin Franklin"),
    ("Dost thou love life? Then do not squander time, for that is the stuff life is made of.", "Benjamin Franklin"),
    ("Little strokes fell great oaks.", "Benjamin Franklin"),
    ("What you seek is seeking you.", "Rumi"),
    ("Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.", "Rumi"),
    ("Whatever you are, be a good one.", "Abraham Lincoln"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("Things which matter most must never be at the mercy of things which matter least.", "Goethe"),
    ("Knowing is not enough; we must apply.", "Goethe"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Courage is resistance to fear, mastery of fear, not absence of fear.", "Mark Twain"),
    ("The best time to plant a tree was twenty years ago. The second best time is now.", "Chinese proverb"),
    ("Fall seven times, stand up eight.", "Japanese proverb"),
    ("Fortune favors the bold.", "Virgil"),
    ("Dare to be wise.", "Horace"),
    ("Dripping water hollows out stone, not through force but through persistence.", "Ovid"),
    ("Before enlightenment, chop wood, carry water. After enlightenment, chop wood, carry water.", "Zen proverb"),
    ("Sitting quietly, doing nothing, spring comes, and the grass grows by itself.", "Zen proverb"),
    ("Slow and steady wins the race.", "Proverb"),
    ("Rome wasn't built in a day.", "Proverb"),
    ("The best is the enemy of the good.", "Voltaire"),
    ("While there's life, there's hope.", "Cicero"),
    # --- Gentle reminders ---
    ("Your screen will wait for you. Your life will not.", ""),
    ("Look up. The real world is still the best show on.", ""),
    ("Rest is not laziness. It is how you come back stronger.", ""),
    ("Every minute away from the screen is a minute given back to yourself.", ""),
    ("Breathe in. Breathe out. Nothing urgent is happening.", ""),
    ("Discipline is choosing what you want most over what you want now.", ""),
    ("Be where your feet are.", ""),
    ("Nothing on your feed is as important as the person in front of you.", ""),
    ("Boredom is the doorway to your best ideas.", ""),
    ("You are not missing out. You are tuning in.", ""),
    ("Drink some water. Your brain will thank you.", ""),
    ("Stand up and stretch. Your body has been waiting.", ""),
    ("Call someone you love instead of scrolling past them.", ""),
    ("Ten quiet minutes can change the whole day.", ""),
    ("Attention is the most valuable thing you own. Spend it on purpose.", ""),
    ("The notifications can wait. They always do.", ""),
    ("Small breaks protect big goals.", ""),
    ("A calm mind does better work than a busy one.", ""),
    ("Go outside. The sky is free and has no ads.", ""),
    ("Close your eyes for a moment. Let your thoughts settle.", ""),
    ("You don't have to answer everything right now.", ""),
    ("Real life has no refresh button. Enjoy it while it loads.", ""),
    ("Today is made of choices. This is a good one.", ""),
    ("Be proud of yourself for pausing.", ""),
    ("Eyes up, shoulders down, breathe slowly.", ""),
    ("The best ideas often show up when you stop chasing them.", ""),
    ("Progress is quiet. Keep going.", ""),
    ("You are more than your screen time.", ""),
    ("Silence is not empty. It is full of answers.", ""),
    ("Put the world on hold. It will still be there.", ""),
    ("Healthy habits are built one pause at a time.", ""),
    ("Your future self is grateful for this break.", ""),
    ("Let your eyes rest on something far away.", ""),
    ("A walk is a reset for the mind.", ""),
    ("Don't count the minutes. Make the minutes count.", ""),
    ("Focus is a muscle. You're training it right now.", ""),
    ("Slow down. You are not behind.", ""),
    ("Be present. That is where your life is happening.", ""),
    ("Peace of mind is worth more than any notification.", ""),
    ("Do one thing at a time, and do it well.", ""),
    ("Gratitude turns a quiet moment into enough.", ""),
    ("You can always come back to the screen. This moment is only now.", ""),
    ("Fresh air, clear head, better day.", ""),
    ("Kindness to yourself starts with rest.", ""),
    ("Read a few pages of a real book today.", ""),
    ("Write down one thing you're proud of.", ""),
    ("The urge to check will pass. Let it.", ""),
    ("Choose depth over distraction.", ""),
    ("Quiet time is not wasted time.", ""),
    ("You did the hard part: you started. Finish strong.", ""),
]

QUOTE_SECONDS = 20

# How fast the background colour flows. Lower = slower. (0.02 is very slow,
# one full wave takes about 5 minutes. Try 0.01 for even slower.)
COLOR_SPEED = 0.02


# ---------------------------------------------------------------- colours ----
def hsv_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    return (r * 255, g * 255, b * 255)


def mix(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def hexc(c):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(x))) for x in c)


class Background:
    """One smooth dark-blue colour that slowly flows across the whole screen,
    like the Windows 11 Calculator. No circles: just soft, wide waves of light blue
    over deep navy. Everything moves very, very slowly."""

    GRID_WIDTH = 160  # small picture that is stretched to fill the screen (keeps it fast)

    def __init__(self, canvas, width, height):
        self.c = canvas
        self.zoom = max(1, -(-width // self.GRID_WIDTH))   # round up
        self.gw = -(-width // self.zoom)
        self.gh = -(-height // self.zoom)
        self.small = tk.PhotoImage(width=self.gw, height=self.gh)
        self.big = None
        self.item = canvas.create_image(0, 0, anchor="nw")

        # Fixed starting position of two wide waves going in different directions
        c1, s1 = math.cos(math.radians(35)), math.sin(math.radians(35))
        c2, s2 = math.cos(math.radians(-50)), math.sin(math.radians(-50))
        self.wave_a = []
        self.wave_b = []
        for y in range(self.gh):
            ny = y / self.gh
            self.wave_a.append([2 * math.pi * 0.9 * ((x / self.gw) * c1 + ny * s1)
                                for x in range(self.gw)])
            self.wave_b.append([2 * math.pi * 0.6 * ((x / self.gw) * c2 + ny * s2)
                                for x in range(self.gw)])

    def draw(self, t):
        # the blue itself changes extremely slowly between sky-blue and indigo
        hue = 0.62 + 0.025 * math.sin(t * COLOR_SPEED * 0.5)
        dark = hsv_rgb(hue, 0.58, 0.14)
        light = hsv_rgb(hue - 0.01, 0.50, 0.38)
        table = [hexc(mix(dark, light, i / 255)) for i in range(256)]

        p1 = COLOR_SPEED * t
        p2 = -COLOR_SPEED * 0.7 * t
        rows = []
        for ra, rb in zip(self.wave_a, self.wave_b):
            row = [table[int((0.5 + 0.5 * (0.65 * math.sin(a + p1) + 0.35 * math.sin(b + p2))) * 255)]
                   for a, b in zip(ra, rb)]
            rows.append("{" + " ".join(row) + "}")
        self.small.put(" ".join(rows))
        self.big = self.small.zoom(self.zoom)
        self.c.itemconfig(self.item, image=self.big)


# ------------------------------------------------------------------ music ----
AUDIO_EXTS = (".mp3", ".wav", ".wma", ".m4a", ".aac", ".mid", ".midi")


def app_dir():
    if getattr(sys, "frozen", False):          # running as DetoxLock.exe
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def music_folders():
    """Folder 1: 'music' next to the program.  Folder 2: Music/DetoxLock in your Music library."""
    return [os.path.join(app_dir(), "music"),
            os.path.join(os.path.expanduser("~"), "Music", "DetoxLock")]


def ensure_music_folders():
    for folder in music_folders():
        try:
            os.makedirs(folder, exist_ok=True)
        except OSError:
            pass


def find_music():
    files = []
    for folder in music_folders():
        try:
            for name in sorted(os.listdir(folder)):
                if name.lower().endswith(AUDIO_EXTS):
                    files.append(os.path.join(folder, name))
        except OSError:
            pass
    return files


class MusicPlayer:
    """Plays your songs one after another in random order, using Windows' built-in
    audio player (no extra programs needed). Songs that cannot be played are skipped."""

    ALIAS = "detoxsong"

    def __init__(self, files):
        self.files = list(files)
        random.shuffle(self.files)
        self.index = -1
        self.playing = False
        self.enabled = sys.platform == "win32" and bool(self.files)
        self._winmm = None

    def _mci(self, command):
        if self._winmm is None:
            import ctypes
            self._winmm = ctypes.WinDLL("winmm")
        import ctypes
        buf = ctypes.create_unicode_buffer(256)
        err = self._winmm.mciSendStringW(command, buf, 255, 0)
        return err, buf.value

    def start(self):
        if not self.enabled:
            return False
        self.next_track()
        return self.playing

    def next_track(self):
        self.playing = False
        self._mci("close " + self.ALIAS)
        for _ in range(len(self.files)):
            self.index = (self.index + 1) % len(self.files)
            path = self.files[self.index].replace('"', "")
            kind = " type mpegvideo" if path.lower().endswith(".mp3") else ""
            err, _text = self._mci(f'open "{path}"{kind} alias {self.ALIAS}')
            if err != 0:
                continue                       # can't open this one, try the next
            err, _text = self._mci("play " + self.ALIAS)
            if err == 0:
                self.playing = True
                return
            self._mci("close " + self.ALIAS)

    def update(self):
        """Call every half second: starts the next song when one finishes."""
        if not self.enabled or not self.playing:
            return
        err, mode = self._mci("status " + self.ALIAS + " mode")
        if err != 0 or mode.strip().lower() == "stopped":
            self.next_track()

    def stop(self):
        if self.enabled:
            self._mci("stop " + self.ALIAS)
            self._mci("close " + self.ALIAS)
        self.playing = False


# ------------------------------------------------------------- input lock ----
def allowed_keys():
    """Only the keys needed for the exit code, plus Space, Backspace and Enter."""
    keys = set()
    for ch in GIVE_UP_PHRASE:
        if ch.isalpha():
            keys.add(ord(ch.upper()))                 # letters A-Z
        elif ch.isdigit():
            keys.add(ord(ch))                         # top-row digits 0-9
            keys.add(0x60 + int(ch))                  # numeric keypad digits
    keys.update({0x20, 0x08, 0x0D})  # space, backspace, enter
    return keys


class InputLock:
    """Windows only. Freezes the mouse completely and blocks every key except the
    ones needed to type the exit sentence (low-level keyboard and mouse hooks)."""

    def __init__(self):
        self.allowed = allowed_keys()
        self._user32 = None
        self._hooks = []
        self._callbacks = []

    def start(self):
        if sys.platform != "win32":
            return False
        import ctypes
        from ctypes import wintypes

        user32 = ctypes.WinDLL("user32", use_last_error=True)
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        LRESULT = ctypes.c_ssize_t
        HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

        user32.SetWindowsHookExW.argtypes = [ctypes.c_int, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD]
        user32.SetWindowsHookExW.restype = wintypes.HHOOK
        user32.CallNextHookEx.argtypes = [wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM]
        user32.CallNextHookEx.restype = LRESULT
        user32.UnhookWindowsHookEx.argtypes = [wintypes.HHOOK]
        kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
        kernel32.GetModuleHandleW.restype = wintypes.HMODULE

        allowed = self.allowed

        def keyboard_proc(n_code, w_param, l_param):
            try:
                if n_code >= 0:
                    vk = ctypes.cast(l_param, ctypes.POINTER(wintypes.DWORD)).contents.value
                    if vk not in allowed:
                        return 1  # swallow the key
            except Exception:
                pass  # if anything goes wrong, never trap the user: let the key through
            return user32.CallNextHookEx(None, n_code, w_param, l_param)

        def mouse_proc(n_code, w_param, l_param):
            if n_code >= 0:
                return 1  # swallow every mouse move, click and scroll
            return user32.CallNextHookEx(None, n_code, w_param, l_param)

        kb_cb = HOOKPROC(keyboard_proc)
        ms_cb = HOOKPROC(mouse_proc)
        self._callbacks = [kb_cb, ms_cb]  # keep references so Python doesn't delete them
        module = kernel32.GetModuleHandleW(None)
        kb_hook = user32.SetWindowsHookExW(13, kb_cb, module, 0)   # WH_KEYBOARD_LL
        ms_hook = user32.SetWindowsHookExW(14, ms_cb, module, 0)   # WH_MOUSE_LL
        self._user32 = user32
        self._hooks = [h for h in (kb_hook, ms_hook) if h]
        return len(self._hooks) == 2

    def stop(self):
        if self._user32:
            for h in self._hooks:
                self._user32.UnhookWindowsHookEx(h)
        self._hooks = []
        self._user32 = None


# ------------------------------------------------------------- lock screen ---
def run_lock(minutes, play_music=True):
    end = time.time() + minutes * 60
    start = time.time()

    root = tk.Tk()
    root.title("Detox Lock")
    root.configure(bg="#161c2c")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # ignore close button
    root.bind("<Alt-F4>", lambda e: "break")
    root.bind("<Escape>", lambda e: "break")
    root.configure(cursor="none")
    root.update()

    W = root.winfo_screenwidth()
    H = root.winfo_screenheight()

    canvas = tk.Canvas(root, width=W, height=H, highlightthickness=0, bg="#161c2c")
    canvas.configure(cursor="none")
    canvas.pack(fill="both", expand=True)
    bg = Background(canvas, W, H)

    def make_text(x, y, color, **kw):
        """Text with a soft dark shadow so it stays readable on bright colours."""
        shadow = canvas.create_text(x + 2, y + 2, fill="#070a12", **kw)
        main = canvas.create_text(x, y, fill=color, **kw)
        return main, shadow

    def set_text(pair, text):
        for item in pair:
            canvas.itemconfig(item, text=text)

    title = make_text(W / 2, H * 0.10, "#ffffff", text="Detox time",
                      font=("Segoe UI", 36, "bold"))
    timer = make_text(W / 2, H * 0.26, "#ffffff", text="",
                      font=("Consolas", 90, "bold"))
    quote = make_text(W / 2, H * 0.52, "#ffffff", text="",
                      font=("Georgia", 30, "italic"),
                      width=int(W * 0.7), justify="center")
    author = make_text(W / 2, H * 0.68, "#a9c4ff", text="",
                       font=("Segoe UI", 18))
    make_text(W / 2, H * 0.955, "#c5cbe8",
              text=f'Keyboard and mouse are locked. To exit early, type the code  "{GIVE_UP_PHRASE}"  and press Enter',
              font=("Segoe UI", 12))

    entry = tk.Entry(root, font=("Segoe UI", 14), width=40, justify="center")
    canvas.create_window(W / 2, H * 0.91, window=entry)
    entry.focus_force()

    def check_phrase(event=None):
        if entry.get().strip().lower() == GIVE_UP_PHRASE:
            root.destroy()
        else:
            entry.delete(0, "end")

    entry.bind("<Return>", check_phrase)

    # Random quote, never the same one twice in a row
    state = {"last": -1}

    def next_quote():
        choices = [i for i in range(len(QUOTES)) if i != state["last"]]
        i = random.choice(choices)
        state["last"] = i
        text, who = QUOTES[i]
        set_text(quote, f"\u201c{text}\u201d")
        set_text(author, f"\u2014 {who}" if who else "")
        root.after(QUOTE_SECONDS * 1000, next_quote)

    def animate():
        bg.draw(time.time() - start)
        root.after(800, animate)  # very slow, so a gentle refresh is enough

    def tick():
        remaining = int(end - time.time())
        if remaining <= 0:
            root.destroy()
            return
        m, s = divmod(remaining, 60)
        h, m = divmod(m, 60)
        set_text(timer, f"{h:02d}:{m:02d}:{s:02d}")
        music.update()
        root.attributes("-topmost", True)
        root.lift()
        entry.focus_force()
        root.after(500, tick)

    music = MusicPlayer(find_music() if play_music else [])
    music.start()  # your songs play while the screen is locked

    next_quote()
    animate()
    tick()

    locker = InputLock()
    locker.start()  # freeze mouse + keyboard (Windows)
    try:
        root.mainloop()
    finally:
        locker.stop()  # always give the keyboard and mouse back
        music.stop()


# ------------------------------------------------------------ start window ---
def main():
    setup = tk.Tk()
    setup.title("Detox Lock")
    setup.geometry("420x420")
    setup.resizable(False, False)

    tk.Label(setup, text="Lock my computer for (minutes):",
             font=("Segoe UI", 11)).pack(pady=(25, 8))

    minutes_var = tk.StringVar(value="30")
    tk.Spinbox(setup, from_=1, to=720, textvariable=minutes_var,
               width=8, font=("Segoe UI", 14), justify="center").pack()

    text, author = random.choice(QUOTES)
    tk.Label(setup, text=f"\u201c{text}\u201d", font=("Georgia", 10, "italic"),
             wraplength=320, justify="center", fg="#444444").pack(pady=(15, 0))

    ensure_music_folders()
    songs = find_music()
    music_var = tk.BooleanVar(value=True)
    tk.Checkbutton(setup, text="Play music while locked", variable=music_var,
                   font=("Segoe UI", 10)).pack(pady=(14, 0))
    info = (f"{len(songs)} song(s) found" if songs
            else "No songs yet. Click the button below and drop in some mp3 files.")
    tk.Label(setup, text=info, font=("Segoe UI", 9), fg="#555555",
             wraplength=360, justify="center").pack()

    def open_music_folder():
        folder = music_folders()[1]
        try:
            os.makedirs(folder, exist_ok=True)
            os.startfile(folder)
        except Exception:
            pass

    tk.Button(setup, text="Open music folder", command=open_music_folder).pack(pady=(6, 0))

    def start():
        try:
            minutes = int(minutes_var.get())
            if minutes < 1:
                return
        except ValueError:
            return
        setup.destroy()
        run_lock(minutes, music_var.get())

    tk.Button(setup, text="Start Detox", font=("Segoe UI", 12, "bold"),
              bg="#4ade80", command=start).pack(pady=15)

    setup.mainloop()


if __name__ == "__main__":
    main()
