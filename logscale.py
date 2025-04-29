import pandas as pd
import matplotlib.pyplot as plt

# Load Excel sheet (with headers in first row)
df = pd.read_excel(r"C:\Users\asust\Desktop\Book1.xlsx")  # Use raw string to avoid unicode escape error

# Replace 'Frequency' and 'Gain' with your actual column headers
frequency = df['Frequency']
gain = df['Gain']

# Plotting
plt.figure(figsize=(8, 5))
plt.semilogx(frequency, gain, marker='o', linestyle='-', color='b')
plt.title("Frequency Response of Low-Pass Filter")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (V/V or dB)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Save plot as PNG
plt.savefig("low_pass_filter_response.png", dpi=300)

# Show plot
plt.show()
