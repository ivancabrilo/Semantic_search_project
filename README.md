I built a youtube search tool using cosine similarity (trained on titles and transcripts of each video) for a Kurtzgesagt youtube channel. The results are based on the similarity between user's input query with combination of transcripts and titles. I made an API out of this cosine similarity model using FastAPI, containzeried it, and posted it on Docker Hub, from where I was able to make an AWS ECS instance that hosts access to my model's API


![ScreenRecording2025-08-25at1 12 54PM-ezgif com-optimize](https://github.com/user-attachments/assets/39e6b115-3390-4651-86f7-848f96af763a)

