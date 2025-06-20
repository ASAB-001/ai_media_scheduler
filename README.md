AI Media Scheduler

Smart daily playback of your favorite media, powered by AI + Data Science.

   

---

Overview

This project schedules and rotates audio, video, and PDF files for daily playback. Each file is played once per day, and if it’s a PDF, it gets summarized using AI (Hugging Face Transformers). It logs user progress, reminds daily, tracks streaks, and visualizes media usage.

Great for learners, daily routines, or productivity playlists.


---

Features

Plays one media file daily (audio/video/pdf)

AI-powered summaries for PDF documents

Rotates through media files, one per day 


(Here's How It Works (Demo Mode):

Every 1 minute, it simulates a “new day”

It automatically picks the next file in the list

So in a 3-minute demo, it can play 2–3 files!

In real life, this runs daily at your chosen time. But here, I’ve set it to run every minute for demonstration.
)

Daily scheduler with reminders (simulated in Colab. I used colab because my system is to slow to run the program on local drive)

Dashboard with usage visualizations

Daily streak tracking

Media-type recommendation based on usage

AI-generated tags from summarized content

CSV export of activity log



---

How to Use (Google Colab)

1. Mount your Google Drive



from google.colab import drive
drive.mount('/content/drive')

2. Upload your audio/video/pdf files to a folder like:



/content/drive/MyDrive/MediaSchedulerApp/

3. Replace media_schedule with paths to your files.


4. Run the scheduler. It simulates daily playback.




---

Files in the Repo

File	Description

ai_media_scheduler.py	Full source code (Colab or local)
README.md	This file
requirements.txt	List of required Python packages



---

Example Visualizations

Media Type Usage by Date (auto-generated with show_dashboard())

Text summaries from your PDFs

User engagement streak



---

Dependencies

Install all at once:

pip install -r requirements.txt

Or manually:

pip install transformers PyPDF2 schedule matplotlib seaborn pandas


---

Hashtags for Contest

#3MTTLearningCommunity #My3MTT #AIProject #PythonApp #MediaScheduler


---

Author

Abubakar Saleh Adam 


For 3MTT Knowledge Showcase 


---

License

Free to use, remix, and extend for learning and non-commercial purposes.


---

> By Abubakar Saleh Adam & Chatgpt Open AI, for smart learning and time mastery.



