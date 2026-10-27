# -*- coding: utf-8 -*-
"""Domain 4: Networking & Protocols (100 core terms)"""

terms = [
    ("Computer Network", "/kəmˈpjuː.tər ˈnet.wɜːk/", "noun", "networking", "Mạng máy tính",
     "Mạng máy tính: hệ thống các thiết bị tính toán kết nối với nhau để chia sẻ tài nguyên và dữ liệu.",
     "The enterprise computer network links branch offices across continents.", "Mạng máy tính doanh nghiệp liên kết các văn phòng chi nhánh trên khắp các châu lục.",
     "Mạng máy tính", "🌐", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Local Area Network (LAN)", "/læn/", "noun", "networking", "Mạng máy tính",
     "Mạng cục bộ: mạng kết nối các máy tính trong một phạm vi địa lý hẹp như tòa nhà, văn phòng.",
     "High-speed gigabit switches power the company's local area network.", "Các thiết bị chuyển mạch gigabit tốc độ cao vận hành mạng cục bộ của công ty.",
     "Mạng cục bộ LAN", "🏢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Wide Area Network (WAN)", "/wæn/", "noun", "networking", "Mạng máy tính",
     "Mạng diện rộng: mạng kết nối trên khoảng cách địa lý lớn như giữa các thành phố, quốc gia (Internet là WAN lớn nhất).",
     "SD-WAN technology optimizes traffic routing across corporate WAN networks.", "Công nghệ SD-WAN tối ưu hóa việc định tuyến lưu lượng qua các mạng diện rộng của công ty.",
     "Mạng diện rộng WAN", "🌍", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("Metropolitan Area Network (MAN)", "/mæn/", "noun", "networking", "Mạng máy tính",
     "Mạng đô thị: mạng kết nối quy mô bao phủ một thành phố hoặc khuôn viên trường đại học lớn.",
     "City governments lay fiber optic rings to create civic metropolitan area networks.", "Chính quyền thành phố lắp đặt vòng cáp quang để tạo ra mạng đô thị công cộng.",
     "Mạng đô thị MAN", "🏙️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Virtual Local Area Network (VLAN)", "/viː læn/", "noun", "networking", "Mạng máy tính",
     "Mạng LAN ảo: phân chia logic một mạng vật lý thành các phân đoạn mạng cô lập để tăng tính bảo mật.",
     "VLAN isolation keeps financial department traffic separated from guest Wi-Fi.", "Sự cô lập VLAN giữ cho lưu lượng phòng tài chính tách biệt khỏi Wi-Fi khách.",
     "Mạng ảo VLAN", "🔒", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Virtual Private Network (VPN)", "/ˌviː.piːˈen/", "noun", "networking", "Mạng máy tính",
     "Mạng riêng ảo: tạo đường hầm mã hóa an toàn qua Internet công cộng để truy cập mạng nội bộ.",
     "Employees connect through a corporate VPN when working remotely from home.", "Nhân viên kết nối qua VPN công ty khi làm việc từ xa tại nhà.",
     "Mạng riêng ảo VPN", "🛡️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("OSI Model", "/ˌoʊ.esˈaɪ ˈmɒd.əl/", "noun", "networking", "Mạng máy tính",
     "Mô hình OSI: mô hình khái niệm 7 tầng chuẩn hóa chức năng truyền thông của hệ thống viễn thông.",
     "Understanding the OSI model is essential for network troubleshooting.", "Hiểu mô hình OSI là điều thiết yếu để khắc phục sự cố mạng máy tính.",
     "Mô hình 7 tầng OSI", "🏛️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Physical Layer", "/ˈfɪz.ɪ.kəl ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng vật lý (Tầng 1): truyền tải các bit nhị phân thô qua môi trường vật lý (cáp quang, dây đồng, sóng vô tuyến).",
     "Damaged Ethernet cables cause physical layer connection drops.", "Cáp mạng Ethernet bị hỏng gây mất kết nối ở tầng vật lý.",
     "Tầng vật lý Tầng 1", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Data Link Layer", "/ˈdeɪ.tə lɪŋk ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng liên kết dữ liệu (Tầng 2): truyền khung dữ liệu (frame) tin cậy giữa hai nút mạng trực tiếp qua địa chỉ MAC.",
     "Network switches operate primarily at the Data Link layer using MAC addresses.", "Thiết bị chuyển mạch switch hoạt động chủ yếu ở tầng liên kết dữ liệu dùng địa chỉ MAC.",
     "Tầng liên kết Tầng 2", "🔗", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Network Layer", "/ˈnet.wɜːk ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng mạng (Tầng 3): định tuyến các gói tin (packet) qua nhiều mạng trung gian bằng địa chỉ IP.",
     "Routers inspect IP packet headers at the network layer to make routing decisions.", "Bộ định tuyến router kiểm tra tiêu đề gói IP ở tầng mạng để quyết định hướng đi.",
     "Tầng mạng Tầng 3", "🧭", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Transport Layer", "/ˈtræns.pɔːt ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng giao vận (Tầng 4): cung cấp truyền thông đầu cuối đáng tin cậy giữa các tiến trình thông qua TCP hoặc UDP.",
     "The transport layer manages flow control, error checking, and port multiplexing.", "Tầng giao vận quản lý điều khiển luồng, kiểm tra lỗi và dồn kênh số cổng.",
     "Tầng giao vận Tầng 4", "🚚", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Session Layer", "/ˈseʃ.ən ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng phiên (Tầng 5): thiết lập, quản lý và kết thúc các phiên kết nối giao tiếp giữa các ứng dụng.",
     "The session layer synchronizes dialogs between communicating machines.", "Tầng phiên đồng bộ hóa các cuộc hội thoại giữa các máy tính đang giao tiếp.",
     "Tầng phiên Tầng 5", "🤝", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Presentation Layer", "/ˌprez.ənˈteɪ.ʃən ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng trình diễn (Tầng 6): định dạng, mã hóa ký tự, nén dữ liệu và mã hóa bảo mật như TLS/SSL.",
     "Data encryption and decryption occur at the presentation layer.", "Mã hóa và giải mã dữ liệu diễn ra tại tầng trình diễn.",
     "Tầng trình diễn Tầng 6", "🎭", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Application Layer", "/ˌæp.lɪˈkeɪ.ʃən ˈleɪ.ər/", "noun", "networking", "Mạng máy tính",
     "Tầng ứng dụng (Tầng 7): giao diện tương tác trực tiếp với người dùng và phần mềm (HTTP, DNS, SMTP, SSH).",
     "Web browsers interact with servers using application layer protocols like HTTP.", "Trình duyệt web giao tiếp với máy chủ bằng các giao thức tầng ứng dụng như HTTP.",
     "Tầng ứng dụng Tầng 7", "📱", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("TCP/IP Model", "/ˌtiː.siːˈpiː aɪˈpiː ˈmɒd.əl/", "noun", "networking", "Mạng máy tính",
     "Mô hình TCP/IP: bộ giao thức 4 tầng thực tế tạo nên cấu trúc nền tảng của mạng Internet toàn cầu.",
     "The TCP/IP model defines Network Access, Internet, Transport, and Application layers.", "Mô hình TCP/IP gồm 4 tầng: Truy cập mạng, Internet, Giao vận và Ứng dụng.",
     "Mô hình chuẩn TCP/IP", "🌐", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("IP Address", "/aɪˈpiː əˈdres/", "noun", "networking", "Mạng máy tính",
     "Địa chỉ IP: nhãn số định danh duy nhất cho mỗi thiết bị tham gia vào mạng máy tính sử dụng giao thức IP.",
     "Every device on the local network receives an IP address dynamically via DHCP.", "Mỗi thiết bị trên mạng cục bộ nhận một địa chỉ IP động thông qua giao thức DHCP.",
     "Địa chỉ IP", "🏷️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("IPv4", "/ˌaɪ.piː.viːˈfɔːr/", "noun", "networking", "Mạng máy tính",
     "Giao thức IPv4: định dạng địa chỉ 32-bit gồm bốn số thập phân ngăn cách bởi dấu chấm (tối đa 4,3 tỷ địa chỉ).",
     "IPv4 address exhaustion accelerated the adoption of IPv6 across mobile carriers.", "Sự cạn kiệt địa chỉ IPv4 đã thúc đẩy các nhà mạng viễn thông áp dụng IPv6.",
     "Giao thức IPv4", "🔢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("IPv6", "/ˌaɪ.piː.viːˈsɪks/", "noun", "networking", "Mạng máy tính",
     "Giao thức IPv6: định dạng địa chỉ 128-bit biểu diễn bằng các cụm số thập lục phân, cung cấp không gian địa chỉ vô hạn.",
     "IPv6 provides roughly 340 undecillion unique addresses worldwide.", "IPv6 cung cấp khoảng 340 nghìn tỷ tỷ tỷ địa chỉ duy nhất trên toàn cầu.",
     "Giao thức IPv6", "♾️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Subnet", "/ˈsʌb.net/", "noun", "networking", "Mạng máy tính",
     "Mạng con: một phân vùng logic của một mạng IP lớn hơn giúp quản lý lưu lượng và bảo mật tốt hơn.",
     "Dividing a corporate network into subnets limits broadcast traffic congestion.", "Chia mạng doanh nghiệp thành các mạng con giúp giới hạn nghẽn lưu lượng quảng bá.",
     "Mạng con Subnet", "🔲", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Subnet Mask", "/ˈsʌb.net mɑːsk/", "noun", "networking", "Mạng máy tính",
     "Mặt nạ mạng con: số 32-bit phân chia địa chỉ IP thành hai phần: phần địa chỉ mạng và phần máy trạm.",
     "The subnet mask 255.255.255.0 designates the first 24 bits as the network portion.", "Mặt nạ mạng 255.255.255.0 chỉ định 24 bit đầu tiên là phần địa chỉ mạng.",
     "Mặt nạ mạng con", "🎭", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("CIDR (Classless Inter-Domain Routing)", "/ˈsaɪ.dər/", "noun", "networking", "Mạng máy tính",
     "Ký hiệu định tuyến không phân lớp: ký hiệu kèm dấu gạch chéo (/24, /16) chỉ định số lượng bít của mạng.",
     "The CIDR block 192.168.1.0/24 accommodates up to 254 usable host addresses.", "Khối CIDR 192.168.1.0/24 chứa tối đa 254 địa chỉ máy trạm có thể sử dụng.",
     "Định tuyến CIDR", "📏", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Default Gateway", "/dɪˈfɔːlt ˈɡeɪt.weɪ/", "noun", "networking", "Mạng máy tính",
     "Cổng mặc định: địa chỉ nút mạng (thường là router) nơi máy tính chuyển tiếp các gói tin gửi ra ngoài mạng cục bộ.",
     "Without a configured default gateway, computers cannot reach external websites.", "Nếu không có cổng mặc định được cấu hình, máy tính không thể truy cập các trang web bên ngoài.",
     "Cổng mặc định Gateway", "🚪", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Router", "/ˈruː.tər/", "noun", "networking", "Mạng máy tính",
     "Bộ định tuyến: thiết bị mạng chuyển tiếp các gói tin giữa các mạng máy tính khác nhau dựa trên địa chỉ IP.",
     "Edge routers route packets through optimal paths across the internet backbone.", "Bộ định tuyến biên điều hướng các gói tin theo đường đi tối ưu qua mạng trục Internet.",
     "Bộ định tuyến Router", "📡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Switch", "/swɪtʃ/", "noun", "networking", "Mạng máy tính",
     "Thiết bị chuyển mạch: thiết bị kết nối nhiều thiết bị trong cùng mạng LAN và chuyển tiếp khung dữ liệu theo địa chỉ MAC.",
     "A managed switch segments traffic into distinct virtual LAN environments.", "Thiết bị switch có quản lý phân chia lưu lượng vào các môi trường LAN ảo riêng biệt.",
     "Bộ chuyển mạch Switch", "🔀", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Network Hub", "/ˈnet.wɜːk hʌb/", "noun", "networking", "Mạng máy tính",
     "Bộ tập trung Hub: thiết bị mạng đơn giản tầng 1 phát tán bản sao của mọi tín hiệu nhận được tới tất cả các cổng.",
     "Legacy network hubs caused severe packet collisions and have been replaced by switches.", "Các hub mạng cũ gây ra đụng độ gói tin nghiêm trọng và đã bị thay thế bởi switch.",
     "Bộ tập trung Hub", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Bridge", "/brɪdʒ/", "noun", "networking", "Mạng máy tính",
     "Cầu nối mạng: thiết bị kết nối hai phân đoạn mạng khác nhau ở tầng liên kết dữ liệu để tạo thành một mạng thống nhất.",
     "Network bridges connect legacy Ethernet segments to modern fiber infrastructure.", "Cầu nối mạng kết nối các đoạn Ethernet cũ với hạ tầng cáp quang hiện đại.",
     "Cầu nối mạng Bridge", "🌉", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Modem", "/ˈməʊ.dem/", "noun", "networking", "Mạng máy tính",
     "Bộ điều chế & giải chế: thiết bị chuyển đổi tín hiệu số từ máy tính thành tín hiệu tương tự qua đường truyền viễn thông.",
     "The fiber optic modem translates optical light pulses into digital Ethernet packets.", "Modem quang chuyển đổi các xung ánh sáng thành các gói tin Ethernet kỹ thuật số.",
     "Bộ giải điều chế Modem", "📟", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Access Point (AP)", "/ˈæk.ses pɔɪnt/", "noun", "networking", "Mạng máy tính",
     "Điểm truy cập không dây: thiết bị phát sóng Wi-Fi cho phép các thiết bị không dây kết nối vào mạng có dây.",
     "Installing multiple ceiling access points ensures seamless Wi-Fi roaming in offices.", "Lắp đặt nhiều AP trần nhà đảm bảo vùng phủ sóng Wi-Fi liền mạch trong văn phòng.",
     "Điểm truy cập Access Point", "📶", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("NIC (Network Interface Card)", "/ˌen.aɪˈsiː/", "noun", "networking", "Mạng máy tính",
     "Card mạng: thành phần phần cứng máy tính cung cấp cổng kết nối vật lý với cáp mạng hoặc ăng-ten không dây.",
     "Enterprise servers feature dual 10Gbps NICs for high-bandwidth failover.", "Máy chủ doanh nghiệp trang bị hai card mạng 10Gbps để dự phòng thông lượng cao.",
     "Card mạng NIC", "💳", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("MAC Address", "/mæk əˈdres/", "noun", "networking", "Mạng máy tính",
     "Địa chỉ MAC: địa chỉ phần cứng 48-bit duy nhất được nhà sản xuất gán cố định cho từng card mạng.",
     "Routers maintain ARP tables to map IP addresses to physical MAC addresses.", "Bộ định tuyến duy trì bảng ARP để ánh xạ địa chỉ IP sang địa chỉ MAC phần cứng.",
     "Địa chỉ phần cứng MAC", "🏷️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Packet", "/ˈpæk.ɪt/", "noun", "networking", "Mạng máy tính",
     "Gói tin: đơn vị dữ liệu được định tuyến độc lập giữa điểm xuất phát và điểm đích trên mạng IP.",
     "Data streams are segmented into smaller packets before traversing the network.", "Luồng dữ liệu được chia nhỏ thành các gói tin trước khi truyền qua mạng.",
     "Gói tin Packet", "📦", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Frame", "/freɪm/", "noun", "networking", "Mạng máy tính",
     "Khung truyền dữ liệu: đơn vị truyền dữ liệu ở tầng liên kết dữ liệu (Tầng 2) được đóng gói kèm địa chỉ MAC.",
     "Ethernet frames contain preamble, source/destination MAC, payload, and CRC check.", "Khung Ethernet gồm tiền tố, MAC nguồn/đích, tải trọng và mã kiểm tra lỗi CRC.",
     "Khung truyền Frame", "🖼️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Segment", "/ˈseɡ.mənt/", "noun", "networking", "Mạng máy tính",
     "Phân đoạn giao vận: đơn vị dữ liệu ở tầng giao vận (TCP) được đánh số thứ tự và kiểm soát luồng.",
     "TCP segments track sequence numbers to reassemble bytes in the exact original order.", "Các phân đoạn TCP theo dõi số thứ tự để ghép lại các byte theo đúng trật tự ban đầu.",
     "Phân đoạn TCP Segment", "🧩", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Datagram", "/ˈdeɪ.tə.ɡræm/", "noun", "networking", "Mạng máy tính",
     "Bản tin dữ liệu: gói dữ liệu độc lập tự chứa đầy đủ thông tin địa chỉ trong giao thức không kết nối như UDP.",
     "UDP sends datagrams without establishing prior handshakes or delivery guarantees.", "UDP gửi datagram mà không cần thiết lập bắt tay trước hay bảo đảm việc nhận.",
     "Bản tin Datagram", "✉️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Payload", "/ˈpeɪ.ləʊd/", "noun", "networking", "Mạng máy tính",
     "Tải trọng dữ liệu: phần dữ liệu thực tế hữu ích được chuyên chở bên trong gói tin, loại trừ phần tiêu đề.",
     "Inspect the packet payload to analyze the raw JSON transmitted over HTTP.", "Kiểm tra phần tải trọng của gói tin để phân tích JSON thô truyền qua HTTP.",
     "Tải trọng dữ liệu", "📦", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Packet Header", "/ˈpæk.ɪt ˈhed.ər/", "noun", "networking", "Mạng máy tính",
     "Tiêu đề gói tin: phần thông tin chỉ dẫn ở đầu gói chứa địa chỉ nguồn, đích, độ dài và cờ điều khiển.",
     "The IPv4 header typically spans 20 bytes when optional fields are omitted.", "Tiêu đề IPv4 thường dài 20 byte khi không sử dụng các trường tùy chọn.",
     "Tiêu đề gói tin", "📋", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("MTU (Maximum Transmission Unit)", "/ˌem.tiːˈjuː/", "noun", "networking", "Mạng máy tính",
     "Đơn vị truyền tối đa: kích thước gói tin lớn nhất tính bằng byte mà một giao diện mạng có thể gửi mà không bị phân mảnh.",
     "Standard Ethernet interfaces configure a default MTU size of 1500 bytes.", "Giao diện Ethernet tiêu chuẩn định cấu hình kích thước MTU mặc định là 1500 byte.",
     "Đơn vị truyền tối đa MTU", "📏", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Bandwidth", "/ˈbænd.wɪtθ/", "noun", "networking", "Mạng máy tính",
     "Băng thông: dung lượng truyền tải dữ liệu tối đa lý thuyết qua đường truyền mạng trong một giây (bps, Mbps, Gbps).",
     "Upgrading to fiber broadband increased company bandwidth to 1 Gigabit per second.", "Nâng cấp lên mạng cáp quang đã tăng băng thông của công ty lên 1 Gigabit mỗi giây.",
     "Băng thông truyền dẫn", "🌊", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Latency", "/ˈleɪ.tən.si/", "noun", "networking", "Mạng máy tính",
     "Độ trễ mạng: khoảng thời gian cần thiết để một gói tin đi từ nguồn đến đích (thường tính bằng mili-giây ms).",
     "Low latency is crucial for smooth online gaming and financial trading.", "Độ trễ thấp là yếu tố sống còn cho trò chơi trực tuyến mượt mà và giao dịch tài chính.",
     "Độ trễ mạng Latency", "⏱️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Throughput", "/ˈθruː.pʊt/", "noun", "networking", "Mạng máy tính",
     "Thông lượng thực tế: lượng dữ liệu hữu ích thực sự được truyền tải thành công qua mạng trong một đơn vị thời gian.",
     "Packet loss and network congestion cause throughput to fall below bandwidth limits.", "Mất gói và nghẽn mạng khiến thông lượng thực tế giảm xuống dưới giới hạn băng thông.",
     "Thông lượng thực tế", "📈", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Jitter", "/ˈdʒɪt.ər/", "noun", "networking", "Mạng máy tính",
     "Biến thiên độ trễ: sự dao động không ổn định về thời gian truyền giữa các gói tin liên tiếp nhau.",
     "High jitter causes robotic audio stuttering during VoIP video conference calls.", "Biến thiên độ trễ cao khiến âm thanh bị giật tiếng robot trong các cuộc gọi video VoIP.",
     "Biến thiên độ trễ Jitter", "〰️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Packet Loss", "/ˈpæk.ɪt lɒs/", "noun", "networking", "Mạng máy tính",
     "Mất gói tin: hiện tượng các gói dữ liệu bị thất lạc hoặc rơi rớt trên đường truyền không tới được đích.",
     "Even 2 percent packet loss degrades streaming video quality substantially.", "Chỉ 2% tỷ lệ mất gói tin cũng làm giảm đáng kể chất lượng xem video trực tuyến.",
     "Mất gói tin Packet Loss", "❌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("TCP (Transmission Control Protocol)", "/ˌtiː.siːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức TCP: giao thức hướng kết nối đảm bảo truyền tải dữ liệu tin cậy, không mất gói và đúng thứ tự.",
     "TCP automatically retransmits dropped segments until acknowledgment arrives.", "TCP tự động truyền lại các phân đoạn bị mất cho đến khi nhận được xác nhận.",
     "Giao thức tin cậy TCP", "🤝", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("UDP (User Datagram Protocol)", "/ˌjuː.diːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức UDP: giao thức không kết nối ưu tiên tốc độ tối đa và độ trễ thấp, chấp nhận có thể mất gói.",
     "Voice calls and multiplayer games prioritize UDP for low-latency transmission.", "Cuộc gọi thoại và trò chơi nhiều người chơi ưu tiên UDP vì độ trễ cực thấp.",
     "Giao thức tốc độ UDP", "⚡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Three-Way Handshake", "/θriː weɪ ˈhænd.ʃeɪk/", "noun", "networking", "Mạng máy tính",
     "Bắt tay ba bước: quy trình gồm SYN, SYN-ACK, ACK thiết lập kết nối tin cậy giữa client và máy chủ trong TCP.",
     "TCP establishes every secure connection via a three-way handshake.", "TCP thiết lập mọi kết nối tin cậy thông qua quy trình bắt tay ba bước.",
     "Bắt tay ba bước TCP", "🤝", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("SYN Packet", "/sɪn ˈpæk.ɪt/", "noun", "networking", "Mạng máy tính",
     "Gói tin đồng bộ: gói tin đầu tiên do máy trạm gửi đi để yêu cầu đồng bộ hóa số thứ tự phiên TCP.",
     "A SYN flood attack overwhelms server connection queues with fake connection requests.", "Tấn công SYN flood làm tê liệt hàng đợi kết nối của máy chủ bằng các yêu cầu giả mạo.",
     "Gói tin SYN", "🟢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("ACK Packet", "/æk ˈpæk.ɪt/", "noun", "networking", "Mạng máy tính",
     "Gói tin xác nhận: gói tin gửi lại để báo hiệu đã nhận thành công dữ liệu từ phía đối diện.",
     "Upon receiving the segment, the client responds immediately with an ACK packet.", "Khi nhận được phân đoạn, máy trạm phản hồi ngay lập tức bằng gói tin xác nhận ACK.",
     "Gói tin xác nhận ACK", "✅", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("FIN Packet", "/fɪn ˈpæk.ɪt/", "noun", "networking", "Mạng máy tính",
     "Gói tin kết thúc: gói tin gửi đi để yêu cầu đóng và giải phóng kết nối TCP đã hoàn tất công việc.",
     "Sending a FIN packet gracefully initiates teardown of the active connection.", "Việc gửi gói tin FIN khởi tạo quy trình đóng kết nối đang hoạt động một cách lịch sự.",
     "Gói tin kết thúc FIN", "🏁", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Port", "/pɔːt/", "noun", "networking", "Mạng máy tính",
     "Cổng mạng: điểm cuối logic 16-bit xác định dịch vụ hoặc tiến trình cụ thể chạy trên máy tính.",
     "Standard web servers bind port 80 for HTTP and port 443 for HTTPS.", "Máy chủ web tiêu chuẩn liên kết cổng 80 cho HTTP và cổng 443 cho HTTPS.",
     "Cổng mạng Port", "🚪", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Port Number", "/pɔːt ˈnʌm.bər/", "noun", "networking", "Mạng máy tính",
     "Số hiệu cổng: số từ 0 đến 65535 dùng kết hợp với địa chỉ IP để định tuyến dữ liệu tới đúng ứng dụng.",
     "Port numbers below 1024 are reserved well-known system ports.", "Các số hiệu cổng dưới 1024 là các cổng hệ thống nổi tiếng được bảo lưu.",
     "Số hiệu cổng", "🔢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Port Forwarding", "/pɔːt ˈfɔː.wəd.ɪŋ/", "noun", "networking", "Mạng máy tính",
     "Chuyển tiếp cổng: cấu hình router chuyển tiếp lưu lượng đến từ Internet vào một cổng của máy chủ nội bộ.",
     "Configure port forwarding on the router to expose a local game server to the web.", "Cấu hình chuyển tiếp cổng trên router để mở máy chủ game nội bộ ra ngoài mạng Internet.",
     "Chuyển tiếp cổng", "⏩", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Socket", "/ˈsɒk.ɪt/", "noun", "networking", "Mạng máy tính",
     "Điểm cuối kết nối mạng (Socket): kết hợp giữa địa chỉ IP và số cổng để truyền thông dữ liệu hai chiều.",
     "Network applications open stream sockets to establish real-time TCP connections.", "Ứng dụng mạng mở socket luồng để thiết lập kết nối TCP thời gian thực.",
     "Điểm cuối Socket", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("DNS (Domain Name System)", "/ˌdiː.enˈes/", "noun", "networking", "Mạng máy tính",
     "Hệ thống tên miền: danh bạ Internet phân giải tên miền dạng chữ thân thiện thành địa chỉ IP số học.",
     "DNS translates google.com into an IP address that network routers understand.", "DNS dịch google.com thành địa chỉ IP mà các router mạng có thể hiểu được.",
     "Hệ thống tên miền DNS", "🌐", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("DNS Server", "/ˌdiː.enˈes ˈsɜː.vər/", "noun", "networking", "Mạng máy tính",
     "Máy chủ DNS: máy chủ chứa cơ sở dữ liệu các tên miền và địa chỉ IP công cộng tương ứng.",
     "Google provides public DNS servers reachable at 8.8.8.8 and 8.8.4.4.", "Google cung cấp các máy chủ DNS công cộng truy cập được tại 8.8.8.8 và 8.8.4.4.",
     "Máy chủ DNS", "🖥️", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("Domain Name", "/dəʊˈmeɪn neɪm/", "noun", "networking", "Mạng máy tính",
     "Tên miền: chuỗi định danh thân thiện với con người đại diện cho một trang web hoặc dịch vụ mạng.",
     "Renewing your domain name prevents malicious hijackers from taking it over.", "Gia hạn tên miền giúp ngăn chặn kẻ xấu chiếm đoạt thương hiệu của bạn.",
     "Tên miền Domain", "🏷️", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("Top-Level Domain (TLD)", "/tɒp ˈlev.əl dəʊˈmeɪn/", "noun", "networking", "Mạng máy tính",
     "Tên miền cấp cao nhất: phần đuôi cuối cùng của tên miền như .com, .org, .net, .edu hoặc .vn.",
     "The .io top-level domain has become universally popular among tech startups.", "Tên miền cấp cao nhất .io đã trở nên cực kỳ phổ biến trong giới khởi nghiệp công nghệ.",
     "Tên miền cấp cao TLD", "🌐", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("DNS Propagation", "/ˌdiː.enˈes ˌprɒp.əˈɡeɪ.ʃən/", "noun", "networking", "Mạng máy tính",
     "Lan truyền DNS: khoảng thời gian cần thiết để các thay đổi bản ghi DNS cập nhật trên toàn bộ máy chủ Internet.",
     "DNS propagation can take between a few minutes and 48 hours to complete fully.", "Sự lan truyền DNS có thể mất từ vài phút tới 48 giờ để hoàn tất trên toàn cầu.",
     "Lan truyền bản ghi DNS", "⏳", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("A Record", "/eɪ ˈrek.ɔːd/", "noun", "networking", "Mạng máy tính",
     "Bản ghi A: bản ghi DNS cơ bản nhất ánh xạ trực tiếp một tên miền tới địa chỉ IPv4 32-bit.",
     "Point the A record to the elastic IP address of the production server.", "Trỏ bản ghi A tới địa chỉ IP tĩnh của máy chủ môi trường sản xuất.",
     "Bản ghi A Record", "📍", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("CNAME Record", "/ˈsiː.neɪm ˈrek.ɔːd/", "noun", "networking", "Mạng máy tính",
     "Bản ghi CNAME: bản ghi bí danh trỏ một tên miền hoặc tên miền phụ tới một tên miền chuẩn tắc khác.",
     "Use a CNAME record to alias www.example.com directly to example.com.", "Dùng bản ghi CNAME để làm bí danh cho www.example.com trỏ trực tiếp về example.com.",
     "Bản ghi CNAME", "🔗", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("MX Record", "/ˌemˈeks ˈrek.ɔːd/", "noun", "networking", "Mạng máy tính",
     "Bản ghi MX: bản ghi DNS chỉ định máy chủ thư điện tử chịu trách nhiệm nhận email cho tên miền.",
     "Configure Google Workspace MX records to handle your enterprise business email.", "Cấu hình bản ghi MX của Google Workspace để xử lý email doanh nghiệp của bạn.",
     "Bản ghi email MX", "✉️", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("TXT Record", "/tiː.eksˈtiː ˈrek.ɔːd/", "noun", "networking", "Mạng máy tính",
     "Bản ghi TXT: bản ghi DNS chứa văn bản tự do thường dùng cho SPF, DKIM và xác minh quyền sở hữu tên miền.",
     "Add a TXT record to prove domain ownership during SSL certificate issuance.", "Thêm bản ghi TXT để chứng minh quyền sở hữu tên miền khi phát hành chứng chỉ SSL.",
     "Bản ghi văn bản TXT", "📄", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("HTTP (HyperText Transfer Protocol)", "/ˌeɪtʃ.tiː.tiːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức truyền siêu văn bản: giao thức tầng ứng dụng nền tảng cho việc truyền tải trang web qua mạng.",
     "HTTP operates as a stateless request-response protocol over TCP.", "HTTP hoạt động như một giao thức không lưu trạng thái kiểu yêu cầu - phản hồi trên nền TCP.",
     "Giao thức web HTTP", "🌐", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("HTTPS", "/ˌeɪtʃ.tiː.tiːˈpiː ˈes/", "noun", "networking", "Mạng máy tính",
     "Giao thức HTTP an toàn: HTTP được mã hóa qua lớp bảo mật SSL/TLS để bảo vệ dữ liệu chống nghe trộm.",
     "Modern browsers mark sites as insecure if they fail to provide HTTPS encryption.", "Các trình duyệt hiện đại gắn cờ không an toàn nếu website không có mã hóa HTTPS.",
     "Giao thức an toàn HTTPS", "🔒", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("HTTP/2", "/ˌeɪtʃ.tiː.tiːˈpiː tuː/", "noun", "networking", "Mạng máy tính",
     "Giao thức HTTP/2: phiên bản cải tiến hỗ trợ dồn kênh đa luồng (multiplexing) trên một kết nối TCP duy nhất.",
     "HTTP/2 multiplexing removes head-of-line blocking on web asset loading.", "Tính năng dồn kênh đa luồng của HTTP/2 loại bỏ tình trạng tắc nghẽn nạp tài nguyên web.",
     "Giao thức HTTP/2", "⚡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("HTTP/3", "/ˌeɪtʃ.tiː.tiːˈpiː θriː/", "noun", "networking", "Mạng máy tính",
     "Giao thức HTTP/3: phiên bản HTTP mới nhất chạy trên nền giao thức UDP thông qua QUIC để giảm độ trễ tối đa.",
     "HTTP/3 accelerates connection establishment on mobile devices switching networks.", "HTTP/3 tăng tốc thiết lập kết nối trên thiết bị di động khi chuyển đổi mạng.",
     "Giao thức HTTP/3 QUIC", "🚀", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("QUIC Protocol", "/kwɪk ˈprəʊ.tə.kɒl/", "noun", "networking", "Mạng máy tính",
     "Giao thức QUIC: giao thức truyền tải tầng giao vận hiện đại dựa trên UDP, tích hợp sẵn mã hóa TLS 1.3.",
     "QUIC eliminates head-of-line blocking by handling stream multiplexing natively.", "QUIC loại bỏ tắc nghẽn đầu hàng bằng cách xử lý dồn kênh luồng tự nhiên.",
     "Giao thức nhanh QUIC", "⚡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("WebSocket", "/ˈwebˌsɒk.ɪt/", "noun", "networking", "Mạng máy tính",
     "Giao thức WebSocket: giao thức truyền thông hai chiều song công toàn phần thời gian thực qua một kết nối TCP.",
     "Financial stock tickers use WebSockets for continuous, sub-second price streaming.", "Bảng giá cổ phiếu tài chính dùng WebSocket để truyền trực tiếp giá theo thời gian thực.",
     "Giao thức WebSocket", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("WebRTC", "/ˌweb.ɑːr.tiːˈsiː/", "noun", "networking", "Mạng máy tính",
     "Công nghệ giao tiếp thời gian thực cho web: cho phép truyền âm thanh, video và dữ liệu ngang hàng P2P không cần plugin.",
     "Video conferencing web apps run audio and video through WebRTC connections.", "Các ứng dụng hội nghị truyền hình web chạy âm thanh và hình ảnh qua WebRTC.",
     "Giao tiếp P2P WebRTC", "📹", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("FTP (File Transfer Protocol)", "/ˌef.tiːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức truyền tệp: giao thức tiêu chuẩn dùng để trao đổi tệp giữa máy khách và máy chủ qua mạng.",
     "Legacy FTP sends credentials in cleartext, making it vulnerable on modern networks.", "FTP cũ gửi mật khẩu dưới dạng văn bản thuần, khiến nó dễ bị tấn công trên mạng hiện đại.",
     "Giao thức truyền tệp FTP", "📁", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("SFTP", "/ˌes.ef.tiːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức truyền tệp an toàn: truyền tải và quản trị tệp an toàn thông qua đường hầm mã hóa SSH.",
     "Automated deployment scripts use SFTP to transfer build archives securely.", "Kịch bản triển khai tự động dùng SFTP để truyền tệp nén bản dựng an toàn.",
     "Giao thức SFTP an toàn", "🛡️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("SSH (Secure Shell)", "/ˌes.esˈeɪtʃ/", "noun", "networking", "Mạng máy tính",
     "Giao thức dòng lệnh an toàn: cho phép quản trị viên đăng nhập và điều khiển máy chủ Linux từ xa qua kênh mã hóa.",
     "Log into remote cloud instances using SSH keys rather than vulnerable passwords.", "Đăng nhập vào máy chủ đám mây từ xa bằng khóa SSH thay vì mật khẩu dễ bị lộ.",
     "Giao thức dòng lệnh SSH", "🔐", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Telnet", "/ˈtel.net/", "noun", "networking", "Mạng máy tính",
     "Giao thức Telnet: giao thức dòng lệnh cổ điển không mã hóa, hiện chỉ còn dùng để kiểm tra cổng mở mạng.",
     "Engineers use 'telnet host 80' to check if a remote port is open.", "Kỹ sư dùng lệnh 'telnet host 80' để kiểm tra xem một cổng từ xa có mở hay không.",
     "Giao thức kiểm tra Telnet", "📟", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("SMTP", "/ˌes.em.tiːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức truyền thư đơn giản: giao thức tiêu chuẩn dùng để gửi email đi từ máy khách lên máy chủ hoặc giữa các máy chủ.",
     "Web applications connect to SendGrid via SMTP on port 587.", "Ứng dụng web kết nối tới SendGrid thông qua giao thức SMTP trên cổng 587.",
     "Giao thức gửi mail SMTP", "✉️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("POP3", "/ˌpiː.oʊˈpiː θriː/", "noun", "networking", "Mạng máy tính",
     "Giao thức POP3: tải toàn bộ thư từ máy chủ về máy cục bộ và thường xóa bản sao trên máy chủ.",
     "POP3 is suited for single-device email checking without cloud synchronization.", "POP3 thích hợp cho việc kiểm tra email trên một thiết bị đơn lẻ không cần đồng bộ đám mây.",
     "Giao thức tải mail POP3", "📬", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("IMAP", "/ˈaɪ.mæp/", "noun", "networking", "Mạng máy tính",
     "Giao thức IMAP: đồng bộ hóa thư điện tử hai chiều giữa máy khách và máy chủ, giữ nguyên hộp thư trên đám mây.",
     "IMAP keeps email read status synchronized across phones, tablets, and laptops.", "IMAP giữ trạng thái đã đọc của email được đồng bộ trên điện thoại, máy tính bảng và laptop.",
     "Giao thức đồng bộ mail IMAP", "🔄", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("DHCP (Dynamic Host Configuration Protocol)", "/ˌdiː.eɪtʃ.siːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức cấp phát IP động: tự động phân phối địa chỉ IP, subnet mask và DNS cho các thiết bị khi vào mạng.",
     "The router's DHCP server assigns available IP leases to connecting phones.", "Máy chủ DHCP của router cấp phát các gói thuê địa chỉ IP cho điện thoại khi kết nối.",
     "Cấp phát IP động DHCP", "⚙️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("ARP (Address Resolution Protocol)", "/ɑːp/", "noun", "networking", "Mạng máy tính",
     "Giao thức phân giải địa chỉ: chuyển đổi địa chỉ IP tầng 3 thành địa chỉ MAC tầng 2 trong mạng cục bộ.",
     "ARP broadcast queries ask 'who owns IP 192.168.1.1' to find the physical MAC.", "Bản tin quảng bá ARP hỏi 'ai sở hữu IP 192.168.1.1' để tìm địa chỉ MAC vật lý.",
     "Phân giải địa chỉ ARP", "🔍", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("ICMP (Internet Control Message Protocol)", "/ˌaɪ.siː.emˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức thông điệp điều khiển: dùng cho các thiết bị mạng gửi thông báo lỗi và kiểm tra trạng thái kết nối.",
     "Routers return ICMP destination unreachable packets when target hosts are down.", "Bộ định tuyến trả về gói ICMP không thể tiếp cận khi máy chủ đích bị sập.",
     "Thông điệp điều khiển ICMP", "📢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Ping", "/pɪŋ/", "noun", "networking", "Mạng máy tính",
     "Lệnh Ping: công cụ kiểm tra khả năng tiếp cận của một máy chủ và đo thời gian khứ hồi (RTT) qua ICMP.",
     "Run 'ping 8.8.8.8' to verify whether your computer can reach the internet.", "Chạy lệnh 'ping 8.8.8.8' để xác minh xem máy tính của bạn có ra được Internet hay không.",
     "Kiểm tra kết nối Ping", "📶", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Traceroute", "/ˈtreɪs.ruːt/", "noun", "networking", "Mạng máy tính",
     "Lệnh lần vết đường đi: hiển thị danh sách tất cả các chặng router trung gian mà gói tin đi qua để tới đích.",
     "Traceroute pinpoints the exact intermediate router where packet drops occur.", "Traceroute chỉ ra chính xác bộ định tuyến trung gian nơi xảy ra hiện tượng mất gói tin.",
     "Lần vết đường đi Traceroute", "🗺️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("NAT (Network Address Translation)", "/næt/", "noun", "networking", "Mạng máy tính",
     "Biên dịch địa chỉ mạng: kỹ thuật ánh xạ dải địa chỉ IP riêng nội bộ sang một địa chỉ IP công cộng ra Internet.",
     "NAT allows hundreds of office computers to share a single public IPv4 address.", "NAT cho phép hàng trăm máy tính văn phòng chia sẻ một địa chỉ IPv4 công cộng duy nhất.",
     "Biên dịch địa chỉ NAT", "🔄", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Reverse Proxy", "/rɪˈvɜːs ˈprɒk.si/", "noun", "networking", "Mạng máy tính",
     "Máy chủ ủy nhiệm ngược: đứng trước các máy chủ web nội bộ để điều hướng yêu cầu, cân bằng tải và chấm dứt SSL.",
     "Nginx acts as a high-performance reverse proxy for backend microservices.", "Nginx đóng vai trò như một reverse proxy hiệu năng cao cho các vi dịch vụ phía sau.",
     "Ủy nhiệm ngược Reverse Proxy", "🛡️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Forward Proxy", "/ˈfɔː.wəd ˈprɒk.si/", "noun", "networking", "Mạng máy tính",
     "Máy chủ ủy nhiệm xuôi: đứng giữa các máy trạm nội bộ và mạng Internet để kiểm duyệt và ghi nhật ký truy cập web.",
     "Corporate forward proxies filter employee web browsing and enforce policies.", "Forward proxy của công ty lọc duyệt web của nhân viên và thực thi các chính sách.",
     "Ủy nhiệm xuôi Forward Proxy", "🏢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Load Balancer", "/ləʊd ˈbæl.ən.sər/", "noun", "networking", "Mạng máy tính",
     "Bộ cân bằng tải: thiết bị hoặc phần mềm phân phối lưu lượng truy cập đồng đều qua một nhóm máy chủ phía sau.",
     "The load balancer routes traffic away from unhealthy server instances.", "Bộ cân bằng tải điều hướng lưu lượng tránh xa các máy chủ đang gặp sự cố.",
     "Bộ cân bằng tải Load Balancer", "⚖️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Round Robin Load Balancing", "/raʊnd ˈrɒb.ɪn/", "noun", "networking", "Mạng máy tính",
     "Cân bằng tải luân phiên: thuật toán phân phối lần lượt từng yêu cầu mới tới từng máy chủ theo vòng tròn.",
     "Round Robin distributes requests sequentially across available web worker pods.", "Round Robin phân phối các yêu cầu tuần tự qua các pod máy chủ web khả dụng.",
     "Cân bằng tải luân phiên", "🔄", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Keep-Alive Connection", "/kiːp əˈlaɪv/", "noun", "networking", "Mạng máy tính",
     "Kết nối duy trì: kỹ thuật giữ mở kết nối TCP để tái sử dụng gửi nhiều yêu cầu HTTP mà không cần bắt tay lại.",
     "HTTP Keep-Alive reduces network latency by reusing the same TCP connection.", "HTTP Keep-Alive giảm độ trễ mạng bằng cách tái sử dụng cùng một kết nối TCP.",
     "Kết nối duy trì Keep-Alive", "⚡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("SSL/TLS", "/ˌes.esˈel ˌtiː.elˈes/", "noun", "networking", "Mạng máy tính",
     "Giao thức bảo mật tầng truyền tải: mã hóa liên lạc qua mạng máy tính để bảo đảm tính bí mật và toàn vẹn dữ liệu.",
     "TLS 1.3 optimizes the handshake to establish encrypted channels in one roundtrip.", "TLS 1.3 tối ưu hóa quá trình bắt tay để thiết lập kênh mã hóa chỉ trong một vòng truyền.",
     "Bảo mật SSL/TLS", "🔒", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("TLS Handshake", "/ˌtiː.elˈes ˈhænd.ʃeɪk/", "noun", "networking", "Mạng máy tính",
     "Bắt tay TLS: chuỗi trao đổi giữa client và server để xác thực chứng chỉ số và thương lượng khóa phiên mã hóa.",
     "The client and server negotiate cipher suites during the initial TLS handshake.", "Client và server thương lượng bộ thuật toán mật mã trong quá trình bắt tay TLS ban đầu.",
     "Bắt tay bảo mật TLS", "🤝", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cipher Suite", "/ˈsaɪ.fər swiːt/", "noun", "networking", "Mạng máy tính",
     "Bộ mật mã: tập hợp các thuật toán dùng để xác thực, trao đổi khóa và mã hóa khối dữ liệu.",
     "Modern security standards disable weak cipher suites like RC4 and DES.", "Các tiêu chuẩn bảo mật hiện đại vô hiệu hóa các bộ mật mã yếu như RC4 và DES.",
     "Bộ thuật toán mật mã", "🗝️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Certificate Authority (CA)", "/səˈtɪf.ɪ.kət ɔːˌθɒr.ə.ti/", "noun", "networking", "Mạng máy tính",
     "Tổ chức cấp phát chứng chỉ: đơn vị tin cậy được ủy quyền ký và phát hành các chứng chỉ số SSL/TLS.",
     "Let's Encrypt provides free automated TLS certificates as a recognized CA.", "Let's Encrypt cung cấp chứng chỉ TLS tự động miễn phí với tư cách là một cơ quan CA uy tín.",
     "Tổ chức cấp chứng chỉ CA", "🏛️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Content Delivery Network (CDN)", "/ˌsiː.diːˈen/", "noun", "networking", "Mạng máy tính",
     "Mạng phân phối nội dung: hệ thống các máy chủ đặt khắp toàn cầu để lưu đệm và phục vụ nội dung gần người dùng nhất.",
     "Cloudflare CDN caches static assets globally to minimize server load.", "Cloudflare CDN lưu đệm các tài nguyên tĩnh trên toàn cầu để giảm tải cho máy chủ.",
     "Mạng phân phối CDN", "🌍", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("Anycast Routing", "/ˈen.i.kɑːst ˈruː.tɪŋ/", "noun", "networking", "Mạng máy tính",
     "Định tuyến Anycast: kỹ thuật cho phép gán cùng một địa chỉ IP cho nhiều máy chủ ở các vị trí địa lý khác nhau.",
     "DNS root servers and modern CDNs utilize Anycast to route clients to the nearest node.", "Các máy chủ gốc DNS và CDN hiện đại dùng Anycast để dẫn client tới nút gần nhất.",
     "Định tuyến Anycast", "🌐", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("BGP (Border Gateway Protocol)", "/ˌbiː.dʒiːˈpiː/", "noun", "networking", "Mạng máy tính",
     "Giao thức cổng biên BGP: giao thức định tuyến cốt lõi của Internet điều phối lưu lượng giữa các hệ thống tự trị (AS).",
     "BGP route misconfigurations can accidentally take major internet platforms offline.", "Cấu hình sai tuyến đường BGP có thể vô tình làm sập các nền tảng Internet lớn.",
     "Giao thức định tuyến BGP", "🗺️", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("OSPF (Open Shortest Path First)", "/ˌoʊ.es.piːˈef/", "noun", "networking", "Mạng máy tính",
     "Giao thức OSPF: giao thức định tuyến nội bộ dùng thuật toán Dijkstra để tìm đường đi ngắn nhất trong cùng một mạng doanh nghiệp.",
     "Large enterprise intranets employ OSPF for rapid dynamic routing convergence.", "Mạng nội bộ doanh nghiệp lớn dùng OSPF để hội tụ định tuyến động nhanh chóng.",
     "Định tuyến nội bộ OSPF", "🌲", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Firewall", "/ˈfaɪə.wɔːl/", "noun", "networking", "Mạng máy tính",
     "Tường lửa: hệ thống giám sát và lọc lưu lượng mạng vào ra dựa trên các quy tắc bảo mật xác định trước.",
     "The network firewall blocks incoming traffic on non-standard ports by default.", "Tường lửa mạng chặn lưu lượng đến trên các cổng không chuẩn theo mặc định.",
     "Tường lửa mạng Firewall", "🔥", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("DMZ (Demilitarized Zone)", "/ˌdiː.emˈzed/", "noun", "networking", "Mạng máy tính",
     "Vùng phi quân sự: phân đoạn mạng vật lý hoặc logic chứa các dịch vụ công khai tiếp xúc với Internet bên ngoài.",
     "Web servers and mail gateways reside in the DMZ to protect internal databases.", "Máy chủ web và cổng mail nằm trong vùng DMZ để bảo vệ CSDL nội bộ.",
     "Vùng an ninh DMZ", "🛡️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Intrusion Detection System (IDS)", "/ɪnˈtruː.ʒən dɪˌtek.ʃən/", "noun", "networking", "Mạng máy tính",
     "Hệ thống phát hiện xâm nhập: giám sát lưu lượng mạng để phát hiện các hoạt động đáng ngờ và cảnh báo cho quản trị viên.",
     "The network IDS flagged abnormal scanning traffic originating from an external IP.", "Hệ thống IDS mạng đã gắn cờ lưu lượng quét bất thường bắt nguồn từ một IP bên ngoài.",
     "Hệ thống phát hiện xâm nhập IDS", "🚨", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Packet Sniffing", "/ˈpæk.ɪt ˈsnɪf.ɪŋ/", "noun", "networking", "Mạng máy tính",
     "Bắt gói tin: hành động thu thập và kiểm tra dữ liệu truyền qua mạng máy tính để phân tích lỗi hoặc nghe lén.",
     "Unencrypted credentials can be extracted in plaintext through packet sniffing.", "Mật khẩu không mã hóa có thể bị trích xuất dạng văn bản thuần qua việc bắt gói tin.",
     "Bắt gói tin Sniffing", "🕵️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Wireshark", "/ˈwaɪə.ʃɑːk/", "noun", "networking", "Mạng máy tính",
     "Phần mềm Wireshark: công cụ phân tích giao thức mạng mã nguồn mở hàng đầu thế giới dùng chụp và mổ xẻ gói tin.",
     "Engineers open Wireshark to inspect TCP retransmission flags during network outages.", "Các kỹ sư mở Wireshark để kiểm tra cờ truyền lại TCP trong lúc mạng bị sự cố.",
     "Phân tích mạng Wireshark", "🦈", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Webhook", "/ˈweb.hʊk/", "noun", "networking", "Mạng máy tính",
     "Cơ chế Webhook: thông báo HTTP POST tự động được gửi từ hệ thống này sang hệ thống khác khi xảy ra một sự kiện.",
     "Stripe triggers a webhook to our server immediately when a subscription is paid.", "Stripe kích hoạt một webhook tới máy chủ của chúng tôi ngay khi thuê bao được trả tiền.",
     "Cơ chế Webhook", "🪝", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 4 terms count: {len(terms)}")
