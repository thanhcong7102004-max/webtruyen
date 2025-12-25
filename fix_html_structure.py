import re
import os

# Danh sách các file cần sửa
files_to_fix = [
    r"c:\xampp\htdocs\webtruyen\web\yeuthich.php",
    r"c:\xampp\htdocs\webtruyen\web\truyen.php",
    r"c:\xampp\htdocs\webtruyen\web\trongsinh.php",
    r"c:\xampp\htdocs\webtruyen\web\timkiem1.php",
    r"c:\xampp\htdocs\webtruyen\web\tienhiep.php",
    r"c:\xampp\htdocs\webtruyen\web\thongbao.php",
    r"c:\xampp\htdocs\webtruyen\web\theodoi.php",
    r"c:\xampp\htdocs\webtruyen\web\theloai.php",
    r"c:\xampp\htdocs\webtruyen\web\ngontinh.php",
    r"c:\xampp\htdocs\webtruyen\web\lichsu.php",
    r"c:\xampp\htdocs\webtruyen\web\kiemhiep.php",
    r"c:\xampp\htdocs\webtruyen\web\giaodien.php",
    r"c:\xampp\htdocs\webtruyen\web\frontend\story.php",
    r"c:\xampp\htdocs\webtruyen\web\dothi.php",
    r"c:\xampp\htdocs\webtruyen\web\dinang.php",
    r"c:\xampp\htdocs\webtruyen\web\chuong.php"
]

# Pattern để tìm và thay thế
# Tìm: </div>\n</li>\n        <div class="timkiem">.....</div>\n    </ul>
# Thay: </div>\n</li>\n    </ul>\n        <div class="timkiem">.....</div>

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"File không tồn tại: {file_path}")
        continue
    
    try:
        # Đọc nội dung file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern để tìm cấu trúc sai
        # Tìm: </div>\r\n</li>\r\n        <div class="timkiem">...(bất kỳ nội dung nào)...</div>\r\n    </ul>
        pattern = r'(</div>\r\n</li>\r\n)(        <div class="timkiem">.*?</div>\r\n)(    </ul>)'
        
        # Thay thế: di chuyển </ul> lên trước <div class="timkiem">
        replacement = r'\1\3\n\2'
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Kiểm tra xem có thay đổi gì không
        if new_content != content:
            # Ghi lại file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Đã sửa: {file_path}")
        else:
            print(f"○ Không cần sửa: {file_path}")
    
    except Exception as e:
        print(f"✗ Lỗi khi xử lý {file_path}: {str(e)}")

print("\nHoàn thành!")
