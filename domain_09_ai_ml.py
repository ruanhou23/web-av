# -*- coding: utf-8 -*-
"""Domain 9: AI, Machine Learning & LLMs (100 core terms)"""

terms = [
    ("Artificial Intelligence (AI)", "/ˌɑː.tɪˈfɪʃ.əl ɪnˈtel.ɪ.dʒəns/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Trí tuệ nhân tạo: lĩnh vực khoa học máy tính chuyên tạo ra các hệ thống có khả năng mô phỏng trí thông minh của con người.",
     "Artificial intelligence powers autonomous vehicles, medical diagnosis, and conversational agents.", "Trí tuệ nhân tạo vận hành xe tự hành, chẩn đoán y tế và các trợ lý đàm thoại.",
     "Trí tuệ nhân tạo AI", "🤖", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Machine Learning (ML)", "/məˈʃiːn ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học máy: phân nhánh của AI cho phép máy tính tự học hỏi các quy luật từ dữ liệu mà không cần lập trình quy tắc thủ công.",
     "Machine learning algorithms improve prediction accuracy as more training data is ingested.", "Thuật toán học máy cải thiện độ chính xác dự đoán khi nạp thêm nhiều dữ liệu huấn luyện.",
     "Học máy Machine Learning", "🧠", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Deep Learning (DL)", "/diːp ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học sâu: tập con của học máy dựa trên mạng nơ-ron nhân tạo nhiều lớp (deep neural networks) để mô hình hóa dữ liệu phức tạp.",
     "Deep learning achieved revolutionary breakthroughs in image recognition and speech synthesis.", "Học sâu đã tạo ra những đột phá mang tính cách mạng trong nhận dạng ảnh và tổng hợp giọng nói.",
     "Học sâu Deep Learning", "🌊", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Supervised Learning", "/ˈsuː.pə.vaɪzd ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học có giám sát: phương pháp huấn luyện mô hình trên tập dữ liệu đã có sẵn nhãn đáp án (labeled data).",
     "Spam email classifiers are trained using supervised learning on labeled message archives.", "Bộ phân loại email rác được huấn luyện bằng học có giám sát trên kho thư đã gắn nhãn.",
     "Học có giám sát", "👨‍🏫", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Unsupervised Learning", "/ˌʌnˈsuː.pə.vaɪzd ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học không giám sát: mô hình tự tìm ra các mẫu ẩn và cấu trúc bên trong dữ liệu chưa hề được gắn nhãn.",
     "Clustering customer shopping habits into segments relies on unsupervised learning.", "Phân cụm thói quen mua sắm của khách hàng thành từng nhóm dựa vào học không giám sát.",
     "Học không giám sát", "🔍", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Semi-Supervised Learning", "/ˌsem.i ˈsuː.pə.vaɪzd/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học bán giám sát: kết hợp một lượng nhỏ dữ liệu có nhãn với một lượng lớn dữ liệu chưa gán nhãn để huấn luyện mô hình.",
     "Semi-supervised learning drastically cuts data annotation costs for medical imagery.", "Học bán giám sát giảm đáng kể chi phí gán nhãn dữ liệu cho hình ảnh y tế.",
     "Học bán giám sát", "🌓", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Reinforcement Learning (RL)", "/ˌriː.ɪnˈfɔːs.mənt ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học tăng cường: phương pháp huấn luyện tác tử (agent) tự đưa ra quyết định thông qua thử - sai dựa trên phần thưởng và hình phạt.",
     "AlphaGo mastered the ancient game of Go using reinforcement learning with self-play.", "AlphaGo làm chủ cờ vây cổ xưa bằng học tăng cường thông qua việc tự đấu với chính mình.",
     "Học tăng cường RL", "🎮", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Neural Network (ANN)", "/ˈnjʊə.rəl ˈnet.wɜːk/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mạng nơ-ron nhân tạo: hệ thống điện toán lấy cảm hứng từ cấu trúc mạng tế bào thần kinh sinh học của não bộ.",
     "An artificial neural network transmits signals through layers of weighted mathematical nodes.", "Mạng nơ-ron nhân tạo truyền tín hiệu qua các tầng nút toán học có trọng số.",
     "Mạng nơ-ron nhân tạo", "🕸️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Perceptron", "/pəˈsep.trɒn/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Nơ-ron Perceptron: đơn vị nơ-ron nhân tạo cơ bản nhất tính tổng có trọng số của các đầu vào và áp dụng hàm kích hoạt.",
     "The single-layer perceptron forms the historic cornerstone of modern artificial intelligence.", "Perceptron đơn tầng tạo nền móng lịch sử cho trí tuệ nhân tạo hiện đại.",
     "Đơn vị Perceptron", "⚪", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Convolutional Neural Network (CNN)", "/ˌkɒn.vəˈluː.ʃən.əl/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mạng nơ-ron tích chập (CNN): kiến trúc học sâu chuyên xử lý dữ liệu dạng lưới không gian như ảnh và video.",
     "CNNs use convolutional filter kernels to detect edges, textures, and objects in photos.", "CNN sử dụng các hạt nhân lọc tích chập để phát hiện cạnh, kết cấu và vật thể trong ảnh.",
     "Mạng nơ-ron tích chập CNN", "🖼️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Recurrent Neural Network (RNN)", "/rɪˈkʌr.ənt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mạng nơ-ron hồi quy (RNN): kiến trúc mạng có các vòng lặp phản hồi bên trong, phù hợp xử lý dữ liệu chuỗi tuần tự theo thời gian.",
     "RNNs process sequential time-series data by retaining internal hidden memory states.", "RNN xử lý dữ liệu chuỗi thời gian tuần tự bằng cách duy trì trạng thái ẩn nội bộ.",
     "Mạng hồi quy RNN", "🔄", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Long Short-Term Memory (LSTM)", "/lɒŋ ʃɔːt tɜːm/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mạng bộ nhớ ngắn-dài hạn: biến thể nâng cao của RNN có các cổng quên (forget gate) giúp giải quyết triệt tiêu gradient.",
     "LSTMs successfully capture long-range text dependencies across lengthy paragraphs.", "LSTM nắm bắt thành công các phụ thuộc xa trong văn bản qua các đoạn văn dài.",
     "Mạng nhớ dài-ngắn LSTM", "🧠", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Transformer Architecture", "/trænsˈfɔː.mər/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kiến trúc Transformer: kiến trúc học sâu do Google giới thiệu dựa hoàn toàn vào cơ chế chú ý (attention), nền tảng của mọi LLM ngày nay.",
     "The 2017 paper 'Attention Is All You Need' established the ubiquitous Transformer architecture.", "Bài báo năm 2017 'Attention Is All You Need' đã thiết lập kiến trúc Transformer phổ biến.",
     "Kiến trúc Transformer", "🤖", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Self-Attention Mechanism", "/self əˈten.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Cơ chế tự chú ý: cơ chế cho phép từng từ trong câu liên hệ và đánh giá mức độ quan trọng với tất cả các từ khác cùng lúc.",
     "Self-attention dynamically links pronouns like 'it' to their rightful antecedent nouns.", "Cơ chế tự chú ý liên kết động các đại từ như 'it' với đúng danh từ tiền đề của nó.",
     "Cơ chế tự chú ý Self-Attention", "👁️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Head Attention", "/ˈmʌl.ti hed əˈten.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Cơ chế chú ý đa đầu: chia nhỏ cơ chế chú ý thành nhiều nhánh độc lập để đồng thời nắm bắt các mối quan hệ ngữ nghĩa khác nhau.",
     "Multi-head attention allows models to simultaneously track syntax, tone, and factual relations.", "Chú ý đa đầu cho phép mô hình đồng thời theo dõi cú pháp, giọng văn và quan hệ thực tế.",
     "Chú ý đa đầu Multi-Head", "🐙", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Large Language Model (LLM)", "/lɑːdʒ ˈlæŋ.ɡwɪdʒ ˈmɒd.əl/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mô hình ngôn ngữ lớn (LLM): mô hình AI khổng lồ được huấn luyện trên hàng nghìn tỷ từ ngữ để hiểu và sinh văn bản tự nhiên.",
     "GPT-4, Gemini, and Claude are state-of-the-art large language models powering conversational applications.", "GPT-4, Gemini và Claude là những mô hình ngôn ngữ lớn hàng đầu vận hành ứng dụng đối thoại.",
     "Mô hình ngôn ngữ lớn LLM", "📚", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Generative AI (GenAI)", "/ˈdʒen.ər.ə.tɪv eɪ.aɪ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Trí tuệ nhân tạo tạo sinh: các hệ thống AI có khả năng sáng tạo nội dung mới (văn bản, tranh vẽ, âm nhạc, mã lập trình).",
     "Generative AI automates content generation, code authoring, and customer response workflows.", "AI tạo sinh tự động hóa sáng tạo nội dung, viết mã nguồn và quy trình trả lời khách hàng.",
     "AI tạo sinh GenAI", "✨", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Natural Language Processing (NLP)", "/ˈnætʃ.ər.əl ˈlæŋ.ɡwɪdʒ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Xử lý ngôn ngữ tự nhiên: lĩnh vực nghiên cứu giúp máy tính đọc hiểu, diễn giải và thao tác với ngôn ngữ loài người.",
     "Sentiment analysis and machine translation are classic pillars of natural language processing.", "Phân tích cảm xúc và dịch máy là những trụ cột kinh điển của xử lý ngôn ngữ tự nhiên.",
     "Xử lý ngôn ngữ tự nhiên NLP", "🗣️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Computer Vision (CV)", "/kəmˈpjuː.tər ˈvɪʒ.ən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Thị giác máy tính: lĩnh vực giúp máy tính hiểu và trích xuất thông tin ý nghĩa từ hình ảnh kỹ thuật số hoặc video.",
     "Self-driving cars use computer vision to recognize pedestrian crossings and street signs.", "Xe tự hành dùng thị giác máy tính để nhận diện vạch sang đường và biển báo giao thông.",
     "Thị giác máy tính CV", "👁️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Speech Recognition", "/spiːtʃ ˌrek.əɡˈnɪʃ.ən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Nhận dạng giọng nói (ASR): công nghệ chuyển đổi âm thanh giọng nói con người thành văn bản dạng chữ.",
     "Whisper is a state-of-the-art open-source speech recognition model from OpenAI.", "Whisper là mô hình nhận dạng giọng nói mã nguồn mở tiên tiến nhất của OpenAI.",
     "Nhận dạng giọng nói", "🎙️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Reinforcement Learning from Human Feedback (RLHF)", "/ˌriː.ɪnˈfɔːs.mənt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học tăng cường từ phản hồi của con người (RLHF): kỹ thuật căn chỉnh mô hình AI theo tiêu chuẩn đạo đức và hữu ích của con người.",
     "RLHF transforms raw next-token predictors into helpful, harmless, and honest assistants.", "RLHF biến mô hình đoán từ tiếp theo thô ráp thành trợ lý hữu ích, vô hại và trung thực.",
     "Căn chỉnh mô hình RLHF", "👥", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Foundation Model", "/faʊnˈdeɪ.ʃən ˈmɒd.əl/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mô hình nền tảng: mô hình AI khổng lồ được huấn luyện trên kho dữ liệu quy mô lớn làm gốc để tùy chỉnh cho hàng loạt tác vụ.",
     "Foundation models can be adapted via fine-tuning to perform legal or financial analysis.", "Mô hình nền tảng có thể được tinh chỉnh để thực hiện phân tích luật pháp hay tài chính.",
     "Mô hình nền tảng", "🏛️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Pre-training", "/priː ˈtreɪ.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tiền huấn luyện: giai đoạn đầu tốn kém tính toán nhất huấn luyện mô hình dự đoán từ tiếp theo trên dữ liệu văn bản toàn cầu.",
     "Pre-training modern frontier models costs millions of dollars in GPU cluster compute.", "Tiền huấn luyện mô hình tiên tiến tiêu tốn hàng triệu đô la chi phí cụm GPU.",
     "Giai đoạn tiền huấn luyện", "🏋️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Fine-Tuning", "/faɪn ˈtʃuː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tinh chỉnh mô hình: huấn luyện tiếp mô hình đã có sẵn trên một tập dữ liệu chuyên ngành hẹp để thành thạo lĩnh vực đó.",
     "Fine-tuning a base LLM on medical case records produces an expert clinical assistant.", "Tinh chỉnh mô hình LLM trên hồ sơ bệnh án tạo ra một trợ lý lâm sàng chuyên gia.",
     "Tinh chỉnh chuyên ngành", "🎯", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("LoRA (Low-Rank Adaptation)", "/ˈlɔː.rə/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kỹ thuật LoRA: phương pháp tinh chỉnh mô hình hiệu quả bằng cách cố định trọng số gốc và chỉ huấn luyện ma trận hạng thấp nhỏ.",
     "LoRA fine-tunes multi-billion parameter models on affordable consumer gaming GPUs.", "LoRA tinh chỉnh các mô hình hàng tỷ tham số ngay trên card GPU chơi game phổ thông.",
     "Tinh chỉnh tham số LoRA", "📉", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("QLoRA", "/kjuː ˈlɔː.rə/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kỹ thuật QLoRA: phiên bản lượng tử hóa 4-bit của LoRA giúp giảm tiêu tốn bộ nhớ VRAM gấp bội khi huấn luyện.",
     "QLoRA allows developers to fine-tune a 65B parameter model on a single 48GB GPU.", "QLoRA cho phép lập trình viên tinh chỉnh mô hình 65B tham số trên một GPU 48GB duy nhất.",
     "Lượng tử hóa QLoRA", "⚡", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Transfer Learning", "/ˈtræns.fɜː ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học chuyển giao: tái sử dụng tri thức đã học được từ bài toán lớn này để áp dụng cho bài toán nhỏ khác liên quan.",
     "Transfer learning lets models recognize rare diseases with only a few hundred sample scans.", "Học chuyển giao giúp mô hình nhận diện bệnh hiếm chỉ với vài trăm mẫu chụp quét.",
     "Học chuyển giao", "🔄", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Prompt Engineering", "/prɒmpt ˌen.dʒɪˈnɪə.rɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kỹ thuật đặt câu lệnh Prompt: nghệ thuật thiết kế và tinh chỉnh lời nhắc đầu vào để khai thác câu trả lời tối ưu từ LLM.",
     "Effective prompt engineering significantly enhances code generation quality without fine-tuning.", "Kỹ thuật đặt câu lệnh hiệu quả nâng cao rõ rệt chất lượng sinh mã mà không cần huấn luyện lại.",
     "Kỹ thuật câu lệnh Prompt", "💬", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("System Prompt", "/ˈsɪs.təm prɒmpt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Lời nhắc hệ thống: chỉ dẫn chỉ định vai trò, giọng điệu và các quy tắc ứng xử cốt lõi đặt ở đầu phiên hội thoại với AI.",
     "The system prompt instructs the assistant to behave as a patient software engineering tutor.", "Lời nhắc hệ thống chỉ thị cho trợ lý đóng vai trò là một gia sư kỹ thuật phần mềm kiên nhẫn.",
     "Lời nhắc hệ thống System Prompt", "📜", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Zero-Shot Learning", "/ˈzɪə.rəʊ ʃɒt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học Zero-Shot: khả năng mô hình AI giải quyết chính xác một tác vụ mới mà không cần xem bất kỳ ví dụ mẫu nào trước đó.",
     "Zero-shot classification categorizes texts into new labels without prior domain training.", "Phân loại zero-shot xếp tài liệu vào các nhãn mới mà không cần huấn luyện chuyên ngành trước.",
     "Học không ví dụ Zero-Shot", "🎯", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Few-Shot Learning", "/fjuː ʃɒt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học Few-Shot: cung cấp từ hai đến một vài ví dụ minh họa mẫu bên trong prompt để mô hình hiểu và làm theo đúng cấu trúc.",
     "Few-shot prompting provides two input-output pairs to guide desired JSON formats.", "Lời nhắc few-shot cung cấp hai cặp đầu vào - đầu ra để định hướng định dạng JSON mong muốn.",
     "Học ít ví dụ Few-Shot", "💡", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("In-Context Learning", "/ɪn ˈkɒn.tekst ˈlɜː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Học trong ngữ cảnh: khả năng mô hình nắm bắt quy luật ngay từ ngữ cảnh được cung cấp trong prompt mà không thay đổi trọng số.",
     "In-context learning allows LLMs to adapt to new user rules during the ongoing chat.", "Học trong ngữ cảnh cho phép LLM thích ứng với quy tắc mới ngay trong đoạn chat đang diễn ra.",
     "Học trong ngữ cảnh", "📖", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Chain-of-Thought (CoT)", "/tʃeɪn əv θɔːt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Chuỗi suy luận (CoT): kỹ thuật yêu cầu mô hình trình bày từng bước suy luận logic trước khi đưa ra câu trả lời cuối cùng.",
     "Prompting the model to 'think step by step' triggers chain-of-thought mathematical reasoning.", "Yêu cầu mô hình 'suy nghĩ từng bước' sẽ kích hoạt khả năng suy luận chuỗi giải toán.",
     "Chuỗi suy luận CoT", "⛓️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("AI Hallucination", "/həˌluː.sɪˈneɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Ảo giác AI: hiện tượng mô hình AI tự tin tạo ra thông tin hoàn toàn sai sự thật hoặc trích dẫn các nguồn không hề tồn tại.",
     "RAG architectures ground model responses with verified documents to curb hallucinations.", "Kiến trúc RAG neo câu trả lời vào tài liệu kiểm chứng để ngăn chặn ảo giác AI.",
     "Ảo giác AI Hallucination", "👻", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Retrieval-Augmented Generation (RAG)", "/ˌɑː.eɪˈdʒiː/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tạo sinh tăng cường truy xuất (RAG): kỹ thuật tra cứu tài liệu thực tế từ CSDL véc-tơ rồi chèn vào prompt để AI trả lời chính xác.",
     "RAG allows internal corporate chatbots to answer questions using private policy PDFs.", "RAG cho phép chatbot nội bộ doanh nghiệp trả lời câu hỏi dựa trên các tệp PDF chính sách mật.",
     "Tăng cường truy xuất RAG", "📚", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Vector Database", "/ˈvek.tər ˈdeɪ.tə.beɪs/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Cơ sở dữ liệu véc-tơ: hệ thống CSDL chuyên dụng lưu trữ và tìm kiếm các điểm dữ liệu véc-tơ đa chiều dựa trên khoảng cách ngữ nghĩa.",
     "Pinecone and ChromaDB are dedicated vector databases powering AI search systems.", "Pinecone và ChromaDB là những CSDL véc-tơ chuyên dụng vận hành hệ thống tìm kiếm AI.",
     "CSDL véc-tơ AI", "🎯", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Vector Embedding", "/ˈvek.tər ɪmˈbed.ɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Véc-tơ nhúng: chuỗi số thực n chiều biểu diễn ý nghĩa ngữ nghĩa của một đoạn văn, hình ảnh hay âm thanh.",
     "Words with similar semantic meanings map to nearby coordinates in vector embedding space.", "Các từ có ý nghĩa tương đồng được ánh xạ tới tọa độ gần nhau trong không gian véc-tơ.",
     "Véc-tơ nhúng Embedding", "🔢", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Cosine Similarity", "/ˈkəʊ.saɪn ˌsɪm.ɪˈlær.ə.ti/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Độ tương đồng Cosine: thước đo góc giữa hai véc-tơ xác định mức độ gần gũi về mặt ý nghĩa ngữ nghĩa giữa hai văn bản.",
     "A cosine similarity score approaching 1.0 indicates near-identical contextual intent.", "Điểm tương đồng cosine tiến gần 1.0 cho thấy ý định ngữ cảnh gần như giống hệt nhau.",
     "Độ tương đồng Cosine", "📐", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Semantic Search", "/sɪˈmæn.tɪk sɜːtʃ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tìm kiếm theo ngữ nghĩa: tìm kiếm dựa trên ý nghĩa thực sự của câu hỏi thay vì chỉ so khớp từng từ khóa thô.",
     "Semantic search understands that 'puppy care' matches articles discussing 'caring for young dogs'.", "Tìm kiếm ngữ nghĩa hiểu rằng 'chăm sóc cún con' khớp với các bài viết về 'nuôi chó nhỏ'.",
     "Tìm kiếm ngữ nghĩa", "🔍", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Token", "/ˈtəʊ.kən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Đơn vị Token: mảnh từ ngữ cơ bản (khoảng 4 ký tự hoặc 0.75 từ) mà mô hình ngôn ngữ đọc và xử lý.",
     "API pricing for LLMs is calculated per million input and output tokens consumed.", "Chi phí gọi API của LLM được tính trên mỗi triệu token đầu vào và đầu ra sử dụng.",
     "Đơn vị Token", "🎟️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Tokenization", "/ˌtəʊ.kən.aɪˈzeɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Quá trình bẻ token: thao tác chia nhỏ văn bản thô thành danh sách các token số nguyên bằng thuật toán BPE.",
     "Byte-Pair Encoding (BPE) is the predominant tokenization algorithm in modern transformers.", "Byte-Pair Encoding (BPE) là thuật toán bẻ token thống trị trong các mô hình Transformer hiện đại.",
     "Quá trình bẻ Token", "✂️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Context Window", "/ˈkɒn.tekst ˈwɪn.dəʊ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Cửa sổ ngữ cảnh: dung lượng token tối đa mà một mô hình LLM có thể tiếp nhận và ghi nhớ trong một lượt gọi.",
     "Gemini 1.5 Pro features a massive 2-million token context window to parse entire book series.", "Gemini 1.5 Pro trang bị cửa sổ ngữ cảnh 2 triệu token khổng lồ đọc được cả bộ sách.",
     "Cửa sổ ngữ cảnh Context", "🪟", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Temperature Parameter", "/ˈtem.prə.tʃər/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tham số nhiệt độ: tham số điều khiển độ ngẫu nhiên và sáng tạo của câu trả lời do LLM sinh ra.",
     "Lower the temperature to 0.1 for deterministic mathematical and coding tasks.", "Hạ nhiệt độ xuống 0.1 cho các tác vụ toán học và lập trình cần độ chính xác tuyệt đối.",
     "Tham số nhiệt độ Temperature", "🌡️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Top-P Sampling (Nucleus)", "/tɒp piː ˈsɑːm.plɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Lấy mẫu theo xác suất tích lũy: chỉ chọn ngẫu nhiên trong nhóm các từ có tổng xác suất tích lũy đạt ngưỡng P.",
     "Setting top_p to 0.9 discards unlikely tail tokens to preserve fluent phrasing.", "Đặt top_p bằng 0.9 loại bỏ các từ xác suất cực thấp để giữ lời văn trôi chảy.",
     "Lấy mẫu Top-P Nucleus", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Top-K Sampling", "/tɒp keɪ ˈsɑːm.plɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Lấy mẫu Top-K: giới hạn lựa chọn từ tiếp theo chỉ trong K từ có xác suất cao nhất.",
     "Top-k sampling with k=40 prevents bizarre words from entering the output stream.", "Lấy mẫu top-k với k=40 ngăn các từ kỳ quặc xuất hiện trong câu trả lời.",
     "Lấy mẫu Top-K", "🔢", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Perplexity", "/pəˈplek.sə.ti/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Độ bối rối: chỉ số đo lường mức độ bất ngờ của mô hình khi đọc văn bản mới, điểm càng thấp mô hình càng tốt.",
     "A lower perplexity score indicates superior language prediction capabilities.", "Điểm perplexity thấp hơn cho thấy khả năng dự đoán ngôn ngữ vượt trội hơn.",
     "Độ bối rối Perplexity", "❓", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Loss Function", "/lɒs ˈfʌŋk.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hàm mất mát: hàm toán học tính toán độ sai lệch giữa kết quả mô hình dự đoán và nhãn thực tế.",
     "Training minimizes the loss function through successive gradient updates.", "Quá trình huấn luyện cực tiểu hóa hàm mất mát qua các cập nhật gradient liên tiếp.",
     "Hàm mất mát Loss Function", "📉", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Mean Squared Error (MSE)", "/miːn skweəd ˈer.ər/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Sai số bình phương trung bình: hàm mất mát tiêu chuẩn cho các bài toán hồi quy định lượng số.",
     "MSE penalizes large outlier errors more heavily due to the squaring operation.", "MSE phạt nặng các sai số đột biến lớn hơn do phép bình phương.",
     "Sai số bình phương MSE", "📐", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Cross-Entropy Loss", "/krɒs ˈen.trə.pi lɒs/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mất mát entropy chéo: hàm đo lường khoảng cách giữa hai phân phối xác suất trong các bài toán phân loại.",
     "Cross-entropy loss evaluates classification accuracy across multiple output categories.", "Mất mát entropy chéo đánh giá độ chính xác phân loại trên nhiều nhóm đầu ra.",
     "Mất mát Cross-Entropy", "⚖️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Gradient Descent", "/ˈɡreɪ.di.ənt dɪˈsent/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Thuật toán hạ độ dốc: thuật toán tối ưu hóa lặp từng bước theo hướng ngược chiều đạo hàm để tìm điểm cực tiểu của hàm mất mát.",
     "Gradient descent adjusts weights proportionally to downscale prediction errors.", "Hạ độ dốc điều chỉnh các trọng số theo tỷ lệ để giảm dần sai số dự đoán.",
     "Thuật toán hạ độ dốc", "⛰️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Stochastic Gradient Descent (SGD)", "/stəˈkæs.tɪk/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hạ độ dốc ngẫu nhiên: tính toán gradient trên một mẫu hoặc một lô nhỏ ngẫu nhiên thay vì toàn bộ tập dữ liệu khổng lồ.",
     "SGD accelerates optimization on massive multi-gigabyte datasets.", "SGD tăng tốc tối ưu hóa trên các tập dữ liệu khổng lồ hàng gigabyte.",
     "Hạ độ dốc ngẫu nhiên SGD", "🎲", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Adam Optimizer", "/ˈæd.əm ˈɒp.tɪ.maɪ.zər/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Bộ tối ưu Adam: thuật toán tối ưu hóa thích ứng kết hợp ưu điểm của quán tính (Momentum) và RMSprop phổ biến nhất hiện nay.",
     "The Adam optimizer automatically adapts individual learning rates for each parameter.", "Bộ tối ưu Adam tự động điều chỉnh tốc độ học riêng biệt cho từng tham số.",
     "Bộ tối ưu Adam Optimizer", "⚡", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Learning Rate", "/ˈlɜː.nɪŋ reɪt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tốc độ học: siêu tham số quy định độ lớn của bước nhảy khi cập nhật trọng số tại mỗi chu kỳ.",
     "Setting the learning rate too high prevents loss convergence, causing divergent oscillations.", "Đặt tốc độ học quá cao ngăn hàm mất mát hội tụ và gây ra dao động phân kỳ.",
     "Tốc độ học Learning Rate", "🏃", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Epoch", "/ˈiː.pɒk/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Chu kỳ huấn luyện Epoch: một lần duyệt hoàn chỉnh qua toàn bộ tập dữ liệu huấn luyện.",
     "Training completed after 50 epochs when validation accuracy plateaued.", "Quá trình huấn luyện hoàn thành sau 50 epoch khi độ chính xác kiểm chứng đi vào thế đi ngang.",
     "Chu kỳ huấn luyện Epoch", "🔄", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Batch Size", "/bætʃ saɪz/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kích thước lô mẫu: số lượng mẫu dữ liệu được nạp vào mô hình cùng một lúc trước khi cập nhật trọng số.",
     "Larger batch sizes maximize GPU parallelism but require substantial VRAM.", "Kích thước lô lớn tối đa hóa tính song song của GPU nhưng đòi hỏi nhiều bộ nhớ VRAM.",
     "Kích thước lô mẫu Batch Size", "📦", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Forward Pass", "/ˈfɔː.wəd pɑːs/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Lan truyền tiến: quá trình tính toán đầu vào qua các tầng nơ-ron để tạo ra dự đoán đầu ra.",
     "During the forward pass, activations are cached to assist subsequent gradient calculations.", "Trong lan truyền tiến, các giá trị kích hoạt được lưu tạm để hỗ trợ tính gradient sau đó.",
     "Lan truyền tiến Forward", "➡️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Backpropagation", "/ˈbækˌprɒp.əˈɡeɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Lan truyền ngược: thuật toán tính đạo hàm theo quy tắc chuỗi từ đầu ra ngược về các tầng đầu để cập nhật trọng số.",
     "Backpropagation calculates gradients efficiently for millions of interconnected nodes.", "Lan truyền ngược tính toán gradient hiệu quả cho hàng triệu nút liên kết nhau.",
     "Lan truyền ngược Backpropagation", "⬅️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Activation Function", "/ˌæk.tɪˈveɪ.ʃən ˈfʌŋk.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hàm kích hoạt: hàm phi tuyến tính đưa vào mạng nơ-ron giúp mạng có khả năng học các mối quan hệ phức tạp.",
     "Non-linear activation functions enable neural networks to approximate universal functions.", "Hàm kích hoạt phi tuyến cho phép mạng nơ-ron xấp xỉ các hàm toán học vạn năng.",
     "Hàm kích hoạt Activation", "⚡", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("ReLU (Rectified Linear Unit)", "/ˈrel.juː/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hàm kích hoạt ReLU: trả về giá trị x nếu x > 0 và trả về 0 nếu x <= 0, phổ biến nhất trong mạng sâu.",
     "ReLU avoids vanishing gradient problems and computes lightning-fast on GPUs.", "ReLU tránh được vấn đề triệt tiêu gradient và tính toán siêu nhanh trên GPU.",
     "Hàm kích hoạt ReLU", "📈", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Sigmoid Function", "/ˈsɪɡ.mɔɪd ˈfʌŋk.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hàm Sigmoid: nén mọi giá trị đầu vào thành khoảng xác suất từ 0 đến 1 theo đường cong hình chữ S.",
     "Sigmoid is ideal for the final output layer of binary classification models.", "Hàm Sigmoid lý tưởng cho tầng đầu ra cuối cùng của các mô hình phân loại nhị phân.",
     "Hàm chữ S Sigmoid", "〰️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Softmax Function", "/ˈsɒft.mæks/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hàm Softmax: biến đổi một véc-tơ các số thực thành phân phối xác suất có tổng bằng 1 trong phân loại nhiều lớp.",
     "The softmax output gives the predicted probability for every token in vocabulary.", "Đầu ra softmax cung cấp xác suất dự đoán cho từng token trong từ điển.",
     "Hàm phân phối Softmax", "🥧", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Overfitting", "/ˌəʊ.vəˈfɪt.ɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hiện tượng học vẹt (Overfitting): mô hình học thuộc lòng dữ liệu huấn luyện quá mức nên dự đoán rất kém trên dữ liệu mới.",
     "Dropout and weight decay are applied to prevent the network from overfitting.", "Kỹ thuật dropout và suy giảm trọng số được áp dụng để ngăn mạng bị học vẹt.",
     "Hiện tượng học vẹt Overfitting", "⚠️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Underfitting", "/ˌʌn.dəˈfɪt.ɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Hiện tượng chưa khớp (Underfitting): mô hình quá đơn giản không thể nắm bắt được các quy luật cơ bản của dữ liệu.",
     "Increasing model capacity and training epochs resolves severe underfitting.", "Tăng dung lượng mô hình và chu kỳ huấn luyện giải quyết hiện tượng chưa khớp.",
     "Hiện tượng chưa khớp Underfitting", "📉", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Regularization", "/ˌreɡ.jə.lər.aɪˈzeɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kỹ thuật điều chuẩn: thêm các số hạng phạt vào hàm mất mát để hạn chế độ phức tạp của mô hình và chống quá khớp.",
     "L1 and L2 regularization discourage overly large weight magnitudes.", "Điều chuẩn L1 và L2 ngăn chặn các trọng số có độ lớn quá cao.",
     "Kỹ thuật điều chuẩn", "⚖️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Dropout", "/ˈdrɒp.aʊt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kỹ thuật ngắt nơ-ron: ngẫu nhiên vô hiệu hóa một tỷ lệ nơ-ron trong quá trình huấn luyện để tránh phụ thuộc lẫn nhau.",
     "A dropout rate of 0.2 forces neurons to learn redundant robust features.", "Tỷ lệ dropout 0.2 buộc các nơ-ron phải học các đặc trưng bền vững độc lập.",
     "Ngắt nơ-ron Dropout", "🔌", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Weight Decay", "/weɪt dɪˈkeɪ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Suy giảm trọng số: cơ chế giảm dần giá trị trọng số về 0 sau mỗi bước lặp để giữ mô hình ổn định.",
     "Weight decay stabilizes optimization and improves generalizability.", "Suy giảm trọng số giúp ổn định tối ưu hóa và tăng khả năng tổng quát hóa.",
     "Suy giảm trọng số", "📉", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Hyperparameter Tuning", "/ˌhaɪ.pə.pəˈræm.ɪ.tər ˈtʃuː.nɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tinh chỉnh siêu tham số: tìm kiếm tổ hợp siêu tham số tối ưu (learning rate, batch size) trước khi huấn luyện.",
     "Bayesian optimization speeds up automated hyperparameter tuning across complex search spaces.", "Tối ưu hóa Bayes tăng tốc tinh chỉnh siêu tham số tự động qua không gian tìm kiếm phức tạp.",
     "Tinh chỉnh siêu tham số", "🎛️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Training Set", "/ˈtreɪ.nɪŋ set/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tập dữ liệu huấn luyện: phần lớn dữ liệu (thường 70-80%) được dùng trực tiếp để mô hình học các trọng số.",
     "The training set contains thousands of curated text samples with verified human labels.", "Tập huấn luyện chứa hàng ngàn mẫu văn bản được chọn lọc kèm nhãn con người kiểm chứng.",
     "Tập huấn luyện Training Set", "📚", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Validation Set", "/ˌvæl.ɪˈdeɪ.ʃən set/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tập dữ liệu kiểm chứng: phần dữ liệu dùng để đánh giá mô hình trong khi huấn luyện và điều chỉnh siêu tham số.",
     "Check validation set performance to decide when early stopping should halt training.", "Kiểm tra kết quả trên tập kiểm chứng để quyết định khi nào nên dừng huấn luyện sớm.",
     "Tập kiểm chứng Validation Set", "🔍", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Test Set", "/test set/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tập dữ liệu kiểm tra: tập dữ liệu độc lập chưa từng được mô hình nhìn thấy, dùng để đánh giá năng lực cuối cùng.",
     "Final benchmark metrics must only be evaluated against the unseen test set.", "Các chỉ số đo chuẩn cuối cùng bắt buộc chỉ được đánh giá trên tập kiểm tra chưa từng thấy.",
     "Tập kiểm tra Test Set", "🧪", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("K-Fold Cross-Validation", "/keɪ fəʊld/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kiểm chứng chéo K-lần: chia tập dữ liệu thành K phần bằng nhau, luân phiên dùng 1 phần để kiểm tra và K-1 phần để học.",
     "5-fold cross-validation provides an unbiased estimate of generalization performance.", "Kiểm chứng chéo 5 lần mang lại ước tính khách quan về năng lực tổng quát hóa của mô hình.",
     "Kiểm chứng chéo K-Fold", "🔄", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Bias-Variance Tradeoff", "/ˈbaɪ.əs ˈveə.ri.əns/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Sự đánh đổi giữa độ lệch và phương sai: cân bằng giữa lỗi do mô hình quá đơn giản (bias cao) và quá nhạy cảm với dữ liệu (variance cao).",
     "Machine learning practitioners balance the bias-variance tradeoff to achieve peak accuracy.", "Người thực hành học máy cân bằng sự đánh đổi độ lệch và phương sai để đạt độ chính xác đỉnh cao.",
     "Đánh đổi Bias - Variance", "⚖️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Precision Metric", "/prɪˈsɪʒ.ən ˈmet.rɪk/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Độ chuẩn xác Precision: tỷ lệ các mẫu dự đoán là tích cực mà thực sự là tích cực (trong số các dự đoán đúng bao nhiêu %).",
     "High precision is critical in spam detection to avoid flagging legitimate emails as spam.", "Độ chuẩn xác cao rất quan trọng khi lọc thư rác để tránh gắn cờ nhầm email quan trọng.",
     "Độ chuẩn xác Precision", "🎯", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Recall Metric", "/rɪˈkɔːl ˈmet.rɪk/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Độ bao phủ Recall: tỷ lệ các mẫu tích cực thực tế được mô hình phát hiện ra (tìm được bao nhiêu % trên tổng số).",
     "Medical cancer screenings prioritize high recall over precision to catch every potential case.", "Sàng lọc ung thư ưu tiên độ bao phủ recall cao hơn precision để không bỏ sót ca bệnh.",
     "Độ bao phủ Recall", "🧲", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("F1 Score", "/ˌefˈwʌn skɔːr/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Chỉ số F1: trung bình điều hòa giữa Precision và Recall, phản ánh toàn diện chất lượng mô hình khi dữ liệu mất cân bằng.",
     "The F1 score provides a balanced evaluation on heavily imbalanced fraud datasets.", "Chỉ số F1 mang lại đánh giá cân bằng trên các tập dữ liệu phát hiện gian lận mất cân bằng.",
     "Chỉ số F1 Score", "🏆", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Accuracy Metric", "/ˈæk.jə.rə.si ˈmet.rɪk/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Độ chính xác toàn thể: tỷ lệ tổng số dự đoán đúng trên toàn bộ số mẫu dự đoán.",
     "Accuracy can be misleading when 99 percent of records belong to a single class.", "Độ chính xác có thể gây hiểu lầm khi 99% bản ghi chỉ thuộc về một nhóm duy nhất.",
     "Độ chính xác Accuracy", "✅", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("ROC-AUC Curve", "/ˌɑːr.oʊˈsiː ˌeɪ.juːˈsiː/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Đường cong ROC và diện tích dưới đường cong: đồ thị đánh giá năng lực phân loại của mô hình ở mọi ngưỡng quyết định xác suất.",
     "An AUC score of 0.95 demonstrates superior binary classification discrimination.", "Điểm AUC đạt 0.95 chứng minh khả năng phân biệt phân loại nhị phân vượt trội.",
     "Đường cong ROC-AUC", "📈", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Confusion Matrix", "/kənˈfjuː.ʒən ˈmeɪ.trɪks/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Ma trận nhầm lẫn: bảng thống kê chi tiết số ca Đúng Tích cực (TP), Sai Tích cực (FP), Đúng Tiêu cực (TN) và Sai Tiêu cực (FN).",
     "Inspecting the confusion matrix reveals which categories are frequently misclassified.", "Kiểm tra ma trận nhầm lẫn cho thấy những nhóm nào thường xuyên bị phân loại sai.",
     "Ma trận nhầm lẫn", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Classification", "/ˌklæs.ɪ.fɪˈkeɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Bài toán phân loại: tác vụ học máy gán nhãn cho các điểm dữ liệu đầu vào vào một trong các nhóm rời rạc xác định trước.",
     "Image classification determines whether a picture depicts a dog, cat, or bird.", "Phân loại hình ảnh xác định xem một bức ảnh chụp con chó, con mèo hay con chim.",
     "Bài toán phân loại", "🏷️", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Regression", "/rɪˈɡreʃ.ən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Bài toán hồi quy: tác vụ học máy dự đoán một giá trị số liên tục (như giá nhà, doanh số bán hàng, nhiệt độ).",
     "Linear regression models predict real estate house prices based on square footage.", "Mô hình hồi quy tuyến tính dự đoán giá bất động sản dựa trên diện tích mét vuông.",
     "Bài toán hồi quy", "📉", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Clustering", "/ˈklʌs.tər.ɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Bài toán phân cụm: nhóm các điểm dữ liệu tương đồng lại với nhau mà không có sự hướng dẫn của nhãn trước.",
     "Customer clustering helps marketing teams target specific demographic groups.", "Phân cụm khách hàng giúp nhóm tiếp thị nhắm mục tiêu vào các nhóm nhân khẩu học cụ thể.",
     "Bài toán phân cụm Clustering", "👥", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("K-Means Clustering", "/keɪ miːnz/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Phân cụm K-Means: thuật toán phân chia n điểm dữ liệu vào K cụm dựa trên khoảng cách tới tâm cụm.",
     "K-Means clustering iteratively recalculates cluster centroids until positions stabilize.", "Thuật toán K-Means tính toán lại trọng tâm cụm theo vòng lặp cho đến khi vị trí ổn định.",
     "Thuật toán K-Means", "🎯", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Decision Tree", "/dɪˈsɪʒ.ən triː/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Cây quyết định: mô hình dự đoán phân nhánh hình cây trực quan chia nhỏ dữ liệu theo các câu hỏi điều kiện.",
     "Decision trees provide easily explainable classification rules for bank loan approvals.", "Cây quyết định cung cấp quy tắc phân loại dễ giải thích cho việc phê duyệt khoản vay ngân hàng.",
     "Cây quyết định Decision Tree", "🌲", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Random Forest", "/ˈræn.dəm ˈfɒr.ɪst/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Rừng ngẫu nhiên: phương pháp học kết hợp (ensemble) xây dựng hàng trăm cây quyết định và tổng hợp kết quả bầu chọn.",
     "Random forests reduce variance and prevent overfitting compared to individual decision trees.", "Rừng ngẫu nhiên giảm phương sai và chống quá khớp so với từng cây quyết định riêng lẻ.",
     "Rừng ngẫu nhiên Random Forest", "🌳", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Gradient Boosting", "/ˈɡreɪ.di.ənt ˈbuːst.ɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tăng cường độ dốc: kỹ thuật xây dựng tuần tự các cây mới để khắc phục và bù đắp sai số của các cây trước đó.",
     "Gradient boosting algorithms consistently dominate tabular data competitions on Kaggle.", "Thuật toán tăng cường độ dốc liên tục thống trị các cuộc thi dữ liệu bảng trên Kaggle.",
     "Tăng cường độ dốc Boosting", "🚀", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("XGBoost", "/ˌeks.dʒiːˈbuːst/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Thư viện XGBoost: triển khai tối ưu hóa cao độ của Gradient Boosting với tốc độ tính toán song song cực nhanh.",
     "XGBoost is the gold standard algorithm for financial fraud prediction models.", "XGBoost là thuật toán tiêu chuẩn vàng cho các mô hình dự đoán gian lận tài chính.",
     "Thuật toán XGBoost", "⚡", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Support Vector Machine (SVM)", "/səˈpɔːt ˈvek.tər/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Máy véc-tơ hỗ trợ: thuật toán tìm siêu phẳng tối ưu phân tách các lớp dữ liệu với lề khoảng cách lớn nhất.",
     "SVMs use kernel tricks to classify high-dimensional non-linear patterns effectively.", "SVM sử dụng kỹ thuật kernel để phân loại các mẫu phi tuyến tính nhiều chiều hiệu quả.",
     "Máy véc-tơ hỗ trợ SVM", "📐", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Feature Engineering", "/ˈfiː.tʃər ˌen.dʒɪˈnɪə.rɪŋ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Kỹ nghệ đặc trưng: quá trình trích xuất, biến đổi và tạo ra các thuộc tính mới từ dữ liệu thô để nâng cao hiệu quả mô hình.",
     "Crafting domain-specific features often improves model accuracy more than tuning algorithms.", "Tạo đặc trưng chuyên ngành thường nâng cao độ chính xác nhiều hơn là tinh chỉnh thuật toán.",
     "Kỹ nghệ đặc trưng", "⚙️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Data Normalization", "/ˈdeɪ.tə ˌnɔː.mə.laɪˈzeɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Chuẩn hóa dữ liệu: đưa các giá trị đầu vào về cùng một thang đo (thường từ 0 đến 1) để gradient hội tụ nhanh và ổn định.",
     "Normalizing numerical features prevents large magnitude inputs from dominating the model.", "Chuẩn hóa đặc trưng số ngăn các đầu vào có giá trị lớn lấn át mô hình.",
     "Chuẩn hóa dữ liệu", "📏", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("PCA (Principal Component Analysis)", "/ˌpiː.siːˈeɪ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Phân tích thành phần chính PCA: kỹ thuật giảm chiều dữ liệu bằng cách chiếu dữ liệu sang các hướng có phương sai lớn nhất.",
     "PCA compresses high-dimensional genomic features into two principal visual components.", "PCA nén các đặc trưng gen nhiều chiều thành hai thành phần trực quan chính.",
     "Giảm chiều dữ liệu PCA", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Autoencoder", "/ˈɔː.təʊ.enˌkəʊ.dər/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mạng nơ-ron tự mã hóa: mạng nén dữ liệu đầu vào thành biểu diễn không gian ẩn rồi tái tạo lại nguyên vẹn.",
     "Autoencoders detect manufacturing defects by flagging anomalies during image reconstruction.", "Mạng tự mã hóa phát hiện lỗi sản xuất bằng cách gắn cờ bất thường khi tái tạo ảnh.",
     "Mạng tự mã hóa Autoencoder", "🔄", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("GAN (Generative Adversarial Network)", "/ɡæn/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mạng đối nghịch tạo sinh: hệ thống hai mạng nơ-ron (Bộ tạo sinh và Bộ phân biệt) cạnh tranh nhau để tạo ra dữ liệu như thật.",
     "GANs pioneered the generation of photorealistic synthetic human faces.", "GAN tiên phong trong việc tạo ra khuôn mặt người tổng hợp chân thực như ảnh chụp thật.",
     "Mạng đối nghịch GAN", "🎭", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Diffusion Model", "/dɪˈfjuː.ʒən ˈmɒd.əl/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Mô hình khuếch tán: mô hình tạo sinh học cách khử nhiễu dần dần từ một hình ảnh nhiễu trắng ngẫu nhiên thành bức tranh hoàn chỉnh.",
     "Stable Diffusion and Midjourney generate breathtaking artwork using latent diffusion models.", "Stable Diffusion và Midjourney tạo ra các tác phẩm tranh tuyệt đẹp nhờ mô hình khuếch tán ẩn.",
     "Mô hình khuếch tán Diffusion", "🎨", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Latent Space", "/ˈleɪ.tənt speɪs/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Không gian ẩn: không gian biểu diễn nén đa chiều nơi mô hình nắm bắt các đặc trưng trừu tượng cốt lõi của dữ liệu.",
     "Interpolating between points in latent space produces smooth visual morphing effects.", "Nội suy giữa các điểm trong không gian ẩn tạo ra hiệu ứng biến hình hình ảnh mượt mà.",
     "Không gian ẩn Latent Space", "🌌", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Model Inference", "/ˈmɒd.əl ˈɪn.fər.əns/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Suy luận mô hình: quá trình sử dụng mô hình đã huấn luyện xong để tạo ra dự đoán trên dữ liệu thực tế trong sản xuất.",
     "Optimizing model inference latency delivers sub-second responses to chat users.", "Tối ưu hóa độ trễ suy luận mô hình mang lại câu trả lời dưới 1 giây cho người chat.",
     "Suy luận mô hình Inference", "⚡", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Model Quantization", "/ˌkwɒn.tɪˈzeɪ.ʃən/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Lượng tử hóa mô hình: giảm độ chính xác của trọng số (từ 16-bit float xuống 8-bit hoặc 4-bit) để chạy nhanh và tốn ít RAM hơn.",
     "Quantizing LLMs to 4-bit integer weights enables on-device execution on MacBook laptops.", "Lượng tử hóa LLM sang trọng số 4-bit cho phép chạy trực tiếp trên máy tính xách tay MacBook.",
     "Lượng tử hóa mô hình", "📉", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("ONNX Runtime", "/ˈɒn.ɪks ˈrʌn.taɪm/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Môi trường ONNX: chuẩn định dạng mở và môi trường thực thi tăng tốc suy luận đa nền tảng cho các mô hình AI.",
     "Exporting PyTorch models to ONNX enables accelerated execution across Windows and Linux servers.", "Xuất mô hình PyTorch sang ONNX cho phép tăng tốc thực thi trên máy chủ Windows và Linux.",
     "Định dạng ONNX", "🔄", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("PyTorch", "/ˈpaɪ.tɔːtʃ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Thư viện PyTorch: khung học sâu mã nguồn mở do Meta AI phát triển được giới nghiên cứu học thuật và doanh nghiệp ưa chuộng nhất.",
     "PyTorch's dynamic computational graph makes debugging deep neural networks straightforward.", "Đồ thị tính toán động của PyTorch giúp việc gỡ lỗi mạng nơ-ron sâu trở nên trực quan.",
     "Khung học sâu PyTorch", "🔥", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("TensorFlow", "/ˈten.sə.fləʊ/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Thư viện TensorFlow: nền tảng máy học toàn diện mã nguồn mở của Google tối ưu hóa cho triển khai sản xuất quy mô lớn.",
     "Google uses TensorFlow and TF Lite to serve billions of mobile machine learning inferences.", "Google dùng TensorFlow và TF Lite để phục vụ hàng tỷ lượt suy luận học máy trên thiết bị di động.",
     "Nền tảng TensorFlow", "🟧", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80"),

    ("Autonomous Agent / Tool Calling", "/ɔːˈtɒn.ə.məs ˈeɪ.dʒənt/", "noun", "ai_ml", "Trí tuệ nhân tạo & Máy học",
     "Tác tử tự hành / Gọi công cụ: hệ thống AI có khả năng lập kế hoạch, tự gọi các công cụ API ngoài để hoàn thành mục tiêu phức tạp.",
     "AI agents leverage function calling to browse databases, search websites, and commit code autonomously.", "Tác tử AI tận dụng gọi hàm để tự động tra cứu CSDL, tìm kiếm web và commit mã nguồn.",
     "Tác tử tự hành Agent", "🤖", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 9 terms count: {len(terms)}")
