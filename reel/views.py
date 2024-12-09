import instaloader
import time
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from fake_useragent import UserAgent
from .serializers import ReelDownloadSerializer
from django.http import JsonResponse
import os
import shutil

class ReelDownloadAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReelDownloadSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            if not url:
                return JsonResponse({'error': 'URL is required'}, status=400)
            try:
                ua = UserAgent()
                headers = {'User-Agent': ua.random}
                L = instaloader.Instaloader()

                # Random delay to mimic human behavior
                time.sleep(random.uniform(2, 5))

                # Extract shortcode from the URL (Instagram posts have unique shortcodes in their URLs)
                shortcode = url.split("/")[-2]

                # Download the Instagram post (this works for reels as well)
                post = instaloader.Post.from_shortcode(L.context, shortcode)

                # Define the download directory and file name
                download_dir = os.path.join('media', 'reels')
                os.makedirs(download_dir, exist_ok=True)  # Create the directory if it doesn't exist
                reel_file_path = os.path.join(download_dir, f'{shortcode}.mp4')

                # Temporarily download the post to a directory
                temp_download_path = shortcode
                os.makedirs(temp_download_path, exist_ok=True)
                L.download_post(post, target=temp_download_path)

                # Find the downloaded file and move it to the desired location
                for root, dirs, files in os.walk(temp_download_path):
                    for file in files:
                        if file.endswith('.mp4'):
                            shutil.move(os.path.join(root, file), reel_file_path)
                            break

                # Clean up the temporary directory
                shutil.rmtree(temp_download_path)

                # Build the full URL for the downloaded video
                video_url = request.build_absolute_uri('/' + reel_file_path.replace('\\', '/'))

                return Response({"message": "Reel downloaded successfully!", "video_url": video_url}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
