# Volatility Surface Analyzer

This project provides a Python implementation of a volatility surface for analyzing stock options data. It constructs a 3D surface of implied volatility across different strike prices and times to expiration, useful for options pricing, risk management, and market analysis.

Features
----------
Add options data (strike price, time to expiry, implied volatility).
Generate an interpolated volatility surface using cubic interpolation.
Visualize the surface in a 3D plot.
Query volatility for specific strike/expiry combinations.

Requirements
--------------
Python 3.x
Libraries: numpy, pandas, matplotlib, scipy

Installation
--------------
Clone or Download:
Download the project files: volatility_surface.py and example_usage.py.
Set Up a Virtual Environment (recommended):
python -m venv vol_surface_env

Activate it:
--------------
Windows: vol_surface_env\Scripts\activate
macOS/Linux: source vol_surface_env/bin/activate

Install Dependencies:
------------------------
pip install numpy pandas matplotlib scipy
Project Structure
volatility_surface.py: Contains the VolatilitySurface class with core functionality.
example_usage.py: Demonstrates how to use the class with sample data.
Usage

Run the Example:
------------------
Ensure both files are in the same directory.
Activate your virtual environment (if using one).

Run:
-----
python example_usage.py
This will:
Create a volatility surface with sample data.
Display a 3D plot.
Print an interpolated volatility value for a specific strike and expiry.

Customize:
--------------
Edit example_usage.py to use real options data (e.g., from a market data provider).
Modify strike prices, times to expiry, and implied volatilities in the sample_data list.
Use the Class in Your Own Code:
python


from volatility_surface import VolatilitySurface

vol_surface = VolatilitySurface()
vol_surface.add_option_data(100, 0.5, 0.20)  # strike, expiry, volatility
vol_surface.plot_surface()  # visualize
vol = vol_surface.get_volatility(102, 0.4)  # query a point
print(vol)

Example Output
---------------
A 3D plot showing implied volatility (z-axis) against strike prices (x-axis) and time to expiry (y-axis).
Sample console output:


Implied volatility at strike 102 and expiry 0.4: 0.1987

Notes
-------
The sample data in example_usage.py is hardcoded. Replace it with real market data for practical use.
The surface uses cubic interpolation; you can adjust the method (e.g., to 'linear') in volatility_surface.py if needed.
Future Enhancements
Add support for live data feeds (e.g., via APIs like Yahoo Finance).
Include volatility smile/skew analysis.
Export surface data to CSV or other formats.

License
---------
This project is unlicensed—feel free to use and modify it as you see fit.

