from youtube_transcript_api import YouTubeTranscriptApi
import subprocess


# EXERCISE 4
def subtitles(input_video, subs, output_video):
    """ Download subtitles from a Youtube video and integrate them into another one as a separate optional sub track
        Args:
            input_video: Video without subtitles
            subs: Subtitles generated from ID input video
            output_video: New video with subtitles integrated
    """
    srt = YouTubeTranscriptApi.get_transcript('1q_kuGvj308', languages=['es'])

    with open("subtitles.txt", "w") as f:
        for i in srt:
            f.write("{}\n".format(i))

    ffmpeg_sub = [
        'ffmpeg',
        '-i', input_video,
        '-i', subs,
        '-c', f'copy',
        '-c:s', f'mov_text',
        output_video
    ]

    subprocess.run(ffmpeg_sub)



