import matplotlib.pyplot as plt

k1 = 0.01

timesteps = [i for i in range(0, 10001, 10)]
model = [i * k1 for i in timesteps]
val = 2
model_upper = [i + val for i in model]
model_lower = [i - val for i in model]

t1 = 100
t2 = 2400

plt.plot(timesteps, model, label="Model")
plt.plot(timesteps, model_upper, "r--", label="Bounds")
plt.plot(timesteps, model_lower, "r--")
plt.vlines([t1, t2], 0, 100, linestyles="dashed", colors="gray")
plt.legend()
plt.title("Model bounds visual test")
plt.xlabel("Time [s]")
plt.ylabel("Percentage of pixels crossing the COC [%]")
plt.xlim(0, 10000)
plt.ylim(0, 100)
plt.show()
