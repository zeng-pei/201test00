import random

def draw_lottery():
    """
    從1到23中隨機抽取一個數字。
    """
    return random.randint(1, 23)

if __name__ == "__main__":
    print("歡迎使用1到23抽籤系統！")
    result = draw_lottery()
    print(f"抽到的號碼是：{result}")