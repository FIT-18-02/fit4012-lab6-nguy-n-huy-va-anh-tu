# Report 1 page - Lab 6 AES-CBC Socket

## Thông tin nhóm
- Thành viên 1: Nguyễn Văn Huy (1871020313)
- Thành viên 2: Phạm Anh Tú (1871020615)

## Mục tiêu
Xây dựng hệ thống client-server gửi nhận dữ liệu qua TCP socket. Triển khai thuật toán mã hóa AES-CBC với đệm PKCS#7. Thực hiện tách biệt kiến trúc thành 2 kênh: kênh truyền khóa (KEY_PORT) và kênh truyền dữ liệu (DATA_PORT). Đánh giá bảo mật và viết test tự động cho các luồng.

## Phân công thực hiện
- Nguyễn Văn Huy: Phụ trách `sender.py`, `aes_socket_utils.py` (phần encrypt) và chạy sinh log.
- Phạm Anh Tú: Phụ trách `receiver.py`, `aes_socket_utils.py` (phần decrypt) và cấu trúc unit tests.
- Làm chung: Lên kịch bản lỗi (tamper, wrong key) và viết file Threat Model.

## Cách làm
Sử dụng thư viện `pycryptodome` để khởi tạo AES-CBC. Dữ liệu trước khi mã hóa được đệm (pad) theo chuẩn PKCS#7 để chia hết cho 16 bytes. Giao thức truyền tin tự định nghĩa thêm một header 4-byte (big-endian) chứa độ dài gói tin ở phía trước key/iv và ciphertext để TCP Socket biết cần nhận chính xác bao nhiêu bytes (tránh lỗi nhận thiếu/thừa stream).

## Kết quả
Hệ thống chạy ổn định qua môi trường localhost. Quá trình đóng/mở gói tin chính xác. Pass toàn bộ bài test CI kiểm tra (AES padding, data channel, key channel, tamper, wrong_key). Log minh chứng được ghi nhận đầy đủ tại thư mục `logs/`.

## Kết luận
Về kỹ thuật, nhóm nắm vững cách thiết kế message header độ dài cố định để xử lý TCP stream boundary. Về bảo mật, nhận thức rõ việc mã hóa AES chỉ che giấu dữ liệu (Confidentiality) chứ không có tính xác thực (Authentication/Integrity), và việc truyền key plaintext qua socket là lỗ hổng chí mạng trong thực tế.