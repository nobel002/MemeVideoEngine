@echo %cd%
@cd ../generated/images
@del *.png -r
@echo cleared the images
@cd ../audio
@del *.mp3 -r
@echo removed all the audio files
@cd ../scripts
@del *.txt -r
@echo removed all the scripts
@cd ../videos
@del *.mp4 -r
@del *.avi -r
@echo removed all the video files
@echo finished cleaing up