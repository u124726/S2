import subprocess


# EXERCISE 6
def yuv_hist(input_video, output_video):
    """ Extract YUV histogram from an input video and outputs another one with histogram displayed
        Args:
            input_video: Video to extract YUV histogram
            output_video: New video with histogram displayed
    """

    ffmpeg_yh = [
        'ffmpeg',
        '-i', input_video,
        '-vf', f'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay',
        output_video
    ]

    subprocess.run(ffmpeg_yh)


