# -*- coding: utf-8 -*-
import json
import re
import requests


def get_video_length(video_id):
    api_key = "AIzaSyCKsLGM632TYM8PyJ-ohQb3u-L9D6twQNE"
    searchUrl = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=contentDetails"

    response = requests.get(searchUrl)
    data = json.loads(response.text)

    all_data = data['items']
    contentDetails = all_data[0]['contentDetails']
    duration = contentDetails['duration']

    hour = re.findall('[0-9]+H', duration)
    minute = re.findall('[0-9]+M', duration)
    second = re.findall('[0-9]+S', duration)

    return_list = []
    if len(hour) == 0:
        return_list.append(0)
    else:
        return_list.append(int(hour[0][:-1]))

    if len(minute) == 0:
        return_list.append(0)
    else:
        return_list.append(int(minute[0][:-1]))

    if len(second) == 0:
        return_list.append(0)
    else:
        return_list.append(int(second[0][:-1]))

    return return_list


print(get_video_length('ECI_1WAKEaY'))
