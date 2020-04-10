import pyaudio

p = pyaudio.PyAudio()
for index, ii in enumerate(range(p.get_device_count())):
	print(index , p.get_device_info_by_index(ii).get('name')) 