import cdsapi

# Initialize the CDS API client
c = cdsapi.Client()

# Parameters for the request
dataset = "reanalysis-era5-single-levels"
variables = [
    "2m_temperature",
    "total_precipitation",
    "2m_dewpoint_temperature",
    "mean_sea_level_pressure",
    "total_cloud_cover",
    "volumetric_soil_water_layer_1",
    "evaporation",
    "10m_u_component_of_wind",
    "10m_v_component_of_wind"
]
years = [str(year) for year in range(2019, 2024)]  # Last 10 years
times = ["00:00", "12:00"]  # 3 datapoints per day
area = [44, -10, 36, 4]  # North, West, South, East (Spain and surrounding areas)

# Build the request
request = {
    "product_type": "reanalysis",  # Correct type
    "format": "grib",  # Output format
    "variable": variables,
    "year": years,
    "month": [f"{i:02d}" for i in range(1, 13)],  # All months
    "day": [f"{i:02d}" for i in range(1, 32)],    # All days
    "time": times,
    "area": area,  # [N, W, S, E]
    "grid": [1, 1]  # Reduced spatial resolution
}

# Output target file
target = "era5_spain.grib"

# Retrieve the data
c.retrieve(dataset, request, target)
