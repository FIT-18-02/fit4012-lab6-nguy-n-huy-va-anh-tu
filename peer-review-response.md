## Phản hồi đánh giá chéo

### 1. Về Sender và Receiver
- **Nhận xét**: Code sender và receiver hoạt động đúng, có xử lý timeout và log.
- **Phản hồi**: Cảm ơn nhận xét. Chúng tôi đã kiểm tra kỹ và đảm bảo luồng gửi/nhận qua 2 kênh (`KEY_PORT` và `DATA_PORT`) hoạt động ổn định. Ngoài ra, nhóm cũng bổ sung xử lý exception và logging để thuận tiện cho việc debug và theo dõi kết nối.

### 2. Về mã hóa AES-CBC
- **Nhận xét**: Sử dụng đúng AES-128, PKCS#7 padding, IV ngẫu nhiên.
- **Phản hồi**: Đúng vậy. Chúng tôi đã cài đặt `encrypt_aes_cbc` và `decrypt_aes_cbc` theo đúng chuẩn AES-128 CBC với PKCS#7 padding. IV được sinh ngẫu nhiên cho mỗi lần mã hóa nhằm tăng tính bảo mật.

### 3. Về kiểm thử
- **Nhận xét**: Có đủ test cho happy path, wrong key, tamper ciphertext.
- **Phản hồi**: Chúng tôi đã bổ sung đầy đủ 7 test cases bao gồm các trường hợp hợp lệ và lỗi như wrong key, modified ciphertext, timeout và invalid data. Tất cả test đều pass và đã được lưu lại trong report.

### 4. Về Threat Model
- **Nhận xét**: Đã chỉ ra key disclosure, tampering, replay attack.
- **Phản hồi**: Cảm ơn góp ý. Nhóm đã phân tích đầy đủ các assets cần bảo vệ, các threats phổ biến, biện pháp giảm thiểu (mitigations) và residual risks còn tồn tại trong hệ thống.

### 5. Cải thiện đề xuất
- **Nhận xét**: Nên thêm xác thực (AES-GCM) thay vì CBC.
- **Phản hồi**: Đồng ý. Trong thực tế, AES-GCM sẽ phù hợp hơn vì vừa hỗ trợ mã hóa vừa đảm bảo tính toàn vẹn và xác thực dữ liệu, giúp hạn chế các nguy cơ tampering.

## Kết luận

Nhóm đã hoàn thành đầy đủ yêu cầu của lab, bao gồm:
- Mã nguồn sender/receiver
- Mã hóa AES-CBC
- Test cases và log
- Report và threat model
- Peer review response

Thông qua bài lab này, nhóm hiểu rõ hơn về lập trình socket, mã hóa đối xứng và các vấn đề bảo mật trong truyền dữ liệu qua mạng.