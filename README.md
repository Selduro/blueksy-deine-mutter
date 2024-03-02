# blueksy-deine-mutter
Skript, zum automatisierten Posten von vorgefertigten Texten auf Bluesky. Es liest aus einer Zeile, beginnend bei 1, den Text der Zeile und postet diesen. Bei der nächsten Ausführung wird der Text der nächsten Zeile gepostet.
Voraussetzungen: 
1. Python3 und zugehöriges pip ist installiert
2. atproto installieren: "pip install atproto" ins terminal
3. Die Dateien "create_post.py" und "deine_mutter_witze.txt"  und "create_cronjob.py" befinden sich im selben Verzeichnis
4. Im Skript (Bearbeiten mit einem Texteditor) Nutzername und Passwort anpassen und anschließend speichern.
5. In der Witze-Textdatei steht genau ein Witz pro Zeile. Zeilenumbrüche innerhalb eines Witzes funktionieren nicht, weil das Skript immer genau eine Zeile postet. Daher auch Leerzeilen am Ende der Datei vermeiden.
6. Für Automatisierung einen cronjob einrichten: 
6.1 Im Verzeichnis, in dem die Dateien liegen "chmod +x create_post.py" ins terminal
6.2 cronjob erstellen: "python create_cronjob.py" ins terminal, das erstellt den cronjob. Dann wird jeden Abend um 20 Uhr gepostet. Sollte das anders gewünscht sein, danach per "crontab -e" die Zeiten anpassen. https://crontab.guru
