#!/bin/sh

# 現在時刻を取得
filename=`date +"%y_%m%d__%H%M%S"`

#拡張子
ext=paste

# クリップボードの中身をリダイレクト
pbpaste > $filename.$ext

# 間違えて上書きしてしまう状態を防止
chmod 555 $filename.$ext
