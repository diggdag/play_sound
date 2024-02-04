# play_sound
ルームシェア特化のスマートホームソリューション
音（生活音）を定期的に流すだけ。音源は自分で用意して


Macをスリープにさせない
sudo pmset disablesleep 1

12:00から15分おきに3回サウンドを再生
./play_sound.py 12:00 15 3 /sound.mp3
