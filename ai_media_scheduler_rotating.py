
import os
import datetime
import schedule
import time
import threading
import random
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate audio/video/pdf play
def simulate_play(file):
    print(f"🎵 Simulated Playing: {file['path']}")

# Simulated AI summary for PDF
def summarize_pdf(file_path):
    return "This is a simulated summary of the PDF."

# Log storage
media_log = []

# Your list of media files
media_schedule = [
    {"title": "Day 1", "type": "audio", "path": "/content/drive/MyDrive/MediaSchedulerApp/audio1.mp3"},
    {"title": "Day 2", "type": "video", "path": "/content/drive/MyDrive/MediaSchedulerApp/video1.mp4"},
    {"title": "Day 3", "type": "pdf", "path": "/content/drive/MyDrive/MediaSchedulerApp/doc1.pdf"},
    {"title": "Day 4", "type": "audio", "path": "/content/drive/MyDrive/MediaSchedulerApp/audio2.mp3"},
    {"title": "Day 5", "type": "pdf", "path": "/content/drive/MyDrive/MediaSchedulerApp/doc2.pdf"},
]

def get_next_media():
    # Rotate based on log length (simulate "new day")
    current_index = len(media_log) % len(media_schedule)
    return media_schedule[current_index]

def log_play(file):
    media_log.append({
        "title": file["title"],
        "type": file["type"],
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": "Played"
    })

def play_media():
    file = get_next_media()
    simulate_play(file)
    log_play(file)
    if file["type"] == "pdf":
        summary = summarize_pdf(file["path"])
        print(f"📄 Summary: {summary}")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Set for 1-minute interval for demo
schedule.every(1).minutes.do(play_media)

# Start scheduler thread
threading.Thread(target=run_schedule, daemon=True).start()

# Dashboard
def show_log():
    df = pd.DataFrame(media_log)
    display(df)
    return df

def show_dashboard():
    df = pd.DataFrame(media_log)
    if df.empty:
        print("No media played yet.")
        return
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    plt.figure(figsize=(8,4))
    sns.countplot(data=df, x='date', hue='type')
    plt.title("Media Summary by Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print("\nSummary Stats:")
    print("- Total sessions:", len(df))
    print("- Unique days used:", df['date'].nunique())
    print("- Media breakdown:")
    print(df['type'].value_counts())

def export_usage():
    df = pd.DataFrame(media_log)
    df.to_csv("/content/drive/MyDrive/MediaSchedulerApp/media_usage_log.csv", index=False)
    print("✅ Usage log saved as 'media_usage_log.csv'")
