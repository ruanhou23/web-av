# -*- coding: utf-8 -*-
"""Domain 5: Cybersecurity & Cryptography (100 core terms)"""

terms = [
    ("Cybersecurity", "/ˌsaɪ.bə.sɪˈkjʊə.rə.ti/", "noun", "security", "An ninh mạng & Mật mã",
     "An ninh mạng: việc bảo vệ các hệ thống máy tính, mạng và dữ liệu khỏi các cuộc tấn công kỹ thuật số.",
     "Investing in cybersecurity shields business operations from devastating data thefts.", "Đầu tư vào an ninh mạng bảo vệ hoạt động kinh doanh khỏi các vụ đánh cắp dữ liệu tàn khốc.",
     "An ninh mạng", "🛡️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cryptography", "/krɪpˈtɒɡ.rə.fi/", "noun", "security", "An ninh mạng & Mật mã",
     "Mật mã học: khoa học nghiên cứu việc mã hóa thông tin để ngăn bên thứ ba đọc được thông điệp.",
     "Modern internet banking relies entirely on advanced mathematical cryptography.", "Ngân hàng trực tuyến hiện đại phụ thuộc hoàn toàn vào mật mã học toán học tiên tiến.",
     "Mật mã học Cryptography", "🔐", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Encryption", "/ɪnˈkrɪp.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã hóa: quá trình chuyển đổi bản rõ có thể đọc được thành bản mã bí mật bằng thuật toán.",
     "Database encryption protects customer payment records even if hard drives are stolen.", "Mã hóa CSDL bảo vệ hồ sơ thanh toán của khách ngay cả khi ổ cứng bị đánh cắp.",
     "Mã hóa dữ liệu", "🔒", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Decryption", "/diːˈkrɪp.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Giải mã: quá trình chuyển đổi dữ liệu đã mã hóa trở lại dạng bản rõ ban đầu bằng khóa bí mật.",
     "The client application performs decryption using the shared session key.", "Ứng dụng máy trạm thực hiện giải mã bằng cách dùng khóa phiên được chia sẻ.",
     "Giải mã dữ liệu", "🔓", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Plaintext", "/ˈpleɪn.tekst/", "noun", "security", "An ninh mạng & Mật mã",
     "Bản rõ: dữ liệu ở dạng gốc chưa mã hóa mà bất kỳ ai cũng có thể đọc hiểu được trực tiếp.",
     "Never store plaintext passwords in database columns.", "Tuyệt đối không lưu mật khẩu dạng bản rõ trong các cột cơ sở dữ liệu.",
     "Bản rõ Plaintext", "📄", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Ciphertext", "/ˈsaɪ.fə.tekst/", "noun", "security", "An ninh mạng & Mật mã",
     "Bản mã: kết quả đầu ra sau khi bản rõ được mã hóa bằng thuật toán mật mã.",
     "Without the decryption key, the ciphertext appears as random gibberish.", "Nếu không có khóa giải mã, bản mã chỉ trông giống các ký tự vô nghĩa ngẫu nhiên.",
     "Bản mã Ciphertext", "🧩", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Symmetric Encryption", "/sɪˈmet.rɪk ɪnˈkrɪp.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã hóa đối xứng: sử dụng duy nhất một khóa bí mật chung cho cả hai quá trình mã hóa và giải mã.",
     "AES is the global industry standard for high-speed symmetric encryption.", "AES là tiêu chuẩn công nghiệp toàn cầu cho việc mã hóa đối xứng tốc độ cao.",
     "Mã hóa đối xứng", "🗝️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Asymmetric Encryption", "/ˌeɪ.sɪˈmet.rɪk ɪnˈkrɪp.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã hóa bất đối xứng: sử dụng một cặp khóa gồm khóa công khai để mã hóa và khóa riêng để giải mã.",
     "Asymmetric encryption solves the difficult problem of secure key exchange.", "Mã hóa bất đối xứng giải quyết bài toán hóc búa về việc trao đổi khóa an toàn qua mạng.",
     "Mã hóa bất đối xứng", "🔑", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Public Key", "/ˈpʌb.lɪk kiː/", "noun", "security", "An ninh mạng & Mật mã",
     "Khóa công khai: khóa trong cặp khóa bất đối xứng có thể chia sẻ rộng rãi cho mọi người.",
     "Share your public key on GitHub to verify signed commits.", "Chia sẻ khóa công khai của bạn trên GitHub để xác minh các commit đã được ký số.",
     "Khóa công khai Public Key", "🌐", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Private Key", "/ˈpraɪ.vət kiː/", "noun", "security", "An ninh mạng & Mật mã",
     "Khóa bí mật: khóa trong cặp khóa bất đối xứng phải được giữ tuyệt mật và không bao giờ chia sẻ.",
     "If a server's private key leaks, all encrypted communications are compromised.", "Nếu khóa bí mật của máy chủ bị rò rỉ, mọi liên lạc mã hóa đều bị xâm phạm.",
     "Khóa bí mật Private Key", "🤫", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Key Exchange", "/kiː ɪksˈtʃeɪndʒ/", "noun", "security", "An ninh mạng & Mật mã",
     "Trao đổi khóa: giao thức cho phép hai bên thống nhất một khóa mật mã chung qua kênh không an toàn.",
     "Diffie-Hellman key exchange enables safe key negotiation across the internet.", "Trao đổi khóa Diffie-Hellman cho phép thương lượng khóa an toàn qua mạng Internet.",
     "Trao đổi khóa", "🤝", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("RSA Algorithm", "/ˌɑːr.esˈeɪ ˈæl.ɡə.rɪ.ðəm/", "noun", "security", "An ninh mạng & Mật mã",
     "Thuật toán RSA: thuật toán mật mã bất đối xứng dựa trên độ khó của bài toán phân tích thừa số nguyên lớn.",
     "RSA-4096 keys provide resilient security against modern brute-force computation.", "Khóa RSA-4096 mang lại độ an toàn vững chắc trước sức mạnh tính toán vét cạn hiện đại.",
     "Thuật toán mã hóa RSA", "🏛️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("AES (Advanced Encryption Standard)", "/ˌeɪ.iːˈes/", "noun", "security", "An ninh mạng & Mật mã",
     "Tiêu chuẩn mã hóa tiên tiến: chuẩn mã hóa khối đối xứng được chính phủ và các tập đoàn toàn cầu tin dùng.",
     "AES-256 is trusted worldwide to safeguard highly classified government data.", "AES-256 được tin dùng trên toàn thế giới để bảo vệ dữ liệu tối mật của chính phủ.",
     "Chuẩn mã hóa AES", "🛡️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("DES (Data Encryption Standard)", "/ˌdiː.iːˈes/", "noun", "security", "An ninh mạng & Mật mã",
     "Tiêu chuẩn mã hóa dữ liệu cũ: chuẩn mã hóa đối xứng 56-bit đã lỗi thời và dễ dàng bị bẻ khóa.",
     "DES is deprecated because its 56-bit key can be cracked in hours.", "DES đã bị ngừng sử dụng vì khóa 56-bit của nó có thể bị bẻ khóa chỉ trong vài giờ.",
     "Chuẩn DES cũ", "⚠️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Elliptic Curve Cryptography (ECC)", "/ɪˈlɪp.tɪk kɜːv/", "noun", "security", "An ninh mạng & Mật mã",
     "Mật mã đường cong elliptic: kỹ thuật mật mã bất đối xứng cung cấp độ an toàn cao với kích thước khóa nhỏ hơn nhiều so với RSA.",
     "ECC provides equivalent cryptographic strength to RSA with much shorter key sizes.", "ECC mang lại độ bảo mật tương đương RSA nhưng với kích thước khóa ngắn hơn nhiều.",
     "Mật mã đường cong ECC", "📈", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cryptographic Hash", "/ˌkrɪp.təˈɡræf.ɪk hæʃ/", "noun", "security", "An ninh mạng & Mật mã",
     "Hàm băm mật mã: hàm một chiều tạo ra chuỗi tóm lược kích thước cố định, không thể đảo ngược.",
     "A cryptographic hash must resist preimage, second preimage, and collision attacks.", "Một hàm băm mật mã phải chống lại được tấn công tiền ảnh và đụng độ băm.",
     "Hàm băm mật mã", "⚙️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("SHA-256", "/ˌes.eɪtʃˈeɪ/", "noun", "security", "An ninh mạng & Mật mã",
     "Thuật toán băm an toàn 256-bit: thuật toán băm tạo ra chuỗi giá trị 64 ký tự hex, dùng trong SSL và Bitcoin.",
     "Bitcoin mining calculates quadrillions of SHA-256 hashes per second.", "Khai thác Bitcoin tính toán hàng triệu tỷ hàm băm SHA-256 mỗi giây.",
     "Thuật toán băm SHA-256", "🔢", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("MD5", "/ˌem.diːˈfaɪv/", "noun", "security", "An ninh mạng & Mật mã",
     "Thuật toán băm MD5: tạo chuỗi 128-bit, đã bị bẻ gãy đụng độ và không còn an toàn cho mục đích bảo mật.",
     "Do not hash passwords with MD5 due to severe collision vulnerabilities.", "Không được băm mật khẩu bằng MD5 vì các lỗ hổng đụng độ nghiêm trọng.",
     "Thuật toán MD5 cũ", "⚠️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Digital Signature", "/ˈdɪdʒ.ɪ.təl ˈsɪɡ.nə.tʃər/", "noun", "security", "An ninh mạng & Mật mã",
     "Chữ ký số: cơ chế toán học dùng khóa riêng để xác thực tính toàn vẹn và nguồn gốc của dữ liệu điện tử.",
     "Software installers include digital signatures to confirm authentic origins.", "Trình cài đặt phần mềm tích hợp chữ ký số để xác nhận nguồn gốc chính chủ.",
     "Chữ ký số", "✍️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Digital Certificate", "/ˈdɪdʒ.ɪ.təl səˈtɪf.ɪ.kət/", "noun", "security", "An ninh mạng & Mật mã",
     "Chứng chỉ số: chứng thực điện tử gắn kết một khóa công khai với danh tính của một tổ chức do bên CA ký.",
     "The browser verified the server's identity through its TLS digital certificate.", "Trình duyệt đã xác minh danh tính của máy chủ thông qua chứng chỉ số TLS của nó.",
     "Chứng chỉ số điện tử", "📜", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Public Key Infrastructure (PKI)", "/ˌpiː.keɪˈaɪ/", "noun", "security", "An ninh mạng & Mật mã",
     "Hạ tầng khóa công khai: hệ thống các quy tắc, chính sách và phần mềm để quản lý, cấp phát và thu hồi chứng chỉ số.",
     "Enterprise PKI infrastructure distributes device certificates across the fleet.", "Hạ tầng PKI doanh nghiệp phân phối các chứng chỉ thiết bị trong toàn hệ thống.",
     "Hạ tầng PKI", "🏛️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("End-to-End Encryption (E2EE)", "/end tu end ɪnˈkrɪp.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã hóa đầu cuối: dữ liệu chỉ được mã hóa trên thiết bị gửi và chỉ giải mã trên thiết bị nhận, máy chủ trung gian không thể đọc.",
     "Signal uses end-to-end encryption to prevent eavesdropping by telecom providers.", "Signal dùng mã hóa đầu cuối để ngăn chặn nhà mạng viễn thông nghe lén.",
     "Mã hóa đầu cuối E2EE", "🔒", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Zero-Knowledge Proof", "/ˈzɪə.rəʊ ˈnɒl.ɪdʒ pruːf/", "noun", "security", "An ninh mạng & Mật mã",
     "Bằng chứng không kiến thức: phương pháp toán học chứng minh một điều là đúng mà không để lộ bất kỳ thông tin nào về điều đó.",
     "Zero-knowledge proofs verify user eligibility without revealing personal ages.", "Bằng chứng không kiến thức xác minh tính đủ điều kiện của người dùng mà không để lộ tuổi tác.",
     "Bằng chứng không kiến thức", "🔮", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Salt", "/sɒlt/", "noun", "security", "An ninh mạng & Mật mã",
     "Muối bảo mật: chuỗi ngẫu nhiên được thêm vào mật khẩu trước khi băm để chống lại tấn công bảng cầu vồng.",
     "Generating a unique cryptographic salt per user stops rainbow table lookups.", "Tạo muối mật mã duy nhất cho mỗi người dùng chặn việc tra cứu qua bảng cầu vồng.",
     "Muối mật mã Salt", "🧂", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Pepper", "/ˈpep.ər/", "noun", "security", "An ninh mạng & Mật mã",
     "Tiêu bảo mật: giá trị bí mật bổ sung lưu trữ riêng biệt ngoài CSDL và thêm vào mọi mật khẩu khi băm.",
     "Unlike a salt, the secret pepper is stored separately inside an HSM.", "Khác với muối, tiêu bí mật được lưu riêng biệt bên trong thiết bị phần cứng HSM.",
     "Tiêu mật mã Pepper", "🌶️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Bcrypt", "/ˈbiː.krɪpt/", "noun", "security", "An ninh mạng & Mật mã",
     "Thuật toán Bcrypt: hàm băm mật khẩu có cơ chế điều chỉnh độ khó tính toán để làm chậm các nỗ lực vét cạn.",
     "Bcrypt includes adaptive work factors that increase with CPU speeds.", "Bcrypt có hệ số chi phí thích ứng tăng dần theo tốc độ phát triển của CPU.",
     "Hàm băm mật khẩu Bcrypt", "🔒", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Argon2", "/ˈɑːr.ɡɒn tuː/", "noun", "security", "An ninh mạng & Mật mã",
     "Thuật toán Argon2: hàm băm mật khẩu hiện đại nhất thế giới, chiến thắng giải vô địch băm mật khẩu PHC.",
     "Argon2id protects against both GPU cracking and side-channel timing attacks.", "Argon2id chống lại cả tấn công bẻ khóa bằng GPU lẫn tấn công kênh kề thời gian.",
     "Chuẩn băm Argon2", "🏆", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("PBKDF2", "/ˌpiː.biː.keɪ.diː.efˈtuː/", "noun", "security", "An ninh mạng & Mật mã",
     "Hàm phái sinh khóa: kỹ thuật lặp lại hàm băm hàng trăm nghìn lần để tạo khóa mã hóa từ mật khẩu.",
     "NIST guidelines recommend at least 600,000 iterations for PBKDF2 with SHA-256.", "Hướng dẫn của NIST khuyến nghị ít nhất 600.000 vòng lặp cho PBKDF2 với SHA-256.",
     "Hàm phái sinh khóa PBKDF2", "🔄", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Authentication", "/ɔːˌθen.tɪˈkeɪ.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Xác thực danh tính: quá trình chứng minh người dùng hay hệ thống đúng là người mà họ tự nhận (Who are you?).",
     "Authentication validates user credentials before granting session tokens.", "Xác thực kiểm tra thông tin đăng nhập của người dùng trước khi cấp token phiên.",
     "Xác thực danh tính", "🆔", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Authorization", "/ˌɔː.θər.aɪˈzeɪ.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Ủy quyền / Phân quyền: quá trình xác định người dùng đã xác thực có quyền truy cập tài nguyên nào (What can you do?).",
     "Authorization checks ensure standard members cannot edit admin settings.", "Kiểm tra phân quyền đảm bảo thành viên thường không thể sửa cài đặt quản trị.",
     "Phân quyền Authorization", "🛂", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Factor Authentication (MFA)", "/ˌmʌl.ti ˈfæk.tər/", "noun", "security", "An ninh mạng & Mật mã",
     "Xác thực đa yếu tố: yêu cầu ít nhất hai bằng chứng độc lập (mật khẩu, điện thoại, vân tay) để đăng nhập.",
     "Enforcing MFA on company accounts blocks over 99 percent of automated attacks.", "Bắt buộc dùng MFA trên tài khoản công ty ngăn chặn trên 99% các cuộc tấn công tự động.",
     "Xác thực đa yếu tố MFA", "📱", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Two-Factor Authentication (2FA)", "/tuː ˈfæk.tər/", "noun", "security", "An ninh mạng & Mật mã",
     "Xác thực hai yếu tố: trường hợp cụ thể của MFA yêu cầu kết hợp hai yếu tố xác thực riêng biệt.",
     "Receive a 6-digit TOTP code on your authenticator app for 2FA.", "Nhận mã TOTP gồm 6 chữ số trên ứng dụng xác thực để thực hiện 2FA.",
     "Xác thực hai yếu tố 2FA", "📲", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Biometric Authentication", "/ˌbaɪ.əʊˈmet.rɪk/", "noun", "security", "An ninh mạng & Mật mã",
     "Xác thực sinh trắc học: nhận diện danh tính dựa trên đặc điểm sinh học như vân tay, khuôn mặt hoặc mống mắt.",
     "Modern smartphones support fingerprint and facial biometric authentication.", "Điện thoại thông minh hiện đại hỗ trợ xác thực sinh trắc học bằng vân tay và khuôn mặt.",
     "Xác thực sinh trắc học", "👁️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Single Sign-On (SSO)", "/ˈsɪŋ.ɡəl saɪn ɒn/", "noun", "security", "An ninh mạng & Mật mã",
     "Đăng nhập một lần: giải pháp cho phép người dùng đăng nhập một lần duy nhất để truy cập tất cả ứng dụng.",
     "SSO simplifies enterprise onboarding via centralized Okta accounts.", "SSO đơn giản hóa quy trình đăng nhập doanh nghiệp thông qua tài khoản Okta tập trung.",
     "Đăng nhập một lần SSO", "🚪", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("OAuth 2.0", "/ˈoʊ.ɔːθ tuː/", "noun", "security", "An ninh mạng & Mật mã",
     "Chuẩn ủy quyền mở: giao thức cho phép ứng dụng bên thứ ba truy cập tài nguyên người dùng mà không cần biết mật khẩu.",
     "Signing in with Google or GitHub leverages the OAuth 2.0 authorization framework.", "Đăng nhập bằng tài khoản Google hoặc GitHub tận dụng khung ủy quyền OAuth 2.0.",
     "Chuẩn ủy quyền OAuth 2.0", "🔑", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("OpenID Connect (OIDC)", "/ˌoʊ.pən.aɪˈdiː/", "noun", "security", "An ninh mạng & Mật mã",
     "Tầng xác thực OIDC: lớp xác thực danh tính người dùng xây dựng trên nền tảng của khung ủy quyền OAuth 2.0.",
     "OIDC issues an ID Token containing authenticated user profile claims.", "OIDC phát hành ID Token chứa thông tin hồ sơ người dùng đã được xác thực.",
     "Chuẩn định danh OIDC", "🆔", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("JSON Web Token (JWT)", "/dʒɒt/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã thông báo JWT: chuẩn nhỏ gọn an toàn để truyền thông tin giữa các bên dưới dạng đối tượng JSON có chữ ký số.",
     "Stateless REST APIs verify incoming requests using signed JWT bearer tokens.", "API REST phi trạng thái xác minh các yêu cầu gửi đến bằng JWT có chữ ký số.",
     "Mã thông báo JWT", "🎟️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Session Hijacking", "/ˈseʃ.ən ˈhaɪ.dʒæk.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Chiếm đoạt phiên làm việc: hành vi đánh cắp mã session ID hợp lệ của người dùng để mạo danh họ trên hệ thống.",
     "Enforcing HTTPS and secure cookie flags prevents session hijacking over Wi-Fi.", "Bắt buộc HTTPS và cờ cookie an toàn ngăn chặn chiếm đoạt phiên qua mạng Wi-Fi.",
     "Chiếm đoạt phiên", "🏴‍☠️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Session Fixation", "/ˈseʃ.ən fɪkˈseɪ.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Cố định phiên: kẻ tấn công ép nạn nhân sử dụng một session ID đã biết trước để sau đó đăng nhập mạo danh.",
     "Regenerate session identifiers upon user login to prevent session fixation.", "Tái tạo lại định danh phiên sau khi người dùng đăng nhập để ngăn chặn tấn công cố định phiên.",
     "Tấn công cố định phiên", "📌", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Vulnerability", "/ˌvʌl.nər.əˈbɪl.ə.ti/", "noun", "security", "An ninh mạng & Mật mã",
     "Lỗ hổng bảo mật: điểm yếu hoặc lỗi sai trong thiết kế hoặc mã nguồn phần mềm có thể bị khai thác.",
     "A security audit found an unpatched vulnerability in the legacy web framework.", "Đợt kiểm toán bảo mật đã phát hiện lỗ hổng chưa vá trong framework web cũ.",
     "Lỗ hổng bảo mật", "🕳️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Exploit", "/ɪkˈsplɔɪt/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã khai thác: chương trình hoặc đoạn mã đặc thù được thiết kế để tấn công một lỗ hổng cụ thể.",
     "Security researchers published a proof-of-concept exploit for the zero-day flaw.", "Các nhà nghiên cứu bảo mật đã công bố mã khai thác minh chứng cho lỗ hổng zero-day.",
     "Mã khai thác Exploit", "💣", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Zero-Day Exploit", "/ˈzɪə.rəʊ deɪ/", "noun", "security", "An ninh mạng & Mật mã",
     "Khai thác Zero-Day: cuộc tấn công nhắm vào lỗ hổng chưa từng được nhà phát triển biết đến hoặc chưa có bản vá.",
     "Zero-day exploits command high prices on underground cybercrime markets.", "Các khai thác zero-day có giá rất cao trên thị trường tội phạm mạng ngầm.",
     "Khai thác Zero-Day", "⏳", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("CVE (Common Vulnerabilities and Exposures)", "/ˌsiː.viːˈiː/", "noun", "security", "An ninh mạng & Mật mã",
     "Hệ thống định danh CVE: danh bạ chuẩn hóa gán mã định danh duy nhất cho các lỗ hổng an ninh được công bố.",
     "Log4j's famous remote code execution flaw was tracked under CVE-2021-44228.", "Lỗ hổng thực thi mã từ xa nổi tiếng của Log4j được theo dõi dưới mã CVE-2021-44228.",
     "Định danh lỗ hổng CVE", "🏷️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Attack Surface", "/əˈtæk ˈsɜː.fɪs/", "noun", "security", "An ninh mạng & Mật mã",
     "Bề mặt tấn công: tổng số điểm tiếp xúc, cổng mở và giao diện mà kẻ tấn công có thể xâm nhập hệ thống.",
     "Closing unused firewall ports reduces the overall attack surface drastically.", "Đóng các cổng tường lửa không dùng giúp thu hẹp đáng kể bề mặt tấn công tổng thể.",
     "Bề mặt tấn công", "🎯", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Threat Modeling", "/θret ˈmɒd.əl.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Mô hình hóa mối đe dọa: quy trình kỹ thuật xác định các nguy cơ an ninh tiềm ẩn và lập kế hoạch giảm thiểu rủi ro.",
     "Engineers conduct threat modeling during architectural design to safeguard APIs.", "Kỹ sư tiến hành mô hình hóa mối đe dọa khi thiết kế kiến trúc để bảo vệ API.",
     "Mô hình hóa mối đe dọa", "📐", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Penetration Testing (Pen Test)", "/ˌpen.ɪˈtreɪ.ʃən ˈtes.tɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Kiểm thử thâm nhập: mô phỏng cuộc tấn công thực tế có đạo đức để tìm ra các lỗ hổng của hệ thống.",
     "Banks mandate annual penetration testing by certified third-party ethical hackers.", "Ngân hàng bắt buộc kiểm thử thâm nhập hàng năm bởi các hacker mũ trắng có chứng chỉ.",
     "Kiểm thử thâm nhập", "🕵️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Ethical Hacking", "/ˈeθ.ɪ.kəl ˈhæk.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Hacking có đạo đức: việc sử dụng các kỹ thuật tấn công với sự cho phép để bảo vệ và vá lỗi hệ thống.",
     "Ethical hacking strengthens organizational defenses against state-sponsored actors.", "Hacking có đạo đức củng cố hàng phòng thủ của tổ chức trước các thế lực tấn công.",
     "Hacking có đạo đức", "🎩", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("White Hat Hacker", "/waɪt hæt ˈhæk.ər/", "noun", "security", "An ninh mạng & Mật mã",
     "Hacker mũ trắng: chuyên gia an ninh mạng hợp pháp tìm kiếm lỗ hổng để báo cáo và giúp khắc phục.",
     "White hat hackers report flaws responsibly through official disclosure programs.", "Hacker mũ trắng báo cáo lỗ hổng một cách có trách nhiệm qua các chương trình công bố.",
     "Hacker mũ trắng", "⚪", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Black Hat Hacker", "/blæk hæt ˈhæk.ər/", "noun", "security", "An ninh mạng & Mật mã",
     "Hacker mũ đen: tin tặc bất hợp pháp đột nhập hệ thống nhằm mục đích trục lợi cá nhân hoặc phá hoại.",
     "Black hat hackers trade stolen customer databases on illicit forums.", "Hacker mũ đen mua bán cơ sở dữ liệu khách hàng bị đánh cắp trên các diễn đàn ngầm.",
     "Hacker mũ đen", "⚫", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Red Team", "/red tiːm/", "noun", "security", "An ninh mạng & Mật mã",
     "Đội Đỏ: nhóm chuyên gia an ninh đóng vai kẻ tấn công nhằm kiểm tra độ vững chắc của phòng tuyến tổ chức.",
     "The red team simulated an advanced social engineering breach against employees.", "Đội đỏ đã mô phỏng một cuộc tấn công phi kỹ thuật tinh vi nhắm vào nhân viên.",
     "Đội tấn công Red Team", "🔴", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Blue Team", "/bluː tiːm/", "noun", "security", "An ninh mạng & Mật mã",
     "Đội Xanh: nhóm phòng thủ an ninh chịu trách nhiệm giám sát, phát hiện và đẩy lùi các cuộc tấn công.",
     "The blue team responded quickly to contain the simulated malware infection.", "Đội xanh phản ứng mau lẹ để cô lập sự cố lây nhiễm mã độc được mô phỏng.",
     "Đội phòng thủ Blue Team", "🔵", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Bug Bounty", "/bʌɡ ˈbaʊn.ti/", "noun", "security", "An ninh mạng & Mật mã",
     "Chương trình săn tiền thưởng lỗi: chính sách thưởng tiền cho các nhà nghiên cứu độc lập phát hiện và báo lỗi bảo mật.",
     "Tech companies reward researchers up to tens of thousands of dollars per critical bug.", "Các công ty công nghệ trao thưởng tới hàng chục nghìn đô la cho mỗi lỗi nghiêm trọng.",
     "Săn tiền thưởng lỗi", "💰", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Malware", "/ˈmæl.weər/", "noun", "security", "An ninh mạng & Mật mã",
     "Phần mềm độc hại: thuật ngữ chung chỉ mọi phần mềm gây hại cho máy tính (virus, worm, ransomware, v.v.).",
     "Antivirus software monitors file activity to block malware execution.", "Phần mềm diệt virus giám sát hoạt động tệp để ngăn chặn phần mềm độc hại thực thi.",
     "Phần mềm độc hại Malware", "👾", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Ransomware", "/ˈræn.səm.weər/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã độc tống tiền: loại malware mã hóa toàn bộ tệp dữ liệu của nạn nhân và đòi tiền chuộc để giải mã.",
     "Offline immutable backups protect companies from debilitating ransomware attacks.", "Sao lưu bất biến ngoại tuyến bảo vệ công ty khỏi các đợt tấn công mã độc tống tiền.",
     "Mã độc tống tiền Ransomware", "💸", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Spyware", "/ˈspaɪ.weər/", "noun", "security", "An ninh mạng & Mật mã",
     "Phần mềm gián điệp: phần mềm bí mật theo dõi hoạt động và thu thập thông tin người dùng mà họ không hay biết.",
     "Spyware exfiltrates browsing histories and keyboard inputs to covert command servers.", "Phần mềm gián điệp tuồn lịch sử duyệt web và thao tác phím về máy chủ điều khiển bí mật.",
     "Phần mềm gián điệp", "🕵️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Trojan Horse", "/ˌtrəʊ.dʒən ˈhɔːs/", "noun", "security", "An ninh mạng & Mật mã",
     "Ngựa Trojan: phần mềm độc hại ngụy trang dưới dạng ứng dụng hữu ích để lừa người dùng cài đặt.",
     "A malicious trojan horse was disguised as a harmless PDF viewer utility.", "Một con trojan độc hại đã được ngụy trang dưới dạng tiện ích xem PDF vô hại.",
     "Mã độc Trojan Horse", "🐴", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Computer Worm", "/kəmˈpjuː.tər wɜːm/", "noun", "security", "An ninh mạng & Mật mã",
     "Sâu máy tính: phần mềm độc hại có khả năng tự nhân bản và tự lan truyền qua mạng mà không cần can thiệp con người.",
     "The WannaCry worm spread across vulnerable SMB network ports automatically.", "Sâu WannaCry đã tự động lây lan qua các cổng mạng SMB có lỗ hổng.",
     "Sâu máy tính Worm", "🪱", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Rootkit", "/ˈruːt.kɪt/", "noun", "security", "An ninh mạng & Mật mã",
     "Mã độc chiếm quyền gốc: phần mềm ẩn nấp sâu trong kernel hệ điều hành để che giấu dấu vết của kẻ tấn công.",
     "Rootkits hide running malicious processes from the operating system task manager.", "Rootkit che giấu các tiến trình độc hại đang chạy khỏi trình quản lý tác vụ của hệ điều hành.",
     "Mã độc chiếm quyền Rootkit", "🌱", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Keylogger", "/ˈkiːˌlɒɡ.ər/", "noun", "security", "An ninh mạng & Mật mã",
     "Trình ghi thao tác phím: phần mềm hoặc phần cứng ghi lại mọi phím gõ để đánh cắp mật khẩu và thông tin thẻ tín dụng.",
     "Keyloggers capture passwords in real-time as users type them into login forms.", "Keylogger ghi lại mật khẩu theo thời gian thực khi người dùng gõ vào form đăng nhập.",
     "Trình ghi phím Keylogger", "⌨️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Botnet", "/ˈbɒt.net/", "noun", "security", "An ninh mạng & Mật mã",
     "Mạng máy tính ma: mạng lưới hàng triệu thiết bị bị nhiễm độc điều khiển từ xa để thực hiện các cuộc tấn công DDoS lớn.",
     "Mirai botnet commandeered millions of IoT devices to launch crippling internet attacks.", "Botnet Mirai đã thâu tóm hàng triệu thiết bị IoT để mở các đợt tấn công mạng tê liệt.",
     "Mạng máy tính ma Botnet", "🤖", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Denial of Service (DoS)", "/dɪˈnaɪ.əl əv ˈsɜː.vɪs/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công từ chối dịch vụ: làm quá tải tài nguyên máy chủ khiến người dùng hợp pháp không thể truy cập dịch vụ.",
     "A single DoS script flooded the web application with bogus compute-heavy queries.", "Một script DoS đơn lẻ đã làm ngập ứng dụng web bằng các truy vấn giả lập tính toán nặng.",
     "Từ chối dịch vụ DoS", "🚫", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Distributed Denial of Service (DDoS)", "/ˌdiː.dɒs/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công DDoS phân tán: huy động đồng loạt lưu lượng khổng lồ từ nhiều máy tính khắp thế giới để đánh sập mục tiêu.",
     "Cloudflare mitigated a record-shattering 71 million requests per second DDoS assault.", "Cloudflare đã giảm thiểu đợt tấn công DDoS kỷ lục 71 triệu yêu cầu mỗi giây.",
     "Tấn công từ chối dịch vụ DDoS", "🌊", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Brute Force Attack", "/bruːt fɔːs əˈtæk/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công vét cạn: thử lần lượt từng tổ hợp mật khẩu có thể có cho đến khi đoán trúng.",
     "Rate limiting login attempts blocks automated brute force attacks effectively.", "Giới hạn số lần đăng nhập chặn hiệu quả các cuộc tấn công vét cạn tự động.",
     "Tấn công vét cạn", "🔨", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Dictionary Attack", "/ˈdɪk.ʃən.ər.i əˈtæk/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công từ điển: thử các từ ngữ thông dụng và các mật khẩu phổ biến nhất có trong danh sách từ điển.",
     "A dictionary attack rapidly compromises accounts using common dictionary words.", "Tấn công từ điển nhanh chóng chiếm đoạt các tài khoản dùng từ ngữ thông dụng.",
     "Tấn công từ điển", "📖", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Rainbow Table Attack", "/ˈreɪn.bəʊ ˈteɪ.bəl/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công bảng cầu vồng: dùng bảng tính sẵn hàng triệu hàm băm của các mật khẩu để đảo ngược giá trị băm trong tích tắc.",
     "Salting password hashes completely neutralizes precomputed rainbow table attacks.", "Thêm muối vào chuỗi băm mật khẩu vô hiệu hóa hoàn toàn tấn công bảng cầu vồng.",
     "Tấn công bảng cầu vồng", "🌈", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Phishing", "/ˈfɪʃ.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công lừa đảo: gửi email hoặc tin nhắn giả danh tổ chức uy tín để lừa người dùng cung cấp thông tin mật.",
     "Employees underwent security training to recognize suspicious phishing emails.", "Nhân viên đã tham gia đào tạo an ninh mạng để nhận biết các email lừa đảo đáng ngờ.",
     "Tấn công lừa đảo Phishing", "🎣", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Spear Phishing", "/spɪə ˈfɪʃ.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Lừa đảo có chủ đích: cuộc tấn công lừa đảo được thiết kế riêng nhắm vào một cá nhân hoặc tổ chức cụ thể.",
     "Spear phishing campaigns target company executives using personalized fake memos.", "Chiến dịch lừa đảo có chủ đích nhắm vào ban giám đốc dùng văn bản giả mạo cá nhân hóa.",
     "Lừa đảo chủ đích Spear Phishing", "🎯", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Social Engineering", "/ˌsəʊ.ʃəl ˌen.dʒɪˈnɪə.rɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công phi kỹ thuật: thao túng tâm lý con người để khiến họ tự nguyện tiết lộ thông tin bí mật.",
     "Social engineering exploits human trust rather than technical software bugs.", "Tấn công phi kỹ thuật lợi dụng lòng tin con người thay vì lỗi phần mềm kỹ thuật.",
     "Tấn công phi kỹ thuật", "🧠", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Man-in-the-Middle (MitM)", "/mæn ɪn ðə ˈmɪd.əl/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công kẻ đứng giữa: kẻ tấn công bí mật chặn bắt và có thể chỉnh sửa liên lạc giữa hai bên đang trao đổi.",
     "Public open Wi-Fi hotspots without encryption are susceptible to MitM eavesdropping.", "Điểm phát Wi-Fi công cộng không mã hóa rất dễ bị nghe lén bởi tấn công kẻ đứng giữa.",
     "Tấn công kẻ đứng giữa", "🕵️‍♂️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("SQL Injection (SQLi)", "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Tiêm mã SQL: chèn các đoạn mã SQL độc hại vào ô nhập liệu để thao túng hoặc đánh cắp dữ liệu cơ sở dữ liệu.",
     "Parameterized queries and ORM layers eliminate SQL injection vulnerabilities.", "Truy vấn tham số hóa và tầng ORM loại bỏ hoàn toàn các lỗ hổng tiêm mã SQL.",
     "Lỗ hổng tiêm SQLi", "💉", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cross-Site Scripting (XSS)", "/ˌkrɒs.saɪt ˈskrɪp.tɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Tấn công XSS: tiêm mã kịch bản JavaScript độc hại vào trang web để chạy trên trình duyệt của người dùng khác.",
     "Sanitizing HTML outputs shields web visitors from cross-site scripting exploits.", "Làm sạch đầu ra HTML bảo vệ khách truy cập web khỏi các khai thác kịch bản chéo XSS.",
     "Tấn công kịch bản chéo XSS", "📜", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Stored XSS", "/stɔːd ˌkrɒs.saɪt ˈskrɪp.tɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "XSS lưu trữ: mã JavaScript độc được lưu vĩnh viễn vào CSDL và chạy mỗi khi người dùng khác tải trang xem bài viết.",
     "A stored XSS payload in a comment section executed inside everyone's browser.", "Đoạn mã XSS lưu trữ trong mục bình luận đã tự chạy bên trong trình duyệt của tất cả người xem.",
     "Lỗ hổng Stored XSS", "💾", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Reflected XSS", "/rɪˈflek.tɪd ˌkrɒs.saɪt ˈskrɪp.tɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "XSS phản xạ: mã kịch bản độc hại được phản xạ trực tiếp từ tham số URL trong yêu cầu HTTP về lại giao diện.",
     "Reflected XSS attacks trick users into clicking links containing malicious script parameters.", "Tấn công XSS phản xạ lừa người dùng nhấp vào các liên kết chứa tham số kịch bản độc hại.",
     "Lỗ hổng Reflected XSS", "🪞", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cross-Site Request Forgery (CSRF)", "/ˌkrɒs.saɪt rɪˈkwest ˈfɔː.dʒər.i/", "noun", "security", "An ninh mạng & Mật mã",
     "Giả mạo yêu cầu chéo: lừa trình duyệt của người dùng gửi yêu cầu trái phép tới trang web họ đã đăng nhập.",
     "SameSite cookie attributes and anti-CSRF tokens defend forms from forgery.", "Thuộc tính cookie SameSite và token chống CSRF bảo vệ biểu mẫu khỏi bị giả mạo.",
     "Giả mạo yêu cầu CSRF", "🎭", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Server-Side Request Forgery (SSRF)", "/ˌes.es.ɑːrˈef/", "noun", "security", "An ninh mạng & Mật mã",
     "Giả mạo yêu cầu phía máy chủ: lừa máy chủ thực hiện các yêu cầu mạng nội bộ mà kẻ tấn công không thể tiếp cận trực tiếp.",
     "SSRF exploits can read cloud instance metadata at internal IP 169.254.169.254.", "Khai thác SSRF có thể đọc siêu dữ liệu máy chủ đám mây tại IP nội bộ 169.254.169.254.",
     "Lỗ hổng giả mạo SSRF", "📡", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Clickjacking", "/ˈklɪkˌdʒæk.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Gài bẫy nhấp chuột: chèn iframe trong suốt lên trên các nút bấm hợp pháp để lừa người dùng nhấp chuột ngoài ý muốn.",
     "Set X-Frame-Options to DENY to shield applications from clickjacking.", "Thiết lập X-Frame-Options thành DENY để bảo vệ ứng dụng khỏi bẫy nhấp chuột.",
     "Gài bẫy nhấp Clickjacking", "🖱️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Path Traversal", "/pɑːθ trəˈvɜː.səl/", "noun", "security", "An ninh mạng & Mật mã",
     "Duyệt đường dẫn trái phép: dùng chuỗi '../' để truy cập vào các tệp hệ thống nhạy cảm ngoài thư mục cho phép.",
     "Path traversal allowed attackers to download /etc/passwd from the server.", "Lỗ hổng duyệt đường dẫn cho phép kẻ tấn công tải về tệp /etc/passwd từ máy chủ.",
     "Duyệt đường dẫn trái phép", "📁", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Command Injection", "/kəˈmɑːnd ɪnˈdʒek.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Tiêm lệnh hệ điều hành: truyền các câu lệnh hệ thống độc hại thông qua đầu vào ứng dụng chưa được kiểm duyệt.",
     "Passing unsanitized user inputs to shell execution commands risks complete server takeover.", "Truyền đầu vào chưa làm sạch vào lệnh shell có nguy cơ bị chiếm toàn quyền máy chủ.",
     "Tiêm lệnh hệ điều hành", "💻", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Insecure Deserialization", "/ˌɪn.sɪˈkjʊər diːˌsɪə.ri.ə.laɪˈzeɪ.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Giải tuần tự hóa không an toàn: chuyển đổi dữ liệu không tin cậy thành đối tượng dẫn tới thực thi mã từ xa.",
     "Insecure deserialization of Java objects resulted in remote code execution.", "Giải tuần tự hóa không an toàn các đối tượng Java đã dẫn tới việc thực thi mã từ xa.",
     "Giải tuần tự không an toàn", "💥", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Broken Access Control", "/ˈbrəʊ.kən ˈæk.ses kənˈtrəʊl/", "noun", "security", "An ninh mạng & Mật mã",
     "Hỏng kiểm soát truy cập: lỗi phân quyền cho phép người dùng xem hoặc sửa đổi tài nguyên của người dùng khác.",
     "Broken access control is currently the number one risk in the OWASP Top 10.", "Hỏng kiểm soát truy cập hiện là nguy cơ số 1 trong bảng xếp hạng OWASP Top 10.",
     "Hỏng kiểm soát truy cập", "🚪", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Privilege Escalation", "/ˈprɪv.əl.ɪdʒ ˌes.kəˈleɪ.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Leo thang đặc quyền: việc khai thác lỗ hổng để nâng quyền tài khoản thông thường lên quyền quản trị viên cao nhất.",
     "Vertical privilege escalation converts a regular user into a root administrator.", "Leo thang đặc quyền dọc chuyển đổi một người dùng thông thường thành quản trị viên root.",
     "Leo thang đặc quyền", "🪜", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Principle of Least Privilege", "/ˈprɪn.sə.pəl əv liːst ˈprɪv.əl.ɪdʒ/", "noun", "security", "An ninh mạng & Mật mã",
     "Nguyên tắc đặc quyền tối thiểu: chỉ cấp phát đúng những quyền tối thiểu cần thiết để người dùng hay ứng dụng hoàn thành nhiệm vụ.",
     "Under the principle of least privilege, developers do not get write access to production databases.", "Theo nguyên tắc đặc quyền tối thiểu, lập trình viên không có quyền ghi CSDL sản xuất.",
     "Đặc quyền tối thiểu", "🔒", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Access Control List (ACL)", "/ˈæk.ses kənˈtrəʊl lɪst/", "noun", "security", "An ninh mạng & Mật mã",
     "Danh sách kiểm soát truy cập: bảng quy tắc xác định đối tượng nào được phép thực hiện hành động nào trên tài nguyên.",
     "Configure AWS S3 bucket ACLs to prevent public read exposure.", "Cấu hình ACL của bộ chứa AWS S3 để ngăn chặn việc bị lộ đọc công khai.",
     "Danh sách kiểm soát ACL", "📋", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Role-Based Access Control (RBAC)", "/ˌɑːr.bæk/", "noun", "security", "An ninh mạng & Mật mã",
     "Kiểm soát truy cập dựa trên vai trò: gán quyền cho các vai trò công việc thay vì gán trực tiếp cho từng cá nhân.",
     "RBAC models assign permissions to roles like Editor, Manager, or Admin.", "Mô hình RBAC gán quyền cho các vai trò như Biên tập viên, Quản lý hoặc Quản trị viên.",
     "Kiểm soát vai trò RBAC", "👥", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Attribute-Based Access Control (ABAC)", "/ˈeɪ.bæk/", "noun", "security", "An ninh mạng & Mật mã",
     "Kiểm soát truy cập theo thuộc tính: cấp quyền dựa trên các thuộc tính của người dùng, tài nguyên và ngữ cảnh môi trường.",
     "ABAC evaluates conditions like time of day and user location before granting entry.", "ABAC đánh giá các điều kiện như thời điểm trong ngày và vị trí trước khi cấp quyền.",
     "Kiểm soát thuộc tính ABAC", "🏷️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Zero Trust Architecture", "/ˈzɪə.rəʊ trʌst/", "noun", "security", "An ninh mạng & Mật mã",
     "Kiến trúc Không tin cậy: nguyên lý an ninh 'không bao giờ tin tưởng, luôn luôn xác minh' mọi truy cập dù ở trong hay ngoài mạng.",
     "Zero Trust mandates continuous authentication for every microservice request.", "Zero Trust bắt buộc xác thực liên tục cho mọi yêu cầu gửi giữa các vi dịch vụ.",
     "Kiến trúc Không tin cậy", "🛡️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Sandboxing", "/ˈsænd.bɒks.ɪŋ/", "noun", "security", "An ninh mạng & Mật mã",
     "Cô lập môi trường (Sandboxing): kỹ thuật chạy mã nguồn đáng ngờ trong môi trường cô lập để ngăn lây lan hệ thống.",
     "Web browsers sandbox untrusted JavaScript execution to protect host operating systems.", "Trình duyệt web cô lập thực thi JavaScript để bảo vệ hệ điều hành máy chủ.",
     "Môi trường cô lập Sandbox", "🏖️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Web Application Firewall (WAF)", "/wæf/", "noun", "security", "An ninh mạng & Mật mã",
     "Tường lửa ứng dụng web: bộ lọc chuyên dụng kiểm tra và chặn các lưu lượng HTTP độc hại như SQLi, XSS ở tầng 7.",
     "AWS WAF inspects web incoming traffic against known attack signatures.", "AWS WAF kiểm tra lưu lượng web đến dựa trên các mẫu nhận dạng tấn công đã biết.",
     "Tường lửa ứng dụng WAF", "🧱", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Honeypot", "/ˈhʌn.i.pɒt/", "noun", "security", "An ninh mạng & Mật mã",
     "Bẫy mật ảo: hệ thống mồi nhử giả lập có chủ đích để dụ kẻ tấn công nhằm thu thập thông tin về phương thức của chúng.",
     "Deploying a honeypot traps automated bots and records their exploitation vectors.", "Triển khai một honeypot bẫy các bot tự động và ghi lại các vector khai thác của chúng.",
     "Bẫy mật ảo Honeypot", "🍯", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("SIEM (Security Information and Event Management)", "/siːm/", "noun", "security", "An ninh mạng & Mật mã",
     "Hệ thống quản lý sự kiện và an ninh: phần mềm tập hợp và phân tích nhật ký log từ mọi thiết bị theo thời gian thực.",
     "Splunk and Elastic serve as SIEM engines to correlate distributed security alerts.", "Splunk và Elastic đóng vai trò là các SIEM để liên kết các cảnh báo an ninh phân tán.",
     "Hệ thống quản lý SIEM", "📊", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("SOC (Security Operations Center)", "/sɒk/", "noun", "security", "An ninh mạng & Mật mã",
     "Trung tâm điều hành an ninh: đơn vị tập hợp các chuyên gia an ninh túc trực 24/7 để giám sát và phản ứng sự cố.",
     "SOC analysts triage high-severity intrusion alerts around the clock.", "Các chuyên viên phân tích SOC sàng lọc các cảnh báo xâm nhập nghiêm trọng suốt ngày đêm.",
     "Trung tâm điều hành SOC", "🏢", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Incident Response", "/ˈɪn.sɪ.dənt rɪˈspɒns/", "noun", "security", "An ninh mạng & Mật mã",
     "Phản ứng sự cố an ninh: quy trình có cấu trúc để phát hiện, cô lập, tiêu diệt và khôi phục hệ thống sau tấn công.",
     "A rapid incident response plan mitigated financial damage from the data breach.", "Kế hoạch phản ứng sự cố nhanh chóng đã giảm thiểu thiệt hại tài chính từ vụ vi phạm.",
     "Phản ứng sự cố an ninh", "🚨", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Data Breach", "/ˈdeɪ.tə briːtʃ/", "noun", "security", "An ninh mạng & Mật mã",
     "Rò rỉ dữ liệu: sự cố an ninh trong đó thông tin bí mật, nhạy cảm bị các đối tượng trái phép truy cập hoặc đánh cắp.",
     "The company notified affected users within 72 hours of the data breach.", "Công ty đã thông báo cho người dùng bị ảnh hưởng trong vòng 72 giờ kể từ khi rò rỉ dữ liệu.",
     "Rò rỉ dữ liệu Data Breach", "💥", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Data Loss Prevention (DLP)", "/ˈdeɪ.tə lɒs/", "noun", "security", "An ninh mạng & Mật mã",
     "Chống thất thoát dữ liệu: chiến lược và công cụ ngăn chặn nhân viên vô tình hay cố ý gửi dữ liệu nhạy cảm ra ngoài.",
     "DLP software detects and blocks credit card numbers pasted into unauthorized emails.", "Phần mềm DLP phát hiện và chặn số thẻ tín dụng bị dán vào email không được phép.",
     "Chống thất thoát dữ liệu", "🛑", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Non-Repudiation", "/ˌnɒn rɪˌpjuː.diˈeɪ.ʃən/", "noun", "security", "An ninh mạng & Mật mã",
     "Tính chống chối bỏ: đảm bảo bên gửi hoặc bên nhận không thể chối bỏ việc họ đã thực hiện giao dịch hoặc gửi thông điệp.",
     "Digital signatures provide cryptographic non-repudiation in legal electronic contracts.", "Chữ ký số cung cấp tính chống chối bỏ mật mã trong các hợp đồng điện tử pháp lý.",
     "Tính chống chối bỏ", "✍️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cryptanalysis", "/ˌkrɪpt.əˈnæl.ə.sɪs/", "noun", "security", "An ninh mạng & Mật mã",
     "Phân tích thám mã: khoa học nghiên cứu và tìm cách phá vỡ các hệ thống mật mã mà không cần biết khóa giải mã.",
     "Cryptanalysis revealed mathematical biases in earlier pseudo-random generators.", "Thám mã học đã vạch trần các sai lệch toán học trong các bộ tạo số ngẫu nhiên trước đây.",
     "Phân tích thám mã", "🔍", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Digital Forensics", "/ˈdɪdʒ.ɪ.təl fəˈren.zɪks/", "noun", "security", "An ninh mạng & Mật mã",
     "Điều tra số học: việc thu thập, phân tích và lưu giữ chứng cứ kỹ thuật số để phục vụ điều tra pháp lý.",
     "Digital forensics teams extracted memory dumps to identify attacker persistence tools.", "Đội điều tra số học đã trích xuất ảnh chụp RAM để nhận diện công cụ duy trì của kẻ tấn công.",
     "Điều tra số học Forensics", "🔬", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("OWASP Top 10", "/ˈoʊ.wɒsp/", "noun", "security", "An ninh mạng & Mật mã",
     "Bảng xếp hạng OWASP: tài liệu tiêu chuẩn quốc tế liệt kê 10 nguy cơ an ninh nghiêm trọng nhất cho ứng dụng web.",
     "Development teams review the OWASP Top 10 to write defensive backend code.", "Các nhóm phát triển tham khảo OWASP Top 10 để viết mã nguồn phòng thủ phía máy chủ.",
     "Tiêu chuẩn an ninh OWASP", "🔟", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("GDPR Compliance", "/ˌdʒiː.diː.piːˈɑːr kəmˈplaɪ.əns/", "noun", "security", "An ninh mạng & Mật mã",
     "Tuân thủ GDPR: tuân theo Quy định chung về bảo vệ dữ liệu của Liên minh Châu Âu về quyền riêng tư người dùng.",
     "Failing GDPR compliance results in penalties up to four percent of global annual turnover.", "Không tuân thủ GDPR có thể bị phạt tới 4% doanh thu toàn cầu hàng năm.",
     "Tuân thủ quy định GDPR", "⚖️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Defense in Depth", "/dɪˈfens ɪn depθ/", "noun", "security", "An ninh mạng & Mật mã",
     "Phòng thủ theo chiều sâu: chiến lược an ninh triển khai nhiều lớp phòng ngự độc lập bảo vệ lẫn nhau.",
     "Defense in depth ensures an attacker breaching the outer firewall still faces encryption.", "Phòng thủ chiều sâu đảm bảo nếu kẻ tấn công vượt qua tường lửa vẫn gặp lớp mã hóa.",
     "Phòng thủ chiều sâu", "🏰", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 5 terms count: {len(terms)}")
