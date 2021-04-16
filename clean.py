import re
import matplotlib.pyplot as plt


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result


def blur_image():
    img = plt.imread('dc_metro.png')
    plt.imshow(img, cmap=plt.cm.hot)

    blurred = 0

    plt.figure()
    plt.imshow(blurred, cmd=plt.cm.hot)

    plt.show()


states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia',
          'FlOrIda', 'south   carolina##', 'West virginia?']

# print(clean_strings(states))
blur_image()
