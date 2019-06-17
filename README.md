# Cinema Microservice (Python, Mongodb)

## Cài đặt
Dự án chạy trên môi trường docker nên máy cần phải được cài đặt docker

Mở terminal trong dự án và build thành các container trên docker
```
 Cinema> docker-compose up
```
Port của các service
- Booking: 3001 
- Notifications: 3002
- Catalogs: 3003
- Movies: 3004
- Gateway: 80

## Giới thiệu cấu trúc dự án
Dự án microservice xây dựng quản lý rạp phim dựa.
Trong dự án sử dụng:
- Python
- MongoDB
- Docker environment

Trong dự án gồm 5 service chính:
- Movies service (thêm phim, danh sách phim, danh sách công chiếu)
- Catalogs service (danh sách rạp, lịch chiếu)
- Bookings service (Đặt vé, tạo ticket, quản lý user)
- Notifications (Gửi notification qua kênh gmail)
- Gateway (Nginx)
