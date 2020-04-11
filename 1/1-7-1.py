def time_data(x, y, z):
    return f"{x}時の{y}は{z}"

if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4
    result = time_data(x, y, z)
    print(result)