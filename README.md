 Hệ thống Chat Mã hóa Đầu cuối (E2EE Chat) - Nhóm 2

## Giới thiệu dự án
Đây là đồ án thuộc môn **An toàn Thông tin**. Dự án tập trung xây dựng một hệ thống nhắn tin Client-Server theo thời gian thực, trong đó tính bảo mật, quyền riêng tư và toàn vẹn dữ liệu được đặt lên hàng đầu thông qua cơ chế **Mã hóa đầu cuối (End-to-End Encryption - E2EE)**.

## Mục tiêu bảo mật
* **Bảo mật nội dung (Confidentiality):** Server chỉ làm nhiệm vụ trung chuyển, hoàn toàn không có khả năng đọc được nội dung tin nhắn dạng rõ (plaintext).
* **Chống nghe lén (Man-in-the-Middle):** Ngăn chặn kẻ tấn công trên đường truyền đánh cắp hoặc thay đổi gói tin.
* **Xác thực và Toàn vẹn (Integrity & Authentication):** Đảm bảo tin nhắn không bị giả mạo hay chỉnh sửa trong quá trình gửi nhận.

## Kiến trúc Mật mã học
Hệ thống sử dụng các thuật toán mã hóa tiêu chuẩn để bảo vệ dữ liệu:
1. **Trao đổi khóa:** (Điền giao thức nhóm bạn dùng, VD: Diffie-Hellman / RSA) để thiết lập khóa phiên an toàn.
2. **Mã hóa dữ liệu:** Sử dụng thuật toán mã hóa đối xứng (VD: AES-256) với khóa phiên để mã hóa tin nhắn.
3. **Lưu trữ mật khẩu:** Mật khẩu người dùng được băm (hashing) kết hợp salt (VD: SHA-256 / Bcrypt) trước khi lưu vào cơ sở dữ liệu.

## Công nghệ và Ngôn ngữ sử dụng
* **Ngôn ngữ lập trình:** C++
* **Giao tiếp mạng:** Socket TCP/IP
* **Thư viện mã hóa:** (Điền tên thư viện, VD: OpenSSL / Crypto++)

## Hướng dẫn Cài đặt & Chạy ứng dụng

### 1. Yêu cầu hệ thống
* Trình biên dịch C++ (GCC/MinGW)
* (Thêm các thư viện cần cài đặt trước)

### 2. Cách khởi chạy
**Chạy Server:**
\`\`\`bash
# Di chuyển vào thư mục server và biên dịch
cd Server
g++ server.cpp -o server
./server
\`\`\`

**Chạy Client:**
\`\`\`bash
# Di chuyển vào thư mục client và biên dịch
cd Client
g++ client.cpp -o client
./client
\`\`\`
