import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Hàm đọc dữ liệu từ file CSV
def load_data(file_path="F:/Mang_MTVTSL/sensor_data.csv"):
    # Đọc file CSV, chuyển đổi cột 'timestamp' sang kiểu datetime
    try:
        data = pd.read_csv(file_path, parse_dates=['timestamp'])  # Fixed syntax
        return data
    except Exception as e:
        print("Lỗi đọc dữ liệu:", e)  # Fixed Vietnamese text
        return None

# Hàm cập nhật biểu đồ, được gọi định kỳ bởi FuncAnimation
def animate(i):
    data = load_data()
    if data is None or data.empty:
        print("Không có dữ liệu")  # Fixed Vietnamese text
        return
    
    # Lấy dữ liệu thời gian, nhiệt độ và độ ẩm
    x = data['timestamp']
    y_temp = data['temperature']
    y_humid = data['humidity']
    
    # Xóa biểu đồ cũ
    plt.cla()  # Fixed indentation

    # Vẽ biểu đồ nhiệt độ
    plt.plot(x, y_temp, label='Temperature (°C)', color='red', marker='o')  # Fixed parameters
    
    # Vẽ biểu đồ độ ẩm
    plt.plot(x, y_humid, label='Humidity (%)', color='blue', marker='x')  # Fixed parameters
    
    # Định dạng trục x cho dễ đọc: xoay nhãn thời gian
    plt.xticks(rotation=45, ha="right")  # Fixed parameter name
    
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Real-Time IoT Sensor Data")
    plt.legend(loc="upper left")  # Fixed function name
    plt.tight_layout()  # Điều chỉnh bố cục cho gọn

# Tạo figure cho biểu đồ
fig = plt.figure()

# Thiết lập animation: mỗi 5000 ms (5 giây) cập nhật lại biểu đồ
ani = FuncAnimation(fig, animate, interval=5000)
plt.show()