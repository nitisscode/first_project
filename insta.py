import instaloader

ig=instaloader.Instaloader()

#print("******Login please!******")
#user_name=input("Enter your insta id:")
#password=input("Enter your Password:")

profile=input("Enter client Username: ")

print("Downloading...")

ig.download_profile(profile,profile_pic_only=True)
print("Download Completed")


