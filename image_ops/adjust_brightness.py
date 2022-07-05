import numpy as np

def op_adjust_brightness(image, bright_factor):
    out = np.clip(image + bright_factor, 0.0, 1.0)
    return out

if __name__ == "__main__":
    a = np.random.rand(3, 3, 3)
    print(a)
    print(op_adjust_brightness(a, 0.4))