# 検索技術_期末レポート提出
21X3012　イ　ジョンアン

## データの説明
　データセットとして、TOPIX(東証株指環)とSAMSUNG Electronicsの2013/7/22から2023/7/20までの日付別終値を使用した。TOPIXの金額の単位はJPYで、SAMSUNG Electronicsの金額の単位はKRWである。

## 手法の説明
　手法としてLSTM(Long Short-Term Memory)を使用した。LSTMは循環ニューラルネットワーク(RN, Recurrent Neural Network)の一種で、シーケンスデータをモデリングし長期依存性を処理することに特化した人工ニューラルネットワークの一つだ。LSTMは前の時間段階の情報を記憶し、長期的な依存性を把握するのに役立つメモリセル構造を持っている。

## 手法を選んだ理由
　株価データは時間とともに順次的な特性を持っており、過去の価格動向が未来の価格変動に影響を及ぼす。LSTMはこのような長期依存性をキャプチャーし、以前の時間段階の情報を効果的に記憶して株価予測が可能であると考えられた。

## ダウンロード
　pythonのversionは3.10を使用した。
```
git clone https://github.com/bamtor1190/Serching-Technology.git
cd Serching-Technology
```
```
pip install -r requirements.txt
```
