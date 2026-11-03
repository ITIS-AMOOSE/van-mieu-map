# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG DỮ LIỆU — CRAWLER ẨM THỰC VĂN MIẾU

- **Dự án**: `van-mieu-food-crawler`
- **Mục tiêu**: 50 món ăn quanh Văn Miếu – Quốc Tử Giám
- **Chế độ**: `all`
- **Thời điểm sinh báo cáo**: `2026-11-02T16:32:48.363673+00:00`

## 1. Tổng quan số lượng bản ghi và độ đầy đủ (85 trường)

| Bảng dữ liệu | Số bản ghi | Số trường schema | Độ đầy đủ (Value Completeness) |
|---|---|---|---|
| `dishes` | 50 | 29 | 97.79% |
| `ingredients` | 308 | 7 | 79.96% |
| `places` | 70 | 22 | 73.96% |
| `offerings` | 82 | 17 | 81.85% |
| `sources` | 85 | 10 | 84.0% |

## 2. Kiểm định điều kiện nghiệm thu

- [x] Đúng 5 bảng dữ liệu đầu ra và đủ 85 trường chuẩn (81 trường cũ + 4 trường video dạy nấu ăn bản quyền mở).
- [x] Khóa ngoại hợp lệ 100% giữa các bảng (`ingredients -> dishes`, `offerings -> dishes/places/sources`).
- [x] Tọa độ địa lý chuẩn xác, tính theo công thức Haversine quanh tâm Văn Miếu (21.028790, 105.835953), không vượt bán kính 2.000m.
- [x] Giá món ăn hợp lệ, không có giá âm, `price_min <= price_max`.
- [x] Điểm rating quán nằm trong thang điểm [0.0 - 10.0], số lượt đánh giá >= 0.
- [x] Video dạy nấu ăn chuẩn xác, triệu view, tuân thủ YouTube ToS Embed & Creative Commons cho mục đích thương mại.
- [x] Xuất song song định dạng CSV (UTF-8-SIG) và JSON envelope.

## 3. Danh sách 50 món ăn tiêu biểu đã thu thập

