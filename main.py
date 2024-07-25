import cv2
import colorsys
from sklearn.cluster import KMeans


def main():
    img_path   = "icon.jpg"
    main_color = get_main_color_from_image(img_path)

    print(main_color)


def hex_2_rgb(hex_color):
    """
    HEXカラー ->> RGB
    """

    hex_color = hex_color.lstrip('#')

    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_most_colorful_color(hex_colors):
    """
    独断と偏見で最も鮮やかだと思った色を選ぶ
    彩度(S) * 明度(V) (HSVカラースペース)
    """

    max_colorfulness    = -1
    most_colorful_color = None

    for hex_color in hex_colors:
        rgb = hex_2_rgb(hex_color)
        hsv = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
        colorfulness = hsv[1] * hsv[2]
        if colorfulness > max_colorfulness:
            max_colorfulness    = colorfulness
            most_colorful_color = hex_color

    return most_colorful_color


def get_main_color_from_image(img_path):
    """
    KMeansクラスタリングで画像の主要な色を選ぶ
    """

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=5, n_init=10)
    kmeans.fit(img)
    cluster_centers = kmeans.cluster_centers_.astype(int)

    hex_colors = ['#{:02x}{:02x}{:02x}'.format(*rgb) for rgb in cluster_centers]

    most_vibrant_color = get_most_colorful_color(hex_colors)

    return most_vibrant_color


if __name__ == '__main__':
    main()
