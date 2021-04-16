# TODO

## top priority

- add support for gifs
- extract all the text from all the memes (and sinq the text xith the images)
- print that to one file
- save the audio which was generated from the [voice synht](voiceSynth.py)
- combine the audio and video
- convert to mp4
- remove all the extra files like the [images](generated/images), [audio](generated/audio) and the [script](generated/scripts)
- Figure out a better way to store images right before stichingthem together in a video, maybe yb loading in one image at a time and stiching that together as a video. Also find a better way to set the framerate and display time for each meme. This solution shoulld also allow for theincorperation of memes, the minimum frame rate of a final video should be thirty or twenty four fps. So a very bad byut simple solution could be to generate a video frame by frame. Thus allowing for .gif formmats, video's and so on, and a better time controle. At the cost of a huge scrach disk. So i may need to find a way aroud that.
- find a way to sinc the audio with the video, for a set duration per meme we could compare the time of the audio file wioth the given display time of each meme, there for we only need to wory about that. For the frame by frame methode you can use 1/frame rate and multiply by tha amont of rames and so calculate the exact T+ of each meme.

## extra

- update the readme
- find a better voice synth
- add proper documentation
