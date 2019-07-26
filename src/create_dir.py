import os

if __name__ == '__main__':
    try:
        os.makedirs('postgres-data')
    except FileExistsError:
        pass
