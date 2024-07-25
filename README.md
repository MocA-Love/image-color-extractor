# What's up

画像ファイルから主な色を抽出し、独断と偏見で最も鮮やかなだと思う色を特定。
KMeansクラスタリングを使用して画像内の主要な色を抽出後にHSVカラースペースで評価。

## Requirement
Python 3.8.10

- OpenCV
- scikit-learn
- colorsys（標準lib）

```bash
pip install opencv-python scikit-learn
```