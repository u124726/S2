import subprocess
import exercise_4
import exercise_6


class Seminar:

    # EXERCISE 1
    def macro_and_motion(input_video, output_video):
        """ Creates a new video from Big Buck Bunny video which show macro blocks and motion vectors using ffmpeg
            Args:
                input_video: 9 seconds of Big Buck Bunny video
                output_video: New video with macro blocks and motion vectors
        """
        ffmpeg_mm = [
            'ffmpeg',
            '-flags2',
            '+export_mvs',
            '-i', input_video,
            '-vf', f'codecview=mv=pf+bf+bb',
            output_video
        ]
        subprocess.run(ffmpeg_mm)

    #macro_and_motion('big_buck_bunny_9s.mp4', '/mnt/c/Users/dcabo/PycharmProjects/S2/bb_macro_motion.mp4')

    # EXERCISE 2
    def mono_stereo_aac(input_video, output_video, output_audio):
        """ Cut 50 seconds from BBB video and then exports audio files as MP3 mono track, MP3 stereo w/lower bitrate and AAC
        codec from this new video. All this files will be packaged in a .mp4 file using ffmpeg.
            Args:
                input_video: Big Buck Bunny video to be cut
                output_video: New video BBB video of 50 seconds
                output_audio: .mp3 audio from BBB video of 50 seconds
        """
        ffmpeg_cut = [
            'ffmpeg',
            '-i', input_video,
            '-ss', f'00:01:00',
            '-t', f'00:00:50',
            output_video
        ]
        ffmpeg_mp3 = [
            'ffmpeg',
            '-i', input_video,
            '-map', f'0:a',
            output_audio
        ]
        subprocess.run(ffmpeg_cut)
        subprocess.run(ffmpeg_mp3)

    # mono_stereo_aac('BBB.mp4', '/mnt/c/Users/dcabo/PycharmProjects/S2/BBB_50s.mp4','/mnt/c/Users/dcabo/PycharmProjects/S2/BBB_50s_.mp3')

    # EXERCISE 3
    def n_tracks(input_video):
        """ Counts the number of tracks from an input video
            Args:
                input_video: Video to be read
        """
        ffmpeg_tracks = [
            'ffprobe',
            '-i', input_video,
            '-show_streams',
            '-select_streams', f'a:0',
        ]
        subprocess.run(ffmpeg_tracks)

    # n_tracks('BBB.mp4')

    """Podemos ver que el número de tracks para nuestro vídeo quedara definido en la info mostrada en nuestro
     vídeo como channels=2"""

    # EXERCISE 5
    #exercise_4.subtitles('chistes.mp4', 'subtitles.txt', '/mnt/c/Users/dcabo/PycharmProjects/S2/chistes_sub.mp4')

    # EXERCISE 6
    #exercise_6.yuv_hist('BBB.mp4', '/mnt/c/Users/dcabo/PycharmProjects/S2/BBB_hist.mp4')







