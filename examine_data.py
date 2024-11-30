import xarray as xr

# Load the GRIB data file
data = xr.open_dataset("era5_spain.grib", engine="cfgrib")

# Print an overview of the dataset
print(data)
