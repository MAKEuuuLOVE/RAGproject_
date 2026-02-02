# RAGproject_ - 简单的服装需求问答系统
一个基于 **检索增强生成（RAG, Retrieval-Augmented Generation）** 技术构建的服装相关智能问答项目，能够快速检索本地服装知识库，并生成准确、贴合需求的回答。

## 项目介绍
### 核心功能
- 🔍 本地服装知识库检索：基于向量数据库快速匹配相关服装信息（款式、面料、尺码、搭配等）
- 🤖 智能问答生成：结合检索到的知识库内容，生成服装相关回答，可留历史记录
- 📂 支持本地数据持久化：知识库数据本地存储，无需依赖外部接口，隐私性更强
- 🚀 轻量化部署：基于 Python 构建，依赖简单，本地可直接运行

### 技术栈
- **编程语言**：Python 3.8+
- **RAG 核心框架**：LangChain（检索逻辑、问答链构建）
- **向量数据库**：Chroma DB（本地向量存储、快速检索）
- **环境管理**：Python 虚拟环境（.venv）
- **配置管理**：.env 环境变量配置
- **版本控制**：Git & GitHub

## 快速开始
### 前置条件
1. 安装 Python 3.8 及以上版本
2. 安装 Git（可选，用于版本控制）
3. 提前准备服装相关知识库文件（如 .txt、.pdf 等格式）

### 运行步骤
1. **克隆仓库**（如果你分享给他人，他人可通过该命令获取项目；你本地可直接跳过，使用现有项目）
```bash
git clone https://github.com/MAKEuuuLOVE/RAGproject_.git
cd RAGproject_
```
2.  **创建并激活虚拟环境**
```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境（Windows 系统）
.venv\Scripts\activate

# 激活虚拟环境（Mac/Linux 系统）
source .venv/bin/activate
```
3. **安装项目依赖**
```bash
pip install langchain_community
pip instrall streamlit 
pip install config
pip install dotenv
pip install langchain_core
pip install file_history_store
pip install langchain_chroma
pip install langchain_text_splitters
pip install 
......

```
4. **配置环境变量**  
复制项目根目录的 .env   
填写必要的配置项（如API-KEY等）

### 运行项目
1. 确保虚拟环境已激活，且依赖安装完成
2. 执行核心运行脚本
```bash
python rag.py
```
3. 在终端打开app_QA问答网页
```bash
#在项目路径下在终端输入
streamlit run app_QA.py
```
4. 输入服务相关问题，即可获得智能问答


## 项目结构
```plaintext
RAGproject_/
├── .venv/                # Python 虚拟环境（隔离项目依赖，忽略上传）
├── chat_history/         # 存储问答历史记录（本地数据，忽略上传）
├── chroma_db/            # Chroma 向量数据库（存储服装知识库的向量数据，忽略上传）
├── data_close/           # 本地服装知识库文件夹
│   ├── 尺码推荐.txt       # 服装尺码推荐的知识库文档
│   ├── 洗涤养护.txt       # 服装洗涤养护的知识库文档
│   └── 颜色选择.txt       # 服装颜色搭配的知识库文档
├── .env                  # 环境变量配置文件（存储敏感信息/路径配置，忽略上传）
├── .gitignore            # Git 忽略规则文件（过滤无需上传的文件/文件夹）
├── app_file_uploader.py  # 文件上传模块（负责将本地知识库文档导入系统）
├── app_QA.py             # 问答交互模块（处理用户提问、调用检索与生成逻辑）
├── config_data.py        # 配置管理模块（统一管理项目路径、模型参数等配置）
├── file_history_store.py # 历史记录管理模块（存储/读取问答历史）
├── knowledge_base.py     # 知识库管理模块（初始化/更新本地服装知识库）
├── md5.text              # MD5校验文件（用于验证知识库文档的完整性）
├── rag.py                # 项目核心主程序（整合各模块，启动问答系统）
├── README.md             # 项目说明文档（当前文件）
└── vector_stores.py      # 向量库管理模块（负责知识库的向量化存储与检索）
```


## LICENSE
本项目仅供个人学习交流使用，无商业用途。