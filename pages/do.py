import os

phase_articles = {
    1: [],                    # Skip 0-3
    2: range(4, 8),           # 4-7
    3: range(8, 12),          # 8-11
    4: range(12, 16),         # 12-15
    5: range(16, 21),         # 16-20
    6: range(21, 25),         # 21-24
    7: range(25, 30),         # 25-29
    8: range(30, 35),         # 30-34
    9: range(35, 40),         # 35-39
    10: range(40, 45),        # 40-44
}

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
    <link rel="stylesheet" href="../../../css/pico.min.css">
    <link rel="stylesheet" href="../../../css/style.css">
    <script defer src="../../../script.js"></script>
</head>
<body>
    <header class="site-header">
        <nav class="site-nav">

            <div class="nav-left">
                <a href="https://github.com/p4th4k?tab=repositories" target="_blank">Projects</a>
                <a href="https://p4th4k.github.io/writeUps/" target="_blank">Writeups</a>
            </div>

            <div class="nav-right">
                <a class="launch-link" href="https://github.com/p4th4k" target="_blank">Github ↗</a>
            </div>

        </nav>
    </header>
    <main class="article-shell">
        <a href="../../../index.html" class="back-link">
            ← All articles
        </a>

        <div class="meta">
            Date Published:  2026
        </div>

        <h1>
            Title
        </h1>

        <div class="article-content">
            <p>
                <b>Objective</b>: 
            </p>

            <h3>Table Of Contents</h3>

            <ol></ol>

            <div class="next" style="display: flex; justify-content: space-between;">
                <a href="../index.html" style="font-size: 1.1rem;">Previous Article</a>
                <a href="./1.html" style="font-size: 1.1rem;">Next Article</a>
            </div>
        </div>
    </main>
    <footer class="site-footer">
        <p>
            Made with ❤️ by <a href="https://github.com/p4th4k" target="_blank">p4th4k</a>
        </p>
    </footer>
</body>
</html>
"""

for phase in range(1,11):
    phase_dir = f"phase{phase}"
    os.makedirs(phase_dir, exist_ok=True)

    for article in phase_articles[phase]:
        file_path = os.path.join(phase_dir, f"{article}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template.format(article=article))

print("Done!")