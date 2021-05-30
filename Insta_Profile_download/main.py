#pip install instaloader
import instaloader

Ig = instaloader.Instaloader()
pic = input("Enter Insta UserName: ")

Ig.download_profile(pic,profile_pic_only = True)