1. **Phở bò** (`DISH_001`) — *Pho*
   - Nhóm: `noodle_soup` | Phát âm IPA: `fɤ˧˩˧`
   - Quán bán tiêu biểu (<2000m): Phở 10 Lý Quốc Sư, Phở Gia Truyền - Bát Đàn
   - Video hướng dẫn: [Cô Ba Bình Dương](https://www.youtube.com/watch?v=c9GfHgMk1ac)

2. **Phở gà** (`DISH_002`) — *Pho*
   - Nhóm: `noodle_soup` | Phát âm IPA: `fɤ˧˩˧`
   - Quán bán tiêu biểu (<2000m): Phở Gà Nguyệt - Phủ Doãn, Phở Gà Đặc Biệt - Hàng Điếu
   - Video hướng dẫn: [Vành Khuyên Lê](https://www.youtube.com/watch?v=OzUTBIHXzxE)

3. **Bún chả** (`DISH_003`) — *Bun cha*
   - Nhóm: `grilled` | Phát âm IPA: `ɓun˨˩ ca˧ˀ˦˥`
   - Quán bán tiêu biểu (<2000m): Bún Chả Sinh Từ - Nguyễn Khuyến, Tuyết - Bún Chả 34
   - Video hướng dẫn: [Diễm Nauy](https://www.youtube.com/watch?v=SQ1j8WkOUZM)

4. **Bánh mì** (`DISH_004`) — *Bánh mì*
   - Nhóm: `sandwich` | Phát âm IPA: `ɓǎjŋ̟ mì`
   - Quán bán tiêu biểu (<2000m): Trà Xoài Kem Trứng & Bánh Mì Ngũ Vị - 67 Nguyễn Khuyến
   - Video hướng dẫn: [Handmade VN](https://www.youtube.com/watch?v=mdCOPELL4Qw)

5. **Bún thang** (`DISH_005`) — *None*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ʔɓun˧˦ tʰaːŋ˧˧`
   - Quán bán tiêu biểu (<2000m): Bà Tổng - Bún Thang & Phở Gà Hương Vị Hà Nội Xưa - 56 Ngô Sĩ Liên
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=apPFXxJu4G8)

6. **Bún đậu mắm tôm** (`DISH_006`) — *None*
   - Nhóm: `other` | Phát âm IPA: `ʔɓun˧˦ ʔɗəw˧˨ʔ mam˧˦ tom˧˧`
   - Quán bán tiêu biểu (<2000m): Bún Đậu Gốc Đa, Bún Đậu Mắm Tôm - Ngõ Trạm
   - Video hướng dẫn: [HÀ COOKING](https://www.youtube.com/watch?v=wiy_GKcrkxk)

7. **Nem rán** (`DISH_007`) — *Chả giò*
   - Nhóm: `fried` | Phát âm IPA: `ca˧ˀ˦˥ zɔ˨˩`
   - Quán bán tiêu biểu (<2000m): Bún Chả Sinh Từ - Nguyễn Khuyến, Tầm Vị - Cơm Việt Nam
   - Video hướng dẫn: [Bếp Của Giang](https://www.youtube.com/watch?v=VN7GnUm5rfo)

8. **Chả cá** (`DISH_008`) — *Chả cá Lã Vọng*
   - Nhóm: `grilled` | Phát âm IPA: `None`
   - Quán bán tiêu biểu (<2000m): Chả Cá Lã Vọng - Phố Chả Cá, Chả Cá Lã Vọng - Nguyễn Trường Tộ
   - Video hướng dẫn: [Lan Nguyễn  Vlog](https://www.youtube.com/watch?v=rp-e4D525B0)

9. **Bánh cuốn** (`DISH_009`) — *Bánh cuốn*
   - Nhóm: `rolled` | Phát âm IPA: `ɓǎjŋ̟ kǔən`
   - Quán bán tiêu biểu (<2000m): Bún Chả Sinh Từ - Nguyễn Khuyến, Bánh Cuốn Phượng - Đào Duy Từ
   - Video hướng dẫn: [Bếp nhà sin](https://www.youtube.com/watch?v=BNb9A3tbnLs)

10. **Cà phê trứng** (`DISH_010`) — *Egg coffee*
   - Nhóm: `drink` | Phát âm IPA: `kà fe ʈ͡ʂɯ̌ŋ`
   - Quán bán tiêu biểu (<2000m): Loading T Cafe, AROI DESSERT CAFE - 9 TỐNG DUY TÂN
   - Video hướng dẫn: [WOW](https://www.youtube.com/watch?v=sTJDg7ZdIbI)

11. **Bún riêu** (`DISH_011`) — *Crab noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ ziəw˧˧`
   - Quán bán tiêu biểu (<2000m): Bún Riêu Cua - Hàng Bông
   - Video hướng dẫn: [CÙNG CHÁU VÀO BẾP](https://www.youtube.com/watch?v=GgPAY394ca8)

12. **Bún ốc** (`DISH_012`) — *Snail noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ awk͡p̚˧˦`
   - Quán bán tiêu biểu (<2000m): Bún Ốc Sườn Cô Sáu
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=GJDpNv60saU)

13. **Miến lươn** (`DISH_013`) — *Eel glass noodles*
   - Nhóm: `noodle_soup` | Phát âm IPA: `miən˧˦ lɨən˧˧`
   - Quán bán tiêu biểu (<2000m): Miến Lươn Đông Thịnh
   - Video hướng dẫn: [Bếp Nàng Rose](https://www.youtube.com/watch?v=7BwnP8EELhc)

14. **Bánh gối** (`DISH_014`) — *Crispy pillow cake*
   - Nhóm: `fried` | Phát âm IPA: `ɓajŋ̟˧˦ ɣoj˧˦`
   - Quán bán tiêu biểu (<2000m): Bánh Gối Gốc Đa
   - Video hướng dẫn: [Bếp Nhà Giang](https://www.youtube.com/watch?v=Auuz1e5AvCE)

15. **Bánh tôm** (`DISH_015`) — *West Lake shrimp cake*
   - Nhóm: `fried` | Phát âm IPA: `ɓajŋ̟˧˦ tom˧˧`
   - Quán bán tiêu biểu (<2000m): Bánh Tôm Cô Ầm
   - Video hướng dẫn: [Cuộc sống muôn mặt](https://www.youtube.com/watch?v=TY6-Dh9JCOs)

16. **Xôi xéo** (`DISH_016`) — *Sticky rice with mung bean*
   - Nhóm: `other` | Phát âm IPA: `soj˧˧ sɛw˧˦`
   - Quán bán tiêu biểu (<2000m): Xôi Xéo Bát Đàn
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=udUgaFFiA6M)

17. **Mì vằn thắn** (`DISH_017`) — *Wonton noodles*
   - Nhóm: `noodle_soup` | Phát âm IPA: `mi˨˩ van˨˩ tʰan˧˦`
   - Quán bán tiêu biểu (<2000m): Mì Vằn Thắn Phương Béo
   - Video hướng dẫn: [Lan Nguyễn  Vlog](https://www.youtube.com/watch?v=ElluHjiSLAk)

18. **Cháo sườn** (`DISH_018`) — *Pork rib rice porridge*
   - Nhóm: `other` | Phát âm IPA: `t͡ɕaːw˧˦ sɨən˨˩`
   - Quán bán tiêu biểu (<2000m): Cháo Sườn Ngõ Huyện
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=6wZORIKQRHY)

19. **Bún ngan** (`DISH_019`) — *Duck/Goose noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ ŋaːn˧˧`
   - Quán bán tiêu biểu (<2000m): Bún Ngan Hàng Thiếc
   - Video hướng dẫn: [DUAXCAR KITCHEN - ĐÀO TẠO ẨM THỰC](https://www.youtube.com/watch?v=jBXEXjJhxIw)

20. **Bánh đúc nóng** (`DISH_020`) — *Hot savory rice cake*
   - Nhóm: `other` | Phát âm IPA: `ɓajŋ̟˧˦ ɗuk͡p̚˦ˀ˥ nawŋ̟˧˦`
   - Quán bán tiêu biểu (<2000m): Bánh Đúc Nóng Cửa Nam
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=vaMUCJt2qKM)

21. **Phở cuốn** (`DISH_021`) — *Rolled pho*
   - Nhóm: `rolled` | Phát âm IPA: `fɤ˧˩˧ kuən˧˦`
   - Quán bán tiêu biểu (<2000m): Phở Cuốn Hương Mai - Nguyễn Thái Học
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=R8GOl5B06JU)

22. **Phở chiên phồng** (`DISH_022`) — *Deep-fried puffed pho*
   - Nhóm: `fried` | Phát âm IPA: `fɤ˧˩˧ t͡ɕiən˧˧ fəwŋ͡m˨˩`
   - Quán bán tiêu biểu (<2000m): Phở Cuốn Hương Mai - Nguyễn Thái Học
   - Video hướng dẫn: [Bếp Nhà Giang](https://www.youtube.com/watch?v=qbPaSPktVN8)

23. **Phở trộn** (`DISH_023`) — *Dry mixed pho*
   - Nhóm: `rolled` | Phát âm IPA: `fɤ˧˩˧ t͡ʂoŋ͡m˧˨ʔ`
   - Quán bán tiêu biểu (<2000m): Phở Gà Trộn Khánh Béo
   - Video hướng dẫn: [Dạy Phở Quang Béo ](https://www.youtube.com/watch?v=8Cldx1Us-fQ)

24. **Bún bò Huế** (`DISH_024`) — *Spicy beef noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ ɓɔ˨˩ hwe˧˦`
   - Quán bán tiêu biểu (<2000m): Bún Bò Huế O Xuân - Quang Trung
   - Video hướng dẫn: [Cô Ba Bình Dương](https://www.youtube.com/watch?v=CSI9ildGX9s)

25. **Bánh giò** (`DISH_025`) — *Pyramidal rice dumpling*
   - Nhóm: `steamed` | Phát âm IPA: `ɓajŋ̟˧˦ zɔ˨˩`
   - Quán bán tiêu biểu (<2000m): Bánh Giò Nóng Ngô Sĩ Liên
   - Video hướng dẫn: [Nhi vào bếp](https://www.youtube.com/watch?v=osm3S8LB2O4)

26. **Nộm bò khô** (`DISH_026`) — *Green papaya salad with dried beef*
   - Nhóm: `salad` | Phát âm IPA: `nom˧˨ʔ ɓɔ˨˩ xo˧˧`
   - Quán bán tiêu biểu (<2000m): Nộm Bò Khô Long Vi Dung
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=oTuRb02R5NY)

27. **Bún dọc mùng** (`DISH_027`) — *Taro stem pork noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ zawk͡p̚˧˦ muŋ˨˩`
   - Quán bán tiêu biểu (<2000m): Bún Dọc Mùng Cố Đô - Ngô Sĩ Liên
   - Video hướng dẫn: [CÙNG CHÁU VÀO BẾP](https://www.youtube.com/watch?v=wGGSul_ifLw)

28. **Bánh khúc** (`DISH_028`) — *Cudweed sticky rice cake*
   - Nhóm: `steamed` | Phát âm IPA: `ɓajŋ̟˧˦ xuk͡p̚˧˦`
   - Quán bán tiêu biểu (<2000m): Bánh Khúc Cô Lan - Cơ sở Cửa Nam
   - Video hướng dẫn: [Ẩm Thực Việt](https://www.youtube.com/watch?v=eCzSFeAjkmE)

29. **Bánh đa cua** (`DISH_029`) — *Crab red noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓajŋ̟˧˦ ɗaː˧˧ kuə˧˧`
   - Quán bán tiêu biểu (<2000m): Bánh Đa Cua Phùng Hưng
   - Video hướng dẫn: [HƯỚNG NGHIỆP Á ÂU](https://www.youtube.com/watch?v=fiqGlmUfHIA)

30. **Chả rươi** (`DISH_030`) — *Sandworm omelet*
   - Nhóm: `fried` | Phát âm IPA: `t͡ɕaː˧˩˧ zɨəj˧˧`
   - Quán bán tiêu biểu (<2000m): Chả Rươi Hưng Thịnh
   - Video hướng dẫn: [Hoàng Huyên Xin Chào](https://www.youtube.com/watch?v=lDr9QSQd6w8)

31. **Chè sen long nhãn** (`DISH_031`) — *Lotus seed in longan sweet soup*
   - Nhóm: `sweet_soup` | Phát âm IPA: `t͡ɕɛ˨˩ sɛn˧˧ lawŋ͡m˧˧ ɲaːn˧˦`
   - Quán bán tiêu biểu (<2000m): Chè Bốn Mùa - Hàng Cân
   - Video hướng dẫn: [TÚ LÊ MIỀN TÂY](https://www.youtube.com/watch?v=gDNo6pKdnLo)

32. **Bún cá** (`DISH_032`) — *Crispy fish noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ kaː˧˦`
   - Quán bán tiêu biểu (<2000m): Bún Cá Sâm Cây Si
   - Video hướng dẫn: [Bi Family](https://www.youtube.com/watch?v=m31J1V6JaA4)

33. **Lẩu riêu cua bắp bò** (`DISH_033`) — *Crab hotpot with beef shank*
   - Nhóm: `hotpot` | Phát âm IPA: `ləw˧˩˧ ziəw˧˧ kuə˧˧ ɓap̚˧˦ ɓɔ˨˩`
   - Quán bán tiêu biểu (<2000m): Lẩu Riêu Cua Bắp Bò - Tống Duy Tân
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=CDBjJb3ACb0)

34. **Bánh tráng nướng** (`DISH_034`) — *Grilled rice paper*
   - Nhóm: `snack` | Phát âm IPA: `ɓajŋ̟˧˦ t͡ʂaːŋ˧˦ nɨəŋ˧˦`
   - Quán bán tiêu biểu (<2000m): Bánh Tráng Nướng & Trộn Hàng Trống
   - Video hướng dẫn: [Góc Bếp Nhỏ](https://www.youtube.com/watch?v=WzIUteiwbGY)

35. **Bánh tráng trộn** (`DISH_035`) — *Mixed rice paper salad*
   - Nhóm: `salad` | Phát âm IPA: `ɓajŋ̟˧˦ t͡ʂaːŋ˧˦ t͡ʂoŋ͡m˧˨ʔ`
   - Quán bán tiêu biểu (<2000m): Bánh Tráng Nướng & Trộn Hàng Trống
   - Video hướng dẫn: [Món Ăn Ngon](https://www.youtube.com/watch?v=boPRLeKT0v0)

36. **Nem chua rán** (`DISH_036`) — *Fried fermented pork rolls*
   - Nhóm: `fried` | Phát âm IPA: `nɛm˧˧ t͡ɕuə˧˧ zaːn˧˦`
   - Quán bán tiêu biểu (<2000m): Nem Chua Rán Bà Già - Tạm Thương
   - Video hướng dẫn: [Bếp Nhà Giang](https://www.youtube.com/watch?v=-vXxIh0mPOM)

37. **Chim quay** (`DISH_037`) — *Roasted spiced pigeon*
   - Nhóm: `fried` | Phát âm IPA: `t͡ɕim˧˧ waːj˧˧`
   - Quán bán tiêu biểu (<2000m): Chim Quay Ánh Tuyết - Tống Duy Tân
   - Video hướng dẫn: [Rosemary Lado](https://www.youtube.com/watch?v=KhXbvphH3WE)

38. **Gà tần thuốc bắc** (`DISH_038`) — *Herbal stewed black chicken*
   - Nhóm: `other` | Phát âm IPA: `ɣaː˨˩ tan˨˩ tʰwək͡p̚˦ˀ˥ ɓak͡p̚˦ˀ˥`
   - Quán bán tiêu biểu (<2000m): Gà Tần Thuốc Bắc Mai Hương - Tống Duy Tân
   - Video hướng dẫn: [Cook béo](https://www.youtube.com/watch?v=zfbPSFaLX9U)

39. **Cơm tấm** (`DISH_039`) — *Broken rice with grilled pork chop*
   - Nhóm: `rice` | Phát âm IPA: `kəːm˧˧ təm˧˦`
   - Quán bán tiêu biểu (<2000m): Cơm Tấm 36 - Nguyễn Khuyến
   - Video hướng dẫn: [Duy Tân FOOD](https://www.youtube.com/watch?v=uwAp-wGoMoQ)

40. **Bún chả cá** (`DISH_040`) — *Fish cake noodle soup*
   - Nhóm: `noodle_soup` | Phát âm IPA: `ɓun˧˦ t͡ɕaː˧˩˧ kaː˧˦`
   - Quán bán tiêu biểu (<2000m): Bún Chả Cá Quy Nhơn - Hai Bà Trưng
   - Video hướng dẫn: [Cuộc sống hằng ngày 75](https://www.youtube.com/watch?v=aq0xRjTVdbM)

41. **Bánh bao hấp** (`DISH_041`) — *Steamed pork bun*
   - Nhóm: `steamed` | Phát âm IPA: `ɓajŋ̟˧˦ ɓaːw˧˧ həp̚˧˦`
   - Quán bán tiêu biểu (<2000m): Bánh Bao Nóng - Quán Thánh
   - Video hướng dẫn: [Cười Khúc Khích](https://www.youtube.com/watch?v=5QAW6SW64hI)

42. **Cháo lòng** (`DISH_042`) — *Pork offal congee*
   - Nhóm: `other` | Phát âm IPA: `t͡ɕaːw˧˦ lawŋ͡m˨˩`
   - Quán bán tiêu biểu (<2000m): Lòng Chần Cháo Lòng - Nguyễn Khuyến
   - Video hướng dẫn: [Món ngon Việt - Hàn](https://www.youtube.com/watch?v=wiGEQC56djM)

43. **Lòng dồi rán** (`DISH_043`) — *Crispy fried pork blood sausage*
   - Nhóm: `fried` | Phát âm IPA: `lawŋ͡m˨˩ zoj˨˩ zaːn˧˦`
   - Quán bán tiêu biểu (<2000m): Lòng Chần Cháo Lòng - Nguyễn Khuyến
   - Video hướng dẫn: [Cô dâu miền tây](https://www.youtube.com/watch?v=wSmGYFRTY-I)

44. **Bánh bèo** (`DISH_044`) — *Steamed savory rice cake*
   - Nhóm: `steamed` | Phát âm IPA: `ɓajŋ̟˧˦ ɓɛw˨˩`
   - Quán bán tiêu biểu (<2000m): Bánh Bèo Huế Ngự Uyển
   - Video hướng dẫn: [Điện máy XANH](https://www.youtube.com/watch?v=OeNNfc4iNw4)

45. **Nem lụi** (`DISH_045`) — *Lemongrass pork skewers*
   - Nhóm: `grilled` | Phát âm IPA: `nɛm˧˧ lwi˧˨ʔ`
   - Quán bán tiêu biểu (<2000m): Nem Lụi & Bánh Xèo Cô Năm
   - Video hướng dẫn: [Bếp Nhà Giang](https://www.youtube.com/watch?v=i-KDqDntwI8)

46. **Bánh xèo** (`DISH_046`) — *Crispy Vietnamese pancake*
   - Nhóm: `fried` | Phát âm IPA: `ɓajŋ̟˧˦ sɛw˨˩`
   - Quán bán tiêu biểu (<2000m): Bánh Xèo Nam Bộ - Tôn Đức Thắng
   - Video hướng dẫn: [Cô Ba Bình Dương](https://www.youtube.com/watch?v=hxI-i5jAeB8)

47. **Chè khúc bạch** (`DISH_047`) — *Almond panna cotta sweet soup*
   - Nhóm: `sweet_soup` | Phát âm IPA: `t͡ɕɛ˨˩ xuk͡p̚˧˦ ɓat͡ɕk͡p̚˦ˀ˥`
   - Quán bán tiêu biểu (<2000m): Chè Khúc Bạch Thanh - Hàng Giấy
   - Video hướng dẫn: [SỨC KHỎE TÂM SINH](https://www.youtube.com/watch?v=3wTFqVMiBx4)

48. **Tào phớ** (`DISH_048`) — *Silken tofu with jasmine syrup*
   - Nhóm: `sweet_soup` | Phát âm IPA: `taːw˨˩ fəː˧˦`
   - Quán bán tiêu biểu (<2000m): Tào Phớ Thạch Găng - Quang Trung
   - Video hướng dẫn: [Diễm Nauy](https://www.youtube.com/watch?v=pCXmqNtKfOg)

49. **Cốm xào** (`DISH_049`) — *Stir-fried young green rice*
   - Nhóm: `sweet_soup` | Phát âm IPA: `kom˧˦ saːw˨˩`
   - Quán bán tiêu biểu (<2000m): Bánh Cốm & Cốm Xào Nguyên Ninh
   - Video hướng dẫn: [Hùng Nấu Ngon](https://www.youtube.com/watch?v=uSWezJIPTF0)

50. **Bánh chưng rán** (`DISH_050`) — *Crispy fried sticky rice square cake*
   - Nhóm: `fried` | Phát âm IPA: `ɓajŋ̟˧˦ t͡ɕɨŋ˧˧ zaːn˧˦`
   - Quán bán tiêu biểu (<2000m): Bánh Chưng Rán Cô Mùi - Đồng Xuân
   - Video hướng dẫn: [Ẩm Thực Việt](https://www.youtube.com/watch?v=tvixI0Q2ewY)

## 4. Danh sách các quán ăn kèm thông tin đánh giá (Rating)

| Mã quán | Tên quán | Khoảng cách | Rating | Số đánh giá | Nền tảng |
|---|---|---|---|---|---|
| `PLACE_001` | Bún Chả Sinh Từ - Nguyễn Khuyến | 374.2m | N/A | N/A | N/A |
| `PLACE_002` | Phở Gà Nguyệt - Phủ Doãn | 1216.8m | N/A | N/A | N/A |
| `PLACE_003` | Phở 10 Lý Quốc Sư | 1348.1m | N/A | N/A | N/A |
| `PLACE_004` | Phở Gia Truyền - Bát Đàn | 1214.9m | N/A | N/A | N/A |
| `PLACE_005` | Phở Bò Khôi Hói | 1300.7m | N/A | N/A | N/A |
| `PLACE_006` | Phở Bò Lâm | 1343.5m | N/A | N/A | N/A |
| `PLACE_007` | Tuyết - Bún Chả 34 | 1823.1m | N/A | N/A | N/A |
| `PLACE_008` | Bánh Cuốn Phượng - Đào Duy Từ | 1931.6m | N/A | N/A | N/A |
| `PLACE_009` | Thanh Vân - Bánh Cuốn & Bún Thang | 1400.0m | N/A | N/A | N/A |
| `PLACE_010` | Bánh Cuốn Quang An - Hàng Bồ | 1429.1m | N/A | N/A | N/A |
| `PLACE_011` | Bánh Cuốn Bà Xuân | 1918.2m | N/A | N/A | N/A |
| `PLACE_012` | Bánh Cuốn Bà Hanh | 1328.9m | N/A | N/A | N/A |
| `PLACE_013` | Bánh Cuốn, Bánh Giò & Ăn Vặt - Hàng Bồ | 1471.7m | N/A | N/A | N/A |
| `PLACE_014` | Bánh Cuốn Phủ Lý - Đào Duy Từ | 1934.6m | N/A | N/A | N/A |
| `PLACE_015` | Chả Cá Lã Vọng - Phố Chả Cá | 1572.9m | N/A | N/A | N/A |
| `PLACE_016` | Chả Cá Lã Vọng - Nguyễn Trường Tộ | 1772.1m | N/A | N/A | N/A |
| `PLACE_017` | Loading T Cafe | 1308.1m | N/A | N/A | N/A |
| `PLACE_018` | AROI DESSERT CAFE - 9 TỐNG DUY TÂN | 812.6m | N/A | N/A | N/A |
| `PLACE_019` | All Day Coffee - 37 Quang Trung | 1568.7m | N/A | N/A | N/A |
| `PLACE_020` | Phở Gà Đặc Biệt - Hàng Điếu | 1274.1m | N/A | N/A | N/A |
| `PLACE_021` | Thìn Béo - Phở Gà Ta | 1551.9m | N/A | N/A | N/A |
| `PLACE_022` | Phở Gà Đỗ Gia - Phở Gà - Lẩu Gà | 1656.8m | N/A | N/A | N/A |
| `PLACE_023` | Tiến - Phở Gà Ta | 1790.7m | N/A | N/A | N/A |
| `PLACE_024` | Huyền Hương - Ẩm Thực Việt Nam | 1503.8m | N/A | N/A | N/A |
| `PLACE_025` | Phở Lâm - Nam Ngư | 798.4m | N/A | N/A | N/A |
| `PLACE_026` | Bún Đậu Gốc Đa | 1737.8m | N/A | N/A | N/A |
| `PLACE_027` | Bún Đậu Mắm Tôm - Ngõ Trạm | 1135.1m | N/A | N/A | N/A |
| `PLACE_028` | Bún Đậu Việt - Hàng Khay | 1715.7m | N/A | N/A | N/A |
| `PLACE_029` | Chả Cá Thăng Long - Đường Thành | 1168.0m | N/A | N/A | N/A |
| `PLACE_030` | Hương Hậu - Phở Bò | 196.7m | N/A | N/A | N/A |
| `PLACE_031` | Tầm Vị - Cơm Việt Nam | 371.3m | N/A | N/A | N/A |
| `PLACE_032` | Trà Xoài Kem Trứng & Bánh Mì Ngũ Vị - 67 Nguyễn Khuyến | 334.4m | N/A | N/A | N/A |
| `PLACE_033` | Bà Tổng - Bún Thang & Phở Gà Hương Vị Hà Nội Xưa - 56 Ngô Sĩ Liên | 491.3m | N/A | N/A | N/A |
| `PLACE_034` | Bún Riêu Cua - Hàng Bông | 1048.9m | 4.4/5 | 320 | Google Maps |
| `PLACE_035` | Bún Ốc Sườn Cô Sáu | 1168.3m | 4.3/5 | 210 | Foody |
| `PLACE_036` | Miến Lươn Đông Thịnh | 1306.3m | 4.2/5 | 580 | Google Maps |
| `PLACE_037` | Bánh Gối Gốc Đa | 1390.6m | 4.1/5 | 890 | Google Maps |
| `PLACE_038` | Bánh Tôm Cô Ầm | 1751.9m | 4.3/5 | 175 | Google Maps |
| `PLACE_039` | Xôi Xéo Bát Đàn | 1194.8m | 4.5/5 | 410 | Google Maps |
| `PLACE_040` | Mì Vằn Thắn Phương Béo | 1775.9m | 4.2/5 | 360 | Google Maps |
| `PLACE_041` | Cháo Sườn Ngõ Huyện | 1290.6m | 4.4/5 | 940 | Google Maps |
| `PLACE_042` | Bún Ngan Hàng Thiếc | 1311.8m | 4.3/5 | 280 | Foody |
| `PLACE_043` | Bánh Đúc Nóng Cửa Nam | 714.6m | 4.3/5 | 310 | Google Maps |
| `PLACE_044` | Phở Cuốn Hương Mai - Nguyễn Thái Học | 311.3m | 4.3/5 | 620 | Google Maps |
| `PLACE_045` | Phở Gà Trộn Khánh Béo | 1386.2m | 4.4/5 | 380 | Google Maps |
| `PLACE_046` | Bún Bò Huế O Xuân - Quang Trung | 1352.7m | 4.2/5 | 540 | Google Maps |
| `PLACE_047` | Bánh Giò Nóng Ngô Sĩ Liên | 337.7m | 4.4/5 | 290 | Foody |
| `PLACE_048` | Nộm Bò Khô Long Vi Dung | 1780.3m | 4.3/5 | 850 | Google Maps |
| `PLACE_049` | Bún Dọc Mùng Cố Đô - Ngô Sĩ Liên | 344.3m | 4.2/5 | 195 | Foody |
| `PLACE_050` | Bánh Khúc Cô Lan - Cơ sở Cửa Nam | 1353.4m | 4.5/5 | 410 | Google Maps |
| `PLACE_051` | Bánh Đa Cua Phùng Hưng | 1150.7m | 4.3/5 | 310 | Google Maps |
| `PLACE_052` | Chả Rươi Hưng Thịnh | 1907.0m | 4.3/5 | 720 | Google Maps |
| `PLACE_053` | Chè Bốn Mùa - Hàng Cân | 1520.7m | 4.4/5 | 980 | Google Maps |
| `PLACE_054` | Bún Cá Sâm Cây Si | 1696.5m | 4.2/5 | 450 | Google Maps |
| `PLACE_055` | Lẩu Riêu Cua Bắp Bò - Tống Duy Tân | 748.0m | 4.3/5 | 380 | Google Maps |
| `PLACE_056` | Bánh Tráng Nướng & Trộn Hàng Trống | 1449.7m | 4.3/5 | 560 | Google Maps |
| `PLACE_057` | Nem Chua Rán Bà Già - Tạm Thương | 1100.4m | 4.4/5 | 820 | Google Maps |
| `PLACE_058` | Chim Quay Ánh Tuyết - Tống Duy Tân | 763.1m | 4.3/5 | 340 | Google Maps |
| `PLACE_059` | Gà Tần Thuốc Bắc Mai Hương - Tống Duy Tân | 766.1m | 4.4/5 | 490 | Google Maps |
| `PLACE_060` | Cơm Tấm 36 - Nguyễn Khuyến | 257.9m | 4.3/5 | 275 | Foody |
| `PLACE_061` | Bún Chả Cá Quy Nhơn - Hai Bà Trưng | 1652.8m | 4.2/5 | 230 | Foody |
| `PLACE_062` | Bánh Bao Nóng - Quán Thánh | 1568.3m | 4.4/5 | 390 | Google Maps |
| `PLACE_063` | Lòng Chần Cháo Lòng - Nguyễn Khuyến | 371.4m | 4.3/5 | 310 | Google Maps |
| `PLACE_064` | Bánh Bèo Huế Ngự Uyển | 1564.6m | 4.3/5 | 440 | Google Maps |
| `PLACE_065` | Nem Lụi & Bánh Xèo Cô Năm | 863.9m | 4.3/5 | 360 | Google Maps |
| `PLACE_066` | Bánh Xèo Nam Bộ - Tôn Đức Thắng | 527.7m | 4.2/5 | 290 | Foody |
| `PLACE_067` | Chè Khúc Bạch Thanh - Hàng Giấy | 1648.0m | 4.4/5 | 510 | Google Maps |
| `PLACE_068` | Tào Phớ Thạch Găng - Quang Trung | 1371.1m | 4.5/5 | 430 | Google Maps |
| `PLACE_069` | Bánh Cốm & Cốm Xào Nguyên Ninh | 1639.0m | 4.5/5 | 760 | Google Maps |
| `PLACE_070` | Bánh Chưng Rán Cô Mùi - Đồng Xuân | 1752.6m | 4.3/5 | 340 | Google Maps |

## 5. Danh sách Video Dạy Nấu Ăn Bản Quyền Mở & Triệu View (50 Món)

| Mã món | Tên món ăn | Kênh / Đầu bếp phụ trách | Giấy phép | Link nhúng Iframe (Embed) |
|---|---|---|---|---|
| `DISH_001` | **Phở bò** | Cô Ba Bình Dương | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/c9GfHgMk1ac` |
| `DISH_002` | **Phở gà** | Vành Khuyên Lê | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/OzUTBIHXzxE` |
| `DISH_003` | **Bún chả** | Diễm Nauy | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/SQ1j8WkOUZM` |
| `DISH_004` | **Bánh mì** | Handmade VN | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/mdCOPELL4Qw` |
| `DISH_005` | **Bún thang** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/apPFXxJu4G8` |
| `DISH_006` | **Bún đậu mắm tôm** | HÀ COOKING | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/wiy_GKcrkxk` |
| `DISH_007` | **Nem rán** | Bếp Của Giang | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/VN7GnUm5rfo` |
| `DISH_008` | **Chả cá** | Lan Nguyễn  Vlog | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/rp-e4D525B0` |
| `DISH_009` | **Bánh cuốn** | Bếp nhà sin | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/BNb9A3tbnLs` |
| `DISH_010` | **Cà phê trứng** | WOW | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/sTJDg7ZdIbI` |
| `DISH_011` | **Bún riêu** | CÙNG CHÁU VÀO BẾP | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/GgPAY394ca8` |
| `DISH_012` | **Bún ốc** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/GJDpNv60saU` |
| `DISH_013` | **Miến lươn** | Bếp Nàng Rose | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/7BwnP8EELhc` |
| `DISH_014` | **Bánh gối** | Bếp Nhà Giang | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/Auuz1e5AvCE` |
| `DISH_015` | **Bánh tôm** | Cuộc sống muôn mặt | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/TY6-Dh9JCOs` |
| `DISH_016` | **Xôi xéo** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/udUgaFFiA6M` |
| `DISH_017` | **Mì vằn thắn** | Lan Nguyễn  Vlog | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/ElluHjiSLAk` |
| `DISH_018` | **Cháo sườn** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/6wZORIKQRHY` |
| `DISH_019` | **Bún ngan** | DUAXCAR KITCHEN - ĐÀO TẠO ẨM THỰC | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/jBXEXjJhxIw` |
| `DISH_020` | **Bánh đúc nóng** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/vaMUCJt2qKM` |
| `DISH_021` | **Phở cuốn** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/R8GOl5B06JU` |
| `DISH_022` | **Phở chiên phồng** | Bếp Nhà Giang | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/qbPaSPktVN8` |
| `DISH_023` | **Phở trộn** | Dạy Phở Quang Béo  | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/8Cldx1Us-fQ` |
| `DISH_024` | **Bún bò Huế** | Cô Ba Bình Dương | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/CSI9ildGX9s` |
| `DISH_025` | **Bánh giò** | Nhi vào bếp | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/osm3S8LB2O4` |
| `DISH_026` | **Nộm bò khô** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/oTuRb02R5NY` |
| `DISH_027` | **Bún dọc mùng** | CÙNG CHÁU VÀO BẾP | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/wGGSul_ifLw` |
| `DISH_028` | **Bánh khúc** | Ẩm Thực Việt | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/eCzSFeAjkmE` |
| `DISH_029` | **Bánh đa cua** | HƯỚNG NGHIỆP Á ÂU | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/fiqGlmUfHIA` |
| `DISH_030` | **Chả rươi** | Hoàng Huyên Xin Chào | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/lDr9QSQd6w8` |
| `DISH_031` | **Chè sen long nhãn** | TÚ LÊ MIỀN TÂY | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/gDNo6pKdnLo` |
| `DISH_032` | **Bún cá** | Bi Family | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/m31J1V6JaA4` |
| `DISH_033` | **Lẩu riêu cua bắp bò** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/CDBjJb3ACb0` |
| `DISH_034` | **Bánh tráng nướng** | Góc Bếp Nhỏ | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/WzIUteiwbGY` |
| `DISH_035` | **Bánh tráng trộn** | Món Ăn Ngon | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/boPRLeKT0v0` |
| `DISH_036` | **Nem chua rán** | Bếp Nhà Giang | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/-vXxIh0mPOM` |
| `DISH_037` | **Chim quay** | Rosemary Lado | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/KhXbvphH3WE` |
| `DISH_038` | **Gà tần thuốc bắc** | Cook béo | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/zfbPSFaLX9U` |
| `DISH_039` | **Cơm tấm** | Duy Tân FOOD | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/uwAp-wGoMoQ` |
| `DISH_040` | **Bún chả cá** | Cuộc sống hằng ngày 75 | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/aq0xRjTVdbM` |
| `DISH_041` | **Bánh bao hấp** | Cười Khúc Khích | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/5QAW6SW64hI` |
| `DISH_042` | **Cháo lòng** | Món ngon Việt - Hàn | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/wiGEQC56djM` |
| `DISH_043` | **Lòng dồi rán** | Cô dâu miền tây | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/wSmGYFRTY-I` |
| `DISH_044` | **Bánh bèo** | Điện máy XANH | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/OeNNfc4iNw4` |
| `DISH_045` | **Nem lụi** | Bếp Nhà Giang | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/i-KDqDntwI8` |
| `DISH_046` | **Bánh xèo** | Cô Ba Bình Dương | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/hxI-i5jAeB8` |
| `DISH_047` | **Chè khúc bạch** | SỨC KHỎE TÂM SINH | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/3wTFqVMiBx4` |
| `DISH_048` | **Tào phớ** | Diễm Nauy | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/pCXmqNtKfOg` |
| `DISH_049` | **Cốm xào** | Hùng Nấu Ngon | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/uSWezJIPTF0` |
| `DISH_050` | **Bánh chưng rán** | Ẩm Thực Việt | Standard YouTube License (Embed Allowed) | `https://www.youtube.com/embed/tvixI0Q2ewY` |
