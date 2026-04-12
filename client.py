import socket
import hashlib
import random
import binascii

class TruongNetwork:
    def __init__(self):
        self.p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1
        self.g = 2
        self.private_key = random.getrandbits(256)
        self.public_key = pow(self.g, self.private_key, self.p)

    def generate_shared_key(self, partner_pub_key):
        shared_secret = pow(int(partner_pub_key), self.private_key, self.p)
        return hashlib.sha256(str(shared_secret).encode()).digest()

    def run_dh_exchange(self, role='server', host='127.0.0.1', port=65432):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if role == 'server':
                s.bind((host, port))
                s.listen(1)
                print(f"[Trường Server] Đang mở cổng {port}, chờ kết nối...")
                conn, addr = s.accept()
                
                conn.sendall(str(self.public_key).encode())
                partner_pub_key = conn.recv(1024).decode()
            else:
                print(f"[Trường Client] Đang tìm Server tại {host}:{port}...")
                s.connect((host, port))
                conn = s
                partner_pub_key = conn.recv(1024).decode()
                conn.sendall(str(self.public_key).encode())

            shared_key = self.generate_shared_key(partner_pub_key)
            print("[Trường Server/Client] Trao đổi Diffie-Hellman thành công!")
            return conn, shared_key
            
        except Exception as e:
            print(f"[Lỗi Network] {e}")
            return None, None

# --- CHỈ KHÁC NHAU PHẦN NÀY ---
if __name__ == "__main__":
    mang = TruongNetwork()
    # Chạy file này với vai trò CLIENT
    conn, key = mang.run_dh_exchange(role='client')
    
    if key:
        print(f" Khóa chung của CLIENT tính ra là: {binascii.hexlify(key).decode()}")