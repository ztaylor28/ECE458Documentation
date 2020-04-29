import os
import numpy
import PILasOPENCV as OpenCV
import scenedetect
import tqdm
import ffmpeg
import click
from moviepy.editor import *

def main():

    # Executing Directory where .mp4 files have been placed
    directory = "C:\\Users\\kevin\\PycharmProjects\\commercialDetector"

    # i is iterated for each .mp4 file in order to change the name of the commercial-less files
    i = 1

    # For each file in the provided directory..
    for filename in os.listdir(directory):

        # if it is a .mp4 file, call scenedetect using detect-threshold to detect black frames
        # -t: rgb value that frame must be to be considered "black
        # -p:  Percent (%) from 0 to 100 of amount of pixels
        # that must meet the threshold value in order to trigger a scene change.  [default: 95]
        # -m: Minimum size/length of any scene, in number of frames.  [default: 15]
        if filename.endswith(".mp4"):
            os.system("scenedetect -i {} detect-threshold -t 0 -p 99 -m 4000 list-scenes split-video".format(filename))

            # X is used to skip the first "scene" of the .mp4, and alternate which scenes are to be kept,
            # First scene being a show, then to commercial, and alternating. Odd scene #'s = show, Even scene #'s = commercial
            # L is used to store all show scenes of the .mp4
            x = False
            L = []

            # For each scene .mp4 in the directory, delete the even #'d scenes and keep the odd #'d
            for filename in os.listdir(directory):
                if filename.endswith(".mp4") and filename.__contains__("Scene"):
                    if x == True and filename.__contains__("Scene") and filename.endswith(".mp4"):
                        os.unlink(os.path.join(directory, filename))
                        print("Deleted...", os.path.join(directory, filename))
                        x = False
                    else:
                        print(os.path.join(directory, filename))
                        x = True

            # For each even #'d scene, store them into L
            for filename in os.listdir(directory):
                if filename.__contains__("0") and filename.endswith("mp4"):
                    filePath = os.path.join(directory, filename)
                    video = VideoFileClip(filePath)
                    L.append(video)

            # Create name of the commercial-less final video -> Final_#.mp4
            vidName = "Final_" + str(i) + ".mp4"

            # Using moviepy.editor, append the contents of L to one another and create the Final_#.mp4 file
            finalVideo = concatenate_videoclips(L)
            finalVideo.to_videofile(vidName, fps=30, remove_temp = False)
            i = i + 1

            # Remove all scenes and statistic.csv files before continuing to the next available .mp4 file for commercial removal
            for filename in os.listdir(directory):
                if filename.__contains__("Scene") or filename.endswith(".mp3"):
                    os.unlink(os.path.join(directory,filename))

        # If the video file is not int the desired format, provide the user with an error
        # message and continue onto the next available .mp4 file
        elif filename.endswith(".mov") or filename.endswith(".wmv") or filename.endswith(".flv") or filename.endswith(".avi"):
            print("\n!!! Error: Please use .mp4 format to eliminate commercials. !!!! \nMoving to next available .mp4 file...\n")
main()