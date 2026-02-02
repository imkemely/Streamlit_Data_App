# Biscayne Bay Water Quality Dashboard

An interactive Streamlit web application for visualizing and analyzing water quality data from Biscayne Bay, Florida.

## Project Description

This dashboard provides an interface for exploring environmental monitoring data collected from Biscayne Bay. The application allows users to view and analyze various water quality parameters including temperature, pH levels, dissolved oxygen concentrations, and the geographic distribution of sampling locations. Additionally, the dashboard integrates with NASA's Astronomy Picture of the Day API to display daily astronomical imagery.

## Dataset Information

The dataset used in this project contains water quality monitoring data from Biscayne Bay. The CSV file includes the following parameters:

- Temperature measurements in Celsius
- pH levels
- Dissolved oxygen concentration (ODO) in mg/L
- Geographic coordinates (Latitude and Longitude)
- Total water column depth in meters
- Time-series data for tracking changes over time

The data file is named biscayneBay_waterquality.csv and must be placed in the same directory as the main application file.

## Features

The dashboard includes several key features:

- Interactive tab-based navigation system
- Display of raw data and descriptive statistics
- Time series visualization showing temperature trends over time
- Scatter plot analysis showing the relationship between dissolved oxygen and temperature, with pH indicated by color
- Three-dimensional geographic visualization of sampling locations and water depth
- Integration with NASA's API to display the Astronomy Picture of the Day

## Installation Instructions

To run this application locally, follow these steps:

1. Ensure you have Python 3.8 or higher installed on your computer

2. Clone or download this repository to your local machine

3. Install the required Python packages by running:
   pip install -r requirements.txt

4. Create a .env file in the project directory and add your NASA API key:
   NASA_API_KEY=your_api_key_here
   
   You can obtain a free NASA API key by visiting https://api.nasa.gov/

5. Make sure the biscayneBay_waterquality.csv file is in the same directory as dashboard.py

## Running the Application

Once installation is complete, you can run the application using one of the following commands:

streamlit run dashboard.py

Or alternatively:

python -m streamlit run dashboard.py

The application will open in your default web browser. If it does not open automatically, navigate to http://localhost:8501 in your browser.

## User Instructions

The dashboard is organized into four main sections accessible through tabs at the top of the page:

Descriptive Statistics: This tab displays the complete dataset in table format along with summary statistics including mean, standard deviation, minimum, and maximum values for all numeric variables.

2d Plots: This section contains two visualizations. The first is a line chart showing temperature changes over time. The second is a scatter plot that displays the relationship between dissolved oxygen levels and temperature, with points colored by pH level.

3d Plots: This tab presents a three-dimensional scatter plot showing the geographic distribution of sampling locations. The z-axis represents water depth and is reversed to show depth below the surface.

NASA's Astronomy APOD: This final tab displays NASA's Astronomy Picture of the Day, including the image, title, date, and a detailed explanation of the astronomical phenomenon shown.


## Development Approach

This project was developed using Agile software development principles. The work was broken down into manageable tasks, with regular testing and refinement of features. Development followed an iterative approach, allowing for continuous improvement and integration of new functionality.
