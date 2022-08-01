from googleapiclient.discovery import build
YOUTUBE_API_KEY='AIzaSyCvAw9tOLLFHQsO0Z_ebdkpoQdMF1AU5D4'

youtube = build('youtube','v3',developerKey=YOUTUBE_API_KEY)

request = youtube.channels().list(
    part='statistics',
    forUsername='UCHGcYSa023cReUOAXDE0pnw'
)

response = request.execute()
print(response)