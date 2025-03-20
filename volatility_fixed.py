import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from scipy.interpolate import griddata


class VolatilitySurface:
    def __init__(self):
        self.data = pd.DataFrame(
            columns=['strike', 'time_to_expiry', 'implied_vol']
        )
    
    def add_option_data(self, strike, time_to_expiry, implied_vol):
        new_data = pd.DataFrame({
            'strike': [strike],
            'time_to_expiry': [time_to_expiry],
            'implied_vol': [implied_vol]
        })
        self.data = pd.concat([self.data, new_data], ignore_index=True)

    def generate_surface(self):
        min_strike = min(self.data['strike'])
        max_strike = max(self.data['strike'])
        strike_grid = np.linspace(min_strike, max_strike, 50)
        
        min_time = min(self.data['time_to_expiry'])
        max_time = max(self.data['time_to_expiry'])
        time_grid = np.linspace(min_time, max_time, 50)
        
        strike_mesh, time_mesh = np.meshgrid(strike_grid, time_grid)

        vol_surface = griddata(
            (self.data['strike'], self.data['time_to_expiry']),
            self.data['implied_vol'],
            (strike_mesh, time_mesh),
            method='cubic'
        )
        return strike_mesh, time_mesh, vol_surface
    
    def plot_surface(self):
        strike_mesh, time_mesh, vol_surface = self.generate_surface()

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        surf = ax.plot_surface(
            strike_mesh,
            time_mesh,
            vol_surface,
            cmap='viridis',
            edgecolor='none'
        )

        ax.set_xlabel('Strike Price')
        ax.set_ylabel('Time to Expiry')
        ax.set_zlabel('Implied Volatility')
        ax.set_title('VolatilitySurface')

        plt.colorbar(surf)
        plt.show()

    def get_volatility(self, strike, time_to_expiry):
        strike_mesh, time_mesh, vol_surface = self.generate_surface()
        return griddata(
            (strike_mesh.flatten(), time_mesh.flatten()),
            vol_surface.flatten(),
            (strike, time_to_expiry),
            method='cubic'
        )
    

def main():
    vol_surface = VolatilitySurface()
    # sample data that can be replaced with market data
    sample_data = [
        (90, 0.1, 0.25),
        (90, 0.5, 0.23),
        (100, 0.1, 0.20),
        (100, 0.5, 0.18),
        (110, 0.1, 0.22),
        (110, 0.5, 0.20),
        (95, 0.3, 0.24),
        (105, 0.3, 0.21)
    ]
    # To add sample data
    for strike, expiry, vol in sample_data:
        vol_surface.add_option_data(strike, expiry, vol)

    vol_surface.plot_surface()

    sample_strike = 102
    sample_expiry = 0.4
    vol = vol_surface.get_volatility(sample_strike, sample_expiry)
    print(
        f"Implied volatility at strike {sample_strike} "
        f"and expiry {sample_expiry}: {vol:.4f}"
    )


if __name__ == "__main":
    main()