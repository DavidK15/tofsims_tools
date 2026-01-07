import numpy as np

def sum_up(values):
"""
Demo Funktion
"""
return sum(values)

def normalize_spectrum(intensity):
	"""
	Normalisiert ein Intensitätsarray auf 1."
	"""
	intensity = np.asarray(intensity)
	total = np.sum(intensity)
	if total ==0:
		return intensity
	return intensity / total

def integrate_peak(mz, intensity, center, width):
	"""
	Integriert die Intensität um einen m/z-Wert (peak center) +- width/2.
	"""
	mz = np.asarray(mz)
	intensity = np.asarray(intensity)
	mask = (mz >= center - width/2) & (mz <= center + width/2)
	return np.sum(intensity[mask])

#Imaging TOF-SIMS

def sum_image_pixels(image_data):
	"""
	Summiert die Intensität aller Pixel eines 2D-Arrays.
	"""
	return np.sum(image_data)

def normalize_image(image_data):
	"""
	Normalisiert eine 2D-Array auf 1.
	"""
	image_data = np.asarray(image_data, dtype=float)
	total = np.sum(image_data)
	if total == 0:
		return image_data / total
	return image_data / total
