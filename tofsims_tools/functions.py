import numpy as np

def normalize_spectrum(intensity):
	intensity = np.asarray(intensity)
	return intensity / np.sum(intensity)

def interate_peak(mz, intensity, center, width):
	mz = np.asarray(mz)
	intensity = np.asarray(intensity)
	mask = (mz >= center - width/2) & (mz <= center + width/2)
	return np.sum(intensity[mask])