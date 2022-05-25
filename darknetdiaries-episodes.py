#!/usr/bin/python3

#----------------------------------------------------
# Download all Episodes from Darknet Diaries Podcast
# Author : @Maakthon
#---------------------------------------------------

from requests import get
from bs4 import BeautifulSoup as soup
# Generate a various user-agents to bypass detection or prevention
from faker import Faker

fk = Faker()
epiLink   = "https://darknetdiaries.com/episode/"
megaphone = "https://traffic.megaphone.fm/"
mp3       = ".mp3"

def EpiNums(epiLink):
	# Get numbers of total episodes
	headers     = {"User-Agent":fk.user_agent()}
	response    = get(epiLink , headers=headers)
	htmlContent = soup(response.content , "html.parser")
	numberOfEpi = int(htmlContent.find_all("a" , {"class":"button-light"})[0]["href"].split("/")[-2])

	return numberOfEpi

episodes = EpiNums(epiLink)

def downloadEpi(episodes , epiLink , megaphone , mp3):

	print(f"[+] Number of total episodes {episodes}\n")

	for epi in range(1,episodes+1):
		headers     = {"User-Agent":fk.user_agent()}
		fullLink    = epiLink + str(epi)
		response    = get(fullLink , headers=headers)
		htmlContent = soup(response.content , "html.parser")
		title       = str(htmlContent.find("title").text)
		mediaName   = str(htmlContent.find("code").text.split()[-2].split("\"")[-2].split("=")[-1])
		downLink    = megaphone + mediaName + mp3
		media       = get(downLink , headers = headers)

		with open(title , "wb") as f:
			f.write(media.content)
			f.close()
		print(epi , end=" ")

downloadEpi(episodes , epiLink , megaphone , mp3)
