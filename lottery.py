import random
import time
import sys

def animate_lottery(duration=2.5):
    """
    帶動畫效果的抽籤程序
    duration: 動畫持續秒數（預設2.5秒）
    """
    result = random.randint(1, 22)
    
    print("\n" + "="*40)
    print("🎰 開始抽籤 🎰".center(40))
    print("="*40 + "\n")
    
    start_time = time.time()
    speed = 0.05  # 初始速度
    current_num = 1
    
    # 動畫循環
    while time.time() - start_time < duration:
        # 隨機跳轉號碼
        current_num = random.randint(1, 22)
        
        # 清除上一行並顯示當前號碼
        print(f"\r   當前號碼: {current_num:2d}", end="", flush=True)
        
        # 動畫加速效果：後期動畫更快
        elapsed = time.time() - start_time
        progress = elapsed / duration
        current_speed = speed * (1 - progress * 0.7)  # 逐漸加速
        time.sleep(current_speed)
    
    # 清除動畫行，顯示最終結果
    print("\r" + " " * 30 + "\r", end="")
    
    # 顯示最終結果
    print("\n" + "="*40)
    print(f"✨ 恭喜！抽到的號碼是: {result} ✨".center(40))
    print("="*40 + "\n")
    
    return result

if __name__ == "__main__":
    print("歡迎使用1到22號抽籤系統！")
    input("按 Enter 開始抽籤...")
    
    animate_lottery(duration=2.5)