
import datetime
from pathlib import Path

TEMPLATE_PATH = Path("templates/base.md")
NOTES_DIR = Path("notes")

def create_note():
    today = datetime.date.today().isoformat()
    note_path = NOTES_DIR / f"{today}.md"

    if note_path.exists():
        print(f"📒 Note for {today} already exists at {note_path}.")
        return

    if not NOTES_DIR.exists():
        NOTES_DIR.mkdir(parents=True)

    if TEMPLATE_PATH.exists():
        content = TEMPLATE_PATH.read_text()
    else:
        content = f"# {today} – Daily Note\n\n- Mood: \n- Tasks: \n- Ideas: \n"

    note_path.write_text(content)
    print(f"✅ Note created: {note_path}")

if __name__ == "__main__":
    create_note()
