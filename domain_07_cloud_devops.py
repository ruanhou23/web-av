# -*- coding: utf-8 -*-
"""Domain 7: Cloud Computing & DevOps (100 core terms)"""

terms = [
    ("Cloud Computing", "/klaʊd kəmˈpjuː.tɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Điện toán đám mây: việc cung cấp theo yêu cầu các tài nguyên máy tính (máy chủ, lưu trữ, mạng) qua Internet theo mô hình trả tiền theo mức dùng.",
     "Migrating on-premise servers to cloud computing reduces physical data center costs.", "Di chuyển máy chủ tại chỗ lên điện toán đám mây giảm chi phí phòng máy chủ vật lý.",
     "Điện toán đám mây", "☁️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Infrastructure as a Service (IaaS)", "/ˌaɪ.æz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hạ tầng như một dịch vụ: mô hình cung cấp hạ tầng phần cứng ảo hóa cơ bản như máy ảo, mạng và lưu trữ.",
     "AWS EC2 and Google Compute Engine are classic examples of IaaS solutions.", "AWS EC2 và Google Compute Engine là những ví dụ kinh điển về giải pháp hạ tầng IaaS.",
     "Hạ tầng dịch vụ IaaS", "🏗️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Platform as a Service (PaaS)", "/pæz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng như một dịch vụ: môi trường hoàn chỉnh trên mây giúp phát triển, chạy và quản lý ứng dụng mà không cần lo hạ tầng.",
     "Heroku and AWS Elastic Beanstalk provide PaaS environments for rapid code deployment.", "Heroku và AWS Elastic Beanstalk cung cấp môi trường PaaS để triển khai mã nhanh chóng.",
     "Nền tảng dịch vụ PaaS", "📦", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Software as a Service (SaaS)", "/sæz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Phần mềm như một dịch vụ: mô hình phân phối ứng dụng phần mềm hoàn chỉnh chạy trên đám mây qua trình duyệt web.",
     "Google Workspace, Slack, and Salesforce are world-renowned SaaS applications.", "Google Workspace, Slack và Salesforce là những ứng dụng phần mềm dịch vụ SaaS nổi tiếng thế giới.",
     "Phần mềm dịch vụ SaaS", "💻", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Function as a Service (FaaS)", "/fæz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hàm như một dịch vụ: cho phép lập trình viên chạy từng hàm mã nguồn riêng lẻ khi có sự kiện mà không cần quản lý máy chủ.",
     "FaaS allows event-driven code execution with automatic per-millisecond billing.", "FaaS cho phép thực thi mã theo sự kiện với chi phí tính tự động theo từng mili-giây.",
     "Hàm dịch vụ FaaS", "⚡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Serverless Architecture", "/ˈsɜː.və.ləs ˌɑː.kɪ.tek.tʃər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Kiến trúc không máy chủ: mô hình phát triển phần mềm mà nhà cung cấp đám mây tự động cấp phát và mở rộng máy chủ.",
     "Serverless architectures eliminate server patching and scale down to zero when idle.", "Kiến trúc không máy chủ loại bỏ việc vá lỗi máy chủ và tự giảm về 0 khi rảnh rỗi.",
     "Kiến trúc không máy chủ", "🚀", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Public Cloud", "/ˈpʌb.lɪk klaʊd/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Đám mây công cộng: dịch vụ đám mây thuộc sở hữu của nhà cung cấp bên thứ ba và chia sẻ tài nguyên cho nhiều tổ chức.",
     "Startups leverage public cloud infrastructure to avoid upfront capital hardware expenditures.", "Các startup tận dụng đám mây công cộng để tránh chi phí đầu tư phần cứng ban đầu.",
     "Đám mây công cộng", "🌐", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Private Cloud", "/ˈpraɪ.vət klaʊd/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Đám mây riêng: hạ tầng đám mây được dành riêng độc quyền cho một tổ chức duy nhất, đặt tại trung tâm dữ liệu nội bộ.",
     "Government agencies operate private clouds to comply with strict sovereign data laws.", "Các cơ quan chính phủ vận hành đám mây riêng để tuân thủ luật dữ liệu nghiêm ngặt.",
     "Đám mây riêng biệt", "🔒", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Hybrid Cloud", "/ˈhaɪ.brɪd klaʊd/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Đám mây lai: kết hợp giữa đám mây riêng nội bộ và đám mây công cộng, cho phép dữ liệu và ứng dụng chia sẻ qua lại.",
     "Hybrid cloud allows banking systems to keep core ledgers on-premise while bursting to AWS.", "Đám mây lai cho phép hệ thống ngân hàng giữ sổ cái tại chỗ trong khi mở rộng sang AWS.",
     "Đám mây lai Hybrid", "🔄", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Cloud", "/ˌmʌl.tiˈklaʊd/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Đa đám mây: chiến lược sử dụng đồng thời dịch vụ của từ hai nhà cung cấp đám mây trở lên (AWS, GCP, Azure) để tránh phụ thuộc.",
     "A multi-cloud strategy mitigates vendor lock-in and increases global resiliency.", "Chiến lược đa đám mây giảm sự lệ thuộc vào nhà cung cấp và tăng độ chịu lỗi toàn cầu.",
     "Chiến lược Đa đám mây", "🌥️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("AWS (Amazon Web Services)", "/ˌeɪ.dʌb.əl.juːˈes/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng đám mây AWS: nền tảng điện toán đám mây toàn diện và thị phần lớn nhất thế giới của Amazon.",
     "AWS offers hundreds of managed services spanning compute, storage, databases, and AI.", "AWS cung cấp hàng trăm dịch vụ được quản lý từ máy chủ, lưu trữ, CSDL tới AI.",
     "Nền tảng đám mây AWS", "🟧", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Microsoft Azure", "/ˈæʒ.ər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng đám mây Azure: dịch vụ điện toán đám mây của Microsoft được các doanh nghiệp lớn tin dùng.",
     "Enterprises with Active Directory deeply integrate their systems into Microsoft Azure.", "Các doanh nghiệp có Active Directory tích hợp sâu hệ thống vào Microsoft Azure.",
     "Nền tảng đám mây Azure", "🟦", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Google Cloud Platform (GCP)", "/ˌdʒiː.siːˈpiː/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng đám mây GCP: bộ dịch vụ đám mây của Google nổi tiếng về dữ liệu lớn Big Data, AI và Kubernetes.",
     "GCP BigQuery provides serverless SQL analytics over petabyte-scale datasets.", "GCP BigQuery cung cấp phân tích SQL không máy chủ trên các tập dữ liệu quy mô petabyte.",
     "Nền tảng đám mây GCP", "🟥", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Virtual Private Cloud (VPC)", "/ˌviː.piːˈsiː/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Mạng đám mây riêng ảo: phân vùng mạng ảo cô lập riêng biệt của bạn bên trong một hạ tầng đám mây công cộng.",
     "Secure database instances reside inside a private VPC subnet with no direct internet route.", "Máy chủ CSDL an toàn nằm trong subnet VPC riêng không có kết nối Internet trực tiếp.",
     "Mạng riêng ảo VPC", "🔒", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Availability Zone (AZ)", "/əˌveɪ.ləˈbɪl.ə.ti zəʊn/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Vùng sẵn sàng AZ: một hoặc nhiều trung tâm dữ liệu độc lập về nguồn điện, làm mát và mạng trong một vùng đám mây.",
     "Distributing services across multiple AZs guarantees high availability during power outages.", "Phân phối dịch vụ qua nhiều AZ đảm bảo tính sẵn sàng cao khi bị mất điện.",
     "Vùng sẵn sàng AZ", "🏢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Cloud Region", "/klaʊd ˈriː.dʒən/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Khu vực đám mây: một vị trí địa lý trên thế giới chứa từ ba Vùng sẵn sàng (AZ) độc lập trở lên.",
     "Deploy application servers in the Singapore cloud region to reduce latency for Asian users.", "Triển khai máy chủ ở khu vực Singapore để giảm độ trễ cho người dùng châu Á.",
     "Khu vực đám mây Region", "🌏", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Elastic Compute (EC2)", "/ˌiː.siːˈtuː/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Máy chủ ảo đám mây EC2: dịch vụ cung cấp năng lực tính toán máy ảo có thể thay đổi kích thước linh hoạt trên AWS.",
     "We launch c6i compute-optimized EC2 instances for heavy mathematical simulations.", "Chúng tôi khởi tạo các máy ảo EC2 c6i tối ưu tính toán cho các mô phỏng toán học nặng.",
     "Máy chủ ảo EC2", "💻", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Object Storage (S3)", "/ˈɒb.dʒɪkt ˈstɔː.rɪdʒ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Lưu trữ đối tượng S3: lưu trữ dữ liệu phi cấu trúc (ảnh, video, tệp sao lưu) dưới dạng đối tượng kèm siêu dữ liệu và ID duy nhất.",
     "Upload user profile photos directly into Amazon S3 buckets via presigned URLs.", "Tải ảnh đại diện người dùng trực tiếp vào bộ chứa Amazon S3 qua URL ký trước.",
     "Lưu trữ đối tượng S3", "🗄️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Block Storage", "/blɒk ˈstɔː.rɪdʒ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Lưu trữ khối: lưu trữ dữ liệu dưới dạng các khối thô (như ổ cứng ảo EBS), thường gắn trực tiếp vào một máy ảo duy nhất.",
     "AWS EBS provides high-IOPS persistent block storage volumes for relational databases.", "AWS EBS cung cấp các ổ lưu trữ khối IOPS cao bền vững cho các CSDL quan hệ.",
     "Lưu trữ khối Block Storage", "🧱", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Autoscaling", "/ˈɔː.təʊˌskeɪ.lɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Tự động mở rộng quy mô: tự động tăng hoặc giảm số lượng máy chủ dựa trên lưu lượng truy cập thực tế.",
     "Autoscaling ensures the website stays online during Black Friday traffic spikes.", "Tự động mở rộng quy mô giúp trang web luôn online khi lượng truy cập tăng vọt dịp Black Friday.",
     "Tự động co giãn Autoscaling", "📈", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Auto-Scaling Group", "/ˌɔː.təʊ ˈskeɪ.lɪŋ ɡruːp/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nhóm tự động co giãn: tập hợp các máy ảo EC2 được quản lý chung theo chính sách ngưỡng CPU hoặc bộ nhớ.",
     "The auto-scaling group automatically terminated an unhealthy EC2 instance.", "Nhóm tự động co giãn đã tự động hủy bỏ một máy ảo EC2 gặp sự cố sức khỏe.",
     "Nhóm tự động co giãn ASG", "👥", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Elastic Load Balancer (ELB)", "/ɪˈlæs.tɪk ləʊd ˈbæl.ən.sər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Cân bằng tải đàn hồi: dịch vụ cân bằng tải tự động phân phối lưu lượng vào các máy ảo và pod khỏe mạnh.",
     "An Application Load Balancer routes web traffic across instances using URL paths.", "Bộ cân bằng tải ứng dụng ALB định tuyến lưu lượng web qua các máy ảo theo đường dẫn URL.",
     "Cân bằng tải đàn hồi ELB", "⚖️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("CloudFormation", "/klaʊd fɔːˈmeɪ.ʃən/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Dịch vụ CloudFormation: công cụ định nghĩa và khởi tạo toàn bộ tài nguyên AWS bằng tệp mẫu mã JSON hoặc YAML.",
     "Define your entire VPC and database stack in a reusable CloudFormation template.", "Định nghĩa toàn bộ VPC và CSDL của bạn trong một mẫu CloudFormation tái sử dụng.",
     "Khởi tạo hạ tầng CloudFormation", "📋", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Terraform", "/ˈter.ə.fɔːm/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Công cụ Terraform: phần mềm nguồn mở quản lý hạ tầng dưới dạng mã (IaC) độc lập hỗ trợ mọi nền tảng đám mây.",
     "Run 'terraform apply' to provision cloud virtual networks and clusters declaratively.", "Chạy 'terraform apply' để tạo mạng ảo đám mây và cụm máy chủ theo cách khai báo.",
     "Công cụ Terraform IaC", "🌍", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Infrastructure as Code (IaC)", "/ˌɪn.frəˈstrʌk.tʃər æz kəʊd/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hạ tầng dưới dạng mã: quản lý và cung cấp hạ tầng máy tính thông qua các tệp mã định nghĩa thay vì cấu hình thủ công.",
     "IaC enables version-controlled, reproducible server architectures across environments.", "IaC cho phép tạo ra kiến trúc máy chủ có thể tái lập và quản lý phiên bản qua Git.",
     "Hạ tầng dưới dạng mã IaC", "📜", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Ansible", "/ˈæn.sə.bəl/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Công cụ Ansible: công cụ tự động hóa cấu hình không cần cài agent, điều khiển máy chủ từ xa qua SSH.",
     "Ansible playbooks configure packages and users across hundreds of Linux nodes simultaneously.", "Ansible playbook cấu hình các gói và người dùng trên hàng trăm nút Linux cùng lúc.",
     "Tự động cấu hình Ansible", "🤖", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Configuration Management", "/kənˌfɪɡ.jəˈreɪ.ʃən ˈmæn.ɪdʒ.mənt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Quản lý cấu hình: duy trì tính nhất quán về phần mềm, phiên bản và thiết lập trên toàn bộ hệ thống máy chủ.",
     "Configuration management stops server configuration drift across production servers.", "Quản lý cấu hình ngăn chặn sự trôi lệch cấu hình giữa các máy chủ sản xuất.",
     "Quản lý cấu hình hệ thống", "⚙️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Container", "/kənˈteɪ.nər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Bộ chứa (Container): gói phần mềm chuẩn hóa đóng gói mã nguồn và tất cả các phụ thuộc để chạy nhất quán ở mọi nơi.",
     "Containers share the host OS kernel, making them lightweight and rapid to start.", "Bộ chứa chia sẻ nhân OS của máy chủ nên rất nhẹ và khởi động siêu nhanh.",
     "Bộ chứa Container", "📦", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Containerization", "/kənˌteɪ.nər.aɪˈzeɪ.ʃən/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Công nghệ đóng gói bộ chứa: phương pháp đóng gói ứng dụng loại bỏ hoàn toàn lỗi 'chạy trên máy tôi nhưng không chạy trên máy bạn'.",
     "Containerization revolutionized DevOps by unifying dev and production runtime environments.", "Đóng gói bộ chứa đã cách mạng hóa DevOps bằng việc thống nhất môi trường chạy mã.",
     "Công nghệ Containerization", "🚢", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Docker", "/ˈdɒk.ər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng Docker: nền tảng mã nguồn mở phổ biến nhất thế giới để xây dựng, chia sẻ và chạy các bộ chứa container.",
     "Install Docker Desktop on macOS to test containerized applications locally.", "Cài đặt Docker Desktop trên macOS để kiểm thử các ứng dụng container hóa cục bộ.",
     "Nền tảng Docker", "🐳", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Dockerfile", "/ˈdɒk.ə.faɪl/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Tệp Dockerfile: tệp văn bản chứa chuỗi các câu lệnh chỉ dẫn để tự động xây dựng một ảnh Docker hoàn chỉnh.",
     "The Dockerfile specifies the base image, environment variables, and start command.", "Tệp Dockerfile chỉ định ảnh cơ sở, các biến môi trường và câu lệnh khởi động.",
     "Tệp định nghĩa Dockerfile", "📄", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Docker Image", "/ˈdɒk.ər ˈɪm.ɪdʒ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Ảnh Docker: khuôn mẫu bất biến chỉ đọc chứa mã nguồn, thư viện và công cụ dùng để tạo ra các container đang chạy.",
     "Pull the official node:20-alpine Docker image to construct a compact microservice.", "Kéo ảnh Docker node:20-alpine chính thức để xây dựng vi dịch vụ nhỏ gọn.",
     "Ảnh Docker Image", "🖼️", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Docker Compose", "/ˈdɒk.ər kəmˈpəʊz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Công cụ Docker Compose: công cụ định nghĩa và chạy các ứng dụng gồm nhiều container liên kết thông qua tệp docker-compose.yml.",
     "Run 'docker-compose up' to launch the web app, Redis cache, and Postgres DB together.", "Chạy 'docker-compose up' để khởi chạy đồng thời ứng dụng web, Redis và CSDL Postgres.",
     "Điều phối Docker Compose", "🎼", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Container Registry", "/kənˈteɪ.nər ˈredʒ.ɪ.stri/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Kho chứa ảnh bộ chứa: dịch vụ lưu trữ và phân phối các ảnh Docker (Docker Hub, AWS ECR, GitHub Packages).",
     "Push versioned application images to private Amazon ECR container registries.", "Đẩy các ảnh ứng dụng đã gắn số phiên bản lên kho lưu trữ ECR riêng tư của Amazon.",
     "Kho ảnh Container Registry", "🏬", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes (K8s)", "/ˌkuː.bərˈnet.iːz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hệ thống Kubernetes: nền tảng mã nguồn mở chuẩn công nghiệp để tự động hóa triển khai, mở rộng và quản lý container.",
     "Kubernetes manages clustered containers across hundreds of cloud worker nodes.", "Kubernetes quản lý các bộ chứa được gom cụm trên hàng trăm nút máy chủ đám mây.",
     "Điều phối Kubernetes K8s", "☸️", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes Pod", "/ˌkuː.bərˈnet.iːz pɒd/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Pod trong Kubernetes: đơn vị triển khai nhỏ nhất trong K8s, bao gồm một hoặc một nhóm container chia sẻ chung mạng và bộ nhớ.",
     "A Kubernetes pod encapsulates the application container alongside a monitoring sidecar.", "Một pod Kubernetes đóng gói container ứng dụng cùng với một sidecar giám sát.",
     "Đơn vị Pod Kubernetes", "🌱", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes ReplicaSet", "/ˌkuː.bərˈnet.iːz ˈrep.lɪ.kə.set/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Bộ sao chép ReplicaSet: đối tượng đảm bảo luôn có một số lượng chính xác các bản sao Pod đang chạy ổn định.",
     "The ReplicaSet automatically provisions a replacement pod when one pod crashes.", "ReplicaSet tự động cấp phát pod thay thế khi có một pod bị sập.",
     "Bộ sao chép ReplicaSet", "👯", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes Deployment", "/ˌkuː.bərˈnet.iːz dɪˈplɔɪ.mənt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Triển khai Kubernetes: đối tượng quản lý khai báo cập nhật phiên bản cho Pods và ReplicaSets một cách liền mạch.",
     "Deployments support declarative zero-downtime rolling updates of container versions.", "Đối tượng Deployment hỗ trợ cập nhật cuốn chiếu phiên bản container mà không bị gián đoạn.",
     "Đối tượng Deployment K8s", "🚀", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes Service", "/ˌkuː.bərˈnet.iːz ˈsɜː.vɪs/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Dịch vụ Kubernetes: điểm cuối mạng trừu tượng cung cấp một địa chỉ IP và cân bằng tải ổn định tới tập hợp các Pod.",
     "A ClusterIP service allows internal pods to communicate via internal DNS.", "Dịch vụ ClusterIP cho phép các pod nội bộ giao tiếp với nhau qua DNS nội bộ.",
     "Dịch vụ Service K8s", "🔌", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes Ingress", "/ˌkuː.bərˈnet.iːz ˈɪn.ɡres/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Cổng vào Ingress: quản lý định tuyến lưu lượng HTTP/HTTPS từ bên ngoài cụm K8s vào các Service bên trong.",
     "Ingress controllers provide SSL termination and path-based routing for multiple services.", "Bộ điều khiển Ingress cung cấp chấm dứt SSL và định tuyến theo đường dẫn cho nhiều dịch vụ.",
     "Cổng vào Ingress K8s", "🚪", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes ConfigMap", "/ˌkuː.bərˈnet.iːz ˈkɒn.fɪɡ.mæp/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Bản đồ cấu hình ConfigMap: đối tượng lưu trữ các cặp khóa - giá trị của các tham số cấu hình phi bí mật.",
     "Inject application settings into pods as environment variables via ConfigMaps.", "Truyền các thiết lập ứng dụng vào pod dưới dạng biến môi trường thông qua ConfigMap.",
     "Bản đồ cấu hình ConfigMap", "🗺️", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Kubernetes Secret", "/ˌkuː.bərˈnet.iːz ˈsiː.krət/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Bí mật Kubernetes: đối tượng chuyên lưu trữ thông tin nhạy cảm như mật khẩu, khóa bí mật, token được mã hóa Base64.",
     "Store database passwords in a Kubernetes Secret rather than hardcoding in manifests.", "Lưu mật khẩu CSDL trong Kubernetes Secret thay vì gắn cứng vào tệp manifest.",
     "Bí mật K8s Secret", "🤫", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Helm Chart", "/helm tʃɑːt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Gói triển khai Helm: trình quản lý gói cho Kubernetes đóng gói tất cả tệp manifest cần thiết để cài đặt ứng dụng.",
     "Deploying a Redis cluster takes one command using its official Helm chart.", "Triển khai một cụm Redis chỉ tốn một câu lệnh duy nhất nhờ Helm chart chính thức.",
     "Gói triển khai Helm Chart", "📦", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Container Orchestration", "/kənˈteɪ.nər ˌɔː.kɪˈstreɪ.ʃən/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Điều phối bộ chứa: tự động hóa việc cấu hình, điều phối và quản lý vòng đời của hàng ngàn container.",
     "Container orchestration ensures self-healing by restarting failed microservice containers.", "Điều phối container đảm bảo khả năng tự phục hồi bằng cách khởi động lại container bị hỏng.",
     "Điều phối Container", "🎼", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Continuous Integration (CI)", "/kənˌtɪn.ju.əs ˌɪn.tɪˈɡreɪ.ʃən/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Tích hợp liên tục: thực hành tự động hợp nhất mã của nhiều lập trình viên và chạy kiểm thử tự động nhiều lần mỗi ngày.",
     "Continuous Integration catches integration bugs early before code reaches staging.", "Tích hợp liên tục bắt các lỗi tích hợp sớm trước khi mã nguồn tới môi trường staging.",
     "Tích hợp liên tục CI", "🔄", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Continuous Delivery (CD)", "/kənˌtɪn.ju.əs dɪˈlɪv.ər.i/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Chuyển giao liên tục: tự động hóa quá trình đóng gói và phát hành để phần mềm luôn sẵn sàng triển khai lên sản xuất bất kỳ lúc nào.",
     "Continuous Delivery ensures every passing build produces deployable release artifacts.", "Chuyển giao liên tục đảm bảo mọi bản dựng vượt qua kiểm thử đều tạo ra bản phát hành sẵn sàng triển khai.",
     "Chuyển giao liên tục CD", "🚚", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Continuous Deployment", "/kənˌtɪn.ju.əs dɪˈplɔɪ.mənt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Triển khai liên tục: mọi thay đổi vượt qua toàn bộ các bài kiểm thử tự động sẽ được đẩy thẳng trực tiếp lên máy chủ sản xuất không cần phê duyệt thủ công.",
     "Leading tech companies practice continuous deployment, releasing code dozens of times daily.", "Các công ty công nghệ hàng đầu áp dụng triển khai liên tục, phát hành mã hàng chục lần mỗi ngày.",
     "Triển khai liên tục", "🚀", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("CI/CD Pipeline", "/ˌsiː.aɪ ˌsiːˈdiː ˈpaɪp.laɪn/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Đường ống CI/CD: chuỗi các bước tự động hóa gồm kiểm tra cú pháp, chạy kiểm thử, xây dựng container và triển khai lên máy chủ.",
     "A red badge in GitHub indicates that the CI/CD pipeline failed on unit tests.", "Huy hiệu đỏ trên GitHub báo hiệu rằng đường ống CI/CD bị thất bại ở khâu kiểm thử đơn vị.",
     "Đường ống tự động CI/CD", "🚰", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Jenkins", "/ˈdʒeŋ.kɪnz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Máy chủ tự động hóa Jenkins: công cụ mã nguồn mở kinh điển cho phép xây dựng các đường ống CI/CD phức tạp.",
     "Jenkins pipelines are defined using Groovy syntax inside a Jenkinsfile.", "Đường ống Jenkins được định nghĩa bằng cú pháp Groovy bên trong tệp Jenkinsfile.",
     "Hệ thống CI Jenkins", "🤖", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("GitHub Actions", "/ˈɡɪt.hʌb ˈæk.ʃənz/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng GitHub Actions: dịch vụ tự động hóa quy trình CI/CD tích hợp trực tiếp ngay trong kho lưu trữ GitHub bằng tệp YAML.",
     "GitHub Actions runs automated test matrices across Ubuntu, macOS, and Windows runners.", "GitHub Actions chạy ma trận kiểm thử tự động trên máy chạy Ubuntu, macOS và Windows.",
     "Tự động hóa GitHub Actions", "⚡", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("GitLab CI/CD", "/ˈɡɪt.læb ˌsiː.aɪ ˌsiːˈdiː/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hệ thống GitLab CI/CD: công cụ CI/CD tích hợp sẵn của GitLab cấu hình thông qua tệp .gitlab-ci.yml.",
     "GitLab CI/CD offers built-in container registries and auto-DevOps deployment workflows.", "GitLab CI/CD cung cấp sẵn kho lưu trữ container và quy trình triển khai auto-DevOps.",
     "Quy trình GitLab CI/CD", "🦊", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Build Artifact", "/bɪld ˈɑː.tɪ.fækt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Tạo phẩm bản dựng: tệp nhị phân, gói zip hoặc ảnh container được tạo ra thành công sau quá trình biên dịch và đóng gói.",
     "Store build artifacts in cloud storage for deployment rollback verification.", "Lưu trữ tạo phẩm bản dựng trên đám mây để phục vụ việc xác minh khi cần rollback.",
     "Tạo phẩm bản dựng Artifact", "📦", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Artifact Repository", "/ˈɑː.tɪ.fækt rɪˈpɒz.ɪ.tər.i/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Kho lưu trữ tạo phẩm: máy chủ chuyên dụng lưu giữ và phân phối các gói thư viện đã biên dịch (Nexus, JFrog Artifactory).",
     "JFrog Artifactory serves as an enterprise repository for Maven and npm binaries.", "JFrog Artifactory đóng vai trò là kho lưu trữ doanh nghiệp cho các tệp nhị phân Maven và npm.",
     "Kho tạo phẩm Artifact", "🏬", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Blue-Green Deployment", "/bluː ɡriːn dɪˈplɔɪ.mənt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Triển khai Xanh-Lam: kỹ thuật duy trì hai môi trường sản xuất giống nhau (Blue và Green) để chuyển hướng lưu lượng tức thì không có downtime.",
     "Blue-green deployment allows instant rollback to the previous version if errors emerge.", "Triển khai Xanh-Lam cho phép quay ngược phiên bản cũ ngay lập tức nếu phát sinh lỗi.",
     "Triển khai Xanh-Lam", "🔵🟢", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Canary Deployment", "/kəˈneə.ri dɪˈplɔɪ.mənt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Triển khai chim hoàng yến: đưa phiên bản mới thử nghiệm tới một tỷ lệ nhỏ người dùng (5%) trước khi tung ra diện rộng.",
     "Canary deployments limit user impact by detecting regressions on a fraction of real traffic.", "Triển khai chim hoàng yến hạn chế ảnh hưởng bằng cách phát hiện lỗi trên một lượng nhỏ lưu lượng.",
     "Triển khai thử nghiệm Canary", "🐤", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Rolling Update", "/ˈrəʊ.lɪŋ ʌpˈdeɪt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Cập nhật cuốn chiếu: dần dần thay thế từng máy chủ/pod cũ bằng phiên bản mới mà không làm gián đoạn toàn bộ dịch vụ.",
     "Kubernetes executes rolling updates to ensure a minimum number of pods stay healthy.", "Kubernetes thực hiện cập nhật cuốn chiếu để đảm bảo luôn có số pod tối thiểu hoạt động.",
     "Cập nhật cuốn chiếu", "🔄", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Rollback", "/ˈrəʊl.bæk/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hoàn tác phiên bản: quay trở về phiên bản ổn định trước đó khi bản triển khai mới gặp sự cố nghiêm trọng.",
     "Triggering a rollback restored checkout functionality in less than two minutes.", "Kích hoạt hoàn tác phiên bản đã khôi phục chức năng thanh toán chỉ trong chưa đầy hai phút.",
     "Hoàn tác phiên bản Rollback", "🔙", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Site Reliability Engineering (SRE)", "/ˌes.ɑːrˈiː/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Kỹ thuật tin cậy hệ thống: chuyên ngành áp dụng các nguyên lý công nghệ phần mềm vào các vấn đề vận hành hệ thống hạ tầng.",
     "SRE teams automate infrastructure operations and maintain strict error budgets.", "Các đội ngũ SRE tự động hóa vận hành hạ tầng và duy trì ngân sách lỗi nghiêm ngặt.",
     "Kỹ sư tin cậy hệ thống SRE", "👷‍♂️", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Service Level Agreement (SLA)", "/ˌes.elˈeɪ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Cam kết chất lượng dịch vụ: hợp đồng chính thức giữa nhà cung cấp và khách hàng quy định mức độ sẵn sàng và bồi thường.",
     "The cloud provider offers a 99.99 percent uptime SLA with financial credits for breaches.", "Nhà cung cấp đám mây cam kết SLA thời gian hoạt động 99,99% kèm bồi hoàn tiền khi vi phạm.",
     "Cam kết chất lượng SLA", "📜", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Service Level Objective (SLO)", "/ˌes.elˈoʊ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Mục tiêu mức dịch vụ: mục tiêu nội bộ của nhóm kỹ thuật nhằm đạt được một mức độ tin cậy cụ thể (chặt hơn SLA).",
     "Our internal SLO dictates that 99 percent of API requests must return in under 200ms.", "Mục tiêu SLO nội bộ của chúng tôi quy định 99% yêu cầu API phải phản hồi dưới 200 mili-giây.",
     "Mục tiêu mức dịch vụ SLO", "🎯", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Service Level Indicator (SLI)", "/ˌes.elˈaɪ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Chỉ số mức dịch vụ: thước đo định lượng thực tế theo thời gian về mức độ tuân thủ của dịch vụ (ví dụ: tỷ lệ lỗi % hay độ trễ).",
     "HTTP request error rate is our primary SLI to track system health.", "Tỷ lệ lỗi yêu cầu HTTP là chỉ số SLI chính của chúng tôi để theo dõi sức khỏe hệ thống.",
     "Chỉ số mức dịch vụ SLI", "📊", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("High Availability (HA)", "/haɪ əˌveɪ.ləˈbɪl.ə.ti/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Tính sẵn sàng cao: đặc tính của hệ thống đảm bảo duy trì hoạt động liên tục không ngừng nghỉ trong thời gian dài.",
     "Redundant power supplies and clustered nodes are required to achieve high availability.", "Nguồn điện dự phòng và các nút cụm máy chủ là bắt buộc để đạt được tính sẵn sàng cao.",
     "Tính sẵn sàng cao HA", "⚡", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Fault Tolerance", "/fɒlt ˈtɒl.ər.əns/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Khả năng chịu lỗi: khả năng của hệ thống vẫn tiếp tục vận hành bình thường ngay cả khi một hoặc nhiều linh kiện phần cứng bị hỏng hóc.",
     "Fault tolerance prevents total system blackouts when a single server rack loses power.", "Khả năng chịu lỗi ngăn sập toàn bộ hệ thống khi một tủ rack máy chủ đơn lẻ bị mất điện.",
     "Khả năng chịu lỗi", "🛡️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Disaster Recovery (DR)", "/dɪˈzɑː.stər rɪˈkʌv.ər.i/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Phục hồi sau thảm họa: tập hợp các quy trình và chính sách để khôi phục hạ tầng CNTT sau thiên tai hoặc sự cố nghiêm trọng.",
     "Annual disaster recovery drills simulate complete regional cloud data center failures.", "Các buổi diễn tập phục hồi thảm họa hàng năm mô phỏng mất hoàn toàn trung tâm dữ liệu khu vực.",
     "Phục hồi thảm họa DR", "🆘", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Recovery Time Objective (RTO)", "/ˌɑːr.tiːˈoʊ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Thời gian phục hồi mục tiêu: khoảng thời gian tối đa cho phép hệ thống phải được khôi phục sau sự cố.",
     "Our mission-critical database has an aggressive RTO of under fifteen minutes.", "Cơ sở dữ liệu trọng yếu của chúng tôi có mục tiêu RTO khắt khe dưới mười lăm phút.",
     "Thời gian phục hồi RTO", "⏰", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Recovery Point Objective (RPO)", "/ˌɑːr.piːˈoʊ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Điểm phục hồi mục tiêu: lượng dữ liệu tối đa chấp nhận bị mất tính theo khoảng thời gian giữa hai lần sao lưu.",
     "Continuous database replication provides a near-zero RPO for customer orders.", "Sao chép CSDL liên tục mang lại chỉ số RPO gần bằng 0 cho các đơn hàng của khách.",
     "Điểm phục hồi dữ liệu RPO", "💾", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Chaos Engineering", "/ˈkeɪ.ɒs ˌen.dʒɪˈnɪə.rɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Kỹ thuật hỗn loạn: thực hành chủ động gây lỗi giả lập vào hệ thống sản xuất để phát hiện các điểm yếu tiềm ẩn.",
     "Netflix pioneered chaos engineering to ensure their streaming platform survives server outages.", "Netflix tiên phong kỹ thuật hỗn loạn để đảm bảo nền tảng xem phim sống sót qua sự cố máy chủ.",
     "Kỹ thuật hỗn loạn Chaos", "🌪️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Chaos Monkey", "/ˈkeɪ.ɒs ˈmʌŋ.ki/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Công cụ Chaos Monkey: phần mềm do Netflix tạo ra tự động tắt ngẫu nhiên các máy chủ sản xuất trong giờ làm việc.",
     "Chaos Monkey proves that our architecture automatically recovers from unexpected server loss.", "Chaos Monkey chứng minh rằng kiến trúc của chúng tôi tự động hồi phục khi mất máy chủ bất ngờ.",
     "Công cụ Chaos Monkey", "🐒", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Idempotent Infrastructure", "/aɪˈdem.pəʊ.tənt ˌɪn.frəˈstrʌk.tʃər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hạ tầng lũy đẳng: trạng thái mà khi chạy lại kịch bản triển khai nhiều lần thì hệ thống vẫn giữ nguyên cấu hình đích mong muốn.",
     "Ansible modules are idempotent, applying modifications only when state has drifted.", "Các mô-đun Ansible có tính lũy đẳng, chỉ áp dụng sửa đổi khi trạng thái thực sự bị lệch.",
     "Hạ tầng lũy đẳng", "🔄", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Immutable Infrastructure", "/ɪˈmjuː.tə.bəl ˌɪn.frəˈstrʌk.tʃər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hạ tầng bất biến: nguyên tắc không bao giờ sửa đổi máy chủ đang chạy mà luôn tạo máy chủ mới thay thế hoàn toàn khi cập nhật.",
     "Immutable infrastructure prevents configuration rot by replacing entire VM images.", "Hạ tầng bất biến ngăn chặn sự mục nát cấu hình bằng cách thay thế hoàn toàn ảnh máy ảo.",
     "Hạ tầng bất biến", "💎", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("GitOps", "/ˈɡɪt.ɒps/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Mô hình GitOps: dùng kho lưu trữ Git làm nguồn chân lý duy nhất (single source of truth) cho toàn bộ cấu hình hạ tầng.",
     "Under GitOps, merging a pull request to the main branch triggers deployment automatically.", "Theo GitOps, hợp nhất pull request vào nhánh chính sẽ tự động kích hoạt việc triển khai.",
     "Mô hình vận hành GitOps", "🌿", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("ArgoCD", "/ˈɑː.ɡəʊ ˌsiːˈdiː/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Công cụ ArgoCD: công cụ GitOps khai báo cho Kubernetes tự động đồng bộ hóa trạng thái cụm K8s theo mã trong Git.",
     "ArgoCD detects configuration drift and syncs Kubernetes manifests from the Git repository.", "ArgoCD phát hiện lệch cấu hình và tự đồng bộ hóa manifest Kubernetes từ kho lưu trữ Git.",
     "Công cụ GitOps ArgoCD", "🐙", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Service Mesh", "/ˈsɜː.vɪs meʃ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Lưới dịch vụ Service Mesh: tầng hạ tầng chuyên biệt quản lý việc truyền thông an toàn, định tuyến và giám sát giữa các vi dịch vụ.",
     "A service mesh provides mutual TLS encryption without changing application source code.", "Lưới dịch vụ cung cấp mã hóa TLS lẫn nhau mà không cần sửa đổi mã nguồn ứng dụng.",
     "Lưới dịch vụ Service Mesh", "🕸️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Istio", "/ˈɪs.ti.əʊ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng Istio: giải pháp Service Mesh mã nguồn mở hàng đầu dùng proxy Envoy gắn cạnh mỗi container để kiểm soát lưu lượng.",
     "Istio enforces zero-trust traffic policies and circuit breaking between microservices.", "Istio thực thi các chính sách lưu lượng không tin cậy và ngắt mạch giữa các vi dịch vụ.",
     "Nền tảng lưới Istio", "⛵", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Sidecar Pattern", "/ˈsaɪd.kɑː ˈpæt.ən/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Mẫu thiết kế Sidecar: triển khai một container phụ trợ chạy song hành bên cạnh container chính trong cùng một Pod để chia sẻ việc.",
     "The sidecar container collects logs and ships them to Elasticsearch in real-time.", "Container sidecar thu thập log và gửi về Elasticsearch theo thời gian thực.",
     "Mẫu thiết kế Sidecar", "🏍️", "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=600&auto=format&fit=crop&q=80"),

    ("Observability", "/əbˌzɜː.vəˈbɪl.ə.ti/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Khả năng quan sát: khả năng hiểu rõ trạng thái nội tại của hệ thống dựa trên các dữ liệu đầu ra gồm số liệu, nhật ký và vết truy vết.",
     "Observability relies on three pillars: metrics, logs, and distributed traces.", "Khả năng quan sát dựa trên ba trụ cột: số liệu đo, nhật ký log và vết truy vết phân tán.",
     "Khả năng quan sát hệ thống", "👁️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Monitoring", "/ˈmɒn.ɪ.tər.ɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Giám sát hệ thống: hành động liên tục thu thập và theo dõi các chỉ số hiệu năng để biết khi nào hệ thống gặp sự cố.",
     "Continuous monitoring alerts on-call engineers when server memory usage exceeds 90 percent.", "Giám sát liên tục cảnh báo kỹ sư trực khi mức dùng RAM máy chủ vượt quá 90%.",
     "Giám sát hệ thống Monitoring", "🖥️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Metrics", "/ˈmet.rɪks/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Số liệu đo lường: các giá trị số học được đo lường định kỳ theo thời gian như tải CPU, số yêu cầu/giây hay thời gian phản hồi.",
     "Graphing request metrics uncovers unexpected latency spikes during peak hours.", "Vẽ biểu đồ các số liệu yêu cầu làm lộ ra những đợt tăng vọt độ trễ trong giờ cao điểm.",
     "Số liệu đo lường Metrics", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Centralized Logging", "/ˈsen.trə.laɪzd ˈlɒɡ.ɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Ghi nhật ký tập trung: gom toàn bộ nhật ký log từ hàng ngàn container về một kho dữ liệu trung tâm duy nhất để tìm kiếm.",
     "Centralized logging aggregates log streams from hundreds of microservices into one searchable console.", "Ghi nhật ký tập trung gom luồng log từ hàng trăm vi dịch vụ về một bảng điều khiển tìm kiếm.",
     "Ghi nhật ký tập trung", "📜", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Distributed Tracing", "/dɪˈstrɪb.juː.tɪd ˈtreɪs.ɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Truy vết phân tán: kỹ thuật theo dõi đường đi của một yêu cầu khi nó đi qua hàng chục vi dịch vụ khác nhau trong hệ thống.",
     "Distributed tracing pinpoints the exact microservice causing checkout latency bottlenecks.", "Truy vết phân tán chỉ ra chính xác vi dịch vụ gây nghẽn độ trễ khi thanh toán.",
     "Truy vết phân tán Tracing", "🗺️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Prometheus", "/prəˈmiː.θi.əs/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hệ thống giám sát Prometheus: công cụ nguồn mở chuyên thu thập và lưu trữ các chỉ số số liệu chuỗi thời gian dựa trên cơ chế kéo (pull).",
     "Prometheus scrapes metrics endpoints from Kubernetes pods every 15 seconds.", "Prometheus quét các điểm cuối số liệu từ pod Kubernetes mỗi 15 giây.",
     "Hệ thống đo Prometheus", "🔥", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Grafana", "/ɡrəˈfɑː.nə/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng hiển thị Grafana: phần mềm trực quan hóa dữ liệu và xây dựng bảng điều khiển biểu đồ phân tích hàng đầu cho DevOps.",
     "Grafana dashboards visualize real-time cluster memory, network I/O, and HTTP rates.", "Bảng điều khiển Grafana trực quan hóa RAM cụm, vào ra mạng và lưu lượng HTTP thời gian thực.",
     "Bảng điều khiển Grafana", "📈", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("ELK Stack", "/ˌiː.elˈkeɪ stæk/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Bộ công cụ ELK: bộ ba công cụ nguồn mở kết hợp Elasticsearch, Logstash và Kibana dùng để tìm kiếm và phân tích log mạnh mẽ.",
     "Enterprises rely on the ELK Stack to index terabytes of server logs daily.", "Doanh nghiệp dựa vào ELK Stack để lập chỉ mục hàng terabyte log máy chủ mỗi ngày.",
     "Bộ công cụ ELK Stack", "🦌", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Elasticsearch", "/ɪˌlæs.tɪkˈsɜːtʃ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Bộ máy tìm kiếm Elasticsearch: bộ máy tìm kiếm và phân tích dữ liệu phân tán chuẩn RESTful thời gian thực.",
     "Elasticsearch indexes unstructured application logs for rapid full-text search.", "Elasticsearch lập chỉ mục log ứng dụng phi cấu trúc để tìm kiếm toàn văn siêu nhanh.",
     "Bộ máy Elasticsearch", "🔍", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Logstash", "/ˈlɒɡ.stæʃ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Đường ống thu thập Logstash: công cụ thu thập, phân tích cú pháp và biến đổi nhật ký log trước khi gửi tới nơi lưu trữ.",
     "Logstash parses timestamped log lines using grok pattern filters.", "Logstash phân tích các dòng log có dấu thời gian bằng bộ lọc mẫu grok.",
     "Bộ xử lý Logstash", "🪵", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Kibana", "/kɪˈbɑː.nə/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Giao diện Kibana: giao diện trực quan hóa và bảng điều khiển cho dữ liệu được lập chỉ mục trong Elasticsearch.",
     "Engineers use Kibana discover tabs to investigate stack traces during outages.", "Kỹ sư dùng thẻ khám phá Kibana để điều tra dấu vết lỗi stack trace trong sự cố.",
     "Giao diện Kibana", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Datadog", "/ˈdeɪ.tə.dɒɡ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Nền tảng Datadog: dịch vụ SaaS giám sát và phân tích toàn diện trên nền tảng đám mây cho hạ tầng, ứng dụng và bảo mật.",
     "Datadog agents monitor container health and automatically calculate SLO compliance.", "Agent của Datadog giám sát sức khỏe container và tự động tính toán tuân thủ SLO.",
     "Nền tảng giám sát Datadog", "🐶", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("OpenTelemetry", "/ˌoʊ.pən.təˈlem.ə.tri/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Chuẩn OpenTelemetry: chuẩn mở của CNCF cung cấp bộ API và SDK thống nhất để thu thập số liệu, vết truy vết và log.",
     "OpenTelemetry provides a vendor-neutral telemetry standard adopted across modern frameworks.", "OpenTelemetry cung cấp chuẩn thu thập đo từ xa trung lập được chấp nhận rộng rãi.",
     "Chuẩn đo lường OpenTelemetry", "🔭", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Jaeger", "/ˈjeɪ.ɡər/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hệ thống Jaeger: công cụ mã nguồn mở dùng để theo dõi và khắc phục sự cố giao dịch trong các kiến trúc vi dịch vụ phức tạp.",
     "Jaeger visualizes execution spans across network boundaries as interactive waterfall graphs.", "Jaeger trực quan hóa các khoảng thời gian thực thi qua ranh giới mạng dưới dạng biểu đồ thác nước.",
     "Truy vết Jaeger", "🏹", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Alerting", "/əˈlɜː.tɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Cơ chế cảnh báo: tự động gửi thông báo qua PagerDuty, Slack hoặc SMS khi chỉ số hệ thống vượt ngưỡng nguy hiểm.",
     "Effective alerting prevents alert fatigue by notifying only on actionable incidents.", "Cơ chế cảnh báo hiệu quả tránh tình trạng quá tải cảnh báo bằng cách chỉ báo các sự cố cần hành động.",
     "Cơ chế cảnh báo Alerting", "🚨", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Secret Management", "/ˈsiː.krət ˈmæn.ɪdʒ.mənt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Quản lý bí mật: thực hành bảo mật dùng công cụ chuyên dụng để lưu trữ, mã hóa và xoay vòng các khóa API và mật khẩu.",
     "Centralized secret management prevents developers from hardcoding API credentials in git.", "Quản lý bí mật tập trung ngăn ngừa lập trình viên gắn cứng thông tin API vào mã nguồn git.",
     "Quản lý bí mật Secret", "🔐", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("HashiCorp Vault", "/ˈhæʃ.i.kɔːp vɔːlt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Hệ thống Vault: giải pháp bảo mật của HashiCorp chuyên quản lý bí mật, tạo chứng chỉ động và mã hóa dữ liệu.",
     "Vault generates dynamic short-lived database credentials for microservice workers.", "Vault tạo thông tin đăng nhập CSDL động có thời hạn ngắn cho các vi dịch vụ.",
     "Két sắt bí mật Vault", "🏦", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Bastion Host (Jump Box)", "/ˈbæs.ti.ən həʊst/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Máy chủ trung gian bảo vệ: máy chủ được gia cố an ninh đặc biệt làm cổng vào duy nhất để truy cập SSH vào mạng nội bộ.",
     "Admins connect to the bastion host first before jumping into private backend servers.", "Quản trị viên kết nối tới máy chủ bastion trước khi truy cập vào các máy chủ nội bộ.",
     "Máy chủ trung gian Bastion", "🏰", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Cloud Edge Computing", "/klaʊd edʒ kəmˈpjuː.tɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Điện toán biên đám mây: xử lý tính toán ngay tại các máy chủ biên gần với người dùng nhất thay vì đưa về trung tâm dữ liệu.",
     "Cloudflare Workers run edge computing functions within milliseconds of users worldwide.", "Cloudflare Workers chạy các hàm điện toán biên chỉ cách người dùng vài mili-giây trên toàn cầu.",
     "Điện toán biên Edge Computing", "🌐", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    ("Serverless Lambda", "/ˈsɜː.və.ləs ˈlæm.də/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Dịch vụ AWS Lambda: dịch vụ thực thi mã theo sự kiện tự động quản lý toàn bộ tài nguyên tính toán của Amazon.",
     "AWS Lambda handles image thumbnail generation automatically upon new S3 uploads.", "AWS Lambda xử lý việc tạo ảnh thu nhỏ tự động ngay khi có tệp tải lên S3.",
     "Hàm phi máy chủ Lambda", "λ", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Provisioning", "/prəˈvɪʒ.ən.ɪŋ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Cấp phát tài nguyên: quy trình chuẩn bị, cấu hình và kích hoạt các máy chủ, mạng và dịch vụ đám mây sẵn sàng sử dụng.",
     "Automated provisioning spins up an entire staging environment in ten minutes.", "Cấp phát tự động khởi tạo toàn bộ môi trường staging chỉ trong mười phút.",
     "Cấp phát tài nguyên", "🏗️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Golden AMI / Image", "/ˈɡəʊl.dən ˈɪm.ɪdʒ/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Ảnh mẫu chuẩn vàng: ảnh máy ảo đã được cài đặt sẵn các bản vá bảo mật, cấu hình chuẩn và công cụ giám sát của công ty.",
     "All production EC2 instances must be launched from verified corporate golden AMIs.", "Mọi máy ảo EC2 sản xuất đều phải được khởi tạo từ các ảnh mẫu chuẩn vàng của công ty.",
     "Ảnh mẫu chuẩn Golden Image", "🥇", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Cold Start", "/kəʊld stɑːt/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Khởi động nguội: độ trễ ban đầu khi khởi chạy một phiên bản hàm serverless mới từ trạng thái chưa được cấp phát bộ nhớ.",
     "Provisioned concurrency eliminates cold start latency in serverless customer-facing APIs.", "Tính năng dự phòng đồng thời loại bỏ độ trễ khởi động nguội trong các API phục vụ người dùng.",
     "Khởi động nguội Cold Start", "❄️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("FinOps (Cloud Cost Optimization)", "/ˈfɪn.ɒps/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Quản lý tài chính đám mây FinOps: thực hành kết hợp kỹ thuật và tài chính để tối ưu hóa chi tiêu đám mây không lãng phí.",
     "Implementing FinOps practices saved our company 30 percent on monthly AWS billing.", "Áp dụng thực hành FinOps đã giúp công ty tiết kiệm 30% hóa đơn chi phí AWS hàng tháng.",
     "Tối ưu chi phí FinOps", "💰", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Tenancy", "/ˌmʌl.ti ˈten.ən.si/", "noun", "cloud_devops", "Điện toán đám mây & DevOps",
     "Kiến trúc đa khách hàng: mô hình phần mềm trong đó một phiên bản ứng dụng duy nhất phục vụ đồng thời nhiều khách hàng độc lập.",
     "Multi-tenancy models enforce rigorous logical separation between customer datasets.", "Mô hình đa khách hàng thực thi sự phân tách logic nghiêm ngặt giữa dữ liệu các khách hàng.",
     "Kiến trúc đa khách hàng", "🏢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 7 terms count: {len(terms)}")
