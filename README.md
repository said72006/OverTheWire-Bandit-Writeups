<div align="center">

# 🔐 OverTheWire Bandit Writeups

### Linux • SSH • CLI • Cybersecurity Fundamentals

![Linux](https://img.shields.io/badge/Linux-CLI-FCC624?logo=linux&logoColor=black)
![SSH](https://img.shields.io/badge/SSH-Hands--On-2C8EBB?logo=openssh&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Learning-111111?logo=hackthebox&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

A personal learning journal documenting my progress through the **OverTheWire Bandit** wargame.

[🌐 OverTheWire Bandit](https://overthewire.org/wargames/bandit/) • [👤 My GitHub](https://github.com/said72006)

</div>

---

## 🎯 Why This Repository?

I use Bandit to build practical Linux and cybersecurity skills instead of only studying commands theoretically.

Each write-up focuses on:

- Understanding the challenge
- Choosing the right Linux tools
- Explaining the approach
- Recording the commands I practiced
- Writing down the lesson learned

> [!IMPORTANT]
> **Passwords, flags, private keys, and active credentials are intentionally not published.** The repository documents the learning process without publishing credentials or exact target answers.

---

## 📈 Progress

I publish my progress in **5-level milestones** so each update represents a meaningful block of hands-on practice.

| Milestone | Levels | Status |
|---|---|---|
| ✅ Milestone 01 | 0–4 | Completed |
| ✅ Milestone 02 | 5–9 | Completed |
| ✅ Milestone 03 | 10–14 | Completed |
| ⬜ Milestone 04 | 15–19 | Not Started |
| ⬜ Milestone 05 | 20–24 | Not Started |
| ⬜ Milestone 06 | 25–29 | Not Started |
| ⬜ Milestone 07 | 30+ | Not Started |

### Milestone 01 — Levels 0–4 ✅

- [Level 00 — SSH Connection](levels/Level-00.md)
- [Level 01](levels/Level-01.md)
- [Level 02](levels/Level-02.md)
- [Level 03](levels/Level-03.md)
- [Level 04](levels/Level-04.md)

### Milestone 02 — Levels 5–9 ✅

- [Level 05 — Recursive File Search](levels/Level-05.md)
- [Level 06 — Ownership Filters & Error Redirection](levels/Level-06.md)
- [Level 07 — Text Search with grep](levels/Level-07.md)
- [Level 08 — Sorting, Counting & Pipes](levels/Level-08.md)
- [Level 09 — Extracting Readable Strings](levels/Level-09.md)

### Milestone 03 — Levels 10–14 ✅

- [Level 10 — Base64 Decoding](levels/Level-10.md)
- [Level 11 — ROT13 with tr](levels/Level-11.md)
- [Level 12 — Hexdump & Repeated Compression](levels/Level-12.md)
- [Level 13 — SSH Private Key Authentication](levels/Level-13.md)
- [Level 14 — Netcat & Localhost Service](levels/Level-14.md)

---

## 🧠 Skills I'm Practicing

```text
Linux CLI
   ├── Navigation & file handling
   ├── Hidden and unusual filenames
   ├── Permissions & ownership
   ├── Recursive and filesystem-wide searching
   ├── File type, owner, group, and size filtering
   ├── Text searching with grep
   ├── Sorting and duplicate counting
   ├── Extracting readable strings from mixed/binary data
   ├── Base64 encoding and decoding
   ├── ROT13 and character translation with tr
   ├── Reversing hexdumps with xxd
   ├── Identifying real file formats with file
   ├── gzip and bzip2 decompression
   ├── tar archive inspection and extraction
   ├── Working safely in temporary directories
   ├── File permission hardening with chmod
   ├── Command pipelines with |
   ├── Input redirection with <
   ├── Output redirection with >
   ├── Standard output vs standard error
   ├── Error redirection with 2>/dev/null
   └── Shell wildcards

Remote Access & Networking
   ├── SSH
   ├── SSH private key authentication
   ├── Selecting identity files with ssh -i
   ├── Connecting to localhost services
   ├── Understanding destination ports
   └── Basic TCP interaction with Netcat

Cybersecurity Mindset
   ├── Enumeration
   ├── Problem solving
   ├── Reading clues carefully
   ├── Inspecting before acting
   ├── Protecting credentials and private keys
   └── Choosing the right command/tool
```

---

## 🧰 Commands & Tools Used So Far

`ssh` • `ls` • `cd` • `cat` • `more` • `file` • `find` • `grep` • `sort` • `uniq` • `strings` • `base64` • `tr` • `whatis` • `mktemp` • `cp` • `mv` • `xxd` • `gzip` • `bzip2` • `tar` • `chmod` • `nc`

This list contains commands I have actually used during my Bandit progress and will grow as I continue.

---

## 📂 Repository Structure

```text
OverTheWire-Bandit-Writeups/
│
├── README.md
├── LEVEL_TEMPLATE.md
│
└── levels/
    ├── Level-00.md
    ├── Level-01.md
    ├── Level-02.md
    ├── Level-03.md
    ├── Level-04.md
    ├── Level-05.md
    ├── Level-06.md
    ├── Level-07.md
    ├── Level-08.md
    ├── Level-09.md
    ├── Level-10.md
    ├── Level-11.md
    ├── Level-12.md
    ├── Level-13.md
    └── Level-14.md
```

---

## 📝 Write-Up Format

Every level follows a consistent structure:

1. **Goal** — what I need to achieve
2. **Approach** — how I analyze the challenge
3. **Commands Used** — commands and options involved
4. **What I Learned** — the main technical takeaway
5. **Notes** — details worth remembering

A reusable template is available in [`LEVEL_TEMPLATE.md`](LEVEL_TEMPLATE.md).

---

## 🚀 Learning Strategy

```text
Read the goal
     ↓
Explore the system
     ↓
Identify the right Linux tool
     ↓
Solve the challenge
     ↓
Understand why it worked
     ↓
Document the lesson
```

My goal is not simply to reach the next level — it is to understand the Linux concepts behind each solution.

---

## ⚠️ Disclaimer

This repository is for **education and personal learning**. It is based on the intentionally vulnerable OverTheWire Bandit training environment and should not be interpreted as authorization to test systems without permission.

---

<div align="center">

### 🐧 Learn Linux. Break down problems. Build security skills.

**Author:** [Said Ahmed Abu-Fouda](https://github.com/said72006)

</div>
